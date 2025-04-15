# example_7.py
from typing import Protocol


class Handler(Protocol):
    def __call__(self, request: dict) -> dict: ...


def process_request(
        handler: Handler, request: dict
) -> dict:
    return handler(request)
