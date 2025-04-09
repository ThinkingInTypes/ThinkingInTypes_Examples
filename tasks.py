"""
'Invoke' command file.
"""
import sys
from pathlib import Path
from pybooktools.invoke_tasks import examples, validate, namespace
from invoke import task
from rich.console import Console
from rich.prompt import Confirm

markdown_chapters_path = Path("C:/git/ThinkingInTypes.github.io/Chapters")
target_path = Path("C:/git/ThinkingInTypes_Examples")
temp_files = [Path("app.log"), Path("data.txt"), Path("other.txt")]

console = Console()


def confirm(message: str, default: bool = True) -> None:
    if not Confirm.ask(f"[yellow]{message}[/yellow]", default=default):
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
    """Formats documentation strings in Python files"""
    # ctx.run("docformatter -ri .")
    ctx.run("docformatter --in-place --wrap-summaries 50 --wrap-descriptions 50 \
    --make-summary-multi-line --pre-summary-newline -r .")


@task
def extract(ctx) -> None:
    """
    Extracts examples from chapter files into the examples directory.
    """
    ctx.run(f"mdvalid -d {markdown_chapters_path}")

    confirm(f"WARNING: delete the examples in {target_path}?", default=False)

    if target_path.exists():
        ctx.run(f"repoclean -a {target_path}")
    else:
        print(f"Directory does not exist: {target_path}")

    ctx.run(f"mdextract -d {markdown_chapters_path} {target_path}")


@task
def inject(ctx):
    """Injects examples back into the chapter files."""
    confirm("Inject examples back into book?", default=True)
    ctx.run(
        rf"mdinject -i {markdown_chapters_path} {target_path}"
    )


@task
def a(ctx) -> None:
    """
    All workflow tasks: extract, run all scripts, update examples, validate, re-inject examples into book.
    """

    confirm("Erase examples and extract new ones from book?", default=True)
    extract(ctx)

    confirm("Run all examples?", default=True)
    examples(ctx)

    confirm("Update embedded outputs with 'px -r .'?", default=True)
    ctx.run("px -r .")

    confirm("Validate example output?", default=True)
    validate(ctx)

    inject(ctx)

    console.print("[bold green]\n✅ Workflow completed successfully.[/bold green]")

    for file in temp_files:
        if file.exists():
            file.unlink()
            print(f"Deleted {file}")


namespace.add_task(a)
namespace.add_task(extract)
namespace.add_task(inject)
namespace.add_task(z)
namespace.add_task(docformat)
