# phone_number.py
from dataclasses import dataclass
from typing import Self
import re


@dataclass(frozen=True)
class PhoneNumber:
    """Represents a validated and normalized phone number."""

    country_code: str
    number: str  # Digits only, no formatting

    PHONE_REGEX = re.compile(r"^\+?(\d{1,3})?[\s\-.()]*([\d\s\-.()]+)$")

    @classmethod
    def parse(cls, raw: str) -> Self:
        """Parses and validates a raw phone number string."""
        cleaned = raw.strip()
        match = cls.PHONE_REGEX.match(cleaned)
        if not match:
            raise ValueError(f"Invalid phone number: {raw!r}")

        cc, num = match.groups()
        digits = re.sub(r"\D", "", num)
        if not digits:
            raise ValueError(f"No digits found in: {raw!r}")

        country_code = cc if cc else "1"  # default to US
        return cls(country_code=country_code, number=digits)

    def __str__(self) -> str:
        """Formats the phone number as +<country> <formatted number>."""
        formatted = self.format_number()
        return f"+{self.country_code} {formatted}"

    def format_number(self) -> str:
        """Applies simple formatting rules for 10-digit numbers."""
        if len(self.number) == 10:
            return f"({self.number[:3]}) {self.number[3:6]}-{self.number[6:]}"
        return self.number  # fallback: just the digits

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PhoneNumber):
            return NotImplemented
        return self.country_code == other.country_code and self.number == other.number
