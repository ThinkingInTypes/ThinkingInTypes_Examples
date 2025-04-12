# example_10.py
from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int


user = User("Carol", 25)

match user:
    case User(name="Alice", age=age):
        print(f"Found Alice, age {age}")
    case User(name=name, age=age):
        print(f"User {name} is {age} years old")
    case _:
        print("Not a User instance")
