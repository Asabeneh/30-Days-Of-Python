from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DAY_RE = re.compile(r"^day_(\d{2,3})_(.+)$")

current: list[tuple[int, Path, Path]] = []
for path in sorted(ROOT.glob("day_*")):
    if not path.is_dir():
        continue
    match = DAY_RE.match(path.name)
    if not match:
        continue
    number = int(match.group(1))
    target = ROOT / f"day_{number}_{match.group(2)}"
    current.append((number, path, target))

if len(current) != 120 or {number for number, _, _ in current} != set(range(1, 121)):
    raise SystemExit(
        f"Expected one padded lesson directory for each day 1-120; found {len(current)}"
    )

mapping: dict[str, str] = {}
for _, old, target in current:
    mapping[old.name] = target.name
    old_file = old / f"{old.name}.md"
    new_file = target / f"{target.name}.md"
    mapping[str(old_file.relative_to(ROOT))] = str(new_file.relative_to(ROOT))

# Move directories through unique temporary names so no target can collide.
temporary: list[tuple[Path, Path, Path]] = []
for number, old, target in current:
    temporary_path = ROOT / f".__rename_day_{number}_{old.name}"
    old.rename(temporary_path)
    temporary.append((temporary_path, target, old))

for temporary_path, target, old in temporary:
    temporary_path.rename(target)
    old_file = target / f"{old.name}.md"
    new_file = target / f"{target.name}.md"
    if not old_file.exists():
        raise SystemExit(f"Missing lesson file after directory rename: {old_file}")
    old_file.rename(new_file)

# Update text references everywhere in the repository, longest names first.
all_mapping = dict(sorted(mapping.items(), key=lambda item: len(item[0]), reverse=True))
text_suffixes = {".md", ".py", ".json", ".toml", ".txt", ".yml", ".yaml"}
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts or path.suffix not in text_suffixes:
        continue
    text = path.read_text(encoding="utf-8")
    updated = text
    for old, new in all_mapping.items():
        updated = updated.replace(old, new)
    updated = updated.replace("day_{day}_", "day_{day}_")
    updated = updated.replace("day_{number}_", "day_{number}_")
    if updated != text:
        path.write_text(updated, encoding="utf-8")

print(
    "Renamed all lesson directories and files to natural day_1 through day_120 names."
)
