# example_3.py
from typing import Awaitable


async def fetch(url: str) -> str:
    return f"Content from {url}"


def schedule_fetch(url: str) -> Awaitable[str]:
    return fetch(url)
