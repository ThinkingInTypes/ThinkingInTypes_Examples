# example_5.py
from book_utils import Catch


def add(a: int, b: int) -> int:
    return a + b


with Catch():
    # Static type checker flags this:
    add(1, "2")  # type: ignore
## Error: unsupported operand type(s) for +: 'int'
## and 'str'
