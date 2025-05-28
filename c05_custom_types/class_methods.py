# class_methods.py
import inspect


def show_methods(cls: type) -> None:
    print(f"class {cls.__name__}:")
    for name, member in cls.__dict__.items():
        if callable(member):
            sig = inspect.signature(member)
            print(f"  {name}{sig}")
