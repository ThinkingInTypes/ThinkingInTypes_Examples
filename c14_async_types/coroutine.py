# coroutine.py
import asyncio
from typing import Coroutine
from async_resource import Resource


def get_resource_coroutine() -> Coroutine[None, None, Resource]:
    return Resource.get("Coroutine")


async def get_async_resource_coroutine() -> None:
    resource = await get_resource_coroutine()
    print(await resource.process())


asyncio.run(get_async_resource_coroutine())
## Completed: Coroutine
