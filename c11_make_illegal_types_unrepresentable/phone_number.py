# phone_number.py
# Validated and normalized phone number
from dataclasses import dataclass
from typing import Self
import re

_PHONE_RE = re.compile(r"^\+?(\d{1,3})?[\s\-.()]*([\d\s\-.()]+)$")


@dataclass(frozen=True)
class PhoneNumber:
    country_code: str
    number: str  # Digits only, no formatting

    def __new__(cls, *args, **kwargs):
        # Deny subclassing and direct instantiation
        if cls is not PhoneNumber:
            raise TypeError("Subclassing PhoneNumber is not allowed")
        return super().__new__(cls)

    @classmethod
    def of(cls, raw: str) -> Self:
        cleaned = raw.strip()
        match = _PHONE_RE.match(cleaned)
        if not match:
            raise ValueError(f"Invalid phone number: {raw!r}")

        cc, num = match.groups()
        digits = re.sub(r"\D", "", num)
        if not digits:
            raise ValueError(f"No digits in: {raw!r}")

        country_code = cc if cc else "1"  # default to US
        return cls(country_code, digits)

    def format_number(self) -> str:
        if len(self.number) == 10:
            area, prefix, line = (
                self.number[:3],
                self.number[3:6],
                self.number[6:],
            )
            return f"({area}) {prefix}-{line}"
        return self.number  # Fallback: just digits

    def __str__(self) -> str:
        formatted = self.format_number()
        return f"+{self.country_code} {formatted}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PhoneNumber):
            return NotImplemented
        return (
                self.country_code == other.country_code
                and self.number == other.number
        )
