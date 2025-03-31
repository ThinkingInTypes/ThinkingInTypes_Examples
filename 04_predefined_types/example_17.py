# example_17.py
from book_utils import Catch

def calculate_area(radius: int) -> float:
    return 3.14 * radius**2

with Catch():
    calculate_area(3.5)  # Flagged by static type checker
