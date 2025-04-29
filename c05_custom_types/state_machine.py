# state_machine.py
from __future__ import annotations
from enum import Enum
from typing import Callable


def open_next(self: Status) -> Status:
    _ = self  # Silence unused variable warning.
    print("Moving from OPEN to PENDING.")
    return Status.PENDING


def pending_next(self: Status) -> Status:
    _ = self
    print("Moving from PENDING to CLOSED.")
    return Status.CLOSED


def closed_next(self: Status) -> Status:
    _ = self
    print("CLOSED is a final state. Staying put.")
    return Status.CLOSED


class Status(Enum):
    OPEN = ("open", open_next)
    PENDING = ("pending", pending_next)
    CLOSED = ("closed", closed_next)

    def __init__(self, label: str, next_handler: Callable[[Status], Status]) -> None:
        self._label = label
        self._next_handler = next_handler

    def next(self) -> Status:
        return self._next_handler(self)

    @property
    def label(self) -> str:
        return self._label


state = Status.OPEN
while state != Status.CLOSED:
    print(state.label)
    state = state.next()
