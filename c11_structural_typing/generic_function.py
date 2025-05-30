# generic_function.py
from container import Container
from container_types import StringContainer, IntContainer


def print_item_and_return[T](container: Container[T]) -> T:
    item = container.get_item()
    print(f"{item = }, {type(item) = }")
    return item


# Use generic function with different container types:
x: str = print_item_and_return(StringContainer("hello"))
## item = 'hello', type(item) = <class 'str'>
y: int = print_item_and_return(IntContainer(42))
## item = 42, type(item) = <class 'int'>
