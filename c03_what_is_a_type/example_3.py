# example_3.py
from book_utils import Catch

x = 10
with Catch():
    # Can't add a str to an int:
    result = x + "world"  # type: ignore
