# month.py
from enum import Enum
from typing import Self

from month_value import MonthValue


class Month(Enum):
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

    def __int__(self) -> int:
        return self.value.number

    def valid_day(self, day: int) -> None:
        if not 1 <= day <= self.value.days:
            raise ValueError(f"Invalid day {day} for {self}")

    @classmethod
    def _missing_(cls, value: object) -> Self:
        if not isinstance(value, int):
            raise TypeError("Expected int")
        for m in cls:
            if m.value.number == value:
                return m
        raise ValueError(f"No such month: {value}")
