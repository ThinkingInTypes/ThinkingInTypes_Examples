# logger_protocol.py
from typing import Protocol
from pathlib import Path
import tempfile
import os
from contextlib import AbstractContextManager


class Logger(Protocol):
    def log(self, message: str) -> None: ...


class FileLogger(AbstractContextManager):
    """
    Logger that writes to a temporary file.
    Automatically cleans up via the context manager.
    """

    def __init__(self):
        self._temp_file = tempfile.NamedTemporaryFile(
            delete=False, mode="a", encoding="utf-8"
        )
        self.filename = Path(self._temp_file.name)

    def log(self, message: str) -> None:
        self._temp_file.write(message + "\n")
        self._temp_file.flush()

    def __exit__(
        self, exc_type, exc_value, traceback
    ) -> None:
        self._temp_file.close()
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass


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

# logs to list in memory:
test_logger = ListLogger()
run_process("DataCleanup", test_logger)
print("Captured logs:", test_logger.messages)
