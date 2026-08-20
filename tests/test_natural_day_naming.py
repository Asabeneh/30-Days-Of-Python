from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def lesson_directories() -> list[Path]:
    return sorted(
        ROOT.glob("day_*"),
        key=lambda path: int(path.name.split("_", 2)[1]),
    )


def test_lessons_use_natural_day_names() -> None:
    directories = lesson_directories()
    assert len(directories) == 120
    assert [int(path.name.split("_", 2)[1]) for path in directories] == list(
        range(1, 121)
    )
    assert not list(ROOT.glob("day_0[0-9]_*"))
    for directory in directories:
        lesson = directory / f"{directory.name}.md"
        assert lesson.exists()


def test_day_index_is_numeric_and_complete() -> None:
    text = (ROOT / "DAY_INDEX.md").read_text(encoding="utf-8")
    days = [
        int(number)
        for number in re.findall(r"^- \[Day (\d+):", text, flags=re.MULTILINE)
    ]
    assert days == list(range(1, 121))


def test_course_modules_use_natural_names() -> None:
    modules = sorted(
        ROOT.glob("course_days/day*.py"),
        key=lambda path: int(path.stem.removeprefix("day")),
    )
    assert modules
    assert not list(ROOT.glob("course_days/day0*.py"))
