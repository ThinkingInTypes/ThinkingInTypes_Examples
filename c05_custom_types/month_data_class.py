# month_data_class.py
from dataclasses import dataclass, field

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
        assert self.max_days in [28, 30, 31], (
            f"Month max_days {self.max_days}"
        )

    def check_day(self, day: Day):
        assert day.n <= self.max_days, f"{self} {day}"

    @staticmethod
    def make_months():
        return [
            Month(m[0], m[1], m[2])
            for m in [
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
            ]
        ]


@dataclass(frozen=True)
class Months:
    months: list[Month] = field(
        default_factory=Month.make_months
    )

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
        print(
            BirthDate(
                months.number(date[0]),
                Day(date[1]),
                Year(date[2]),
            )
        )
        print("-" * 30)
## (7, 8, 1957)
## BirthDate(m=Month(name='July', n=7, max_days=31), d=Day(n=8),
## y=Year(n=1957))
## ------------------------------
## (0, 32, 1857)
## Error: Month(0)
## (2, 31, 2022)
## Error: Month(name='February', n=2, max_days=28) Day(n=31)
## (9, 31, 2022)
## Error: Month(name='September', n=9, max_days=30) Day(n=31)
## (4, 31, 2022)
## Error: Month(name='April', n=4, max_days=30) Day(n=31)
## (6, 31, 2022)
## Error: Month(name='June', n=6, max_days=30) Day(n=31)
## (11, 31, 2022)
## Error: Month(name='November', n=11, max_days=30) Day(n=31)
## (12, 31, 2022)
## BirthDate(m=Month(name='December', n=12, max_days=31),
## d=Day(n=31), y=Year(n=2022))
## ------------------------------
