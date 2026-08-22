from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

for directory in sorted(ROOT.glob("day_*")):
    match = re.fullmatch(r"day_(\d{3})_.+", directory.name)
    if not match:
        continue
    padded = match.group(1)
    natural = str(int(padded))
    for path in directory.rglob("*"):
        if not path.is_file() or not path.name.startswith(f"day_{natural}_"):
            continue
        target = path.with_name(
            path.name.replace(f"day_{natural}_", f"day_{padded}_", 1)
        )
        path.rename(target)

print("Repaired inner lesson filenames to zero-padded day prefixes.")
