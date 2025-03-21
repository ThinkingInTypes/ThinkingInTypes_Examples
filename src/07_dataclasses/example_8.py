# example_8.py
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    in_stock: bool = True


product = Product("Laptop", 999.99)
print(product)  # Product(name='Laptop', price=999.99, in_stock=True)
