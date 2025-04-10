# example_7.py
from book_utils import Catch


def add(a: int, b: int) -> int:
    return a + b


print(add(10, 5))
with Catch():
    add(10, "5")  # type: ignore
