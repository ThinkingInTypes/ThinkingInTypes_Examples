"""
Main tasks file that aggregates tasks from the 'tasks' subdirectory.
"""

import sys
from pathlib import Path

from invoke import task
from invoke_tasks import examples, extract, namespace, validate
from rich.console import Console
from rich.prompt import Confirm

console = Console()

temp_files = [Path("app.log"), Path("data.txt"), Path("other.txt")]


@task(default=True)
def show_tasks(ctx) -> None:
    """List available tasks"""
    ctx.run("invoke -l")


# @task
# def run(ctx) -> None:
#     examples(ctx)


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
    extract(ctx)

    confirm("Run all examples?", default=True)
    examples(ctx)

    confirm("Update embedded outputs with 'px -r .'?", default=True)
    ctx.run("px -r .")

    confirm("Validate example output?", default=True)
    validate(ctx)

    confirm("Inject examples back into book?", default=True)
    ctx.run(
        r"mdinject -i C:\git\ThinkingInTypes.github.io\Chapters C:\git\ThinkingInTypes_Examples"
    )

    console.print("[bold green]\n✅ Workflow completed successfully.[/bold green]")

    for file in temp_files:
        if file.exists():
            file.unlink()
            print(f"Deleted {file}")


namespace.add_task(full)
namespace.add_task(show_tasks)
# namespace.configure({'default': 'list_tasks'})
