# async_iterator_iterable.py
import asyncio
from typing import AsyncIterator, AsyncIterable

from async_resource import Resource


class ResourceStreamer:
    def __init__(self) -> None:
        self.count = 3

    def __aiter__(self) -> AsyncIterator[Resource]:
        return self

    async def __anext__(self) -> Resource:
        if self.count <= 0:
            raise StopAsyncIteration
        self.count -= 1
        await asyncio.sleep(0.1)
        return Resource(f"3. stream-{self.count}")


async def consume_stream(
    stream: AsyncIterable[Resource],
) -> None:
    async for resource in stream:
        print(await resource.work())


async def consumer() -> None:
    await consume_stream(ResourceStreamer())


asyncio.run(consumer())
## Completed: 3. stream-2
## Completed: 3. stream-1
## Completed: 3. stream-0
