# month_value.py
from dataclasses import dataclass
from enum import Enum
from typing import Self


@dataclass(frozen=True)
class MonthValue:
    number: int
    days: int  # Number of days in the month

    def __post_init__(self) -> None:
        if not 1 <= self.number <= 12:
            raise ValueError(
                f"Invalid month number: {self.number}"
            )
        if not 1 <= self.days <= 31:
            raise ValueError(
                f"Invalid days in month: {self.days}"
            )
