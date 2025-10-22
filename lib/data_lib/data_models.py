from typing import Any

from pydantic import BaseModel, create_model


def generate_model_from_description(
    name: str, description: tuple[Any, ...]
) -> BaseModel:
    column_name: str
    type_code: type
    is_nullable: bool

    fields: dict[str, tuple[Any, ...]] = {}

    for i in description:
        column_name, type_code, is_nullable = i[0], i[1], i[6]
        type_data: tuple[Any, ...] = (
            (type_code | None, None) if is_nullable else (type_code, ...)
        )

        fields[column_name] = type_data

    return create_model(f"{name}Model", **fields)  # type: ignore
