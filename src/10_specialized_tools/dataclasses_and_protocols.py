# dataclasses_and_protocols.py
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
print_id(Product(101, 19.99))
