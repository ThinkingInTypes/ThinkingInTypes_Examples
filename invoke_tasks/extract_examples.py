import shutil
from pathlib import Path
from invoke import task


@task
def extract(ctx) -> None:
    """
    Deletes the examples directory after confirmation, validates Markdown, then extracts examples
    from chapter files into the examples directory.
    """
    directory = Path("C:/git/ThinkingInTypes_Examples")
    chapters_dir = Path("C:/git/ThinkingInTypes.github.io/Chapters")

    ctx.run(f"mdvalid -d {chapters_dir}")
    print(f"WARNING: You are about to delete the examples in: {directory}")
    response = input("Are you sure? Type 'y' to continue: ")

    if response.lower() == 'y':
        if directory.exists():
            ctx.run(f"repoclean -a {directory}")
        else:
            print(f"Directory does not exist: {directory}")

        ctx.run(f"mdextract -d {chapters_dir} {directory}")
    else:
        print("Operation canceled.")
