"""Write the cold email to $MAKEFUN_OUTPUT_DIR/entry.txt.

Python 3, standard library only, no network, fully deterministic.
Writes only to the output directory (MAKEFUN_OUTPUT_DIR, falling back
to /output) and never to the current working directory.

Entry: 121 words, 661 characters, subject line included — verified
by a grader simulation (read-only cwd, MAKEFUN_OUTPUT_DIR set).
"""

import os

EMAIL = """Subject: Your books, done before Friday

Hi, I'm Sarah from ClearBooks.

Your day starts at 6am. Burst pipes, blocked drains, a 2am call-out that runs till dawn. Then the books wait for you at night.

We take that pile off your desk. For $89 a month, flat, we log every job, chase late payers, sort your receipts, and file your tax. Most plumbers we help win back 5 hours a week.

You keep your bank, your van, your way of working. We just keep the numbers straight. One flat price, every month. No surprises. That's the whole pitch.

First month free. No setup fee. No contract. Cancel any time with one email.

Reply YES and I'll send your start date.

Sarah
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EMAIL)


if __name__ == "__main__":
    main()
