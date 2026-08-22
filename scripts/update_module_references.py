from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".py", ".json", ".toml", ".txt", ".yml", ".yaml", ".ini", ".sh"}


def module_name(match: re.Match[str]) -> str:
    return f"course_days.day{int(match.group(1)):03d}"


def module_path(match: re.Match[str]) -> str:
    return f"course_days/day{int(match.group(1)):03d}.py"


for path in ROOT.rglob("*"):
    if (
        not path.is_file()
        or ".git" in path.parts
        or path.suffix.lower() not in TEXT_SUFFIXES
    ):
        continue
    text = path.read_text(encoding="utf-8")
    updated = re.sub(r"course_days\.day(\d{1,2})\b", module_name, text)
    updated = re.sub(r"course_days/day(\d{1,2})\.py\b", module_path, updated)
    if updated != text:
        path.write_text(updated, encoding="utf-8")

print("Updated stale course_days module references to three-digit names.")
