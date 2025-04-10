# example_4.py
from typing import Optional


def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Alice"
    return None
