# example_2.py
from typing import Coroutine


async def get_user(user_id: int) -> dict:
    return {"id": user_id, "name": "Alice"}


async def main() -> Coroutine[None, None, dict]:
    user = await get_user(123)
    return user
