# example_1.py
def greet(name: str, excited: bool = False) -> str:
    return f"Hello, {'!' if excited else ''}{name}"
