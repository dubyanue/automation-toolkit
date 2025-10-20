from lib.dbc_lib import dbc_utils
from lib.dbc_lib.dbc import SQLite

# pylint: disable-next=unused-import
from lib.test_lib.test_fixures import (
    basic_sqlite_db_fixture,
    create_db_sqlite_db_fixture,
)


def test_sqlite_smoke_test_database(basic_sqlite_db_fixture_: SQLite) -> None:
    sqlite: SQLite = basic_sqlite_db_fixture_
    criteria: list[str] = ["ID=3"]
    query_kwargs: dbc_utils.QueryKwargs = dbc_utils.QueryKwargs(None, criteria, None)
    select_query: str = dbc_utils.create_select_query("Animes", query_kwargs)
    assert not sqlite.is_connected()
    if curs := sqlite.execute(select_query):
        assert sqlite.is_connected()
        assert curs.fetchone() == (3, "Bleach", 10.0)


def test_sqlite_connect_disconnect(basic_sqlite_db_fixture_: SQLite) -> None:
    sqlite: SQLite = basic_sqlite_db_fixture_
    assert not sqlite.is_connected()
    assert sqlite.connect() is not None
    assert sqlite.is_connected()
    sqlite.disconnect()
    assert not sqlite.is_connected()


def test_sqlite_bad_connection(basic_sqlite_db_fixture_: SQLite) -> None:
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


def test_sqlite_fetchone(basic_sqlite_db_fixture_: SQLite) -> None:
    sqlite: SQLite = basic_sqlite_db_fixture_
    query: str = dbc_utils.create_select_query(
        "Animes", dbc_utils.QueryKwargs(None, None, ["ORDER BY ID"])
    )
    assert sqlite.fetchone(query) == (1, "One Piece", 9.0)


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
    sqlite.executemany(insert_query, data)
    assert sqlite.fetchall(select_query) == data


def test_sqlite_backup(basic_sqlite_db_fixture_: SQLite) -> None:
    sqlite: SQLite = basic_sqlite_db_fixture_
    sqlite2: SQLite = SQLite()
    query: str = dbc_utils.create_select_query(
        "Animes", dbc_utils.QueryKwargs(None, None, ["ORDER BY ID"])
    )
    assert not sqlite2.fetchall(query)
    if sqlite2.cnxn:
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
