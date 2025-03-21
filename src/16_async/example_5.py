# example_5.py
import asyncio
from contextlib import asynccontextmanager
from typing import AsyncGenerator


@asynccontextmanager
async def database_connection() -> AsyncGenerator[str, None]:
    connection = "db_connection"
    try:
        yield connection
    finally:
        await asyncio.sleep(1)  # simulate closing connection


async def main():
    async with database_connection() as conn:
        print(f"Using {conn}")
