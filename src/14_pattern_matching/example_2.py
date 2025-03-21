# example_2.py
from typing import Union


class Success:
    def __init__(self, result: str):
        self.result = result


class Error:
    def __init__(self, error: str):
        self.error = error


def process(response: Union[Success, Error]) -> str:
    match response := response:
        case Success(result=result):
            return f"Success: {result}"
        case Error(error):
            return f"Error: {error}"
