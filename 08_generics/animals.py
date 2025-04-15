# animals.py
from typing import TypeVar


class Animal:
    def speak(self) -> None:
        print("Animal sound")


class Dog(Animal):
    def speak(self) -> None:
        print("Woof")


TAnimal = TypeVar('TAnimal', bound=Animal)


def make_them_speak(creatures: list[TAnimal]) -> None:
    for creature in creatures:
        creature.speak()


pets: list[Dog] = [Dog(), Dog()]
make_them_speak(pets)  # OK, Dog is a subclass of Animal
make_them_speak([Animal()])  # OK, Animal itself is fine (Animal is the bound)
# make_them_speak(["not an animal"])  # type checker error
