# example_1.py
from typing import Protocol


class Speaker(Protocol):
    def speak(self) -> str: ...
