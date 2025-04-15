# example_6.py
# Without type hints:
def greet1(name):
    return "Hello, " + name


# With type hints:
def greet2(name: str) -> str:
    return "Hello, " + name
