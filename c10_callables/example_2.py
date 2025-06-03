# example_2.py
# ruff: noqa: E731
from typing import Callable

adder: Callable[[int, int], int] = lambda x, y: x + y  # type: ignore
