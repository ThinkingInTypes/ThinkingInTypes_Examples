# example_2.py
from typing import Callable

adder: Callable[[int, int], int] = lambda x, y: x + y  # type: ignore
