# example_6.py
from typing import Generic, TypeVar
from animals import Animal, Dog

T_co = TypeVar('T_co', covariant=True)

class ReadOnlyBox(Generic[T_co]):
    def __init__(self, content: T_co):
        self._content = content

    def get_content(self) -> T_co:
        return self._content

dog_box: ReadOnlyBox[Dog] = ReadOnlyBox(Dog())
animal_box: ReadOnlyBox[Animal] = dog_box  # This is OK because of covariance
pet: Animal = animal_box.get_content()     # pet is an Animal (actually a Dog instance)
