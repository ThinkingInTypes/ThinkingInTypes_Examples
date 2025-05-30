# frozen_person.py
from dataclasses import dataclass

from book_utils import Catch


@dataclass(frozen=True)
class Person:
    name: str
    age: int


person = Person(name="Alice", age=30)
print(person.name)  # "Alice"
## Alice
with Catch():
    # Trying to modify a frozen dataclass field:
    person.age = 31  # type: ignore

person.__dict__["age"] = 31  # Disable 'frozen'
