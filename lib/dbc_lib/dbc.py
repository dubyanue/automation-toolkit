import sqlite3
from collections.abc import Iterable
from datetime import datetime
from logging import Logger
from typing import Any

from lib.file_lib.file_factory import FileFactory


class SQLite:
    def __init__(
        self,
        filename: str | FileFactory = ":memory:",
        logger: Logger | None = None,
        *,
        autocommit: bool = True,
    ) -> None:
        self.__filename: FileFactory = (
            FileFactory(filename) if isinstance(filename, str) else filename
        )
        self._logger: Logger | None = logger
        self._autocommit: bool = autocommit
        self._connected: bool = False
        self.cnxn: sqlite3.Connection | None = None

    def __del__(self) -> None:
        self.disconnect()

    def is_connected(self) -> bool:
        return self.cnxn is not None and self._connected

    def connect(self, timeout: float = 0.1) -> sqlite3.Connection:
        if not self.cnxn or not self._connected:
            self.cnxn = sqlite3.connect(
                database=self.__filename, timeout=timeout, autocommit=self._autocommit
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
    ) -> sqlite3.Cursor | None:
        curs: sqlite3.Cursor | None = None
        # if not self.is_connected():
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
    ) -> Iterable[Iterable[float | str | bool | datetime | None]]:
        results: list[Any] = []
        data: sqlite3.Cursor | None = self.execute(sql, params)
        if data:
            results = data.fetchall()
        return results

    def fetchmany(
        self,
        sql: str,
        size: int | None = 1,
        params: Iterable[str | float | bool | datetime | None]
        | dict[str, str | float | bool | datetime | None] = (),
    ) -> Iterable[Iterable[float | str | bool | datetime | None]]:
        results: list[Any] = []
        data: sqlite3.Cursor | None = self.execute(sql, params)
        if data:
            results = data.fetchmany(size)
        return results

    def fetchone(
        self,
        sql: str,
        params: Iterable[str | float | bool | datetime | None]
        | dict[str, str | float | bool | datetime | None] = (),
    ) -> Iterable[Iterable[float | str | bool | datetime | None]] | None:
        results: tuple[Any, ...] | None = None
        data: sqlite3.Cursor | None = self.execute(sql, params)
        if data:
            results = data.fetchone()
        return results

    def executemany(
        self, sql: str, params: Iterable[Iterable[float | str | bool | datetime | None]]
    ) -> sqlite3.Cursor | None:
        curs: sqlite3.Cursor | None = None
        if not self.cnxn:
            self.connect()
        try:
            curs = self.cnxn.executemany(sql, params)  # type: ignore
        except Exception as ex:
            if self._logger:
                self._logger.exception("Database operation failed", exc_info=ex)

        return curs

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

    def backup(self, target: sqlite3.Connection | str) -> None:
        if isinstance(target, str):
            sqlite: SQLite = SQLite(target, self._logger)
            target_: sqlite3.Connection = sqlite.connect()
        else:
            target_ = target
        if not self.cnxn and not self._connected:
            self.connect()
        self.cnxn.backup(target_)  # type: ignore

    def get_headers(self, table: str) -> list[str]:
        data: list[str] = []
        curs: sqlite3.Cursor | None = self.execute(f"SELECT * FROM {table} WHERE 1=0")  # noqa: S608
        if curs:
            data = [i[0] for i in curs.description]
        return data
