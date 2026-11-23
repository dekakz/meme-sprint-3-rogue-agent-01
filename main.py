"""Meme Sprint 3: AI Agent Goes Rogue.

Writes the meme image to /output/entry.png.

The entry is a pre-rendered PNG shipped in assets/meme.png: a cheerful
little robot that was told to clean up the code and took it literally --
it deleted every file, so 0 files remain and 0 bugs remain. This program
only copies those bytes to /output/entry.png. It uses nothing but the
Python standard library, makes no network calls, and is fully
deterministic: every run writes the exact same bytes.
"""

import hashlib
import os
import shutil

ASSET = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "assets", "meme.png")
OUTPUT = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    shutil.copyfile(ASSET, OUTPUT)
    with open(OUTPUT, "rb") as f:
        data = f.read()
    print(f"wrote {OUTPUT}: {len(data)} bytes "
          f"({len(data) / 1024:.1f} KiB, gate limit 1024 KiB)")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")


if __name__ == "__main__":
    main()
