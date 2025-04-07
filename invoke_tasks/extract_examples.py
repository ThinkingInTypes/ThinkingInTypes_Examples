from pathlib import Path
from invoke import task


@task
def extract(ctx) -> None:
    """
    Deletes the examples target_path after confirmation, validates Markdown, then extracts examples
    from chapter files into the examples target_path.
    """
    markdown_chapters_path = Path("C:/git/ThinkingInTypes.github.io/Chapters")
    target_path = Path("C:/git/ThinkingInTypes_Examples")

    ctx.run(f"mdvalid -d {markdown_chapters_path}")
    print(f"WARNING: You are about to delete the examples in: {target_path}")
    response = input("Are you sure? Type 'y' to continue: ")

    if response.lower() == 'y':
        if target_path.exists():
            ctx.run(f"repoclean -a {target_path}")
        else:
            print(f"Directory does not exist: {target_path}")

        ctx.run(f"mdextract -d {markdown_chapters_path} {target_path}")
    else:
        print("Operation canceled.")
