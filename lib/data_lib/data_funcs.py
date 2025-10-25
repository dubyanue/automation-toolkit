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


def generate_model_code_string(name: str, description: tuple[Any, ...]) -> str:
    """Generate Python code string for a BaseModel class from description."""
    column_name: str
    type_code: type
    is_nullable: bool

    lines = [
        "from typing import Optional",
        "from pydantic import BaseModel",
        "\n" * 2,
        f"class {name}(BaseModel):",
    ]

    for i in description:
        column_name, type_code, is_nullable = i[0], i[1], i[6]

        # Get the type name
        type_name = (
            type_code.__name__ if hasattr(type_code, "__name__") else str(type_code)
        )

        # Handle nullable fields
        if is_nullable:
            field_def = f"    {column_name}: Optional[{type_name}] = None"
        else:
            field_def = f"    {column_name}: {type_name}"

        lines.append(field_def)

    return "\n".join(lines)
