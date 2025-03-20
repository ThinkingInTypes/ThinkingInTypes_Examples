# example_8.py
from typing import List

UserIDs = List[int]


def process_users(user_ids: UserIDs) -> None:
    for uid in user_ids:
        print(f"Processing user {uid}")
