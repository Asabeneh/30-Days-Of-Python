"""Replace residual level-based exercise prose with a direct numbered-exercise route."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    changed = 0
    for lesson in sorted(ROOT.glob("[0-9][0-9][0-9]_day_*/*.md")):
        if lesson.name != f"{lesson.parent.name}.md":
            continue
        text = lesson.read_text(encoding="utf-8")
        replacement = (
            "## Exercises\n\n"
            "Complete the numbered questions in "
            "[practice/exercises.md](practice/exercises.md) in order. "
            "Run the requested commands, produce the requested artifact, "
            "and record the edge case or limitation asked for by the exercise. "
            "Use [hints](practice/hints.md) only after a real attempt and "
            "[solutions](practice/solutions.md) only to compare your reasoning.\n\n"
        )
        updated, count = re.subn(
            r"## Exercises\n.*?(?=## Mental model|## Finish line)",
            replacement,
            text,
            count=1,
            flags=re.DOTALL,
        )
        if count and updated != text:
            lesson.write_text(updated, encoding="utf-8")
            changed += 1
    print(f"Cleaned exercise sections in {changed} lesson pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
