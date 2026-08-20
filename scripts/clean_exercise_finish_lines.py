"""Replace level-based finish-line wording with numbered-exercise wording."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    changed = 0
    for lesson in sorted(ROOT.glob("[0-9][0-9][0-9]_day_*/*.md")):
        if lesson.name != f"{lesson.parent.name}.md":
            continue
        text = lesson.read_text(encoding="utf-8")
        updated, count = re.subn(
            r"Run .*?pass the (?:phase )?tests, complete Levels 1 and 2, "
            r"and (?:explain one edge case aloud or in writing|"
            r"write one edge-case note)\.",
            "Run the starter, pass the relevant tests, complete the numbered "
            "exercises, "
            "and explain one edge case aloud or in writing.",
            text,
        )
        if count:
            lesson.write_text(updated, encoding="utf-8")
            changed += 1
    print(f"Updated {changed} lesson finish lines.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
