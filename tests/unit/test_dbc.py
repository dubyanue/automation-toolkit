from typing import TYPE_CHECKING

from lib.dbc_lib import dbc_utils
from lib.dbc_lib.dbc import DBConnection, PyODBC, SQLite

# pylint: disable-next=unused-import
from tests.test_fixtures import (
    basic_pyodbc_db_fixture,
    basic_sqlite_db_fixture,
    create_db_sqlite_db_fixture,
)

if TYPE_CHECKING:
    import sqlite3


def test_sqlite_smoke_test_database(basic_sqlite_db_fixture_: SQLite) -> None:
    sqlite: SQLite = basic_sqlite_db_fixture_
    criteria: list[str] = ["ID=3"]
    query_kwargs: dbc_utils.QueryKwargs = dbc_utils.QueryKwargs(None, criteria, None)
    select_query: str = dbc_utils.create_select_query("Animes", query_kwargs)
    assert not sqlite.is_connected()
    curs = sqlite.execute(select_query)
    assert sqlite.is_connected()
    assert curs is not None
    assert curs.fetchone() == (3, "Bleach", 10.0)
    curs.close()


def test_sqlite_connect_disconnect(basic_sqlite_db_fixture_: SQLite) -> None:
    sqlite: SQLite = basic_sqlite_db_fixture_
    assert not sqlite.is_connected()
    cnxn: DBConnection = sqlite.connect()
    assert cnxn is not None
    assert sqlite.is_connected()
    assert sqlite.connect() is cnxn
    sqlite.disconnect()
    sqlite.connect()
    sqlite._autocommit = False
    sqlite.disconnect()
    assert not sqlite.is_connected()


def test_sqlite_bad_operation(basic_sqlite_db_fixture_: SQLite) -> None:
    sqlite: SQLite = basic_sqlite_db_fixture_
    query: str = "SELECT * FROM FakeTable"
    assert not sqlite.execute(query)


def test_sqlite_fetchall(basic_sqlite_db_fixture_: SQLite) -> None:
    sqlite: SQLite = basic_sqlite_db_fixture_
    query: str = dbc_utils.create_select_query(
        "Animes", dbc_utils.QueryKwargs(None, None, ["ORDER BY ID"])
    )
    expected = [
        (1, "One Piece", 9.0),
        (2, "Naruto Shippuden", 10.0),
        (3, "Bleach", 10.0),
        (4, "Hunter X Hunter", 8.5),
        (5, "Naruto", 8.0),
        (6, "Berserk", 10.0),
        (7, "Fullmetal Alchemist: Brotherhood", 9.2),
        (8, "Code Geass", 8.9),
        (9, "Trigun", 8.2),
        (10, "Attack On Titan", 8.5),
    ]
    assert sqlite.fetchall(query) == expected


def test_sqlite_fetchmany(basic_sqlite_db_fixture_: SQLite) -> None:
    sqlite: SQLite = basic_sqlite_db_fixture_
    query: str = dbc_utils.create_select_query(
        "Animes", dbc_utils.QueryKwargs(None, None, ["ORDER BY ID"])
    )
    expected = [
        (1, "One Piece", 9.0),
        (2, "Naruto Shippuden", 10.0),
        (3, "Bleach", 10.0),
        (4, "Hunter X Hunter", 8.5),
        (5, "Naruto", 8.0),
    ]
    assert sqlite.fetchmany(query, 5) == expected
    assert not sqlite.fetchmany("SELECT * FROM FAKE")


def test_sqlite_fetchone(basic_sqlite_db_fixture_: SQLite) -> None:
    sqlite: SQLite = basic_sqlite_db_fixture_
    query: str = dbc_utils.create_select_query(
        "Animes", dbc_utils.QueryKwargs(None, None, ["ORDER BY ID"])
    )
    assert sqlite.fetchone(query) == (1, "One Piece", 9.0)
    assert not sqlite.fetchone("SELECT * FROM FAKE")


