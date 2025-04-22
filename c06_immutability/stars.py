# stars.py
from dataclasses import dataclass


@dataclass(frozen=True)
class Stars:
    number: int

    def __post_init__(self) -> None:
        assert 1 <= self.number <= 10, f"{self}"
