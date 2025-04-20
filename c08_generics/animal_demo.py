# animal_demo.py
from animals import Animal, Dog, speak

pets: list[Dog] = [Dog(), Dog()]
speak(pets)  # OK, Dog is a subclass of Animal
## None: Woof
## None: Woof
speak([Animal()])  # OK, Animal is the bound
## None: Animal sound
# make_them_speak(["not an animal"])  # type checker error
