# dataclass_initvar.py
from dataclasses import dataclass, InitVar


@dataclass
class Book:
    title: str
    author: str
    condition: InitVar[str]
    shelf_id: int | None = None

    def __post_init__(self, condition):
        if condition == "Unacceptable":
            self.shelf_id = None


b = Book("Emma", "Austen", "Good", 11)
print(b.__dict__)
## {'title': 'Emma', 'author': 'Austen', 'shelf_id': 11}
