# generic_async_context_manager.py
import asyncio
from contextlib import asynccontextmanager
from typing import AsyncIterator

from async_resource import Resource


@asynccontextmanager
async def manage[T](value: T) -> AsyncIterator[T]:
    print(f"Acquiring {value}")
    yield value
    print(f"Releasing {value}")


async def generic_async_context_manager() -> None:
    async with manage(Resource("7. Generic")) as resource:
        print(await resource.work())


asyncio.run(generic_async_context_manager())
## Acquiring Resource(name='7. Generic')
## Completed: 7. Generic
## Releasing Resource(name='7. Generic')
