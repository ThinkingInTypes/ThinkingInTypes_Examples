# example_26.py
from animals import Animal, Dog
animals: list[Animal] = [Animal()]
dogs: list[Dog] = [Dog()]
animals = dogs  # Type checker error! Incompatible types
