# box.py
from typing import Generic, TypeVar

U = TypeVar('U')  # a generic type for content

class Box(Generic[U]):
    def __init__(self, content: U) -> None:
        self.content: U = content

    def get_content(self) -> U:
        return self.content

int_box = Box(123)          # U is inferred as int
str_box = Box("Python")     # U is inferred as str
print(int_box.get_content())  # 123
print(str_box.get_content())  # Python
