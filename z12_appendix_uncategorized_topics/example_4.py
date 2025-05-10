# example_4.py


def process(value: int | str) -> None:
    if isinstance(value, int):
        print(value + 1)
    else:
        print(value.upper())
