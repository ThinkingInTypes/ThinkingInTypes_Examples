# logger_protocol.py
from typing import Protocol


class Logger(Protocol):
    def log(self, message: str) -> None: ...


class FileLogger:
    """Concrete logger that writes to a file."""

    def __init__(self, filename: str):
        self.filename = filename

    def log(self, message: str) -> None:
        with open(self.filename, "a") as f:
            f.write(message + "\n")


class ListLogger:
    """Concrete logger that stores messages in a list (e.g., for testing)."""

    def __init__(self):
        self.messages: list[str] = []

    def log(self, message: str) -> None:
        self.messages.append(message)


def run_process(task_name: str, logger: Logger) -> None:
    logger.log(f"Starting {task_name}")
    # Perform the task ...
    logger.log(f"Finished {task_name}")


# Using the run_process with different loggers
run_process("DataCleanup", FileLogger("app.log"))  # logs to file
test_logger = ListLogger()
run_process("DataCleanup", test_logger)  # logs to list in memory
print("Captured logs:", test_logger.messages)
## Captured logs: ['Starting DataCleanup',
## 'Finished DataCleanup']
