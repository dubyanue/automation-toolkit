from collections.abc import Generator
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Any

import pytest
from runfiles import Runfiles

from lib.dbc_lib.dbc import SQLite
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


@pytest.fixture(name="basic_sqlite_db_fixture_")
def basic_sqlite_db_fixture() -> Generator[SQLite]:
    db_file_path = FileFactory("tests/data/test.db")

    r = Runfiles.Create()
    sqlite: SQLite | None = None
    if r:
        sql_file = r.Rlocation(f"automation-toolkit/{db_file_path}")
        if sql_file and Path(sql_file).exists():
            sqlite = SQLite(sql_file)

    if db_file_path.exists():
        sqlite = SQLite(db_file_path)

    if sqlite:
        yield sqlite

        if sqlite.is_connected():
            sqlite.disconnect()
    else:
        err_msg: str = f"Could not find test database at {db_file_path}"
        raise FileNotFoundError(err_msg)


@pytest.fixture(name="create_db_sqlite_db_fixture_")
def create_db_sqlite_db_fixture() -> Generator[SQLite]:
    db_file_path = FileFactory("tests/data/test.sql")

    r = Runfiles.Create()
    sqlite: SQLite = SQLite()
    if r:
        sql_file = r.Rlocation(f"automation-toolkit/{db_file_path}")
        if sql_file and Path(sql_file).exists():
            db_file_path = FileFactory(sql_file)

    if db_file_path.exists():
        with db_file_path.open("r") as fh:
            sqlite.executescript(fh.read())

    yield sqlite

    if sqlite.is_connected():
        sqlite.disconnect()
