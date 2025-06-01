# year.py
from dataclasses import dataclass


@dataclass(frozen=True)
class Year:
    value: int

    def __post_init__(self) -> None:
        if self.value <= 0:
            raise ValueError(f"Invalid year: {self.value}")
