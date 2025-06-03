# async_generator.py
import asyncio
from typing import AsyncGenerator

from async_resource import Resource, do_work


async def generate_resources() -> AsyncGenerator[Resource, None]:
    for i in range(3):
        await do_work()
        yield Resource(f"gen-{i}")


async def generate_resources_coroutine() -> None:
    async for r in generate_resources():
        print(await r.process())


asyncio.run(generate_resources_coroutine())
## Completed: gen-0
## Completed: gen-1
## Completed: gen-2
