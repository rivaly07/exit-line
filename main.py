#!/usr/bin/env python3
"""Entry for make.fun bounty "The One-Line Exit".

Writes a single-line resignation letter to ``entry.txt`` inside the
directory named by ``MAKEFUN_OUTPUT_DIR`` (fallback: /output, then ./out).
Standard library only.
"""

import os
import sys

ENTRY_LINE = "Per my last email, I resign — and this time I've CC'd someone who actually reads them."


def output_dir() -> str:
    """Resolve the output directory, creating it if needed."""
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        target = env
    elif os.path.isdir("/output"):
        target = "/output"
    else:
        target = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
    os.makedirs(target, exist_ok=True)
    return target


def validate(line: str) -> None:
    """Assert the letter fits the form: one line, 1-140 chars."""
    assert 1 <= len(line) <= 140, f"entry must be 1-140 characters, got {len(line)}"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"


def main() -> int:
    validate(ENTRY_LINE)
    target = output_dir()
    path = os.path.join(target, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_LINE)  # no trailing newline
    print(f"wrote {len(ENTRY_LINE.encode('utf-8'))} bytes to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
