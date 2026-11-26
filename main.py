"""Funniest Lost Sock Status Update — make.fun bounty entry.

Writes one status update, at most 120 characters, in the voice of a
lost sock that has ended up somewhere it should not be, to
/output/entry.txt. The line is fixed and deterministic: the same
entry is produced on every run.
"""

import os

ENTRY = (
    "I'm a left sock living in the right shoe now. "
    "It's cramped, it's wrong, and honestly the arch support is better."
)

MAX_CHARS = 120


def write_entry(path: str) -> str:
    """Write ENTRY to path and read it back to prove it landed intact."""
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != ENTRY:
        raise SystemExit("entry.txt does not match the entry")
    return written


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise SystemExit(
            f"entry is {len(ENTRY)} characters, must be 1-{MAX_CHARS}"
        )
    if not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    write_entry(path)
    print(ENTRY)
    print(f"({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
