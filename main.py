#!/usr/bin/env python3
"""make.fun competition entry: publish entry.png to the output directory.

Competition: make.fun — brief "Sum up 13 November's world news in one image."

The artwork is pre-made and lives next to this script. The program copies it
to <MAKEFUN_OUTPUT_DIR>/entry.png, creating the directory if it does not
exist, then re-reads the copy and checks that its SHA-256 matches both the
source file and the pinned digest below. A mismatch raises RuntimeError so a
corrupted or substituted image can never be published silently.

Standard library only, no network access.
"""

import hashlib
import os
import shutil
from pathlib import Path

# entry.png sits in the repository root, beside this file.
SOURCE = Path(__file__).resolve().parent / "entry.png"

# Competition default is /output; local runs can override via env var.
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

# Digest of the committed artwork; the published copy must match exactly.
EXPECTED_SHA256 = "ce25d11f3d412dbf9ea223f5133b727344be5b623c4d63e8cdce9a85c5b939fc"

CHUNK_SIZE = 1024 * 1024  # stream in 1 MiB blocks to keep memory flat


def sha256_of(path: Path) -> str:
    """Return the hex SHA-256 digest of a file, read in chunks."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)  # create if missing
    destination = OUTPUT_DIR / "entry.png"
    shutil.copyfile(SOURCE, destination)  # byte-for-byte copy, source untouched

    source_digest = sha256_of(SOURCE)
    copied_digest = sha256_of(destination)

    if copied_digest != source_digest:
        raise RuntimeError(
            f"copy verification failed: {destination} has sha256 {copied_digest}, "
            f"but source {SOURCE} has {source_digest}"
        )
    if copied_digest != EXPECTED_SHA256:
        raise RuntimeError(
            f"artwork verification failed: {SOURCE} has sha256 {source_digest}, "
            f"expected {EXPECTED_SHA256} — entry.png is not the committed artwork"
        )

    print(
        f"wrote {destination} ({destination.stat().st_size} bytes, "
        f"sha256 {copied_digest})"
    )


if __name__ == "__main__":
    main()
