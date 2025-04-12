# example_1.py
from typing import TypeVar

T = TypeVar("T")


def first_item(items: list[T]) -> T:
    return items[0]


print(first_item([1, 2, 3]))  # returns int
## 1
print(first_item(["a", "b"]))  # returns str
## a
