from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def slugify(heading: str) -> str:
    heading = re.sub(r"[`*_]", "", heading.lower())
    heading = re.sub(r"[^a-z0-9\s-]", "", heading)
    return re.sub(r"\s+", "-", heading.strip())


def test_every_lesson_has_one_persistent_toc() -> None:
    lessons = sorted(ROOT.glob("day_*/*.md"))
    assert len(lessons) == 120
    for lesson in lessons:
        text = lesson.read_text(encoding="utf-8")
        assert text.lower().count("## table of contents") == 1
        toc_start = text.lower().index("## table of contents")
        first_section = text.find("\n## ", toc_start + 1)
        assert first_section > toc_start
        toc = text[toc_start:first_section]
        assert "[References](#references)" in toc
        assert "[Finish line](#finish-line)" in toc


def test_toc_anchors_point_to_headings() -> None:
    for lesson in sorted(ROOT.glob("day_*/*.md")):
        text = lesson.read_text(encoding="utf-8")
        headings = {
            slugify(match.group(2))
            for match in re.finditer(r"^(##|###) (.+?)\s*$", text, re.MULTILINE)
            if match.group(2).casefold() != "table of contents"
        }
        toc_start = text.lower().index("## table of contents")
        first_section = text.find("\n## ", toc_start + 1)
        toc = text[toc_start:first_section]
        anchors = re.findall(r"\]\(#([^)]+)\)", toc)
        assert anchors
        assert set(anchors).issubset(headings)
