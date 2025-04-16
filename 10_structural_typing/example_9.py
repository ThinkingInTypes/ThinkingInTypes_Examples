# example_9.py
from typing import TypeVar
from logger_protocol import Logger
## Captured logs: ['Starting DataCleanup',
## 'Finished DataCleanup']

T = TypeVar(
    "T", bound=Logger
)  # using our Logger protocol from earlier
