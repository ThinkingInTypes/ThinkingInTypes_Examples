# dataclass_composition.py
from dataclasses import dataclass


@dataclass
class FullName:
    name: str

    def __post_init__(self) -> None:
        print(f"FullName checking {self.name}")
        assert len(self.name.split()) > 1, (
            f"'{self.name}' needs first and last names"
        )


@dataclass
class BirthDate:
    dob: str

    def __post_init__(self) -> None:
        print(f"BirthDate checking {self.dob}")


@dataclass
class EmailAddress:
    address: str

    def __post_init__(self) -> None:
        print(f"EmailAddress checking {self.address}")


@dataclass
class Person:
    name: FullName
    date_of_birth: BirthDate
    email: EmailAddress


person = Person(
    FullName("Bruce Eckel"),
    BirthDate("7/8/1957"),
    EmailAddress("mindviewinc@gmail.com"),
)
## FullName checking Bruce Eckel
## BirthDate checking 7/8/1957
## EmailAddress checking mindviewinc@gmail.com
print(person)
## Person(name=FullName(name='Bruce Eckel'),
## date_of_birth=BirthDate(dob='7/8/1957'),
## email=EmailAddress(address='mindviewinc@gmail.com'))
