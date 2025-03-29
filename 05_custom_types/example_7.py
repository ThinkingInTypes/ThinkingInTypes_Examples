# example_7.py
from enum import Enum


class Month(Enum):
    JANUARY = (1, 31)
    FEBRUARY = (2, 28)
    # other months

    @staticmethod
    def validate(month_number: int, day: int) -> bool:
        month = Month(month_number)
        return 1 <= day <= month.value[1]
