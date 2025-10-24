import re
from collections.abc import Generator
from contextlib import contextmanager
from pathlib import Path
from typing import IO, Any

COMMENTRE = re.compile(r"//.*$|#.*$", re.MULTILINE)


class FileFactory(Path):
    def __new__(cls, filename: str) -> "FileFactory":
        self = super().__new__(cls, filename)
        self.is_open = False
        return self

    def create(self, mode: int = 0o777) -> bool:
        self.touch(mode, exist_ok=True)
        return self.exists()

    def delete(self) -> bool:
        self.unlink(missing_ok=True)
        return not self.exists()

    def size(self) -> int:
        return self.stat().st_size if self.exists() else 0

    def modified_time(self) -> float:
        return self.stat().st_mtime if self.exists() else 0.0

    def read(self, *, allow_comments: bool = True, encoding: str = "utf-8") -> str:
        exception_msg: str = ""
        if self.is_dir():
            exception_msg = f"Expected file but, '{self}' is a directory."
            raise IsADirectoryError(exception_msg)
        if not self.exists():
            exception_msg = f"File: '{self}' not found."
            raise FileNotFoundError(exception_msg)
        data: str = ""
        with self._open(mode="r", encoding=encoding) as fh:
            if not allow_comments:
                for line in fh:
                    data += re.sub(COMMENTRE, "", line)
            else:
                data = fh.read()
        return data

    def readlines(
        self, *, allow_comments: bool = True, encoding: str = "utf-8"
    ) -> list[str]:
        exception_msg: str = ""
        if self.is_dir():
            exception_msg = f"Expected file but, '{self}' is a directory."
            raise IsADirectoryError(exception_msg)
        if not self.exists():
            exception_msg = f"File: '{self}' not found."
            raise FileNotFoundError(exception_msg)
        lines: list[str] = []
        with self._open(mode="r", encoding=encoding) as fh:
            if allow_comments:
                lines = fh.readlines()
            else:
                lines = [re.sub(COMMENTRE, "", line) for line in fh.readlines()]

        return lines

    @contextmanager
    def _open(self, mode: str = "r", encoding: str = "utf-8") -> Generator[IO[Any]]:
        with self.open(mode=mode, encoding=encoding) as file_handle:
            self.is_open = True
            yield file_handle

        self.is_open = False
