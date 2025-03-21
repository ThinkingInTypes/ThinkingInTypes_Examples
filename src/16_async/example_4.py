# example_4.py
from typing import AsyncGenerator


async def stream_data() -> AsyncGenerator[int, None]:
    for i in range(5):
        yield i
