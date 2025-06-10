# example_3.py
from typing import Never


def fatal_error(msg: str) -> Never:
    raise RuntimeError(msg)
