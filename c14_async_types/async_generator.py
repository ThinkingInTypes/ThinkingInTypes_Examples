# async_generator.py
import asyncio
from typing import AsyncGenerator

from async_resource import Resource


async def generate_resources() -> AsyncGenerator[Resource, None]:
    for i in range(3):
        await asyncio.sleep(0.1)
        yield Resource(f"4. gen-{i}")


async def generate_resources_coroutine() -> None:
    async for r in generate_resources():
        print(await r.work())


asyncio.run(generate_resources_coroutine())
## Completed: 4. gen-0
## Completed: 4. gen-1
## Completed: 4. gen-2
