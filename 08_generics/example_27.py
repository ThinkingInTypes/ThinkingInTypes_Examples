# example_27.py
from typing import TypeVar
T = TypeVar('T')
def sort_items(items: list[T]) -> list[T]:
    return sorted(items)
