# constrained_typevar.py
from typing import TypeVar

# Define a TypeVar that can only be int or float
Number = TypeVar("Number", int, float)


def add(a: Number, b: Number) -> Number:
    print(a + b)
    return a + b


add(5, 10)  # valid, both int
## 15
add(3.5, 2.5)  # valid, both float
## 6.0
# valid, int and float are both allowed types:
add(5, 2.5)
## 7.5
# ERROR: str not allowed for Number:
add("A", "Z")  # type: ignore
## AZ
