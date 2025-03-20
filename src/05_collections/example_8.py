# example_8.py
from typing import Iterable, Iterator


def print_items(items: Iterable[str]) -> None:
    for item in items:
        print(item)


def generate_numbers(n: int) -> Iterator[int]:
    for i in range(n):
        yield i
