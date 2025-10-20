from lib.dbc_lib import dbc_utils

# pylint: disable-next=unused-import
from lib.test_lib.test_fixures import basic_dbc_criteria_fixture


def test_create_where(basic_dbc_criteria_fixture_: dbc_utils.QueryKwargs) -> None:
    where_clause: str = dbc_utils.create_where(basic_dbc_criteria_fixture_.criteria)
    assert where_clause == " WHERE Col1='Val1' AND Col2='Val2'"


def test_create_where_empty() -> None:
    assert not dbc_utils.create_where(None)


def test_create_additionals_and_columns(
    basic_dbc_criteria_fixture_: dbc_utils.QueryKwargs,
) -> None:
    additionals: str = dbc_utils.create_additionals(basic_dbc_criteria_fixture_.columns)
    columns: str = dbc_utils.create_columns(basic_dbc_criteria_fixture_.columns)
    assert additionals == " Col1, Col2, Col3"
    assert " " + columns == additionals


def test_create_additionals_empty() -> None:
    assert not dbc_utils.create_additionals(None)


def test_create_columns_empty() -> None:
    assert dbc_utils.create_columns(None) == "*"


def test_basic_create_select_query(
    basic_dbc_criteria_fixture_: dbc_utils.QueryKwargs,
) -> None:
    table: str = "TestTable"
    query: str = dbc_utils.create_select_query(table, basic_dbc_criteria_fixture_)
    expected: str = f"SELECT Col1, Col2, Col3 FROM {table}"
    expected += " WHERE Col1='Val1' AND Col2='Val2' ORDER BY Col1 DESC, Col2 ASC"
    assert query == expected


def test_create_select_query_no_columns(
    basic_dbc_criteria_fixture_: dbc_utils.QueryKwargs,
) -> None:
    table: str = "TestTable"
    basic_dbc_criteria_fixture_.columns = None
    query: str = dbc_utils.create_select_query(table, basic_dbc_criteria_fixture_)
    expected: str = f"SELECT * FROM {table}"
    expected += " WHERE Col1='Val1' AND Col2='Val2' ORDER BY Col1 DESC, Col2 ASC"
    assert query == expected


def test_create_select_query_barebones(
    basic_dbc_criteria_fixture_: dbc_utils.QueryKwargs,
) -> None:
    table: str = "TestTable"
    basic_dbc_criteria_fixture_.columns = None
    basic_dbc_criteria_fixture_.criteria = None
    basic_dbc_criteria_fixture_.additionals = None
    query: str = dbc_utils.create_select_query(table, basic_dbc_criteria_fixture_)
    expected: str = f"SELECT * FROM {table}"
    assert query == expected


def test_create_placeholders(
    basic_dbc_criteria_fixture_: dbc_utils.QueryKwargs,
) -> None:
    if headers := basic_dbc_criteria_fixture_.columns:
        assert dbc_utils.create_placeholders(headers) == "?,?,?"


def test_columnize_not_columnized() -> None:
    assert dbc_utils.columnize("Column1") == "[Column1]"


def test_columnize() -> None:
    col = "[Column1]"
    assert dbc_utils.columnize(col) == col


def test_columnize_headers() -> None:
    assert (
        dbc_utils.columnize_headers(["Col1", "[Col2]", "Col3"])
        == "([Col1], [Col2], [Col3])"
    )


def test_create_insert_query(
    basic_dbc_criteria_fixture_: dbc_utils.QueryKwargs,
) -> None:
    table: str = "TestTable"
    if headers := basic_dbc_criteria_fixture_.columns:
        insert_query: str = dbc_utils.create_insert_query(table, headers)

        assert (
            f"INSERT INTO {table} ([Col1], [Col2], [Col3]) VALUES (?,?,?)"
            == insert_query
        )
