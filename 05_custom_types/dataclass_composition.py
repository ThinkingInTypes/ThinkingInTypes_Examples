# dataclass_composition.py
from dataclasses import dataclass

@dataclass(frozen=True)
class FullName:
    name: str
    def __post_init__(self) -> None:
        print(f"FullName checking {self.name}")
        assert len(self.name.split()) > 1, \
              f"'{self.name}' needs first and last names"

@dataclass(frozen=True)
class BirthDate:
    dob: str
    def __post_init__(self) -> None:
        print(f"BirthDate checking {self.dob}")

@dataclass(frozen=True)
class EmailAddress:
    address: str
    def __post_init__(self) -> None:
        print(f"EmailAddress checking {self.address}")

@dataclass(frozen=True)
class Person:
    name: FullName
    date_of_birth: BirthDate
    email: EmailAddress

person = Person(
    FullName("Bruce Eckel"),
    BirthDate("7/8/1957"),
    EmailAddress("mindviewinc@gmail.com")
)
print(person)
