# example_5.py
from book_utils import Catch


def add(a: int, b: int) -> int:
    return a + b

with Catch():
    add(1, "2")  # Static type checker flags this
