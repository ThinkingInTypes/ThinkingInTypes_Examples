# example_26.py
from animals import Animal, Dog
## Woof
## Woof
## Animal sound

animals: list[Animal] = [Animal()]
dogs: list[Dog] = [Dog()]
animals = dogs  # type: ignore
