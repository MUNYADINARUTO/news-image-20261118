#!/usr/bin/env python3
"""news-image-20261118 entrypoint.

Writes the finished front-page image for 18 November 2026 to
/output/entry.png. Deterministic: a pure byte copy of the bundled
asset, so every run produces identical bytes. No network access.

After copying, the output is verified against the bundled asset's
SHA-256 so a truncated or corrupted write is caught instead of
being submitted silently.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ASSET = os.path.join(HERE, "entry.png")
OUT_DIR = "/output"
OUT = os.path.join(OUT_DIR, "entry.png")
# SHA-256 of the bundled entry.png (front page for 18 November 2026).
EXPECTED_SHA256 = "bc55e20f4c2598f24fee6728bd2f97ba836f14206bd4d7ca4f17ed776b0401ec"


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(ASSET, OUT)
    digest = _sha256(OUT)
    if digest != EXPECTED_SHA256:
        raise SystemExit(
            f"output hash mismatch: got {digest}, expected {EXPECTED_SHA256}"
        )
    print(f"Wrote {OUT} ({os.path.getsize(OUT)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
