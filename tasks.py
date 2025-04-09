# tasks.py
"""
'Invoke' command file.
"""
import sys
from pathlib import Path
from pybooktools.invoke_tasks import (
    examples,
    validate,
    namespace,
)
from invoke import task
from rich.console import Console
from rich.prompt import Confirm

WIDTH = 60  # Width for code listings and comments

markdown_chapters_path = Path(
    "C:/git/ThinkingInTypes.github.io/Chapters"
)
target_path = Path("C:/git/ThinkingInTypes_Examples")
temp_files = [
    Path("app.log"),
    Path("data.txt"),
    Path("other.txt"),
]

console = Console()


def confirm(message: str, default: bool = True) -> None:
    if not Confirm.ask(
        f"[yellow]{message}[/yellow]",
        default=default,
    ):
        console.print("[red]Cancelled by user.[/red]")
        sys.exit(1)


@task(default=True)
def z(ctx) -> None:
    """
    List available tasks.
    """
    ctx.run("invoke -l")


@task
def docformat(ctx) -> None:
    """
    Formats documentation strings in Python files.
    """
    ctx.run(
        f"docformatter --in-place --wrap-summaries {WIDTH} --wrap-descriptions {WIDTH} \
    --make-summary-multi-line --pre-summary-newline -r ."
    )


@task
def codeformat(ctx) -> None:
    """
    Formats code in Python files.
    """
    ctx.run(f"ruff format --line-length {WIDTH}")


@task
def update_example_output(ctx) -> None:
    """
    Updates embedded `##` outputs in examples.
    """
    confirm(
        "Update embedded outputs with 'px -r .'?",
        default=True,
    )
    ctx.run("px -r .")


@task
def extract(ctx) -> None:
    """
    Extracts examples from chapter files into the
    examples directory.
    """
    ctx.run(f"mdvalid -d {markdown_chapters_path}")
    confirm(
        f"WARNING: delete the examples in {target_path} extract new ones from book?",
        default=False,
    )
    if (
        target_path.exists()
    ):  # Check repoclean to see if it already does this
        ctx.run(f"repoclean -a {target_path}")
    else:
        print(f"Directory does not exist: {target_path}")
    print(
        f"Running: mdextract -d {markdown_chapters_path} {target_path}"
    )
    ctx.run(
        f"mdextract -d {markdown_chapters_path} {target_path}"
    )


@task
def inject(ctx):
    """
    Injects examples back into the chapter files.
    """
    confirm(
        "Inject examples back into book?",
        default=True,
    )
    ctx.run(
        rf"mdinject -i {markdown_chapters_path} {target_path}"
    )


@task
def a(ctx) -> None:
    """
    All workflow tasks: extract, run all scripts, update examples, validate, re-inject examples into book.
    """
    extract(ctx)
    examples(ctx)
    update_example_output(ctx)
    validate(ctx)
    inject(ctx)
    console.print(
        "[bold green]\n✅ Workflow completed successfully.[/bold green]"
    )
    for file in temp_files:
        if file.exists():
            file.unlink()
            print(f"Deleted {file}")


namespace.add_task(a)
namespace.add_task(extract)
namespace.add_task(inject)
namespace.add_task(z)
namespace.add_task(docformat)
namespace.add_task(codeformat)
namespace.add_task(update_example_output)
