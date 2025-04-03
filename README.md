# ThinkingInTypes_Examples

Examples for the book [Thinking in Types](https://thinkingintypes.com/) by Bruce Eckel

This project uses:

- `uv`, a fast Python package manager and virtual environment tool.
- `pyinvoke`, a command runner (automatically installed by the instructions below).

## Setup

1. Clone this repository
2. Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
3. Run `uv run bootstrap.py`
   - Creates a `.venv` directory
   - Installs all dependencies (including dev tools like `invoke`, `ruff`, etc.)
   - Displays instructions to activate the environment
4. Test by running `uvx invoke run-all`, which runs all examples and ensures they succeed.

- If you activate the virtual environment, you can run any example with `python example.py`.
- Without activation, use `uv run example.py`.
