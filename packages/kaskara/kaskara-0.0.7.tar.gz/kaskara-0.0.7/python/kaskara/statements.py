# -*- coding: utf-8 -*-
__all__ = ('Statement', 'ProgramStatements')

from typing import FrozenSet, Dict, Any, List, Iterator
import json
import logging
import os

import attr
import dockerblade as _dockerblade

from .core import FileLocationRange, FileLocation, FileLine
from .exceptions import BondException
from .insertions import InsertionPointDB, InsertionPoint
from .project import Project
from .util import abs_to_rel_flocrange, rel_to_abs_flocrange

logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Statement:
    content: str
    canonical: str
    kind: str  # FIXME this is super memory inefficient
    location: FileLocationRange
    reads: FrozenSet[str]
    writes: FrozenSet[str]
    visible: FrozenSet[str]
    declares: FrozenSet[str]
    live_before: FrozenSet[str]
    requires_syntax: FrozenSet[str]

    @staticmethod
    def from_dict(project: Project, d: Dict[str, Any]) -> 'Statement':
        # FIXME
        location = FileLocationRange.from_string(d['location'])
        location = abs_to_rel_flocrange(project.directory, location)
        return Statement(d['content'],
                         d['canonical'],
                         d['kind'],
                         location,
                         frozenset(d.get('reads', [])),
                         frozenset(d.get('writes', [])),
                         frozenset(d.get('visible', [])),
                         frozenset(d.get('decls', [])),
                         frozenset(d.get('live_before', [])),
                         frozenset(d.get('requires_syntax', [])))

    def to_dict(self, project: Project) -> Dict[str, Any]:
        loc = rel_to_abs_flocrange(project.directory, self.location)
        return {'content': self.content,
                'canonical': self.canonical,
                'kind': self.kind,
                'location': str(loc),
                'live_before': [v for v in self.live_before],
                'reads': [v for v in self.reads],
                'writes': [v for v in self.writes],
                'decls': [v for v in self.declares],
                'visible': [v for v in self.visible],
                'requires_syntax': list(self.requires_syntax)}


class ProgramStatements:
    @classmethod
    def build_for_container(cls,
                            project: Project,
                            container: _dockerblade.Container
                            ) -> 'ProgramStatements':
        logger.debug('finding statements for project: %s', project)

        shell = container.shell()
        workdir = project.directory
        command_args = ['/opt/kaskara/scripts/kaskara-statement-finder']
        command_args += project.files
        command = ' '.join(command_args)
        output_filename = os.path.join(workdir, 'statements.json')
        logger.debug('executing statement finder [%s]: %s', workdir, command)
        try:
            shell.check_call(command, cwd=workdir)
        except _dockerblade.CalledProcessError as err:
            msg = f'statement finder failed with code {err.returncode}'
            logger.exception(msg)
            if not project.ignore_errors:
                raise BondException(msg)

        logger.debug('reading results from file: %s', output_filename)
        files = container.filesystem()
        file_contents = files.read(output_filename)
        jsn: List[Dict[str, Any]] = json.loads(file_contents)
        db = ProgramStatements.from_dict(project, jsn)
        logger.debug('finished reading results')
        return db

    @classmethod
    def build(cls, project: Project) -> 'ProgramStatements':
        with project.provision() as container:
            return cls.build_for_container(project, container)

    @classmethod
    def from_file(cls, project: Project, filename: str) -> 'ProgramStatements':
        logger.debug('reading statement database from file: %s', filename)
        with open(filename, 'r') as fh:
            dict_ = json.load(fh)
        statements = ProgramStatements.from_dict(project, dict_)
        logger.debug("read statement database from file: %s", filename)
        return statements

    @staticmethod
    def from_dict(project: Project,
                  d: List[Dict[str, Any]]
                  ) -> 'ProgramStatements':
        statements = [Statement.from_dict(project, dd) for dd in d]
        return ProgramStatements(statements)

    def __init__(self, statements: List[Statement]) -> None:
        self.__statements = statements
        logger.debug("indexing statements by file")
        self.__file_to_statements = {}  # type: Dict[str, List[Statement]]
        for statement in statements:
            filename = statement.location.filename
            if filename not in self.__file_to_statements:
                self.__file_to_statements[filename] = []
            self.__file_to_statements[filename].append(statement)
        summary = ["  {}: {} statements".format(fn, len(stmts))
                   for (fn, stmts) in self.__file_to_statements.items()]
        logger.debug("indexed statements by file:\n%s", '\n'.join(summary))

    def __iter__(self) -> Iterator[Statement]:
        yield from self.__statements

    def in_file(self, fn: str) -> Iterator[Statement]:
        """
        Returns an iterator over all of the statements belonging to a file.
        """
        yield from self.__file_to_statements.get(fn, [])

    def at_line(self, line: FileLine) -> Iterator[Statement]:
        """
        Returns an iterator over all of the statements located at a given line.
        """
        num = line.num
        for stmt in self.in_file(line.filename):
            if stmt.location.start.line == num:
                yield stmt

    def insertions(self) -> InsertionPointDB:
        logger.debug("computing insertion points")
        points: List[InsertionPoint] = []
        for stmt in self:
            location = FileLocation(stmt.location.filename,
                                    stmt.location.stop)
            point = InsertionPoint(location, stmt.visible)

            # FIXME do not insert after a return

            points.append(point)
        db = InsertionPointDB(points)
        logger.debug("computed insertion points")
        return db

    def to_dict(self, project: Project) -> List[Dict[str, Any]]:
        return [stmt.to_dict(project) for stmt in self.__statements]

    def to_file(self, project: Project, filename: str) -> None:
        logger.debug('writing statement database to file: %s', filename)
        d = self.to_dict(project)
        with open(filename, 'w') as fh:
            json.dump(d, fh)
        logger.debug('wrote statement database to file: %s', filename)
