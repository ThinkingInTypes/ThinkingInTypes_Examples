"""
Main tasks file that aggregates tasks from the 'tasks' subdirectory.
"""
import subprocess
import sys

from invoke import task
from rich.console import Console
from rich.prompt import Confirm

from invoke_tasks import namespace, validate_output, run_all, examples, validate

console = Console()


@task
def full(ctx) -> None:
    """
    Full workflow: extract, run all scripts, update examples, validate, re-inject examples into book.
    """

    def confirm(message: str, default: bool = True) -> None:
        if not Confirm.ask(f"[yellow]{message}[/yellow]", default=default):
            console.print("[red]Cancelled by user.[/red]")
            sys.exit(1)

    confirm("Erase examples and extract new ones from book?", default=True)
    subprocess.run(["powershell", "-File", "..\\ThinkingInTypes.github.io\\extract.ps1"], check=True)

    confirm("Run all examples?", default=True)
    examples(ctx)

    confirm("Update embedded outputs with 'px -r .'?", default=True)
    ctx.run(["px", "-r", "."], check=True)

    confirm("Validate example output?", default=True)
    validate(ctx)

    confirm("Inject examples back into book?", default=True)
    subprocess.run(["powershell", "-File", "..\\ThinkingInTypes.github.io\\inject.ps1"], check=True)

    console.print("[bold green]\n✅ Workflow completed successfully.[/bold green]")


namespace.add_task(full)
