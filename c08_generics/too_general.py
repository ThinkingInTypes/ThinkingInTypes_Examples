# too_general.py
from typing import TypeVar, Iterable

T = TypeVar("T")


def sort_items(items: list[T]) -> list[T]:
    # PyRight issue:
    return sorted(items)  # type: ignore
