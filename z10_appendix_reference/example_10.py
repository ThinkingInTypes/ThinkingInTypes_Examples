# example_10.py
from typing import Callable


def apply_to_ints(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)
