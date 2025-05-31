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
print(state.value)     
print(state.name)      

# Equality and identity:
assert Status.OK == Status.OK
assert Status.OK is Status.OK

# Iteration:
for s in Status:
    print(s.name, s.value)

# Invalid member access:
with Catch():
    Status(4)

# Enum members are immutable:
with Catch():
    Status.OK.value = 42  # type: ignore
