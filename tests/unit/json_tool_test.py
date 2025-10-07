from collections.abc import Generator
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Any

import pytest

from lib.file_libs.file_factory import FileFactory
from lib.file_libs.json_tool import json_read, json_write


@pytest.fixture(name="file_factory")
def fixture_file_factory() -> Generator[tuple[FileFactory, str, dict[str, Any]]]:
    # Setup
    test_json: str = '{"key1":"val1","key2":1,"key3":true}'
    test_dict: dict[str, Any] = {"key1": "val1", "key2": 1, "key3": True}
    with NamedTemporaryFile(
        mode="w+", delete=False, encoding="utf-8", suffix=".json"
    ) as tmp:
        filename_: str = tmp.name

    file_factory_: FileFactory = FileFactory(filename_)
    yield (file_factory_, test_json, test_dict)

    if (file_path := Path(filename_)).exists():
        file_path.unlink(missing_ok=True)


def test_json_read(file_factory: tuple[FileFactory, str, dict[str, Any]]) -> None:
    test_json: str
    test_dict: dict[str, Any]
    file_f: FileFactory
    file_f, test_json, test_dict = file_factory
    with file_f._open("w") as fh:
        fh.write(test_json)
    assert json_read(file_f) == test_dict


def test_json_read_with_comments(
    file_factory: tuple[FileFactory, str, dict[str, Any]],
) -> None:
    test_json: str
    test_dict: dict[str, Any]
    file_f: FileFactory
    file_f, test_json, test_dict = file_factory
    test_json = test_json.replace(
        r'"key2":1,"key3":true}', '// This is a comment\n"key2":1,"key3":true}'
    )
    with file_f._open("w") as fh:
        fh.write(test_json)
    assert json_read(file_f) == test_dict


def test_json_write(file_factory: tuple[FileFactory, str, dict[str, Any]]) -> None:
    test_json: str
    test_dict: dict[str, Any]
    file_f: FileFactory
    file_f, test_json, test_dict = file_factory
    json_write(test_dict, file_f, None, sort_keys=False)
    assert file_f.read() == test_json


if __name__ == "__main__":
    import sys

    sys.exit(pytest.main())
