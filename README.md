# ThinkingInTypes_Examples

Examples for the book [Thinking in Types](https://thinkingintypes.com/) by Bruce Eckel

This project uses:

- [`uv`](https://docs.astral.sh/uv/), a fast Python package manager and virtual environment tool.
- [`pyinvoke`](https://docs.pyinvoke.org/en/stable/), a command runner (automatically installed by the instructions below).

## Setup

1. Clone this repository
2. Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
3. Run `uv run bootstrap.py`
   - Creates a `.venv` directory
   - Installs all dependencies (including dev tools like `invoke`, `ruff`, etc.)
   - Displays instructions to activate the virtual environment
4. Activate the virtual environment.
5. Test by running `invoke run-all`, which runs all examples and ensures they succeed.

If you activate the virtual environment, you can run any example with `python example.py`.
Without activation, use `uv run example.py`.

## Notes

- If you have `pip` issues, try `python -m ensurepip --upgrade`
- If you're trying to see which Python uvx is using, run:
  `uvx python -c "import sys; print(sys.executable)"`

## To Run the Slidev Presentations

- Install `pnpm`. In Windows: `winget install --id pnpm.pnpm`
- `cd slidev`
- `pnpm slidev Slides.md` (or whatever slides Markdown file you want to run)
