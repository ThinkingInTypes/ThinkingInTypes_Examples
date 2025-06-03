# async_iterator_iterable.py
import asyncio
from typing import AsyncIterator, AsyncIterable

from async_resource import Resource, do_work


class ResourceStreamer:
    def __init__(self) -> None:
        self.count = 3

    def __aiter__(self) -> AsyncIterator[Resource]:
        return self

    async def __anext__(self) -> Resource:
        if self.count <= 0:
            raise StopAsyncIteration
        self.count -= 1
        await do_work()
        return Resource(f"Stream-{self.count}")


async def consume(stream: AsyncIterable[Resource]) -> None:
    async for resource in stream:
        print(await resource.process())


async def consumer() -> None:
    await consume(ResourceStreamer())


asyncio.run(consumer())
## Completed: Stream-2
## Completed: Stream-1
## Completed: Stream-0
