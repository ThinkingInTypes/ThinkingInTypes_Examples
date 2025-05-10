# example_11.py
from typing import overload


@overload
def read(data: bytes) -> str: ...


@overload
def read(data: str) -> str: ...


def read(data: str | bytes) -> str:
    # single implementation handling both
    return data.decode() if isinstance(data, bytes) else data
