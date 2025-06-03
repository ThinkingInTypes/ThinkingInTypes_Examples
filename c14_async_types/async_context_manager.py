# async_context_manager.py
import asyncio
from contextlib import asynccontextmanager
from typing import AsyncIterator

from async_resource import Resource


@asynccontextmanager
async def resource_context() -> AsyncIterator[Resource]:
    resource = Resource("Async Context Manager")
    print(f"Acquired {resource}")
    yield resource
    print(f"Releasing {resource}")


async def async_context_manager_async() -> None:
    async with resource_context() as res:
        print(await res.process())


asyncio.run(async_context_manager_async())
## Acquired Resource(name='Async Context Manager')
## Completed: Async Context Manager
## Releasing Resource(name='Async Context Manager')
