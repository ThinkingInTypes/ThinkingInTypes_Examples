# example_5.py
from returns.result import Result, Success, Failure, safe


@safe
def divide(a: int, b: int) -> float:
    return a / b
