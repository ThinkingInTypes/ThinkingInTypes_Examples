# example_14.py
from typing import TypeGuard


def is_str_list(
        vals: list[object],
) -> TypeGuard[list[str]]:
    return all(isinstance(x, str) for x in vals)
