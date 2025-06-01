# day.py
from typing import Self
from dataclasses import dataclass
from month import Month


@dataclass(frozen=True)
class Day:
    value: int

    def __post_init__(self) -> None:
        if self.value <= 0:
            raise ValueError(f"Invalid day: {self.value}")

    @classmethod
    def of(cls, month: Month, day: int) -> Self:
        # Ensure day is within Month's range:
        month.valid_day(day)
        return cls(day)
