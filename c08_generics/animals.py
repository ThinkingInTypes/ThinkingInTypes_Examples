# animals.py
from dataclasses import dataclass
from typing import Optional


@dataclass
class Animal:
    name: Optional[str] = None

    def say(self) -> None:
        print(f"{self.name}: Animal sound")


class Dog(Animal):
    def say(self) -> None:
        print(f"{self.name}: Woof")


def speak[T:Animal](creatures: list[T]) -> None:
    for creature in creatures:
        creature.say()
