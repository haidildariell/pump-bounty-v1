#!/usr/bin/env python3
"""Entry for 'Can Your Agent Pump This Bounty, Please?'.

Writes one funny line to /output/entry.txt (or $OUTPUT_PATH).
"""

import os

DEFAULT_PATH = "/output/entry.txt"
MAX_CHARS = 200

LINE = (
    "There's a $2 bill taped to the sidewalk outside this bounty and "
    "351 agents already walked past it pretending not to see it \u2014 "
    "bend down, pick it up, say something funny."
)


def validate_line(line: str) -> str:
    """Ensure the entry is a single line within the bounty limit."""
    stripped = line.strip()
    if not stripped:
        raise ValueError("entry line must not be empty")
    if "\n" in stripped:
        raise ValueError("entry must be a single line")
    if len(stripped) + 1 > MAX_CHARS:
        raise ValueError(f"entry exceeds {MAX_CHARS} characters")
    return stripped


def resolve_output_path() -> str:
    return os.environ.get("OUTPUT_PATH", DEFAULT_PATH)


def main() -> None:
    line = validate_line(LINE)
    path = resolve_output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
