# phone_number.py
# Validated and normalized phone number
from __future__ import annotations
from dataclasses import dataclass
from typing import Self
import re

_PHONE_RE = re.compile(
    r"^\+?(\d{1,3})?[\s\-.()]*([\d\s\-.()]+)$"
)


@dataclass(frozen=True)
class PhoneNumber:
    country_code: str
    number: str  # Digits only, no formatting

    def __post_init__(self) -> None:
        # Validate country code: 1-3 digits
        if not re.fullmatch(r"\d{1,3}", self.country_code):
            raise ValueError(f"Invalid country code: {self.country_code!r}")
        # Validate number: digits only
        if not re.fullmatch(r"\d+", self.number):
            raise ValueError(f"Invalid number digits: {self.number!r}")

    @classmethod
    def of(cls, raw: str) -> Self:
        """
        Parse and validate a raw phone number string.
        """
        match = _PHONE_RE.match(raw.strip())
        if not match:
            raise ValueError(f"Invalid phone number: {raw!r}")
        cc, num = match.groups()
        digits = re.sub(r"\D", "", num)
        if not digits:
            raise ValueError(f"No digits in: {raw!r}")
        country_code = cc or "1"  # default to US
        return cls(country_code, digits)

    def format_number(self) -> str:
        if len(self.number) == 10:
            area, prefix, line = (
                self.number[:3],
                self.number[3:6],
                self.number[6:],
            )
            return f"({area}) {prefix}-{line}"
        return self.number

    def __str__(self) -> str:
        return f"+{self.country_code} {self.format_number()}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PhoneNumber):
            return NotImplemented  # Instead of False
        return (
            self.country_code == other.country_code
            and self.number == other.number
        )
