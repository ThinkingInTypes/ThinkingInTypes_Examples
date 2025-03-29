# example_5.py
from dataclasses import dataclass


@dataclass(frozen=True)
class Stars:
    stars: int

    def __post_init__(self):
        assert 1 <= self.stars <= 10, "Stars rating must be between 1 and 10."
