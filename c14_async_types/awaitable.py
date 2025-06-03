# awaitable.py
import asyncio
from typing import Awaitable

from async_resource import Resource


def get_resource_awaitable() -> Awaitable[Resource]:
    return Resource.get("Awaitable")


async def get_async_resource_awaitable() -> None:
    resource = await get_resource_awaitable()
    print(await resource.process())


asyncio.run(get_async_resource_awaitable())
## Completed: Awaitable
