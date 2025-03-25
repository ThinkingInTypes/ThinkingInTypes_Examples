# example_3.py
from typing import TypeVar

U = TypeVar("U", int, float)


def add(a: U, b: U) -> U:
    return a + b


add(1, 2)  # valid
add(1.5, 2.5)  # valid
# add("a", "b")  # invalid, detected by type checker
