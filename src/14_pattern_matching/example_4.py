# example_4.py
from typing import Union


class Cat:
    def meow(self) -> str:
        return "Meow"


class Dog:
    def bark(self) -> str:
        return "Woof"


def animal_sound(animal: Union[Cat, Dog]) -> str:
    match animal:
        case Cat():
            return animal.meow()
        case Dog():
            return animal.bark()
