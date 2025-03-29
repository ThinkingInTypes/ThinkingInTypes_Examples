# example_5.py


def add(a: int, b: int) -> int:
    return a + b


add(1, "2")  # R: Static type checker flags this
