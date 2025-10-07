import json
from typing import Any

from lib.file_libs.file_factory import FileFactory


def json_read(file: str | FileFactory) -> dict[str, Any]:
    if isinstance(file, str):
        file = FileFactory(file)
    file_data: str = file.read(allow_comments=False)
    data: dict[str, Any] = json.loads(file_data)
    return data


def json_write(
    item: dict[str, Any] | list[Any],
    file: str | FileFactory,
    indent: int | None = 4,
    *,
    sort_keys: bool = True,
) -> None:
    if isinstance(file, str):
        file = FileFactory(file)
    with file.open("w") as fh:
        json.dump(item, fh, indent=indent, separators=(",", ":"), sort_keys=sort_keys)
