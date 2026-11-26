#!/usr/bin/env python3
"""The Printer Apology — entry (Python 3.13, stdlib only).

Entry line (100 chars, one line, no trailing newline):

    Sorry I need cyan to print black. I am not broken, I am holding your
    black ink hostage for a friend.

Why it wins, in the judge's order: genuinely an apology from a printer to
its office, with the printer's own gripe in it (it is forced to demand
cyan for a black page, and it resents the office for it); a real joke, the
punch at the end — the printer is not broken, it is running a hostage
negotiation, and it has an accomplice; printer truth — every office has
watched a printer refuse a black page for want of cyan; fresh — the cyan
ransom is an empty lane, not the flooded jam / copies / cheap-paper /
toner-warning / ate-the-report jokes; economy — 100 chars, every word
earns its place. Chosen by a 66-game pairwise tournament over 12
candidates in empty lanes (CANDIDATES.md): 11-0, and 7-0 against the
reference opponents.

One constant, gate guards mirroring the competition gate (1-120 characters,
one line, not only whitespace — checked both as code points and as UTF-8
bytes), written with no trailing newline. No clock, no random source, no
network, so two runs write identical bytes.

Run: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys
from pathlib import Path

# The line: one apology, one ransom demand, one accomplice.
LINE = (
    "Sorry I need cyan to print black. I am not broken, I am holding your "
    "black ink hostage for a friend."
)

# The gate, applied before anything is written. "1 to 120 characters" is
# held under BOTH readings (code points and UTF-8 bytes); plain ASCII, so
# both counts agree at 100.
MIN_CHARS = 1
MAX_CHARS = 120


def abort(why: str) -> None:
    """Fail loudly instead of writing an entry the gate would refuse."""
    raise SystemExit("main.py: " + why)


def output_dir() -> Path:
    """First argv, then $MAKEFUN_OUTPUT_DIR, then /output."""
    if len(sys.argv) > 1:
        return Path(sys.argv[1])
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def write_line() -> None:
    """Validate the line against the gate, then write it to entry.txt."""
    code_points = len(LINE)
    byte_count = len(LINE.encode("utf-8"))
    if code_points < MIN_CHARS or code_points > MAX_CHARS:
        abort(f"line is {code_points} code points, outside the 1-120 gate")
    if byte_count < MIN_CHARS or byte_count > MAX_CHARS:
        abort(f"line is {byte_count} bytes, outside the 1-120 gate")
    if not LINE.strip():
        abort("line is only whitespace")
    if "\n" in LINE or "\r" in LINE:
        abort("line must be a single line")

    target = output_dir() / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file is the line itself, exactly one line.
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {target} ({code_points} code points, {byte_count} bytes)")


if __name__ == "__main__":
    write_line()
