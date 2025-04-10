# example_11.py
def add(a: int, b: int) -> int:
    return a + b


result1 = add(10, 5)
result2 = add(10, "5")  # oops, second argument is str
