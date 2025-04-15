# multiple_typevars.py
from typing import TypeVar

A = TypeVar('A')
B = TypeVar('B')


def pairify(x: A, y: B) -> tuple[A, B]:
    return (x, y)


result = pairify("Alice", 5)
# result has type tuple[str, int]
