# example_6.py
from typing import Callable, TypeAlias

RequestHandler: TypeAlias = Callable[[str, dict], dict]


def handle_request(
    path: str, handler: RequestHandler
) -> dict:
    response = handler(path, {})
    return response
