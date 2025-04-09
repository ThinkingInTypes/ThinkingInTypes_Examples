# example_7.py
from typing import Generic, TypeVar

T_co = TypeVar("T_co", covariant=True)


class ReadOnlyList(Generic[T_co]):
    def __init__(self, items: list[T_co]):
        self.items = items


ints: ReadOnlyList[int] = ReadOnlyList([1, 2, 3])
numbers: ReadOnlyList[float] = (
    ints  # Valid due to covariance
)
