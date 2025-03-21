# example_1.py
def calculate(value: int) -> int | str:
    if value == 1:
        return "Invalid argument"
    return value * 2
