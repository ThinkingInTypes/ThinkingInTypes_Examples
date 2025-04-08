# example_2.py
from typing import Union, NamedTuple


class Success(NamedTuple):
    result: str


class Error(NamedTuple):
    error: str


def process(response: Union[Success, Error]) -> str:
    match response:
        case Success(result):
            return f"Success: {result}"
        case Error(error):
            return f"Error: {error}"
        case _:
            raise ValueError("Unhandled response type")
