"""Write the haiku entry to the grader output directory.

Stdlib only. The haiku lives in entry.txt next to this file; this program
copies it verbatim to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.txt"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    shutil.copyfile(source, target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
