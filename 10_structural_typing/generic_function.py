# generic_function.py
from container import Container
from container_types import StringContainer, IntContainer


def print_item_and_return[C](container: Container[C]) -> C:
    item = container.get_item()
    print("Got:", item)
    return item  # The type of item is inferred as C


# Using the generic function with different container types:
x = print_item_and_return(
    StringContainer("hello")
)  # prints "hello", x is str
## Got: hello
y = print_item_and_return(
    IntContainer(42)
)  # prints "42", y is int
## Got: 42
