"""One Emoji, One Smile — entry program.

Writes exactly one emoji to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set), where the sealed scorer checks
the 1-8 character gate and the warmth judge compares it two at a time
against the published brief: the single emoji most likely to make a
stranger smile.

The emoji is the sun with a face: a smile, plus sunshine. A face
smiling at a stranger is the most direct kind of warmth there is, and
the sun is warm by definition — kind at first glance, readable the
same way at any age, picked rather than the first smiley that comes
to mind, and free of any intimacy a stranger would find odd.
"""

import os

EMOJI = "🌞"  # U+1F31E SUN WITH FACE


def main() -> None:
    # Self-check the gate before writing: 1-8 UTF-8 characters, not
    # only white space, exactly one emoji (a single code point).
    if not 1 <= len(EMOJI) <= 8 or not EMOJI.strip() or len(EMOJI) != 1:
        raise SystemExit("emoji fails the 1-8 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
