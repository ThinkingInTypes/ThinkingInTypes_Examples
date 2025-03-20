# example_6.py
from typing import TypeGuard


class Cat:
    def meow(self):
        print("Meow!")


def is_cat(animal: object) -> TypeGuard[Cat]:
    return hasattr(animal, "meow")


animal = Cat()
if is_cat(animal):
    animal.meow()  # Safe to call
