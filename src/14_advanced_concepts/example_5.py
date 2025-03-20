# example_5.py
from typing import Optional


def greet(name: Optional[str]) -> None:
    assert name is not None, "Name cannot be None"
    print(f"Hello, {name}")
