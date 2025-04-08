# example_11.py
from typing import overload, Union


@overload
def read(data: bytes) -> str: ...


@overload
def read(data: str) -> str: ...


def read(data: Union[str, bytes]) -> str:
    # single implementation handling both  
    return data.decode() if isinstance(data, bytes) else data
