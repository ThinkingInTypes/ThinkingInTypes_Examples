# logger_protocol.py
from contextlib import AbstractContextManager
from pathlib import Path
from typing import Protocol


class Logger(Protocol):
    def log(self, message: str) -> None: ...


class FileLogger(AbstractContextManager):
    """
    Logger that writes to a known log file in a fixed directory.
    """

    def __init__(self, path: Path = Path("logs/log.txt")):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.filename = path
        self._file = self.filename.open("a", encoding="utf-8")

    def log(self, message: str) -> None:
        self._file.write(message + "\n")
        self._file.flush()

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self._file.close()


class ListLogger:
    """
    Logger that stores messages in a list
    """

    def __init__(self):
        self.messages: list[str] = []

    def log(self, message: str) -> None:
        self.messages.append(message)


def run_process(task_name: str, logger: Logger) -> None:
    logger.log(f"Starting {task_name}")
    # Perform the task ...
    logger.log(f"Finished {task_name}")


with FileLogger() as file_logger:
    run_process("DataCleanup", file_logger)
    print(f"log file: {file_logger.filename}")
    print(file_logger.filename.read_text(encoding="utf-8"))
## log file: logs\log.txt
## Starting DataCleanup
## Finished DataCleanup
## Starting DataCleanup
## Finished DataCleanup
## Starting DataCleanup
## Finished DataCleanup
## Starting DataCleanup
## Finished DataCleanup
## Starting DataCleanup
## Finished DataCleanup
## Starting DataCleanup
## Finished DataCleanup
## Starting DataCleanup
## Finished DataCleanup
## Starting DataCleanup
## Finished DataCleanup
## Starting DataCleanup
## Finished DataCleanup
## Starting DataCleanup
## Finished DataCleanup
## Starting DataCleanup
## Finished DataCleanup
## Starting DataCleanup
## Finished DataCleanup

# logs to list in memory:
test_logger = ListLogger()
run_process("DataCleanup", test_logger)
print("Captured logs:", test_logger.messages)
## Captured logs: ['Starting DataCleanup',
## 'Finished DataCleanup']
