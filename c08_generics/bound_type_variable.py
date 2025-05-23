# bound_type_variable.py
from typing import Protocol, Any


class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...


def sort_items[U: Comparable](items: list[U]) -> list[U]:
    return sorted(items)
