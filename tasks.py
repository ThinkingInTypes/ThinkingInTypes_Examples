# tasks.py
"""
'Invoke' command file.
"""

import subprocess
import sys
from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed,
)
from pathlib import Path

from invoke import task
from pybooktools.invoke_tasks import (
    examples,
    namespace,
    rewrite_with_semantic_breaks,
    validate,
)
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm

console = Console()

EXCLUDE_PATHS = {
    ".venv",
    "venv",
    "python",
    "__pycache__",
    ".mypy_cache",
    ".git",
    ".pytest_cache",
    ".idea",
    "tasks.py",
    "bootstrap.py",
    "book_utils",
    "xperiments",
}
WIDTH = 60  # Width for code listings and comments

markdown_chapters_path = Path(
    "C:/git/ThinkingInTypes.github.io/Chapters"
)
target_path = Path("C:/git/ThinkingInTypes_Examples")
temp_files = [
    Path("C:/git/ThinkingInTypes_Examples/data.txt"),
    Path("C:/git/ThinkingInTypes_Examples/other.txt"),
]


def cleanup():
    for temp_file in temp_files:
        if temp_file.exists():
            temp_file.unlink()
            # print(f"Deleted {temp_file}")


def confirm(
    message: str,
    default: bool = True,
    force: bool = False,
) -> None:
    if force:
        console.print(
            f"[green]Auto-confirmed:[/] {message}"
        )
        return
    if not Confirm.ask(
        f"[yellow]{message}[/yellow]",
        default=default,
    ):
        console.print("[red]Cancelled by user.[/red]")
        sys.exit(1)


@task(default=True)
def help(ctx) -> None:
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
def ruff(ctx) -> None:
    """
    Formats code in Python files.
    """
    ctx.run(f"ruff format --line-length {WIDTH}")


@task
def update_example_output(ctx, force: bool = False) -> None:
    """
    Updates embedded `##` outputs in examples.
    """
    confirm(
        "Update embedded outputs with 'px -r .'?",
        default=True,
        force=force,
    )
    ctx.run("px -r .")


@task
def extract(ctx, force: bool = False) -> None:
    """
    Extracts examples from chapter files into the examples
    directory.
    """
    ctx.run(f"mdvalid -d {markdown_chapters_path}")
    confirm(
        f"WARNING: delete the examples in {target_path} extract new ones from book?",
        default=False,
        force=force,
    )
    if target_path.exists():
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
def inject(ctx, force: bool = False):
    """
    Injects examples back into the chapter files.
    """
    confirm(
        "Inject examples back into book?",
        default=True,
        force=force,
    )
    ctx.run(
        rf"mdinject -i {markdown_chapters_path} {target_path}"
    )


@task
def sembr(ctx, chapter: Path):
    """
    Adds semantic breaks to the specified chapter.
    """
    _ = ctx
    if not isinstance(chapter, Path):
        chapter = Path(chapter)
    rewrite_with_semantic_breaks(chapter)


@task
def pyright(ctx):
    console.print(
        "[bold green]"
        + " Pyright ".center(80, "-")
        + "[/bold green]"
    )
    ctx.run("pyright")
    console.print(
        "[bold green]"
        + " End Pyright ".center(80, "-")
        + "[/bold green]"
    )


@task
def mypy(ctx) -> None:
    """
    Run mypy in parallel across all valid .py files in the repo.
    """
    _ = ctx
    root = Path(".").resolve()
    files = [
        path
        for path in root.rglob("*.py")
        if not any(
            part in EXCLUDE_PATHS for part in path.parts
        )
    ]

    if not files:
        console.print(
            "[bold red]No Python files found for mypy linting.[/bold red]"
        )
        return

    console.print(
        Panel.fit(
            f"⚡ Running mypy on [cyan]{len(files)}[/cyan] files in parallel...",
            title="Mypy Lint (Parallel)",
            border_style="blue",
        )
    )

    def check_file(path: Path) -> tuple[Path, int, str]:
        result = subprocess.run(
            [
                "mypy",
                "--no-error-summary",
                "--namespace-packages",
                "--ignore-missing-imports",
                str(path),
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        return (
            path,
            result.returncode,
            result.stdout.strip(),
        )

    error_count = 0

    with ThreadPoolExecutor() as executor:
        future_to_file = {
            executor.submit(check_file, path): path
            for path in files
        }
        for future in as_completed(future_to_file):
            path, code, output = future.result()
            if code != 0:
                error_count += 1
                console.print(
                    Panel(
                        output,
                        title=f"❌ {path}",
                        border_style="red",
                    )
                )

    if error_count:
        console.print(
            f"[bold red]❌ mypy failed on {error_count} files[/bold red]"
        )
        sys.exit(1)
    else:
        console.print(
            "[bold green]✅ All files passed mypy[/bold green]"
        )


@task
def a(ctx, force: bool = False) -> None:
    """
    All: extract, run all scripts, update examples, validate, re-inject examples into book. (--force runs w/o prompting)
    """
    extract(ctx, force=force)
    examples(ctx)
    pyright(ctx)
    update_example_output(ctx, force=force)
    validate(ctx)
    ruff(ctx)
    inject(ctx, force=force)
    console.print(
        "[bold green]\n✅ Workflow completed successfully.[/bold green]"
    )
    cleanup()


@task
def extract_and_run(ctx) -> None:
    """
    Extract and run all examples.
    """
    extract(ctx, force=True)
    examples(ctx)
    pyright(ctx)
    cleanup()


@task
def f(ctx, file: Path, force: bool = False) -> None:
    """
    Full workflow for a single file: extract, run, update, validate, inject. (--force runs w/o prompting)
    """
    if not isinstance(file, Path):
        file = Path(file)
    examples(ctx, file=str(file))
    update_example_output(
        ctx, force=force
    )  # Directory needs to be specified here
    validate(ctx)
    ruff(ctx)
    inject(ctx, force=force)
    console.print(
        f"[bold green]\n✅ Workflow completed successfully for {file}.[/bold green]"
    )
    cleanup()


namespace.add_task(a)
namespace.add_task(extract)
namespace.add_task(inject)
namespace.add_task(help)
namespace.add_task(docformat)
namespace.add_task(ruff)
namespace.add_task(update_example_output)
namespace.add_task(sembr)
namespace.add_task(extract_and_run)
namespace.add_task(pyright)
namespace.add_task(mypy)
