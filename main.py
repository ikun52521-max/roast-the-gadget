#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line about the phone -- the gadget used
every day -- to /output/entry.txt, and prints it to stdout.
Deterministic: the line is fixed, no randomness, no clock, no input.
"""

import os

ROAST = (
    "Every Sunday my phone sends me a screen time report like a "
    "disappointed parent: seven hours a day, with charts, as if the "
    "numbers will shame me into putting it down."
)


def main():
    line = ROAST.strip()
    assert line, "roast line must not be blank"
    assert len(line) <= 200, "roast line must be at most 200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)


if __name__ == "__main__":
    main()
