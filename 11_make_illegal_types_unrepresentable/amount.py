# amount.py
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Amount:
    value: Decimal

    def __init__(self, value: int | float | str | Decimal) -> None:
        decimal_value = Decimal(str(value))
        if decimal_value < Decimal("0"):
            raise ValueError(f"Amount({decimal_value}) cannot be negative")
        object.__setattr__(self, "value", decimal_value)

    def __add__(self, other: "Amount") -> "Amount":
        return Amount(self.value + other.value)

    def __sub__(self, other: "Amount") -> "Amount":
        return Amount(self.value - other.value)
