# example_6.py
# Without type annotations:
def greet1(name):
    return "Hello, " + name


# With type annotations:
def greet2(name: str) -> str:
    return "Hello, " + name
