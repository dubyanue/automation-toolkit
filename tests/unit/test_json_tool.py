from typing import Any

import pytest

from lib.file_lib.file_factory import FileFactory
from lib.file_lib.json_tool import json_read, json_write

# pylint: disable-next=unused-import
from lib.test_lib.test_fixures import json_file_factory_fixture


def test_json_read(
    json_file_factory_fixture_: tuple[FileFactory, str, dict[str, Any]],
) -> None:
    test_json: str
    test_dict: dict[str, Any]
    file_f: FileFactory
    file_f, test_json, test_dict = json_file_factory_fixture_
    with file_f._open("w") as fh:
        fh.write(test_json)
    assert json_read(file_f) == test_dict


def test_json_read_from_filename_str(
    json_file_factory_fixture_: tuple[FileFactory, str, dict[str, Any]],
) -> None:
    test_json: str
    test_dict: dict[str, Any]
    file_f: FileFactory
    file_f, test_json, test_dict = json_file_factory_fixture_
    with file_f._open("w") as fh:
        fh.write(test_json)
    assert json_read(str(file_f)) == test_dict


def test_json_read_with_comments(
    json_file_factory_fixture_: tuple[FileFactory, str, dict[str, Any]],
) -> None:
    test_json: str
    test_dict: dict[str, Any]
    file_f: FileFactory
    file_f, test_json, test_dict = json_file_factory_fixture_
    test_json = test_json.replace(
        r'"key2":1,"key3":true}', '// This is a comment\n"key2":1,"key3":true}'
    )
    with file_f._open("w") as fh:
        fh.write(test_json)
    assert json_read(file_f) == test_dict


def test_json_write(
    json_file_factory_fixture_: tuple[FileFactory, str, dict[str, Any]],
) -> None:
    test_json: str
    test_dict: dict[str, Any]
    file_f: FileFactory
    file_f, test_json, test_dict = json_file_factory_fixture_
    json_write(test_dict, file_f, None, sort_keys=False)
    assert file_f.read() == test_json


def test_json_write_to_filename_str(
    json_file_factory_fixture_: tuple[FileFactory, str, dict[str, Any]],
) -> None:
    test_json: str
    test_dict: dict[str, Any]
    file_f: FileFactory
    file_f, test_json, test_dict = json_file_factory_fixture_
    json_write(test_dict, str(file_f), None, sort_keys=False)
    assert file_f.read() == test_json


if __name__ == "__main__":
    import sys

    sys.exit(pytest.main())
