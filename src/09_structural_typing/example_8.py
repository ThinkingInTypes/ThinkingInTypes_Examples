# example_8.py
def print_item_and_return[C](container: Container[C]) -> C:
    item = container.get_item()
    print("Got:", item)
    return item  # The type of item is inferred as C


# Using the generic function with different container types:
x = print_item_and_return(StringContainer("hello"))  # prints "hello", x is str
y = print_item_and_return(IntContainer(42))  # prints "42", y is int
