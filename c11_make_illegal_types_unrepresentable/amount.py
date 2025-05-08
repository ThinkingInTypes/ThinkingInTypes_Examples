# amount.py
from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Self


@dataclass(frozen=True)
class Amount:
    value: Decimal

    @classmethod
    def of(cls, value: int | float | str | Decimal) -> Self:
        if isinstance(value, float):
            text = repr(value)
            if "e" in text.lower():
                raise ValueError(f"{value!r}: out of range")
            parts = text.split(".", 1)
            if len(parts) == 2 and len(parts[1]) > 2:
                raise ValueError(f"{value!r}: >2 decimal places")
            dec = Decimal(text)
        else:
            dec = (
                value
                if isinstance(value, Decimal)
                else Decimal(str(value))
            )

        return cls(dec)

    def __post_init__(self) -> None:
        if self.value < Decimal("0"):
            raise ValueError(f"Negative Amount({self.value})")

        if int(self.value.as_tuple().exponent) > 2:
            raise ValueError(
                f"Amount({self.value}): >2 decimal places"
            )

    def __add__(self, other: Amount) -> Amount:
        return Amount.of(self.value + other.value)

    def __sub__(self, other: Amount) -> Amount:
        return Amount.of(self.value - other.value)
