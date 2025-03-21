# example_3.py
def calculate(value: int) -> Result[int, str]:
    if value == 1:
        return Failure("Invalid argument")
    return Success(value * 2)
