"""Famous Last Words — a one-line epitaph for the make.fun bounty.

The brief asks for the funniest possible famous last words, carved as a
single tombstone epitaph of at most 150 characters. Mine plays on the
modern habit of leaving everyone on read: the deceased's final act is
ghosting the group chat, and his last secret is a Wi-Fi password he
refuses to share even in death. The program below saves that line to
entry.txt so the judge can read it.
"""

import os

LIMIT = 150

ENTRY = (
    "Here lies a man who finally left the group chat on read. He took his "
    "Wi-Fi password to the grave — and his charger went with him."
)


def get_entry():
    return ENTRY.strip()


def write_entry():
    text = get_entry()
    assert 1 <= len(text) <= LIMIT, "epitaph must be 1-150 characters"
    assert "\n" not in text, "epitaph must be one line"
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8") as out:
        out.write(text)
    return target


def main():
    target = write_entry()
    print(f"wrote {target} ({len(get_entry())} chars)")


if __name__ == "__main__":
    main()
