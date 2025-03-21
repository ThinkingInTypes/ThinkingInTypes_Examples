# example_4.py
from typing import Union


def process(value: Union[int, str]) -> None:
    if isinstance(value, int):
        print(value + 1)
    else:
        print(value.upper())
