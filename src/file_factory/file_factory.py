import re
from collections.abc import Generator
from contextlib import contextmanager
from logging import Logger
from pathlib import Path
from typing import IO, Any

COMMENTRE = re.compile(r"//.*$|#.*$", re.MULTILINE)


class FileFactory:
    def __init__(self, filename: str, logger: Logger | None = None) -> None:
        self.__filename: str = filename
        self.__logger: Logger | None = logger
        self.file_path: Path = Path(self.__filename)
        self.is_open: bool = False

    def get_path(self) -> Path:
        return self.file_path

    def exists(self) -> bool:
        return self.file_path.exists()

    def create(self, mode: int = 0o777) -> bool:
        self.file_path.touch(mode, exist_ok=True)
        return self.exists()

    def delete(self) -> bool:
        self.file_path.unlink(missing_ok=True)
        return not self.exists()

    def size(self) -> int:
        return self.file_path.stat().st_size if self.exists() else 0

    def modified_time(self) -> float:
        return self.file_path.stat().st_mtime if self.exists() else 0.0

    def is_file(self) -> bool:
        return self.file_path.is_file()

    def is_dir(self) -> bool:
        return self.file_path.is_dir()

    def read(self, *, allow_comments: bool = True) -> str:
        data: str = ""
        if not self.exists():
            raise FileNotFoundError
        with self.open(mode="r", encoding="utf-8") as fh:
            if not allow_comments:
                for line in fh:
                    data += re.sub(COMMENTRE, "", line)
            else:
                data = fh.read()
        return data

    @contextmanager
    def open(
        self, mode: str = "r", create_mode: int = 0o777, encoding: str = "utf-8"
    ) -> Generator[IO[Any]]:
        """
        Context manager for opening the file.
        Usage: with file_factory.open('w') as f: ...
        """
        if not self.exists():
            self.create(create_mode)

        try:
            with self.file_path.open(mode=mode, encoding=encoding) as file_handle:
                self.is_open = True
                yield file_handle
        except Exception:
            if self.__logger:
                self.__logger.exception("Failed to open file")
            raise
        finally:
            self.is_open = False
