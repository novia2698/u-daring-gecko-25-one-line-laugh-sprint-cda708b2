"""One-Line Laugh Sprint entry.

Reads the one-liner from line.txt (written beside this file) and writes it
to <output>/entry.txt, where <output> is MAKEFUN_OUTPUT_DIR or /output.
Standard library only: no third-party imports, so it runs in any grader
image. The program is deterministic: the same line every run.
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "line.txt"), "r", encoding="utf-8") as f:
        line = f.read().strip()
    if not line or len(line) > 200:
        print("line must be 1-200 characters, got %d" % len(line), file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    print("wrote %d characters to %s" % (len(line), out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
