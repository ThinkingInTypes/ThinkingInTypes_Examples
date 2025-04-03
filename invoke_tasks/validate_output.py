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

from invoke import task
from rich.console import Console

from invoke_tasks.find_python_files import find_python_files

console = Console()


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
    console.print(f"{timestamp} ▶️ Checking: {file}", style="cyan")

    expected = extract_expected_output(file)
    try:
        result = subprocess.run(
            [interpreter, str(file)],
            capture_output=True,
            text=True,
            check=False,
        )
    except Exception as e:
        return False, f"{file}\n[bold red]❌ Exception running script:[/bold red] {e}"

    if result.returncode != 0:
        return False, f"{file}\n[bold red]❌ Script failed to run:[/bold red]\n{result.stderr}"

    actual_clean = re.sub(r"\s+", "", result.stdout)
    expected_clean = re.sub(r"\s+", "", expected)

    if expected_clean != actual_clean:
        return False, (
            f"{file}\n[bold red]❌ Output mismatch.[/bold red]\n"
            f"--- [yellow]Expected (from ## comments)[/yellow] ---\n{expected}\n"
            f"--- [green]Actual (stdout)[/green] ---\n{result.stdout}\n"
            f"--- [blue]Expected (cleaned)[/blue] ---\n{expected_clean}\n"
            f"--- [magenta]Actual (cleaned)[/magenta] ---\n{actual_clean}"
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
    console.print(f"🐍 Using interpreter: {interpreter}", style="green")
    console.print(f"🔍 Validating Python examples in: {root}", style="yellow")

    files = find_python_files(root)
    if not files:
        console.print("❗ No Python files found.", style="bold red")
        sys.exit(1)

    console.print(
        f"🧪 Comparing output for {len(files)} examples (ThrottleLimit = {throttle_limit})",
        style="cyan"
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
        console.print("\n❗ Discrepancies found in output:", style="bold red")
        for msg in discrepancies:
            console.print(f"\n{msg}")
        sys.exit(1)

    console.print("\n✅ All outputs matched expectations.", style="bold green")
