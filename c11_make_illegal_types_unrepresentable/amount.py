# amount.py
from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Self


@dataclass(frozen=True)
class Amount:
    value: Decimal

    @classmethod
    def of(cls, value: int | float | str) -> Self:
        return cls(Decimal(str(value)))

    def __post_init__(self) -> None:  # Runtime check
        if self.value < Decimal("0"):
            raise ValueError(f"Negative Amount({self.value})")

    def __add__(self, other: Amount) -> Amount:
        return Amount(self.value + other.value)

    def __sub__(self, other: Amount) -> Amount:
        return Amount(self.value - other.value)
