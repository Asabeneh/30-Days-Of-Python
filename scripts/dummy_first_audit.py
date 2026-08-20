"""Measure the dummy-first teaching contract without pretending automation replaces review."""
# ruff: noqa: E501

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    "problem": ["## The problem"],
    "vocabulary": ["Vocabulary", "What does", "means"],
    "worked_examples": ["## Worked examples"],
    "trace": ["## Execution trace"],
    "mistakes": ["Common mistake", "Common mistakes"],
    "guided_practice": ["Guided practice", "guided practice"],
    "security_application": ["Security application"],
    "exercises": ["## Independent exercises", "## Exercises"],
    "finish_line": ["## Finish line"],
    "references": ["## References"],
}


def day_number(path: Path) -> int:
    return int(path.parent.name.split("_", 2)[1])


def has_requirement(text: str, alternatives: list[str]) -> bool:
    return any(item in text for item in alternatives)


def classify(text: str) -> str:
    words = len(text.split())
    examples = len(re.findall(r"^### Example ", text, flags=re.MULTILINE))
    code_blocks = len(re.findall(r"^```", text, flags=re.MULTILINE)) // 2
    present = sum(has_requirement(text, options) for options in REQUIRED.values())
    if (
        words >= 1500
        and examples >= 4
        and code_blocks >= 8
        and present == len(REQUIRED)
    ):
        return "teaching-ready"
    if words >= 1000 and examples >= 3 and present >= 7:
        return "needs-human-review"
    return "revision-note-risk"


def main() -> int:
    rows: list[tuple[int, str, int, int, int, int, str]] = []
    for path in sorted(ROOT.glob("day_*/*.md"), key=lambda item: day_number(item)):
        text = path.read_text(encoding="utf-8")
        words = len(text.split())
        code_blocks = len(re.findall(r"^```", text, flags=re.MULTILINE)) // 2
        examples = len(re.findall(r"^### Example ", text, flags=re.MULTILINE))
        present = sum(has_requirement(text, options) for options in REQUIRED.values())
        rows.append(
            (
                day_number(path),
                path.parent.name,
                words,
                code_blocks,
                examples,
                present,
                classify(text),
            )
        )

    ready = sum(row[-1] == "teaching-ready" for row in rows)
    review = sum(row[-1] == "needs-human-review" for row in rows)
    risk = sum(row[-1] == "revision-note-risk" for row in rows)
    lines = [
        "# Dummy-First Teaching Audit",
        "",
        "This report is deliberately stricter than a heading or word-count check. "
        "`teaching-ready` means the lesson has enough observable teaching structure "
        "to receive human review; it does not mean that automation has proved that "
        "the prose is good.",
        "",
        "| Status | Days |",
        "| --- | ---: |",
        f"| Teaching-ready candidate | {ready} |",
        f"| Needs human review | {review} |",
        f"| Revision-note risk | {risk} |",
        "",
        "| Day | Lesson | Words | Code blocks | Examples | Components | Status |",
        "| ---: | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row[0]} | `{row[1]}` | {row[2]} | {row[3]} | "
            f"{row[4]} | {row[5]}/{len(REQUIRED)} | {row[6]} |"
        )
    output = ROOT / "DUMMY_FIRST_AUDIT.md"
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"teaching-ready={ready} needs-review={review} revision-note-risk={risk}")
    print(f"Wrote {output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
