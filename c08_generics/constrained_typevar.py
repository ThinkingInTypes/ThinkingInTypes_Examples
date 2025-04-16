# constrained_typevar.py
from typing import Protocol, Any, TypeVar


class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...


U = TypeVar("U", bound=Comparable)


def sort_items(items: list[U]) -> list[U]:
    return sorted(items)
