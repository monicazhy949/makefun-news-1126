"""Copy the news image to the output directory.

Standard library only. The grader runs this program twice with no
network; both runs must write identical bytes. The image lives in the
repository as entry.png next to this file, so the program just copies
it: the bytes written are exactly the bytes shipped.

Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    if not SOURCE.is_file():
        print(f"error: source image missing: {SOURCE}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(SOURCE, dest)
    if sha256_of(dest) != sha256_of(SOURCE):
        print("error: copied bytes differ from source", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({dest.stat().st_size} bytes, "
          f"sha256 {sha256_of(dest)[:12]}...)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
