# type_safe_date.py
from dataclasses import dataclass
from enum import Enum

@dataclass(frozen=True)
class MonthValue:
    number: int
    days: int    # Number of days in the month

    def __post_init__(self) -> None:
        if not 1 <= self.number <= 12:
            raise ValueError(f"Invalid month number: {self.number}")
        if not 1 <= self.days <= 31:
            raise ValueError(f"Invalid days in month: {self.days}")

    def valid_day(self, day: int) -> None:
        if not 1 <= day <= self.days:
            raise ValueError(f"Invalid day {day} for month {self.number}")

class Month(Enum):  # Enum[MonthValue]
    JANUARY = MonthValue(1, 31)
    FEBRUARY = MonthValue(2, 28)
    MARCH = MonthValue(3, 31)
    APRIL = MonthValue(4, 30)
    MAY = MonthValue(5, 31)
    JUNE = MonthValue(6, 30)
    JULY = MonthValue(7, 31)
    AUGUST = MonthValue(8, 31)
    SEPTEMBER = MonthValue(9, 30)
    OCTOBER = MonthValue(10, 31)
    NOVEMBER = MonthValue(11, 30)
    DECEMBER = MonthValue(12, 31)

    def __str__(self) -> str:
        return self.name

    @classmethod
    def number(cls, month_number: int) -> Month:
        for m in cls:
            if m.value.number == month_number:
                return m
        raise ValueError(f"No such month: {month_number}")

@dataclass(frozen=True)
class Date:
    year: int
    month: Month
    day: int

    def __post_init__(self) -> None:
        if self.year <= 0:
            raise ValueError(f"Invalid year: {self.year}")
        self.month.value.valid_day(self.day)

    def __str__(self) -> str:
        return f"{self.year}-{self.month.value.number:02}-{self.day:02}"
