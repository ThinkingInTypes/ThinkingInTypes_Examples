# file_resource_demo.py
from file_resource import (
    Closable,
    FileResource,
    SocketResource,
)
from typing import Iterable


def close_all(resources: Iterable[Closable]) -> None:
    for res in resources:
        res.close()


# All these have a close():
closables = (
    FileResource("data.txt"),
    SocketResource(),
    open("other.txt", "w"),
)
close_all(closables)
## Socket closed
