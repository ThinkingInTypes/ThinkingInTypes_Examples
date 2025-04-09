# example_3.py
from typing import NoReturn


def fatal_error(msg: str) -> NoReturn:
    raise RuntimeError(msg)
