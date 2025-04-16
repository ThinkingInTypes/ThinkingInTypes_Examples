# ddd.py
from dataclasses import dataclass


@dataclass
class Product:
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
