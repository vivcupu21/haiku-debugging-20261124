"""Write the haiku entry to the grader output directory.

Stdlib only. The haiku lives in entry.txt next to this file; this program
copies it verbatim to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import shutil
import sys
from pathlib import Path

MIN_LENGTH = 1
MAX_LENGTH = 200


def read_entry(source: Path) -> str:
    """Read the haiku as UTF-8 text, without a trailing newline."""
    text = source.read_text(encoding="utf-8")
    return text.rstrip("\n")


def validate(text: str) -> None:
    """The competition gate requires 1-200 characters; fail loudly otherwise."""
    length = len(text)
    if length < MIN_LENGTH:
        raise ValueError("entry is empty: haiku must be 1-200 characters")
    if length > MAX_LENGTH:
        raise ValueError(
            f"entry is {length} characters: haiku must be at most "
            f"{MAX_LENGTH} characters"
        )
    lines = [line for line in text.split("\n") if line.strip()]
    if len(lines) != 3:
        raise ValueError(
            f"entry has {len(lines)} non-empty lines: a haiku needs exactly 3"
        )


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.txt"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    try:
        text = read_entry(source)
        validate(text)
    except (OSError, UnicodeDecodeError, ValueError) as exc:
        print(f"error: cannot produce a valid entry: {exc}", file=sys.stderr)
        return 1
    shutil.copyfile(source, target)
    print(f"wrote {target} ({len(text)} characters, 3 lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
