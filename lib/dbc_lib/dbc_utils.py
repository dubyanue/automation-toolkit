from dataclasses import dataclass


@dataclass
class QueryKwargs:
    columns: list[str] | None
    criteria: list[str] | None
    additionals: list[str] | None


def create_where(criteria: list[str] | None) -> str:
    return "" if not criteria else " WHERE " + " AND ".join(criteria)


def create_additionals(additionals: list[str] | None) -> str:
    return "" if not additionals else " " + ", ".join(additionals)


def create_columns(columns: list[str] | None) -> str:
    return "*" if not columns else ", ".join(columns)


def create_placeholders(headers: list[str]) -> str:
    return ",".join(["?" for _ in headers])


def is_columnized(column: str) -> bool:
    return column.startswith("[") and column.endswith("]")


def columnize(column: str) -> str:
    return column if is_columnized(column) else f"[{column}]"


def columnize_headers(headers: list[str]) -> str:
    columnized_headers: str = str(
        tuple(hd if is_columnized(hd) else columnize(hd) for hd in headers)
    )
    return columnized_headers.replace("'", "")


def create_select_query(table: str, query_kwargs: QueryKwargs) -> str:
    columns: str = create_columns(query_kwargs.columns)
    where_clause: str = create_where(query_kwargs.criteria)
    additionals: str = create_additionals(query_kwargs.additionals)
    return f"SELECT {columns} FROM {table}{where_clause}{additionals}"  # noqa:S608


def create_insert_query(
    table: str,
    headers: list[str],
) -> str:
    base: str = f"INSERT INTO {table} {columnize_headers(headers)}"
    base += f" VALUES ({create_placeholders(headers)})"

    return base
