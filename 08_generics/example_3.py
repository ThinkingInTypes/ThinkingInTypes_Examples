# example_3.py
from typing import TypeVar

# Define a TypeVar that can only be int or float
Number = TypeVar('Number', int, float)

def add(a: Number, b: Number) -> Number:
    return a + b

add(5, 10)      # valid, both int
add(3.5, 2.5)   # valid, both float
add(5, 2.5)     # valid, int and float (both allowed types)
add("5", "2")   # ERROR: str not allowed for Number
