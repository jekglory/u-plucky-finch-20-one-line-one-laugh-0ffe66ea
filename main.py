"""One Line, One Laugh entry: a single original funny line.

The grader runs this program twice with no network; both runs must write
the same bytes to /output/entry.txt. The line is a fixed string, so the
output is deterministic by construction: no clock, no randomness, no I/O
other than the single write. The joke escalates a relatable failure: the
tool meant to remember passwords forgets its own, and the fix (a second
manager) only doubles the distrust.
"""

import os


LINE = (
    "My password manager forgot my master password, so I bought a second "
    "password manager to manage the first one \u2014 and now neither of them "
    "trusts me."
)

OUTPUT_PATH = "/output/entry.txt"

# The competition requires one line of at most 200 characters.
MAX_CHARS = 200


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "line must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text:
        raise SystemExit("line must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write with no trailing newline: the judge reads one line, and a
    # trailing newline would make the file two lines to a strict reader.
    data = text.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the line.
    with open(OUTPUT_PATH, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes do not match the line")
    print(text)


if __name__ == "__main__":
    main()
