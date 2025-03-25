# example_6.py
from dataclasses import dataclass


@dataclass(frozen=True)
class FullName:
    name: str

    def __post_init__(self):
        parts = self.name.split()
        assert len(parts) >= 2, "Full name must include at least two parts."


@dataclass(frozen=True)
class BirthDate:
    year: int
    month: int
    day: int

    def __post_init__(self):
        assert 1900 <= self.year <= 2022, "Year must be between 1900 and 2022."
        assert 1 <= self.month <= 12, "Month must be between 1 and 12."
        assert 1 <= self.day <= 31, "Day must be valid for given month."


@dataclass(frozen=True)
class Email:
    address: str

    def __post_init__(self):
        assert "@" in self.address, "Invalid email address."


@dataclass(frozen=True)
class Person:
    name: FullName
    birthdate: BirthDate
    email: Email
