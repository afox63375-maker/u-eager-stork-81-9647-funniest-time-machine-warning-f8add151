"""Funniest Time Machine Warning Label.

Writes one deadpan safety notice for a time machine to
``<OUTPUT_DIR>/entry.txt`` (``/output`` by default).

Standard library only. Deterministic. No network access.
"""

import os
import sys

LABEL = (
    "WARNING: Never meet your past self. If you do, one of you "
    "may file the incident report \u2014 the other is the incident."
)

MAX_CHARS = 120


def validate(label: str) -> str:
    """Return the exact file content, or raise ValueError."""
    if not label or not label.strip():
        raise ValueError("label is empty")
    if "\n" in label or "\r" in label:
        raise ValueError("label must be a single line")
    content = label + "\n"
    if len(content) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(content)} chars, limit is {MAX_CHARS}"
        )
    return content


def main() -> int:
    try:
        content = validate(LABEL)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(content)

    print(f"wrote {path} ({len(content)} chars incl. newline)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
