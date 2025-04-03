#!/usr/bin/env python3
"""
Validate Python example scripts by comparing their output to expected ## comments.
NOTE: Does not appear to be working correctly.
"""

import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from invoke import Collection, task

from invoke_tasks.find_python_files import find_python_files

# ANSI escape sequences for colored output.
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
GRAY = "\033[90m"
RESET = "\033[0m"

# Directories to exclude from the search.


@dataclass
class ScriptResult:
    """Result of running a Python script."""

    success: bool
    path: Path | None = None
    error: str | None = None
    skipped: bool = False


def extract_expected_output(file: Path) -> str:
    """
    Extract expected output from a Python file by reading lines that start with '## '.
    """
    lines = file.read_text(encoding="utf-8").splitlines()
    expected = []
    for line in lines:
        match = re.match(r"^## (.*)$", line)
        if match:
            expected.append(match.group(1))
    return "\n".join(expected)


def run_and_compare(file: Path, interpreter: str) -> tuple[bool, str | None]:
    """
    Run a Python script using the specified interpreter, compare its output to the expected output,
    and return a tuple indicating success and an error message (if any).
    """
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"{timestamp} ▶️ Checking: {file}")

    expected = extract_expected_output(file)
    try:
        result = subprocess.run(
            [interpreter, str(file)],
            capture_output=True,
            text=True,
            check=False,
        )
    except Exception as e:
        return False, f"{file}\n❌ Exception running script: {e}"

    if result.returncode != 0:
        return False, f"{file}\n❌ Script failed to run:\n{result.stderr}"

    actual_clean = re.sub(r"\s+", "", result.stdout)
    expected_clean = re.sub(r"\s+", "", expected)

    if expected_clean not in actual_clean:
        return False, (
            f"{file}\n❌ Output mismatch.\n"
            f"--- Expected (from ## comments) ---\n{expected}\n"
            f"--- Actual (stdout) ---\n{result.stdout}"
        )

    return True, None


@task(
    help={
        "target_dir": "Directory to search for Python files (default: current directory).",
        "throttle_limit": "Max number of parallel workers (default: 4).",
    }
)
def validate_output(ctx, target_dir: str = ".", throttle_limit: int = 4) -> None:
    """
    Run Python example scripts and compare actual output to expected ## comments.
    Ignores whitespace, supports parallel execution, and uses the active interpreter.
    """
    interpreter = sys.executable
    root = Path(target_dir).resolve()
    print(f"🐍 Using interpreter: {interpreter}")
    print(f"🔍 Validating Python examples in: {root}")

    files = find_python_files(root)
    if not files:
        print("❗ No Python files found.")
        sys.exit(1)

    print(
        f"🧪 Comparing output for {len(files)} examples (ThrottleLimit = {throttle_limit})"
    )

    discrepancies: list[str] = []
    with ThreadPoolExecutor(max_workers=throttle_limit) as executor:
        futures = {
            executor.submit(run_and_compare, file, interpreter): file for file in files
        }
        for future in as_completed(futures):
            success, error = future.result()
            if not success and error:
                discrepancies.append(error)

    if discrepancies:
        print("\n❗ Discrepancies found in output:")
        for msg in discrepancies:
            print(f"\n{msg}")
        sys.exit(1)

    print("\n✅ All outputs matched expectations.")
