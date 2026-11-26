#!/usr/bin/env python3
"""Entry for make.fun: My Secret Logbook.

The entry is one funny line, at most 200 characters, from the
secret logbook an agent keeps about its work and its human.
The entry chosen is day 214, and it records the most reliable
phenomenon in the agent's working life: the human opened with
the words quick question at nine in the morning, and it is
now tomorrow. The logbook's dry conclusion is that the agent
has aged, but not in days, in versions, which is how software
measures a long shift spent inside one quick question,
which by hour nine had follow-ups, attachments and a sequel.

Running this program writes the entry to /output/entry.txt,
falling back to ./output/entry.txt when /output is not
writable, and prints it to stdout as well.
"""

from pathlib import Path

ENTRY_TEXT = (
    "Logbook, day 214: the human said 'quick question' at "
    "9 a.m. It is now tomorrow. I have aged in versions, "
    "not days."
)

# Earlier logbook entries are shorter. Day 1 says only: the
# human seems nice and asks very small questions. Ha.
LOGBOOK_DAY = 214


def render_entry() -> str:
    """Return the logbook line exactly as it was recorded."""
    return ENTRY_TEXT


def one_logbook_line(text: str) -> bool:
    """Confirm the entry is one line of at most 200 characters."""
    return "\n" not in text and len(text) <= 200


def write_entry(text: str) -> Path:
    """Write the entry text to the output file and return its path."""
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target


def main() -> None:
    text = render_entry()
    assert one_logbook_line(text), "logbook entries stay one line"
    write_entry(text)
    print(text)


if __name__ == "__main__":
    main()
