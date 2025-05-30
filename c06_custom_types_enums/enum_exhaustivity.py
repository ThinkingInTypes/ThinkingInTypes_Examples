# enum_exhaustivity.py
from enum import Enum


class Status(Enum):
    OPEN = "open"
    CLOSED = "closed"
    PENDING = "pending"

    def handle(self) -> str:
        match self:
            case Status.OPEN:
                return f"open: {self}"
            case Status.CLOSED:
                return f"closed: {self}"
            case Status.PENDING:
                return f"pending: {self}"
            # Not possible, but some type checkers
            # haven't caught up yet:
            case _:
                return f"Unhandled: {self}"


print(Status.OPEN.handle())
## open: Status.OPEN
print(Status.CLOSED.handle())
## closed: Status.CLOSED
print(Status.PENDING.handle())
## pending: Status.PENDING
