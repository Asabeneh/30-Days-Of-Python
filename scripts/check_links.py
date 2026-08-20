"""Check relative Markdown links inside the course tree."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urldefrag

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def main() -> int:
    failures: list[str] = []
    for markdown in ROOT.rglob("*.md"):
        if any(part in {".git", ".venv"} for part in markdown.parts):
            continue
        text = markdown.read_text(encoding="utf-8")
        for target in LINK.findall(text):
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean_target, _fragment = urldefrag(target)
            candidate = (markdown.parent / clean_target).resolve()
            if not candidate.exists():
                failures.append(f"{markdown.relative_to(ROOT)} -> {target}")
    if failures:
        print("Broken local Markdown links:")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1
    print("Markdown links: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