def test_sqlite_executemany(create_db_sqlite_db_fixture_: SQLite) -> None:
    table: str = "Characters"
    sqlite: SQLite = create_db_sqlite_db_fixture_
    select_query: str = dbc_utils.create_select_query(
        table, dbc_utils.QueryKwargs(None, ["ID IN (7,8,9)"], ["ORDER BY ID"])
    )
    assert not sqlite.fetchall(select_query)
    data = [
        (7, "Rukia Kuchiki", 3),
        (8, "Alphonse Elric", 7),
        (9, "Roronoa Zoro", 1),
    ]
    headers: list[str] = sqlite.get_headers(table)
    insert_query: str = dbc_utils.create_insert_query(table, headers)
    curs = sqlite.executemany(insert_query, data)
    assert curs is not None
    curs.close()
    assert sqlite.fetchall(select_query) == data


def test_sqlite_backup(basic_sqlite_db_fixture_: SQLite) -> None:
    sqlite2: SQLite = SQLite()
    query: str = dbc_utils.create_select_query(
        "Animes", dbc_utils.QueryKwargs(None, None, ["ORDER BY ID"])
    )
    assert not sqlite2.fetchall(query)
    assert sqlite2.cnxn is not None
    with basic_sqlite_db_fixture_ as sqlite:
        sqlite.backup(sqlite2.cnxn)

    expected = [
        (1, "One Piece", 9.0),
        (2, "Naruto Shippuden", 10.0),
        (3, "Bleach", 10.0),
        (4, "Hunter X Hunter", 8.5),
        (5, "Naruto", 8.0),
        (6, "Berserk", 10.0),
        (7, "Fullmetal Alchemist: Brotherhood", 9.2),
        (8, "Code Geass", 8.9),
        (9, "Trigun", 8.2),
        (10, "Attack On Titan", 8.5),
    ]
    assert sqlite2.fetchall(query) == expected


def test_mapped_fetchone(basic_pyodbc_db_fixture_: PyODBC) -> None:
    query: str = dbc_utils.create_select_query(
        "Animes",
        dbc_utils.QueryKwargs(None, ["Name='One Piece'"], None),
    )
    expected: dict[str, str | float] = {"ID": 1, "Name": "One Piece", "Rating": 9}
    pyodbc_: PyODBC = basic_pyodbc_db_fixture_
    # NOTE Not using context manager to allow fixsture to disconnect
    assert pyodbc_.fetchone(query, mapped=True) == expected


def test_mapped_fetchmany(basic_pyodbc_db_fixture_: PyODBC) -> None:
    query: str = dbc_utils.create_select_query(
        "Animes",
        dbc_utils.QueryKwargs(None, ["Name='One Piece'"], None),
    )
    expected: dict[str, str | float] = {"ID": 1, "Name": "One Piece", "Rating": 9}
    with basic_pyodbc_db_fixture_ as pyodbc_:
        assert pyodbc_.fetchmany(query, 1, mapped=True) == [expected]


def test_pyodbc_connect_disconnect(basic_pyodbc_db_fixture_: PyODBC) -> None:
    pyodbc_: PyODBC = basic_pyodbc_db_fixture_
    assert not pyodbc_.is_connected()
    cnxn: DBConnection = pyodbc_.connect()
    assert cnxn is not None
    assert pyodbc_.is_connected()
    assert pyodbc_.connect() is cnxn
    pyodbc_.disconnect()
    pyodbc_.connect()
    pyodbc_._autocommit = False
    pyodbc_.disconnect()
    assert not pyodbc_.is_connected()


def test_pyodbc_failed_executmany(basic_pyodbc_db_fixture_: PyODBC) -> None:
    data: tuple[tuple[int, int], ...] = ((1, 2), (3, 4))
    with basic_pyodbc_db_fixture_ as pyodbc_:
        assert not (
            pyodbc_.executemany("INSERT INTO FAKE([ID], [Name]) VALUES(?,?)", data)
        )


def test_sqlite_failed_executescript(basic_sqlite_db_fixture_: SQLite) -> None:
    sqlite: SQLite = basic_sqlite_db_fixture_
    assert not sqlite.executescript("INSERT INTO FAKE([ID], [Name]) VALUES(?,?)")
    sqlite._logger = None
    assert not sqlite.executescript("INSERT INTO FAKE([ID], [Name]) VALUES(?,?)")
