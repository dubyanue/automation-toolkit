from collections.abc import Generator
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Any

import pytest

from lib.dbc_lib.dbc_utils import QueryKwargs
from lib.file_lib.file_factory import FileFactory


@pytest.fixture(name="common_file_factory_fixture_")
def common_file_factory_fixture() -> Generator[FileFactory]:
    with NamedTemporaryFile(mode="w+", delete=False, encoding="utf-8") as tmp:
        filename_: str = tmp.name

    file_factory_: FileFactory = FileFactory(filename_)
    yield file_factory_

    if (file_path := Path(filename_)).exists():
        file_path.unlink(missing_ok=True)


@pytest.fixture(name="json_file_factory_fixture_")
def json_file_factory_fixture() -> Generator[tuple[FileFactory, str, dict[str, Any]]]:
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


@pytest.fixture(name="basic_dbc_criteria_fixture_")
def basic_dbc_criteria_fixture() -> QueryKwargs:
    test_columns: list[str] = ["Col1", "Col2", "Col3"]
    test_criteria: list[str] = ["Col1='Val1'", "Col2='Val2'"]
    test_additionals: list[str] = ["ORDER BY Col1 DESC", "Col2 ASC"]
    return QueryKwargs(test_columns, test_criteria, test_additionals)
