# example_16.py
from typing import Protocol

class Named(Protocol):
    name: str

def greet(entity: Named) -> None:
    print(f"Hello, {entity.name}!")
