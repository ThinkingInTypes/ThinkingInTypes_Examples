# class_pattern.py
from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int


def identify(user: User) -> str:
    match user:
        case User(name="Alice", age=age):
            return f"Found Alice, age {age}"
        case User(name=name, age=age):
            return f"User {name} is {age} years old"
        case _:
            return "Not a User instance"


print(identify(User("Alice", 27)))
## Found Alice, age 27
print(identify(User("Carol", 25)))
## User Carol is 25 years old
