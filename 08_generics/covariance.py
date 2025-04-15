# covariance.py
from typing import Generic, TypeVar
from animals import Animal, Dog

T_co = TypeVar('T_co', covariant=True)


class ReadOnlyBox(Generic[T_co]):
    def __init__(self, content: T_co):
        self._content = content

    def get_content(self) -> T_co:
        return self._content


dog_box: ReadOnlyBox[Dog] = ReadOnlyBox(Dog())
# Covariance in action:
animal_box: ReadOnlyBox[Animal] = dog_box
# pet is an Animal, a Dog:
pet: Animal = animal_box.get_content()
