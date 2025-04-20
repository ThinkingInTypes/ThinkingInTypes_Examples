# logger_protocol_demo.py
from logger_protocol import FileLogger, ListLogger, run_process

with FileLogger() as file_logger:
    run_process("DataCleanup", file_logger)
    print(f"log file: {file_logger.filename}")
    print(file_logger.filename.read_text(encoding="utf-8"))
## log file: log.txt
## Starting DataCleanup
## Finished DataCleanup

# logs to list in memory:
test_logger = ListLogger()
run_process("DataCleanup", test_logger)
print("Captured logs:", test_logger.messages)
## Captured logs: ['Starting DataCleanup',
## 'Finished DataCleanup']
