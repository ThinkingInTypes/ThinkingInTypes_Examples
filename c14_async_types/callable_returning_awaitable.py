# callable_returning_awaitable.py
import asyncio
from typing import Awaitable, Callable

from async_resource import Resource


def resource_factory() -> Callable[[], Awaitable[Resource]]:
    async def make() -> Resource:
        await asyncio.sleep(0.1)
        return Resource("6. Callable returning Awaitable")

    return make


async def get_resource_factory() -> None:
    factory = resource_factory()
    resource = await factory()
    print(await resource.work())


asyncio.run(get_resource_factory())
## Completed: 6. Callable returning Awaitable
