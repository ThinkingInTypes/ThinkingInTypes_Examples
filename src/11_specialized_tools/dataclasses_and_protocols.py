# dataclasses_and_protocols.py
from dataclasses import dataclass
from typing import Protocol


class Identifiable(Protocol):
    id: int


@dataclass
class User:
    id: int
    name: str


@dataclass
class Product:
    id: int
    price: float


def print_id(entity: Identifiable) -> None:
    print(f"ID: {entity.id}")


print_id(User(1, "Alice"))
## ID: 1
print_id(Product(101, 19.99))
## ID: 101
