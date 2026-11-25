#!/usr/bin/env python3
# Fridge roast entry: one line about the fridge's ice maker, to /output/entry.txt.
# Pure standard library. The gate wants 1-200 characters, a single line.
# The joke is the ice maker: a 3 a.m. rockslide of noise, and the grand
# payoff for all that drama is exactly one cube.

from pathlib import Path

LINE = "My fridge's ice maker wakes me at 3 a.m. sounding like a rockslide, then proudly delivers exactly one cube."
TARGET = Path("/output/entry.txt")


def run() -> None:
    text = LINE.strip()
    assert 0 < len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    run()
