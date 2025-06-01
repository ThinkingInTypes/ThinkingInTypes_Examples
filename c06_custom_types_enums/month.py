# month.py
from enum import Enum
from typing import Self
from month_value import MonthValue


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
