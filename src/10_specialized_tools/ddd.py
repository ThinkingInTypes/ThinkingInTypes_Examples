# ddd.py
from dataclasses import dataclass
from typing import List


@dataclass
class Order:
    order_id: int
    products: List[Product]

    def total_price(self) -> float:
        return sum(product.price for product in self.products)
