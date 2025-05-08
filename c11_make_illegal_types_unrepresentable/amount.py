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
        if isinstance(value, float):
            text = repr(value)
            if "e" in text.lower():
                raise ValueError(
                    f"{value!r}: no scientific notation"
                )
            # Check fractional part length
            if "." in text:
                frac = text.split(".", 1)[1]
                if len(frac) > 2:
                    raise ValueError(
                        f"{value!r}: >2 decimal places"
                    )
            return cls(Decimal(text))
        # For int or str, convert via string to Decimal
        return cls(Decimal(str(value)))

    def __post_init__(self) -> None:
        if self.value < Decimal("0"):
            raise ValueError(f"Negative Amount({self.value})")

        # Determine decimal places:
        match self.value.as_tuple().exponent:
            case int() as exponent if exponent < 0:
                places = -exponent
            case int():
                places = 0
            case _:
                raise ValueError(
                    f"Non-finite Decimal({self.value})"
                )

        if places > 2:
            raise ValueError(
                f"Amount({self.value}): >2 decimal places"
            )

    def __add__(self, other: Amount) -> Amount:
        return Amount(self.value + other.value)

    def __sub__(self, other: Amount) -> Amount:
        return Amount(self.value - other.value)
