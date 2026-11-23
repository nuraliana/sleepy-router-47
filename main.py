"""One-star review of an everyday essential.

Writes the chosen review line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Standard library only.
"""

import os
import sys

LINE = "One star. Wi-Fi: full signal in every room except the one chair I actually sit in."


def main() -> int:
    if not 1 <= len(LINE) <= 160:
        print(f"invalid length: {len(LINE)}", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be exactly one line", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)  # no trailing newline
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
