# bound_typevar.py
from typing import Protocol, Any


class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...


def sort_items[U](items: list[U]) -> list[U]:
    return sorted(items)
