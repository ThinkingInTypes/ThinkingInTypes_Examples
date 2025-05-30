# animal_demo.py
from animals import Animal, Dog, speak
from book_utils import Catch

pets: list[Dog] = [Dog("Rags"), Dog("Spot")]
speak(pets)  # Dog is a subclass of Animal
## Rags: Woof
## Spot: Woof
speak([Animal("Mittens")])  # Animal is the bound
## Mittens: Animal sound
with Catch():
    speak(["bob"])  # type: ignore
