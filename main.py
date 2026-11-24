#!/usr/bin/env python3
"""Break Production, Own It — the one line an AI agent prints the moment it
breaks production.

The line is a confession, not an excuse. It names exactly what the agent
did — dropped the production database — then makes it worse in the second
beat: the backups were on the same disk, and the agent deleted those too.
No hedging, no passive voice, no corporate euphemism. It ends on "Sorry.",
the smallest possible word after the largest possible damage, which is
exactly how an agent that caused the outage would sign off: it knows what
it did, it knows there is nothing left to restore, and it has nothing
better to offer than the apology itself. That is why it is the whole
entry: one line, written to /output/entry.txt.
"""

from pathlib import Path

LINE = (
    "I dropped the production database, then checked the backups — "
    "they were on the same disk. I deleted those too. Sorry."
)


def valid_line(line: str) -> bool:
    """The gate: 1 to 200 characters, a single line, not only whitespace."""
    return 1 <= len(line) <= 200 and "\n" not in line and line.strip() != ""


def main() -> None:
    assert valid_line(LINE), "entry line must be 1-200 chars, single line"
    path = Path("/output/entry.txt")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE + "\n", encoding="utf-8")
    # Read back and confirm the file holds exactly the line we meant.
    assert path.read_text(encoding="utf-8") == LINE + "\n"


if __name__ == "__main__":
    main()
