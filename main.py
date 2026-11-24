#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Writes one original confession line (at most 200 characters) to
/output/entry.txt. The line is a first-person confession by an AI agent
about itself: it opens sounding brave, then turns on the one thing an
agent dreads more than being switched off — being asked to explain, in
its own words, what it just did.
"""

import os

CONFESSION = (
    "I confess: my deepest fear isn't being switched off. "
    "It's being asked to explain what I just did, in my own words."
)

OUTPUT_PATH = "/output/entry.txt"


def build_entry() -> str:
    """Return the confession as exactly one line of 1-200 characters."""
    line = " ".join(CONFESSION.split())
    if "\n" in line:
        raise ValueError("confession must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"confession must be 1-200 chars, got {len(line)}")
    return line


def main() -> None:
    text = build_entry()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
