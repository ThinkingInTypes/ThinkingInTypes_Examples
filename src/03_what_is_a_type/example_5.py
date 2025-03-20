# example_5.py
# mypy detects this error before running
def add(a: int, b: int) -> int:
    return a + b


add(1, "2")  # Static type checker flags this
