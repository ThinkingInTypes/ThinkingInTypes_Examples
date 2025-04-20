# example_9.py
from typing import TypeVar
from logger_protocol import Logger
## log file:
## C:\Users\bruce\AppData\Local\Temp\tmpmsta1v9j
## Starting DataCleanup
## Finished DataCleanup
## Captured logs: ['Starting DataCleanup',
## 'Finished DataCleanup']

T = TypeVar(
    "T", bound=Logger
)  # using our Logger protocol from earlier
