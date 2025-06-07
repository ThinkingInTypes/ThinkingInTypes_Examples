# example_1.py
from book_utils import Catch


def add(x: int, y: int) -> int:
    return x + y


# Without ignore, this produces a type error (int vs. str):
with Catch():
    result = add(5, "7")  # type: ignore
