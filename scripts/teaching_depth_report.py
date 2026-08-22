"""Measure learner-facing teaching completeness across all 120 lessons."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def lesson_file(directory: Path) -> Path:
    return directory / f"{directory.name}.md"


def status(text: str) -> str:
    required = [
        "## Execution trace",
        "## Common mistakes",
        "## Finish line",
    ]
    has_exercises = "## Exercises" in text or "## Independent exercises" in text
    has_sections = all(section in text for section in required) and has_exercises
    has_application = "## Worked examples" in text or "## Project requirements" in text
    examples = len(re.findall(r"^### (?:Example |[0-9]+\.)", text, flags=re.MULTILINE))
    words = len(text.split())
    if has_sections and has_application and examples >= 5 and words >= 700:
        return "dense"
    if has_sections and has_application and examples >= 3 and words >= 450:
        return "developing"
    return "outline"


def main() -> int:
    rows: list[tuple[int, str, int, int, int, str]] = []
    for directory in sorted(ROOT.glob("day_*")):
        number = int(directory.name.split("_", 2)[1])
        text = lesson_file(directory).read_text(encoding="utf-8")
        rows.append(
            (
                number,
                directory.name,
                len(text.split()),
                len(re.findall(r"^```", text, flags=re.MULTILINE)) // 2,
                len(re.findall(r"^### Example ", text, flags=re.MULTILINE)),
                status(text),
            )
        )
    dense = sum(row[-1] == "dense" for row in rows)
    developing = sum(row[-1] == "developing" for row in rows)
    outline = sum(row[-1] == "outline" for row in rows)
    lines = [
        "# Teaching Depth Report",
        "",
        "| Days | Dense | Developing | Outline |",
        "| ---: | ---: | ---: | ---: |",
        f"| 1–120 | {dense} | {developing} | {outline} |",
        "",
        (
            "The report is a measurement aid, not a substitute for human review. "
            "Dense means the page has the required teaching sections, at least "
            "five worked examples or topic demonstrations, and at least 700 words."
        ),
        "",
        "| Day | Lesson | Words | Code blocks | Examples | Status |",
        "| ---: | --- | ---: | ---: | ---: | --- |",
    ]
    for number, name, words, code_blocks, examples, lesson_status in rows:
        lines.append(
            f"| {number} | `{name}` | {words} | {code_blocks} | "
            f"{examples} | {lesson_status} |"
        )
    output = ROOT / "TEACHING_DEPTH_REPORT.md"
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {output.relative_to(ROOT)}")
    print(f"dense={dense} developing={developing} outline={outline}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
