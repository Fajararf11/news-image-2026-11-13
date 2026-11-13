#!/usr/bin/env python3
"""make.fun entry: publish entry.png to the output directory.

The artwork is pre-made and lives next to this script. The program only
copies it to <MAKEFUN_OUTPUT_DIR>/entry.png, creating the directory if it
does not exist. Standard library only, no network access.
"""

import os
import shutil
from pathlib import Path

# entry.png sits in the repository root, beside this file.
SOURCE = Path(__file__).resolve().parent / "entry.png"

# Competition default is /output; local runs can override via env var.
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)  # create if missing
    destination = OUTPUT_DIR / "entry.png"
    shutil.copyfile(SOURCE, destination)  # byte-for-byte copy, source untouched
    print(f"wrote {destination} ({destination.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
