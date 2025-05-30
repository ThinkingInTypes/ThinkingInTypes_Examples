# invariance_confusion.py
from c09_generics.animals import Animal, Dog

animals: list[Animal] = [Animal()]
dogs: list[Dog] = [Dog()]
animals = dogs  # type: ignore
