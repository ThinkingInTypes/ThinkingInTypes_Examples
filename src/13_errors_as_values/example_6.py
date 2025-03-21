# example_6.py
from returns.result import Result, Success, Failure

def func_a(val: int) -> Result[int, str]:
    if val == 1:
        return Failure("Cannot handle 1")
    return Success(val * 10)

def func_b(val: int) -> Result[int, str]:
    if val == 3:
        return Failure("Division by zero risk")
    return Success(val - 1)

def workflow(x: int) -> Result[int, str]:
    return calculate(x).bind(func_b).bind(func_c)
