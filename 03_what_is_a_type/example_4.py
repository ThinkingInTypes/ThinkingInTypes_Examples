# example_4.py
from book_utils import Catch


def add(a, b):
    return a + b


with Catch():
    add(1, "2")  # raises runtime TypeError
## Error: unsupported operand type(s) for +: 'int'
## and 'str'
