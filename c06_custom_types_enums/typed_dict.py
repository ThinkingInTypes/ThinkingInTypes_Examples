# typed_dict.py
from typing import TypedDict


class UserProfile(TypedDict):
    username: str
    email: str
    age: int


user: UserProfile = {
    "username": "alice",
    "email": "alice@example.com",
    "age": 30,
}
