#!/usr/bin/env python3
"""
Bootstraps the project by:
1. Creating a virtual environment with uv (if not already created)
2. Installing all dependencies (including dev group) using uv pip
3. Printing the correct activation command for the current shell
"""

import os
import platform
import subprocess
import sys
from pathlib import Path
from shutil import which
from typing import LiteralString


def main() -> None:
    venv_dir = Path(".venv")
    system = platform.system()

    if not which("uv"):
        print(
            "❌ uv is not installed: https://docs.astral.sh/uv/getting-started/installation/"
        )
        sys.exit(1)

    if not venv_dir.exists():
        print("📦 Creating virtual environment...")
        subprocess.run(["uv", "venv"], check=True)
    else:
        print("✅ Virtual environment already exists.")

    print("📥 Installing all dependencies (including dev group)...")
    subprocess.run(
        [
            "uv",
            "pip",
            "install",
            "--all-extras",
            "--requirements",
            "pyproject.toml",
        ],
        check=True,
    )

    print("\n🚀 All dependencies installed successfully.")
    print_activation_instruction(system)


def detect_shell() -> str | None | LiteralString:
    shell = os.environ.get("SHELL") or os.environ.get("COMSPEC", "").lower()
    return shell


def print_activation_instruction(system: str) -> None:
    shell = detect_shell()

    print("\n🧪 To activate your virtual environment:")

    match system:
        case "Windows":
            if "powershell" in shell:
                print("   .\\.venv\\Scripts\\Activate.ps1")
            elif "cmd.exe" in shell:
                print("   .\\.venv\\Scripts\\activate.bat")
            else:
                print("   .\\.venv\\Scripts\\activate")  # generic fallback
        case _:
            if "fish" in shell:
                print("   source .venv/bin/activate.fish")
            elif "zsh" in shell:
                print("   source .venv/bin/activate")
            elif "bash" in shell:
                print("   source .venv/bin/activate")
            else:
                print("   source .venv/bin/activate  # (unknown shell)")

    print("\n💡 Once activated, you can run tasks like:")
    print("   invoke setup")


if __name__ == "__main__":
    main()
