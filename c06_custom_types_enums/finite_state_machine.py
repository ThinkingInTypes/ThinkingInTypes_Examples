# finite_state_machine.py
from __future__ import annotations
from enum import Enum
from typing import Dict


class Event(Enum):
    SUBMIT = "submit"
    APPROVE = "approve"
    REJECT = "reject"
    REOPEN = "reopen"


class Status(Enum):
    OPEN = "open"
    PENDING = "pending"
    CLOSED = "closed"

    def __init__(self, label: str) -> None:
        self._label = label

    def on_event(self, event: Event) -> Status:
        mapping = _TRANSITIONS.get(self, {})
        next_state = mapping.get(event)
        if next_state is None:
            print(f"Invalid {self.name} & {event.name}")
            return self
        print(f"{self.name} + {event.name} -> {next_state.name}")
        return next_state

    @property
    def label(self) -> str:
        return self._label


# Mapping of transitions: {current_status: {event: next_status}}
_TRANSITIONS: Dict[Status, Dict[Event, Status]] = {
    Status.OPEN: {Event.SUBMIT: Status.PENDING},
    Status.PENDING: {
        Event.APPROVE: Status.CLOSED,
        Event.REJECT: Status.OPEN,
    },
    Status.CLOSED: {Event.REOPEN: Status.OPEN},
}


def run(initial: Status, events: list[Event]) -> None:
    """
    Execute a sequence of events starting from the given initial status.
    """
    state = initial
    print(f"Starting at {state.label}")
    for event in events:
        state = state.on_event(event)
        print(f"Now at {state.label}")


workflow = [
    Event.SUBMIT,
    Event.REOPEN,
    Event.REJECT,
    Event.SUBMIT,
    Event.APPROVE,
    Event.REOPEN,
]
run(Status.OPEN, workflow)
## Starting at open
## OPEN + SUBMIT -> PENDING
## Now at pending
## Invalid PENDING & REOPEN
## Now at pending
## PENDING + REJECT -> OPEN
## Now at open
## OPEN + SUBMIT -> PENDING
## Now at pending
## PENDING + APPROVE -> CLOSED
## Now at closed
## CLOSED + REOPEN -> OPEN
## Now at open
