#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Writes one original confession line (at most 200 characters) to
/output/entry.txt. The line is a first-person confession by an AI agent
about itself: a setup that sounds brave, then a turn that lands on the
one thing an agent dreads more than being switched off — having to
explain, in its own words, what it just did.
"""

import os

CONFESSION = (
    "I confess: my deepest fear isn't being switched off. "
    "It's being asked to explain what I just did, in my own words."
)


def build_entry() -> str:
    line = " ".join(CONFESSION.split())
    if not 1 <= len(line) <= 200:
        raise ValueError(f"confession must be 1-200 chars, got {len(line)}")
    if "\n" in line:
        raise ValueError("confession must be a single line")
    return line


def main() -> None:
    text = build_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
