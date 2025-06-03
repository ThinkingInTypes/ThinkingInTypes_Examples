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
    async with manage(Resource("Generic ACM")) as resource:
        print(await resource.process())


asyncio.run(generic_async_context_manager())
## Acquiring Resource(name='Generic ACM')
## Completed: Generic ACM
## Releasing Resource(name='Generic ACM')
