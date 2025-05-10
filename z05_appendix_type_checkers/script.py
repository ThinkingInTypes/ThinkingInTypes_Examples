# script.py


def greet(name: str) -> str:
    return f"Hello, {name}!"


# Incorrect type:
print(greet(123))  # type: ignore
## Hello, 123!
