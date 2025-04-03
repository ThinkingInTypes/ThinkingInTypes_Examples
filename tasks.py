#!/usr/bin/env python3
"""
Use pyinvoke to run all Python scripts in a directory tree (or a specific subdirectory) in parallel.
Skips __init__.py files and anything inside venv/.venv directories.
Prints colored output with timestamps and stops all jobs on first failure.
This file is a conversion of the PowerShell script "RunAllPythonExamplesParallel.ps1" to pyinvoke.
"""

import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from invoke import task

# ANSI escape sequences for colored output.
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
GRAY = "\033[90m"
RESET = "\033[0m"

# Directories to exclude from the search.
EXCLUDED_DIRS = {"venv", ".venv", "__pycache__", ".git"}
EXCLUDED_FILES = {"__init__.py", "tasks.py"}


@dataclass
class ScriptResult:
    """Result of running a Python script."""

    success: bool
    path: Path | None = None
    error: str | None = None
    skipped: bool = False


def find_python_files(target_dir: Path) -> list[Path]:
    """
    Recursively find all Python files (*.py) in target_dir,
    excluding __init__.py files and files in excluded directories.
    """
    python_files: list[Path] = []
    for file in target_dir.rglob("*.py"):
        if file.name in EXCLUDED_FILES:
            continue
        if any(ex_dir in file.parts for ex_dir in EXCLUDED_DIRS):
            continue
        python_files.append(file)
    return python_files


def run_script(file: Path, failure_event: threading.Event) -> ScriptResult:
    """
    Run the Python script specified by file.
    If the failure_event is set, skip running.
    Uses a polling loop to allow early termination if a failure is detected.
    """
    if failure_event.is_set():
        return ScriptResult(
            success=False,
            path=file,
            error="Skipped due to a previous failure",
            skipped=True,
        )

    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"{timestamp} {CYAN}▶️ Running: {file}{RESET}")

    try:
        process = subprocess.Popen(
            ["python", str(file)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        # Polling loop to check for a failure flag.
        while True:
            if failure_event.is_set():
                if process.poll() is None:
                    process.terminate()
                    process.wait()
                    return ScriptResult(
                        success=False,
                        path=file,
                        error="Terminated due to another failure",
                    )
            ret = process.poll()
            if ret is not None:
                break
            time.sleep(0.1)
        stdout, stderr = process.communicate()

        if ret != 0:
            failure_event.set()
            return ScriptResult(success=False, path=file, error=stderr)
        else:
            if stdout:
                print(f"{GRAY}{stdout}{RESET}")
            return ScriptResult(success=True)
    except Exception as e:
        failure_event.set()
        return ScriptResult(success=False, path=file, error=str(e))


@task(
    help={
        "target_dir": "Directory to search for Python files (default: current directory).",
        "throttle_limit": "Maximum number of parallel processes (default: number of processors).",
    }
)
def run_all(ctx, target_dir: str = ".", throttle_limit: int | None = None) -> None:
    """
    Run all Python scripts in a directory tree in parallel.

    This task searches for Python files (skipping __init__.py and files in directories
    such as venv, .venv, __pycache__, or .git) and runs them concurrently with a throttle
    limit on the number of parallel processes. If any script fails (i.e. exits with a nonzero
    status), the task stops further execution and prints an error message.
    """
    target_path = Path(target_dir).resolve()
    print(f"{YELLOW}🔍 Searching for Python files in: {target_path}{RESET}")

    python_files = find_python_files(target_path)
    if not python_files:
        print(f"{RED}❗ No Python files found.{RESET}")
        sys.exit(1)

    if throttle_limit is None:
        try:
            import os

            throttle_limit = os.cpu_count() or 1
        except Exception:
            throttle_limit = 1

    print(
        f"{GREEN}🚀 Running {len(python_files)} scripts in parallel (ThrottleLimit = {throttle_limit}){RESET}"
    )

    failure_event = threading.Event()
    results: list[ScriptResult] = []

    # Use ThreadPoolExecutor to limit parallelism.
    with ThreadPoolExecutor(max_workers=throttle_limit) as executor:
        future_to_file = {
            executor.submit(run_script, file, failure_event): file
            for file in python_files
        }
        for future in as_completed(future_to_file):
            result = future.result()
            results.append(result)
            if not result.success and not result.skipped:
                print(f"\n{RED}Failed: {result.path}\n{result.error}{RESET}")
                # Setting the failure_event should signal other tasks to terminate if possible.
                failure_event.set()
                break

    if any(not res.success and not res.skipped for res in results):
        print(f"\n{RED}❌ One or more scripts failed.{RESET}")
        sys.exit(1)

    print(f"\n{GREEN}✅ All scripts ran successfully.{RESET}")
