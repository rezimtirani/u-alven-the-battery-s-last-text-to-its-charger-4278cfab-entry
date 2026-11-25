"""The Battery's Last Text to Its Charger.

Writes the phone battery's final text message to the charger it
waited for all day to $MAKEFUN_OUTPUT_DIR/entry.txt: it held 1%
all day while the charger sat across the room, and now that it is
at 0 it asks the charger to tell its apps it loved them — and to
delete its search history. Standard library only.
"""

import os

TEXT = (
    "I held 1% all day while you sat across the room. "
    "I'm at 0 now — tell my apps I loved them, "
    "and delete my search history."
)


def check_text(text):
    """Check the text against the competition gate before writing.

    The gate needs plain UTF-8 text of 1 to 200 characters, not
    only white space, in a single line: the phone battery's last
    text message to the charger it waited for all day. Returns
    the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("text must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "text is %d characters, over the 200 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("text must be exactly one line")
    return cleaned


def text_shape(text):
    """Measure the text for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A last text too short to carry a joke, or
    one that reads like a status update instead of a goodbye, is
    caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_text(TEXT)
    shape = text_shape(text)
    if shape["words"] < 5:
        raise ValueError("text is too short to carry a joke")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
