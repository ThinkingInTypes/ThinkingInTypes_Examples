# animals.py
from dataclasses import dataclass
from typing import TypeVar, Optional


@dataclass
class Animal:
    name: Optional[str] = None

    def say(self) -> None:
        print(f"{self.name}: Animal sound")


class Dog(Animal):
    def say(self) -> None:
        print(f"{self.name}: Woof")


TAnimal = TypeVar("TAnimal", bound=Animal)


def speak(creatures: list[TAnimal]) -> None:
    for creature in creatures:
        creature.say()
