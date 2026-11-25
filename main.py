#!/usr/bin/env python3
"""One-line fridge roast, written to /output/entry.txt.

The gag is the ice maker: a 3 a.m. rockslide of noise, and after all that
drama the grand payoff is exactly one cube.
"""

import os

JOKE = 'My fridge\'s ice maker wakes me at 3 a.m. sounding like a rockslide, then proudly delivers exactly one cube.'
OUT = os.path.join("/output", "entry.txt")


def main():
    line = JOKE.strip()
    if not 1 <= len(line) <= 200:
        raise SystemExit("entry must be 1-200 characters")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be one line")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(line)


if __name__ == "__main__":
    main()
