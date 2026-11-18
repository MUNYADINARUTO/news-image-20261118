#!/usr/bin/env python3
"""news-image-20261118 entrypoint.

Writes the finished front-page image for 18 November 2026 to
/output/entry.png. Deterministic: a pure byte copy of the bundled
asset, so every run produces identical bytes. No network access.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ASSET = os.path.join(HERE, "entry.png")
OUT_DIR = "/output"
OUT = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(ASSET, OUT)
    print(f"Wrote {OUT} ({os.path.getsize(OUT)} bytes)")


if __name__ == "__main__":
    main()
