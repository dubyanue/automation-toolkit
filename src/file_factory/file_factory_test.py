from collections.abc import Generator
from pathlib import Path
from tempfile import NamedTemporaryFile

import pytest

from src.file_factory.file_factory import FileFactory


@pytest.fixture(name="file_factory")
def fixture_file_factory() -> Generator[FileFactory]:
    # Setup
    with NamedTemporaryFile(mode="w+", delete=False, encoding="utf-8") as tmp:
        filename_: str = tmp.name

    file_factory_: FileFactory = FileFactory(filename_)
    yield file_factory_

    if (file_path := Path(filename_)).exists():
        file_path.unlink(missing_ok=True)


def test_basic_file_factory(file_factory: FileFactory) -> None:
    file_f: FileFactory
    file_f = file_factory
    assert file_f.is_open is False
    assert file_f.is_file() is True
    assert isinstance(file_f.get_path(), Path)
    assert file_f.exists() is True


def test_delete_create(file_factory: FileFactory) -> None:
    file_f: FileFactory
    file_f = file_factory
    assert file_f.is_open is False
    assert file_f.exists() is True
    assert file_f.delete() is True
    assert file_f.exists() is False
    assert file_f.create() is True
    assert file_f.exists() is True


def test_read_write(file_factory: FileFactory) -> None:
    file_f: FileFactory
    test_str: str = "Who the hell do you think I am!?\n"
    file_f = file_factory
    with file_f.open("w") as fh:
        fh.write(test_str)
        assert file_f.is_open is True

    assert file_f.is_open is False

    with file_f.open("r") as fh:
        assert fh.read() == test_str
        assert file_f.is_open is True


def test_read(file_factory: FileFactory) -> None:
    file_f: FileFactory
    test_str: str = "Basic test string"
    file_f = file_factory
    with file_f.open("w") as fh:
        fh.write(test_str)
    data: str = file_f.read()
    assert data == test_str


def test_read_with_comments(file_factory: FileFactory) -> None:
    file_f: FileFactory
    file_f = file_factory
    with file_f.open("w") as fh:
        fh.write('{"test": "yes","test2": "no",// "test3": "commented"\n}')
    assert file_f.read(allow_comments=False) == '{"test": "yes","test2": "no",\n}'


if __name__ == "__main__":
    import sys

    sys.exit(pytest.main())
