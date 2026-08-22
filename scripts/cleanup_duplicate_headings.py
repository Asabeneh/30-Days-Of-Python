from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for path in sorted(ROOT.glob("day_*/*.md")):
    text = path.read_text(encoding="utf-8")
    updated = text.replace(
        "## Worked examples\n## Worked examples\n", "## Worked examples\n"
    )
    if updated != text:
        path.write_text(updated, encoding="utf-8")
print("Removed duplicate lesson headings.")
