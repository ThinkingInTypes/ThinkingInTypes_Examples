# example_4.py
from typing import TypeVar


class Animal:
    def speak(self) -> str:
        return "..."


A = TypeVar("A", bound=Animal)


def animal_sound(animal: A) -> str:
    return animal.speak()


class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"


print(animal_sound(Dog()))  # "Woof!"
## Woof!
