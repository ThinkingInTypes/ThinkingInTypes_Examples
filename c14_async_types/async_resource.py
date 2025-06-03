# async_resource.py
# For reuse in subsequent examples
import asyncio
from dataclasses import dataclass


async def do_work():
    await asyncio.sleep(0.1)


@dataclass
class Resource:
    name: str

    @classmethod
    async def get(cls, name: str) -> Resource:
        await do_work()
        return cls(name=name)

    async def process(self) -> str:
        await do_work()
        return f"Completed: {self.name}"
