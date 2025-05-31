# type_safe_date.py
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

    def valid_day(self, day: int) -> None:
        if not 1 <= day <= self.days:
            raise ValueError(
                f"Invalid day {day} for month {self.number}"
            )


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
    def number(cls, month_number: int) -> Self:
        for m in cls:
            if m.value.number == month_number:
                return m
        raise ValueError(f"No such month: {month_number}")


@dataclass(frozen=True)
class Year:
    value: int

    def __post_init__(self) -> None:
        if self.value <= 0:
            raise ValueError(f"Invalid year: {self.value}")


@dataclass(frozen=True)
class Day:
    value: int

    def __post_init__(self) -> None:
        if self.value <= 0:
            raise ValueError(f"Invalid day: {self.value}")

    @classmethod
    def of(cls, month: Month, day: int) -> Self:
        month.value.valid_day(day)
        return cls(day)


@dataclass(frozen=True)
class Date:
    year: Year
    month: Month
    day: Day

    def __post_init__(self) -> None:
        # Validate day against month:
        object.__setattr__(self, 'day', Day.of(self.month, self.day.value))

    def __str__(self) -> str:
        return f"{self.year.value}-{self.month.value.number:02}-{self.day.value:02}"
