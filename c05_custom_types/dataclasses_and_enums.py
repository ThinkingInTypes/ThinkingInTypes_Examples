# dataclasses_and_enums.py
from dataclasses import dataclass
from enum import Enum


class Status(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


@dataclass
class User:
    id: int
    name: str
    status: Status


print(User(id=1, name="Alice", status=Status.ACTIVE))
## User(id=1, name='Alice', status=<Status.ACTIVE:
## 'active'>)
