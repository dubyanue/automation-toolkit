from collections.abc import Generator
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import TYPE_CHECKING, Any

import pytest
from runfiles import Runfiles

from lib.config_lib import config
from lib.dbc_lib.dbc import PyODBC, SQLite
from lib.dbc_lib.dbc_utils import QueryKwargs, create_basic_connstring
from lib.file_lib.file_factory import FileFactory
from lib.file_lib.json_tool import json_write
from lib.logger_lib.logger import get_logger

if TYPE_CHECKING:
    from logging import Logger


def create_named_file(
    data: str | None = None,
    mode: str = "w+",
    suffix: str | None = None,
    *,
    delete: bool = False,
) -> str:
    filename: str
    with NamedTemporaryFile(
        mode=mode, delete=delete, encoding="utf-8", suffix=suffix
    ) as tmp:
        filename = tmp.name
        if data:
            tmp.write(data)
    return filename


@pytest.fixture(name="common_file_factory_fixture_")
def common_file_factory_fixture() -> Generator[FileFactory]:
    filename_: str = create_named_file()
    file_factory_: FileFactory = FileFactory(filename_)
    yield file_factory_

    if (file_path := Path(filename_)).exists():
        file_path.unlink(missing_ok=True)


@pytest.fixture(name="json_file_factory_fixture_")
def json_file_factory_fixture() -> Generator[tuple[FileFactory, str, dict[str, Any]]]:
    # Setup
    test_json: str = '{"key1":"val1","key2":1,"key3":true}'
    test_dict: dict[str, Any] = {"key1": "val1", "key2": 1, "key3": True}
    filename_: str = create_named_file(suffix=".json")
    file_factory_: FileFactory = FileFactory(filename_)
    yield (file_factory_, test_json, test_dict)

    if (file_path := Path(filename_)).exists():
        file_path.unlink(missing_ok=True)


@pytest.fixture(name="json_database_config_fixture_")
def json_database_config_fixture() -> Generator[config.JsonDatabaseConfiguration]:
    # Setup
    test_creds: dict[str, str] = {
        "username": "user1",
        "password": "pass1",
        "server": "server1",
        "driver": "driver1",
        "database": "database1",
    }
    filename_: str = create_named_file(suffix=".json")
    file_factory_: FileFactory = FileFactory(filename_)
    json_write(test_creds, file_factory_)
    jdc: config.JsonDatabaseConfiguration = config.JsonDatabaseConfiguration(
        file_factory_
    )
    yield jdc

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
    logger: Logger = get_logger(basic_sqlite_db_fixture.__name__)

    r = Runfiles.Create()
    sqlite: SQLite | None = None
    if r:
        sql_file = r.Rlocation(f"automation-toolkit/{db_file_path}")
        if sql_file and Path(sql_file).exists():
            sqlite = SQLite(sql_file, logger)

    if db_file_path.exists():
        sqlite = SQLite(db_file_path, logger)

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


@pytest.fixture(name="basic_pyodbc_db_fixture_")
def basic_pyodbc_db_fixture() -> Generator[PyODBC]:
    db_file_path = FileFactory("tests/data/test.db")
    logger: Logger = get_logger(basic_pyodbc_db_fixture.__name__)

    r = Runfiles.Create()
    pyodbc_: PyODBC | None = None
    sql_file: FileFactory | str | None = None

    creds: dict[str, str] = {"driver": "SQLite3"}

    if r:
        sql_file = r.Rlocation(f"automation-toolkit/{db_file_path}")
        if sql_file and Path(sql_file).exists():
            creds["database"] = sql_file

    if not sql_file and db_file_path.exists():
        creds["database"] = str(db_file_path)

    conn_str: str = create_basic_connstring(**creds)

    pyodbc_ = PyODBC(conn_str, logger)

    if pyodbc_:
        yield pyodbc_

        if pyodbc_.is_connected():
            pyodbc_.disconnect()
    else:
        err_msg: str = f"Could not find test database at {db_file_path}"
        raise FileNotFoundError(err_msg)
