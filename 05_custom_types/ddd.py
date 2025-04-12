# ddd.py
from dataclasses import dataclass
from typing import NamedTuple


class Product(NamedTuple):
    name: str
    price: float


@dataclass
class Order:
    order_id: int
    products: list[Product]

    def total(self) -> float:
        return sum(
            product.price for product in self.products
        )
