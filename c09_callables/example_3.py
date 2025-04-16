# example_3.py
from typing import Callable


def operate(
        a: int, b: int, func: Callable[[int, int], int]
) -> int:
    return func(a, b)


result = operate(
    5, 3, lambda x, y: x * y
)  # returns 15
