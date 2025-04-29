# example_6.py
from typing import TypeVar

T = TypeVar("T")


def identity(item: T) -> T:
    return item
