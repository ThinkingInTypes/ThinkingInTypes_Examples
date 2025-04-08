# example_8.py
from typing import Generic, TypeVar  
T = TypeVar('T')  
class Box(Generic[T]):  
    def __init__(self, content: T):  
        self.content = content  
    def get_content(self) -> T:  
        return self.content
