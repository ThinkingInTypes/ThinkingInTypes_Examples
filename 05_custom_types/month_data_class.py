# month_data_class.py
from dataclasses import dataclass, field
from typing import List

from book_utils import Catch


@dataclass(frozen=True)
class Day:
    n: int
    def __post_init__(self) -> None:
        assert 1 <= self.n <= 31, f"Day({self.n})"


@dataclass(frozen=True)
class Year:
    n: int
    def __post_init__(self) -> None:
        assert 1900 < self.n <= 2022, f"Year({self.n})"


@dataclass(frozen=True)
class Month:
    name: str
    n: int
    max_days: int
    def __post_init__(self):
        assert 1 <= self.n <= 12, f"Month({self.n})"
        assert self.max_days in [28, 30, 31], f"Month max_days {self.max_days}"

    def check_day(self, day: Day):
        assert day.n <= self.max_days, f"{self} {day}"

    @staticmethod
    def make_months():
        return [Month(m[0], m[1], m[2]) for m in [
            ("January", 1, 31),
            ("February", 2, 28),
            ("March", 3, 31),
            ("April", 4, 30),
            ("May", 5, 31),
            ("June", 6, 30),
            ("July", 7, 31),
            ("August", 8, 31),
            ("September", 9, 30),
            ("October", 10, 31),
            ("November", 11, 30),
            ("December", 12, 31),
        ]]


@dataclass(frozen=True)
class Months:
    months: List[Month] = field(default_factory=Month.make_months)

    def number(self, month_number: int):
        assert 1 <= month_number <= 12, f"Month({month_number})"
        return self.months[month_number - 1]


@dataclass(frozen=True)
class BirthDate:
    m: Month
    d: Day
    y: Year

    def __post_init__(self):
        self.m.check_day(self.d)


months = Months()
for date in [
    (7, 8, 1957),
    (0, 32, 1857),
    (2, 31, 2022),
    (9, 31, 2022),
    (4, 31, 2022),
    (6, 31, 2022),
    (11, 31, 2022),
    (12, 31, 2022),
]:
    with Catch():
        print(date)
        print(BirthDate(months.number(date[0]), Day(date[1]), Year(date[2])))
        print('-' * 30)
