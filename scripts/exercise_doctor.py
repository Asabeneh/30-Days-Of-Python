"""Validate the question-driven exercise contract."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NUMBERED = re.compile(r"^\d+\.\s+", re.MULTILINE)


def main() -> int:
    errors: list[str] = []
    lessons = sorted(ROOT.glob("day_*"))
    for directory in lessons:
        lesson = directory / f"{directory.name}.md"
        lesson_text = lesson.read_text(encoding="utf-8")
        exercise_heading = re.search(r"^## (Independent exercises|Exercises)\s*$", lesson_text, re.MULTILINE)
        if not exercise_heading:
            errors.append(f"missing canonical exercise section: {lesson.relative_to(ROOT)}")
            continue
        exercise_tail = lesson_text[exercise_heading.end() :]
        next_heading = re.search(r"^## ", exercise_tail, re.MULTILINE)
        exercise_text = exercise_tail[: next_heading.start() if next_heading else len(exercise_tail)]
        question_count = len(NUMBERED.findall(exercise_text))
        if question_count < 12:
            errors.append(f"fewer than twelve numbered exercises in lesson: {lesson.relative_to(ROOT)}")
        if len(exercise_text.split()) < 120:
            errors.append(f"lesson exercise section is too short: {lesson.relative_to(ROOT)}")
        hints = directory / "practice" / "hints.md"
        solutions = directory / "practice" / "solutions.md"
        legacy_exercise = directory / "practice" / "exercises.md"
        if legacy_exercise.exists():
            errors.append(f"redundant exercise companion remains: {legacy_exercise.relative_to(ROOT)}")
        for companion in (hints, solutions):
            if not companion.exists():
                errors.append(f"missing companion: {companion.relative_to(ROOT)}")
                continue
            companion_text = companion.read_text(encoding="utf-8")
            if len(companion_text.split()) < 150:
                errors.append(f"companion file is too short: {companion.relative_to(ROOT)}")
            if len(NUMBERED.findall(companion_text)) < 12:
                errors.append(f"companion needs twelve numbered entries: {companion.relative_to(ROOT)}")
            if "Use the exercise numbers in order." in companion_text:
                errors.append(f"generic placeholder companion remains: {companion.relative_to(ROOT)}")
        for link in ("../README.md", "../SETUP.md", "../VS_CODE_SETUP.md", "../DAY_INDEX.md", "practice/hints.md", "practice/solutions.md"):
            if link not in lesson_text:
                errors.append(f"lesson missing navigation or practice link {link}: {lesson.relative_to(ROOT)}")
        if "practice/exercises.md" in lesson_text or "practice/prompts.md" in lesson_text:
            errors.append(f"legacy exercise or prompts link remains: {lesson.relative_to(ROOT)}")
    legacy = list(ROOT.rglob("prompts.md"))
    if legacy:
        errors.extend(
            f"legacy prompt file remains: {path.relative_to(ROOT)}" for path in legacy
        )
    if errors:
        print("Exercise doctor found:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Exercise doctor: OK ({len(lessons)} lessons with substantive practice routes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
