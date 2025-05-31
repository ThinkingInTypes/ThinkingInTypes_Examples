# status.py
from enum import Enum
from book_utils import Catch


class Status(Enum):
    OK = 1
    ERROR = 2
    RETRY = 3


# Accessing members:
state = Status.OK
print(state)
## Status.OK
print(state.value)
## 1
print(state.name)
## OK

# Equality and identity:
assert Status.OK == Status.OK
assert Status.OK is Status.OK

# Iteration:
for s in Status:
    print(s.name, s.value)
## OK 1
## ERROR 2
## RETRY 3

# Invalid member access:
with Catch():
    Status(4)
## Error: 4 is not a valid Status

# Enum members are immutable:
with Catch():
    Status.OK.value = 42  # type: ignore
