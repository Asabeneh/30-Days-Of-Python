from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
module_files = sorted(ROOT.glob("course_days/day[0-9][0-9][0-9].py"))
if not module_files:
    raise SystemExit("No padded course_days modules found")

mapping: dict[str, str] = {}
for old in module_files:
    number = int(old.stem[3:])
    new_name = f"day{number}.py"
    mapping[old.name] = new_name

for old in module_files:
    temporary = old.with_name(f".__{old.name}")
    old.rename(temporary)
for old_name, new_name in mapping.items():
    temporary = ROOT / "course_days" / f".__{old_name}"
    temporary.rename(ROOT / "course_days" / new_name)

patterns = [
    (
        re.compile(r"course_days\.day(\d{3})"),
        lambda match: f"course_days.day{int(match.group(1))}",
    ),
    (
        re.compile(r"course_days/day(\d{3})\.py"),
        lambda match: f"course_days/day{int(match.group(1))}.py",
    ),
    (re.compile(r"day(\d{3})\.py"), lambda match: f"day{int(match.group(1))}.py"),
]
text_suffixes = {".md", ".py", ".txt", ".toml", ".json", ".yaml", ".yml"}
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts or path.suffix not in text_suffixes:
        continue
    text = path.read_text(encoding="utf-8")
    updated = text
    for pattern, replacement in patterns:
        updated = pattern.sub(replacement, updated)
    updated = updated.replace("day{lesson.day}", "day{lesson.day}")
    updated = updated.replace("day{spec.day}", "day{spec.day}")
    if updated != text:
        path.write_text(updated, encoding="utf-8")

print("Renamed internal course_days modules to natural day1-style names.")
