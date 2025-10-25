from pathlib import Path

import pytest

from lib.file_lib.file_factory import FileFactory

# pylint: disable-next=unused-import
from tests.test_fixtures import common_file_factory_fixture, temp_directory_fixture


def test_basic_file_factory(common_file_factory_fixture_: FileFactory) -> None:
    file_f: FileFactory = common_file_factory_fixture_
    assert file_f.is_open is False
    assert file_f.is_file() is True
    assert isinstance(file_f, Path)
    assert file_f.exists() is True
    assert file_f.size() == 0
    assert file_f.modified_time() > 0
    file_f.delete()


def test_delete_create(common_file_factory_fixture_: FileFactory) -> None:
    file_f: FileFactory = common_file_factory_fixture_
    assert file_f.is_open is False
    assert file_f.exists() is True
    assert file_f.delete() is True
    assert file_f.exists() is False
    assert file_f.create() is True
    assert file_f.exists() is True


def test_file_factory_read_errors(temp_directory_fixture_: str) -> None:
    dir_name: str = temp_directory_fixture_
    fake_file: str = "/fake/fake_file.txt"
    with pytest.raises(
        IsADirectoryError, match=f"Expected file but, '{dir_name}' is a directory."
    ):
        FileFactory(dir_name).read()

    with pytest.raises(FileNotFoundError, match=f"File: '{fake_file}' not found."):
        FileFactory(fake_file).read()


def test_file_factory_readlines_errors(temp_directory_fixture_: str) -> None:
    dir_name: str = temp_directory_fixture_
    fake_file: str = "/fake/fake_file.txt"
    with pytest.raises(
        IsADirectoryError, match=f"Expected file but, '{dir_name}' is a directory."
    ):
        FileFactory(dir_name).readlines()

    with pytest.raises(FileNotFoundError, match=f"File: '{fake_file}' not found."):
        FileFactory(fake_file).readlines()
    Path(dir_name).rmdir()


def test_read_write(common_file_factory_fixture_: FileFactory) -> None:
    file_f: FileFactory
    test_str: str = "Who the hell do you think I am!?\n"
    file_f = common_file_factory_fixture_
    with file_f.open_("w") as fh:
        fh.write(test_str)
        assert file_f.is_open is True

    assert file_f.is_open is False

    with file_f.open_("r") as fh:
        assert fh.read() == test_str
        assert file_f.is_open is True


def test_read(common_file_factory_fixture_: FileFactory) -> None:
    file_f: FileFactory
    test_str: str = "Basic test string"
    file_f = common_file_factory_fixture_
    with file_f.open_("w") as fh:
        fh.write(test_str)
    data: str = file_f.read()
    assert data == test_str


def test_read_disallow_comments(common_file_factory_fixture_: FileFactory) -> None:
    file_f: FileFactory = common_file_factory_fixture_
    with file_f.open_("w") as fh:
        fh.write('{"test": "yes","test2": "no",// "test3": "commented"\n}')
    assert file_f.read(allow_comments=False) == '{"test": "yes","test2": "no",\n}'


def test_read_allow_comments(common_file_factory_fixture_: FileFactory) -> None:
    file_f: FileFactory = common_file_factory_fixture_
    data: str = '{"test": "yes","test2": "no",// "test3": "commented"\n}'
    with file_f.open_("w") as fh:
        fh.write(data)
    assert file_f.read(allow_comments=True) == data


def test_readlines_disallow_comments(common_file_factory_fixture_: FileFactory) -> None:
    file_f: FileFactory = common_file_factory_fixture_
    with file_f.open_("w") as fh:
        fh.write('{"test": "yes",\n"test2": "no",\n// "test3": "commented"\n}')

    expected: list[str] = ['{"test": "yes",\n', '"test2": "no",\n', "\n", "}"]
    assert file_f.readlines(allow_comments=False) == expected


def test_readlines_allow_comments(common_file_factory_fixture_: FileFactory) -> None:
    file_f: FileFactory = common_file_factory_fixture_
    with file_f.open_("w") as fh:
        fh.write('{"test": "yes",\n"test2": "no",\n// "test3": "commented"\n}')

    expected: list[str] = [
        '{"test": "yes",\n',
        '"test2": "no",\n',
        '// "test3": "commented"\n',
        "}",
    ]
    assert file_f.readlines(allow_comments=True) == expected
