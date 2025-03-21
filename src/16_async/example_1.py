# example_1.py
import asyncio


async def fetch_data(url: str) -> str:
    await asyncio.sleep(1)
    return f"Data from {url}"
