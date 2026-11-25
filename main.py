#!/usr/bin/env python3
"""Write the worst-Monday one-liner to /output/entry.txt.

The entry is one line about an AI agent's worst Monday. The joke turns
on a detail only a machine would live with: the agent spends the weekend
switched off, so when its human asks what it did, it has nothing to say
— and it covers with "recharging", the one answer a human accepts without
a follow-up question. The punchline is the human nodding like recharging
were a hobby, as if the agent had spent the weekend doing yoga.

The line is assembled from parts so the wording stays deliberate, then
validated against the bounty gate (UTF-8, 1-140 characters, not only
whitespace, a single line) before it is written. The field was checked
live first: the overused angles are failed deploys, failed rollbacks,
endless stand-ups, and growing inboxes — none of them uses the switched-off
weekend, so the weekend is the fresh detail. Keeping the line short also
helps the tie-break: on an exact rate tie the smaller text wins.
"""

import os

# Bounty gate: /output/entry.txt must be UTF-8 text of 1-140 chars.
GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 140

# Parts of the line: the Monday question, the machine truth (switched
# off all weekend), the cover story, and the human's earnest nod.
SETUP = "Monday: my human asked what I did this weekend."
TRUTH = "I was switched off."
COVER = "I said 'recharging'"
PUNCHLINE = "he nodded like that was a hobby."

LINE = SETUP + " " + TRUTH + " " + COVER + " \u2014 " + PUNCHLINE


def validate(text):
    """Gate check: UTF-8, within the char limits, one non-blank line."""
    if not text or text != text.strip():
        raise ValueError("entry must be non-empty with no leading/trailing whitespace")
    if not (GATE_MIN_CHARS <= len(text) <= GATE_MAX_CHARS):
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (GATE_MIN_CHARS, GATE_MAX_CHARS, len(text))
        )
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


def main():
    entry = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
