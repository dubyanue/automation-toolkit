"""File factory module for enhanced file operations.

This module provides the FileFactory class which extends pathlib.Path with additional
file operations and utilities for file management.
"""

import re
from collections.abc import Generator
from contextlib import contextmanager
from pathlib import Path
from typing import IO, Any

COMMENTRE = re.compile(r"//.*$|#.*$", re.MULTILINE)


class FileFactory(Path):
    """Enhanced file handling class extending pathlib.Path.

    Provides additional file operations like create, delete, size checking,
    and enhanced reading capabilities with comment filtering.

    Attributes:
        is_open: Boolean flag indicating if the file is currently open.
    """

    def __new__(cls, filename: str) -> "FileFactory":
        """Create a new FileFactory instance.

        Args:
            filename: Path to the file as a string.

        Returns:
            A new FileFactory instance with is_open set to False.
        """
        self = super().__new__(cls, filename)
        self.is_open = False
        return self

    def create(self, mode: int = 0o777) -> bool:
        """Create the file with specified permissions.

        Args:
            mode: File permissions in octal notation. Defaults to 0o777.

        Returns:
            True if file exists after creation attempt, False otherwise.
        """
        self.touch(mode, exist_ok=True)
        return self.exists()

    def delete(self) -> bool:
        """Delete the file if it exists.

        Returns:
            True if file was successfully deleted or doesn't exist, False otherwise.
        """
        self.unlink(missing_ok=True)
        return not self.exists()

    def size(self) -> int:
        """Get the file size in bytes.

        Returns:
            File size in bytes, or 0 if file doesn't exist.
        """
        return self.stat().st_size if self.exists() else 0

    def modified_time(self) -> float:
        """Get the last modification time of the file.

        Returns:
            Last modification time as a Unix timestamp, or 0.0 if file doesn't exist.
        """
        return self.stat().st_mtime if self.exists() else 0.0

    def read(self, *, allow_comments: bool = True, encoding: str = "utf-8") -> str:
        """Read the entire file content as a string.

        Args:
            allow_comments: If False, strips comments starting with // or #.
                Defaults to True.
            encoding: Text encoding to use when reading. Defaults to "utf-8".

        Returns:
            Complete file content as a string.

        Raises:
            IsADirectoryError: If the path points to a directory.
            FileNotFoundError: If the file doesn't exist.
        """
        exception_msg: str = ""
        if self.is_dir():
            exception_msg = f"Expected file but, '{self}' is a directory."
            raise IsADirectoryError(exception_msg)
        if not self.exists():
            exception_msg = f"File: '{self}' not found."
            raise FileNotFoundError(exception_msg)
        data: str = ""
        with self.open_(mode="r", encoding=encoding) as fh:
            if not allow_comments:
                for line in fh:
                    data += re.sub(COMMENTRE, "", line)
            else:
                data = fh.read()
        return data

    def readlines(
        self, *, allow_comments: bool = True, encoding: str = "utf-8"
    ) -> list[str]:
        """Read the file content as a list of lines.

        Args:
            allow_comments: If False, strips comments starting with // or #.
                Defaults to True.
            encoding: Text encoding to use when reading. Defaults to "utf-8".

        Returns:
            List of strings, each representing a line from the file.

        Raises:
            IsADirectoryError: If the path points to a directory.
            FileNotFoundError: If the file doesn't exist.
        """
        exception_msg: str = ""
        if self.is_dir():
            exception_msg = f"Expected file but, '{self}' is a directory."
            raise IsADirectoryError(exception_msg)
        if not self.exists():
            exception_msg = f"File: '{self}' not found."
            raise FileNotFoundError(exception_msg)
        lines: list[str] = []
        with self.open_(mode="r", encoding=encoding) as fh:
            if allow_comments:
                lines = fh.readlines()
            else:
                lines = [re.sub(COMMENTRE, "", line) for line in fh.readlines()]

        return lines

    @contextmanager
    def open_(self, mode: str = "r", encoding: str = "utf-8") -> Generator[IO[Any]]:
        """Context manager for opening files with state tracking.

        Args:
            mode: File open mode. Defaults to "r".
            encoding: Text encoding to use. Defaults to "utf-8".

        Yields:
            File handle for the opened file.

        Note:
            Sets is_open to True during file operation and False when closed.
        """
        with self.open(mode=mode, encoding=encoding) as file_handle:
            self.is_open = True
            yield file_handle

        self.is_open = False
