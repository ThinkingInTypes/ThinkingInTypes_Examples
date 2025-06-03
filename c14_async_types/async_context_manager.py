# async_context_manager.py
import asyncio
from contextlib import asynccontextmanager
from typing import AsyncIterator

from async_resource import Resource


@asynccontextmanager
async def resource_context() -> AsyncIterator[Resource]:
    print("5. Acquiring resource")
    await asyncio.sleep(0.1)
    yield Resource("5. AsyncContextManager")
    print("5. Releasing resource")
    await asyncio.sleep(0.1)


async def get_resource_manager_async() -> None:
    async with resource_context() as res:
        print(await res.work())


asyncio.run(get_resource_manager_async())
## 5. Acquiring resource
## Completed: 5. AsyncContextManager
## 5. Releasing resource
