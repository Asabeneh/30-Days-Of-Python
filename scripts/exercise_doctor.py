"""Validate the question-driven exercise contract."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NUMBERED = re.compile(r"^\d+\.\s+", re.MULTILINE)


def main() -> int:
    errors: list[str] = []
    lessons = sorted(ROOT.glob("[0-9][0-9][0-9]_day_*"))
    for directory in lessons:
        lesson = directory / f"{directory.name}.md"
        exercise = directory / "practice" / "exercises.md"
        hints = directory / "practice" / "hints.md"
        solutions = directory / "practice" / "solutions.md"
        if not exercise.exists():
            errors.append(f"missing exercises: {exercise.relative_to(ROOT)}")
            continue
        text = exercise.read_text(encoding="utf-8")
        question_count = len(NUMBERED.findall(text))
        if question_count < 4:
            errors.append(
                f"fewer than four numbered exercises: {exercise.relative_to(ROOT)}"
            )
        if not hints.exists() or not solutions.exists():
            errors.append(f"missing hint or solution companion: {directory.name}")
        lesson_text = lesson.read_text(encoding="utf-8")
        if "practice/exercises.md" not in lesson_text:
            errors.append(
                f"lesson does not link exercises.md: {lesson.relative_to(ROOT)}"
            )
        if "practice/prompts.md" in lesson_text:
            errors.append(f"legacy prompts link remains: {lesson.relative_to(ROOT)}")
    legacy = list(ROOT.rglob("prompts.md"))
    if legacy:
        errors.extend(
            f"legacy prompt file remains: {path.relative_to(ROOT)}" for path in legacy
        )
    if errors:
        print("Exercise doctor found:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Exercise doctor: OK ({len(lessons)} numbered exercise files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
