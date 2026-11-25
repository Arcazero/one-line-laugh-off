#!/usr/bin/env python3
"""One-Line Laugh-Off — make.fun entry.

Writes exactly one funny line to /output/entry.txt: a smart speaker
tries to comfort a lonely human and lands the wrong way round.
The program is deterministic: it always writes the same fixed line.
"""

import os

LINE = "I told my smart speaker I felt lonely, so it started playing the sound of a party I'm not invited to."


def main() -> None:
    # Gate: the bounty only accepts a single line of 1-200 chars.
    assert 1 <= len(LINE) <= 200, f"entry line is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE, "entry line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
