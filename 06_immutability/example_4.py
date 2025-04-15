# example_4.py
from typing import Final
from dataclasses import dataclass


@dataclass
class User:
    name: Final[str] = "Uninitialized"
    id: Final[int] = -1

    def __init__(self, name: str, id: int):
        object.__setattr__(self, "name", name)
        object.__setattr__(self, "id", id)
