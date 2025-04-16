# generic_function.py
from typing import TypeVar
from container import Container, T
from container_types import StringContainer, IntContainer


def print_item_and_return(container: Container[T]) -> T:
    item = container.get_item()
    print(f"{item = }, {type(item) = }")
    return item  # Type inferred as C


# Use generic function with different container types:
x: str = print_item_and_return(StringContainer("hello"))
y: int = print_item_and_return(IntContainer(42))
