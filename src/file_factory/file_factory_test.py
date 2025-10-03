from collections.abc import Generator
from pathlib import Path

import pytest

from src.file_factory.file_factory import FileFactory


@pytest.fixture
def file_factory() -> Generator[tuple[str, FileFactory]]:
    filename_: str = "/fake/file/test.txt"
    file_factory_: FileFactory = FileFactory(filename_)
    yield (filename_, file_factory_)


def test_basic_file_factory(file_factory_fixture) -> None:
    file_f: FileFactory

    _, file_f = file_factory_fixture
    assert isinstance(file_f.get_path(), Path)


if __name__ == "__main__":
    import sys

    sys.exit(pytest.main())
