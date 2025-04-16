# example_2.py
from typing import Annotated

UserID = Annotated[int, "Database primary key"]


def fetch_user(user_id: UserID) -> dict:
    return {"id": user_id, "name": "Alice"}
