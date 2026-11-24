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


def main() -> None:
    path = Path("/output/entry.txt")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
