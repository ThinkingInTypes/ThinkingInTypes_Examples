# async_resource.py
# For reuse in subsequent examples
import asyncio
from dataclasses import dataclass


@dataclass
class Resource:
    name: str

    @classmethod
    async def get(cls, name: str) -> Resource:
        await asyncio.sleep(0.1)
        return cls(name=name)

    async def work(self) -> str:
        await asyncio.sleep(0.1)
        return f"Completed: {self.name}"
