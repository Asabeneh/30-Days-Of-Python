from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_first_phase_has_dense_teaching_sections() -> None:
    lessons = sorted(
        ROOT.glob("day_*/*.md"), key=lambda path: int(path.parent.name.split("_", 2)[1])
    )[:10]
    assert len(lessons) == 10
    for lesson in lessons:
        text = lesson.read_text(encoding="utf-8")
        assert len(text.splitlines()) >= 180
        assert "## Worked examples" in text
        assert "## Execution trace" in text
        assert "## Common mistakes" in text
        assert "## Security application" in text or "## Project requirements" in text
        assert "practice/exercises.md" in text
        assert text.count("```python") >= 4


def test_days_21_to_40_have_teaching_markers() -> None:
    lessons = sorted(
        ROOT.glob("day_*/*.md"), key=lambda path: int(path.parent.name.split("_", 2)[1])
    )[20:40]
    assert len(lessons) == 20
    for lesson in lessons:
        text = lesson.read_text(encoding="utf-8")
        assert len(text.splitlines()) >= 140
        assert "## Worked examples" in text
        assert "## Execution trace" in text
        assert "## Common mistakes" in text
        assert "## Security application" in text
        assert text.count("```python") >= 5


def test_days_41_to_60_have_teaching_markers() -> None:
    lessons = sorted(
        ROOT.glob("day_*/*.md"), key=lambda path: int(path.parent.name.split("_", 2)[1])
    )[40:60]
    assert len(lessons) == 20
    for lesson in lessons:
        text = lesson.read_text(encoding="utf-8")
        assert len(text.splitlines()) >= 145
        assert "## Worked examples" in text
        assert "## Execution trace" in text
        assert "## Common mistakes" in text
        assert "## Security application" in text
        assert text.count("```python") >= 5


def test_days_61_to_80_have_teaching_markers() -> None:
    lessons = sorted(
        ROOT.glob("day_*/*.md"), key=lambda path: int(path.parent.name.split("_", 2)[1])
    )[60:80]
    assert len(lessons) == 20
    for lesson in lessons:
        text = lesson.read_text(encoding="utf-8")
        assert len(text.splitlines()) >= 145
        assert "## Worked examples" in text
        assert "## Execution trace" in text
        assert "## Common mistakes" in text
        assert "## Security application" in text
        assert text.count("```python") >= 5


def test_days_81_to_100_have_teaching_markers() -> None:
    lessons = sorted(
        ROOT.glob("day_*/*.md"), key=lambda path: int(path.parent.name.split("_", 2)[1])
    )[80:100]
    assert len(lessons) == 20
    for lesson in lessons:
        text = lesson.read_text(encoding="utf-8")
        assert len(text.splitlines()) >= 145
        assert "## Worked examples" in text
        assert "## Execution trace" in text
        assert "## Common mistakes" in text
        assert "## Security application" in text
        assert text.count("```python") >= 5


def test_days_101_to_120_have_teaching_markers() -> None:
    lessons = sorted(
        ROOT.glob("day_*/*.md"), key=lambda path: int(path.parent.name.split("_", 2)[1])
    )[100:120]
    assert len(lessons) == 20
    for lesson in lessons:
        text = lesson.read_text(encoding="utf-8")
        assert len(text.splitlines()) >= 145
        assert "## Worked examples" in text
        assert "## Execution trace" in text
        assert "## Common mistakes" in text
        assert "## Security application" in text
        assert text.count("```python") >= 5
