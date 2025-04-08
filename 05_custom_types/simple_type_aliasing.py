# simple_type_aliasing.py
from typing import NewType

UserId = NewType("UserId", int)

user_id = UserId(42)


def get_user(uid: UserId) -> str:
    return f"User {uid}"


# get_user(42)  # type checker error
get_user(user_id)  # correct usage
