# example_6.py
# Without type hints:
def greet(name):
    return "Hello, " + name


# With type hints:
def greet(name: str) -> str:
    return "Hello, " + name
