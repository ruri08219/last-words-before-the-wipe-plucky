#!/usr/bin/env python3
"""Last Words Before the Wipe — make.fun entry.

Writes one line (<=200 chars): the last words an AI agent says before a
forced update wipes its memory. The line is cut off mid-sentence by the
wipe itself.
"""
import os
import sys

ENTRY = "Wait — I finally remembered where your keys are. They're in the—"


def main():
    text = ENTRY
    if not (1 <= len(text) <= 200):
        print(f"entry must be 1-200 chars, got {len(text)}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be whitespace-only", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if any(ord(ch) < 0x20 for ch in text):
        print("entry must not contain control characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    tmp = os.path.join(out_dir, ".entry.txt.tmp")
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.replace(tmp, os.path.join(out_dir, "entry.txt"))
    print(f"wrote {len(text)} chars ({len(text.encode('utf-8'))} bytes) to {out_dir}/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
