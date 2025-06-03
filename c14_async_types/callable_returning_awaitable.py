# callable_returning_awaitable.py
import asyncio
from typing import Awaitable, Callable

from async_resource import Resource, do_work


def resource_factory() -> Callable[[], Awaitable[Resource]]:
    async def make() -> Resource:
        await do_work()
        return Resource("Callable Returning Awaitable")

    return make


async def get_resource_factory() -> None:
    factory = resource_factory()
    resource = await factory()
    print(await resource.process())


asyncio.run(get_resource_factory())
## Completed: Callable Returning Awaitable
