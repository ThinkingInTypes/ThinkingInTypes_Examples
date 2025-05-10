# tasks.py
"""
'Invoke' command file.
"""
import re
import shutil
import subprocess
import sys
from collections import defaultdict
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
from rich.text import Text

WIDTH = 65  # Width for code listings and comments
# 65 works for slidev with zoom: 2.0

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
    "slidev",
}

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
        console.print(f"[green]Auto-confirmed:[/] {message}")
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


def clean_pyright_output(text: str) -> str:
    # Fix common encoding artifacts
    text = text.replace("Â ", "  ")
    text = re.sub(r"[^\x00-\x7F]+", "", text)
    return text


def group_output_by_file(output: str) -> dict[str, list[str]]:
    """
    Groups Pyright output lines by file.
    Returns a dictionary mapping relative file paths to lists of lines.
    """
    file_groups: dict[str, list[str]] = defaultdict(list)
    current_file: str | None = None

    for line in output.splitlines():
        line_stripped = line.strip()

        if line_stripped.endswith(".py") and Path(line_stripped).is_absolute():
            try:
                current_file = str(Path(line_stripped).resolve().relative_to(Path.cwd()))
            except ValueError:
                current_file = Path(line_stripped).name
            file_groups[current_file] = []
        elif current_file:
            file_groups[current_file].append(line)

    return file_groups


@task
def pyright(ctx):
    console.print("[bold green]" + " Pyright ".center(80, "-") + "[/bold green]")

    result = ctx.run(
        "pyright", env={"PYRIGHT_DISABLE_COLOR": "1"}, warn=True, hide=True
    )

    cleaned_output = clean_pyright_output(result.stdout)
    grouped = group_output_by_file(cleaned_output)

    if not grouped:
        console.print("[bold green]No output from Pyright.[/bold green]")
    else:
        for path, lines in grouped.items():
            panel = Panel.fit(
                Text("\n".join(lines)),
                title=path,
                border_style="cyan"
            )
            console.print(panel)

    if result.exited != 0:
        console.print(f"[red]Pyright exited with code {result.exited}[/red]")

    console.print("[bold green]" + " End Pyright ".center(80, "-") + "[/bold green]")


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
        if not any(part in EXCLUDE_PATHS for part in path.parts)
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
    ruff(ctx)
    examples(ctx)
    pyright(ctx)
    update_example_output(ctx, force=force)
    validate(ctx)
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
def slideshow(ctx) -> None:
    """
    Launch Slidev in a brand-new pwsh window, detach immediately, and avoid
    the libuv assertion by pre-setting the console title.
    """
    _ = ctx
    # 1) Locate PowerShell 7+ or fall back
    pwsh = shutil.which("pwsh") or shutil.which("powershell.exe")
    if not pwsh:
        print(
            "❌ Neither pwsh nor powershell.exe were found on PATH."
        )
        return

    # 2) Compute the absolute path to slidev
    slides_dir = Path("slidev").resolve()

    # 3) Pick a title for the new console (must be nonempty!)
    window_title = "Slide Show"

    # 4) Build the pwsh -Command string:
    #    1. Set the console title so libuv has something non-null
    #    2. Change directory into your slidev folder
    #    3. Launch the dev server
    pwsh_cmd = (
        rf"[Console]::Title='{window_title}';"
        rf"Set-Location '{slides_dir}';"
        "pnpm slidev Slides.md"
    )

    # 5) Finally, spawn the new console fully detached.
    #    - shell=True so that `start` is interpreted by cmd.exe
    #    - CREATE_NEW_CONSOLE ensures a brand-new window
    subprocess.Popen(
        f'start "" "{pwsh}" -NoExit -Command "{pwsh_cmd}"',
        shell=True,
        creationflags=subprocess.CREATE_NEW_CONSOLE,
    )


# else:
#     # fallback for POSIX: allocate a PTY
#     with ctx.cd("slidev"):
#         ctx.run("pnpm slidev Slides.md", pty=True)
# @task
# def slideshow(ctx) -> None:
#     """
#     Run slidev
#     """
#     ctx.run("cd slidev && pnpm slidev Slides.md")


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
namespace.add_task(slideshow)
