# box.py
from dataclasses import dataclass
from typing_extensions import reveal_type


@dataclass
class Box[U]:
    content: U

    def get_content(self) -> U:
        reveal_type(self.content)
        return self.content


int_box = Box(123)  # U is inferred as int
str_box = Box("Python")  # U is inferred as str
print(int_box.get_content())
## 123
print(str_box.get_content())
## Python
