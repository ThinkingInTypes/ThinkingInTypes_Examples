# type_safe_date.py
from dataclasses import dataclass
from year import Year
from month import Month
from day import Day


@dataclass(frozen=True)
class Date:
    year: Year
    month: Month
    day: Day

    def __post_init__(self) -> None:
        # Validate day against month:
        object.__setattr__(
            self, "day", Day.of(self.month, self.day.value)
        )

    def __str__(self) -> str:
        return f"{self.year.value}-{self.month.value.number:02}-{self.day.value:02}"
