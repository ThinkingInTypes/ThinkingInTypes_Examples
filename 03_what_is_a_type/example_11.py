# example_11.py
from book_utils import Catch


def add(a: int, b: int) -> int:
    return a + b


print(add(10, 5))
with Catch():
    # Second arg is not an int:
    add(10, "5")  # type: ignore
