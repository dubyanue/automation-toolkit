import sqlite3
from collections.abc import Iterable
from datetime import datetime
from logging import Logger
from typing import Any, TypeAlias

import pyodbc  # type: ignore

from lib.dbc_lib.dbc_utils import DUMMY_QUERY, map_table_data
from lib.file_lib.file_factory import FileFactory

DBConnection: TypeAlias = sqlite3.Connection | pyodbc.Connection
DBCursor: TypeAlias = sqlite3.Cursor | pyodbc.Cursor


class PyODBC:
    def __init__(
        self,
        connection_str: str | FileFactory,
        logger: Logger | None = None,
        *,
        autocommit: bool = True,
    ) -> None:
        self._connection_str: str | FileFactory = connection_str
        self._logger: Logger | None = logger
        self._autocommit: bool = autocommit
        self._connected: bool = False
        self.cnxn: DBConnection | None = None

    def __del__(self) -> None:
        self.disconnect()

    def is_connected(self) -> bool:
        return self.cnxn is not None and self._connected

    def connect(self, timeout: int = 1) -> DBConnection:
        if not self.cnxn or not self._connected:
            self.cnxn = pyodbc.connect(
                str(self._connection_str), timeout=timeout, autocommit=self._autocommit
            )
            self._connected = True

        return self.cnxn

    def disconnect(self, *, commit: bool = True) -> None:
        if self.cnxn and self._connected:
            if commit and not self._autocommit:
                self.cnxn.commit()
            self.cnxn.close()
            self.cnxn = None
            self._connected = False

    def execute(
        self,
        sql: str,
        params: Iterable[str | float | bool | datetime | None]
        | dict[str, str | float | bool | datetime | None] = (),
    ) -> DBCursor | None:
        curs: DBCursor | None = None
        if not self.cnxn:
            self.connect()
        try:
            curs = self.cnxn.execute(sql, params)  # type: ignore
        except Exception as ex:
            if self._logger:
                self._logger.exception("Database operation failed", exc_info=ex)

        return curs

    def fetchall(
        self,
        sql: str,
        params: Iterable[str | float | bool | datetime | None]
        | dict[str, str | float | bool | datetime | None] = (),
        *,
        mapped: bool = False,
    ) -> list[Any]:
        results: list[Any] = []
        data: DBCursor | None = self.execute(sql, params)
        if data:
            results = (
                data.fetchall()
                if not mapped
                else [map_table_data(row, data.description) for row in data.fetchall()]
            )
        return results

    def fetchmany(
        self,
        sql: str,
        size: int = 1,
        params: Iterable[str | float | bool | datetime | None]
        | dict[str, str | float | bool | datetime | None] = (),
        *,
        mapped: bool = False,
    ) -> list[Any]:
        results: list[Any] = []
        data: DBCursor | None = self.execute(sql, params)
        if data:
            results = (
                data.fetchmany(size)
                if not mapped
                else [
                    map_table_data(row, data.description)
                    for row in data.fetchmany(size)
                ]
            )
        return results

    def fetchone(
        self,
        sql: str,
        params: Iterable[str | float | bool | datetime | None]
        | dict[str, str | float | bool | datetime | None] = (),
        *,
        mapped: bool = False,
    ) -> pyodbc.Row | dict[str, Any] | None:
        results: pyodbc.Row | dict[str, Any] | None = None
        data: DBCursor | None = self.execute(sql, params)
        if data:
            results = data.fetchone()
            if mapped and results and isinstance(results, pyodbc.Row):
                results = map_table_data(results, data.description)
        return results

    def executemany(
        self, sql: str, params: Iterable[Iterable[float | str | bool | datetime | None]]
    ) -> DBCursor | None:
        curs: DBCursor | None = None
        if not self.cnxn:
            self.connect()
        try:
            curs = self.cnxn.executemany(sql, params)  # type: ignore
        except Exception as ex:
            if self._logger:
                self._logger.exception("Database operation failed", exc_info=ex)

        return curs

    def get_description(self, table: str) -> tuple[Any, ...]:
        description: tuple[Any, ...] = ()
        curs: DBCursor | None = self.execute(DUMMY_QUERY.format(table))
        if curs:
            description = curs.description

        return description

    def get_headers(self, table: str) -> list[str]:
        return [i[0] for i in self.get_description(table)]


class SQLite(PyODBC):
    def __init__(
        self,
        filename: str | FileFactory = ":memory:",
        logger: Logger | None = None,
        *,
        autocommit: bool = True,
    ) -> None:
        super().__init__(filename, logger, autocommit=autocommit)
        self._connection_str = (
            FileFactory(filename) if isinstance(filename, str) else filename
        )
        self._logger: Logger | None = logger
        self._autocommit: bool = autocommit
        self._connected: bool = False
        self.cnxn: DBConnection | None = None

    def connect(self, timeout: int = 1) -> DBConnection:
        if not self.cnxn or not self._connected:
            self.cnxn = sqlite3.connect(
                database=self._connection_str,
                timeout=timeout,
                autocommit=self._autocommit,
            )
            self._connected = True

        return self.cnxn

    def executescript(self, sql: str) -> sqlite3.Cursor | None:
        curs: sqlite3.Cursor | None = None
        if not self.cnxn:
            self.connect()
        try:
            curs = self.cnxn.executescript(sql)  # type: ignore
        except Exception as ex:
            if self._logger:
                self._logger.exception("Database operation failed", exc_info=ex)

        return curs

    def backup(self, target: DBConnection | str) -> None:
        if isinstance(target, str):
            sqlite: SQLite = SQLite(target, self._logger)
            target_: DBConnection = sqlite.connect()
        else:
            target_ = target
        if not self.cnxn and not self._connected:
            self.connect()
        self.cnxn.backup(target_)  # type: ignore
