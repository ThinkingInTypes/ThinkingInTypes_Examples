# generic_alias.py
from typing import TypeVar

T = TypeVar("T")
Pair = tuple[T, T]  # A pair of two items of the same type
StrDict = dict[
    str, T
]  # A dictionary with string keys and values of type T
