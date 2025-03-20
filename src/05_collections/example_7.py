# example_7.py
from typing import Mapping


def get_user_age(users: Mapping[str, int], username: str) -> int:
    return users.get(username, 0)
