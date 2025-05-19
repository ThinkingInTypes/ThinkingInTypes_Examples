# covariance.py
from animals import Animal, Dog

class ReadOnlyBox[T]:
    def __init__(self, content: T):
        self._content = content

    def get_content(self) -> T:
        return self._content


dog_box: ReadOnlyBox[Dog] = ReadOnlyBox(Dog())
# Covariance in action:
animal_box: ReadOnlyBox[Animal] = dog_box
# pet is an Animal, a Dog:
pet: Animal = animal_box.get_content()
