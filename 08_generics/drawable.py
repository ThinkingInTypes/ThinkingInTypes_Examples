# drawable.py
from typing import Protocol


class Drawable(Protocol):
    def draw(self) -> None:
        ...
