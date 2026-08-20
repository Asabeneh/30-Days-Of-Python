# ruff: noqa: E501
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def slugify(heading: str) -> str:
    heading = re.sub(r"[`*_]", "", heading.lower())
    heading = re.sub(r"[^a-z0-9\s-]", "", heading)
    return re.sub(r"\s+", "-", heading.strip())


def build_toc(text: str) -> str:
    entries: list[tuple[int, str, str]] = []
    for line in text.splitlines():
        match = re.match(r"^(##|###) (.+?)\s*$", line)
        if not match:
            continue
        heading = match.group(2)
        if heading.casefold() in {"table of contents", "on this page"}:
            continue
        level = 0 if match.group(1) == "##" else 1
        entries.append((level, heading, slugify(heading)))
    lines = ["## Table of contents", ""]
    for level, heading, anchor in entries:
        indent = "  " * level
        lines.append(f"{indent}- [{heading}](#{anchor})")
    return "\n".join(lines) + "\n"


for path in sorted(ROOT.glob("day_*/*.md")):
    text = path.read_text(encoding="utf-8")
    text = re.sub(
        r"\n## Table of contents\n.*?(?=\n## |\Z)|\n## Table of Contents\n.*?(?=\n## |\Z)",
        "\n",
        text,
        flags=re.DOTALL,
    )
    lines = text.splitlines(keepends=True)
    insert_at = next(
        (index for index, line in enumerate(lines) if line.startswith("## ")),
        len(lines),
    )
    toc = build_toc(text)
    lines.insert(insert_at, toc + "\n")
    path.write_text("".join(lines), encoding="utf-8")

print("Added a persistent table of contents to all 120 lesson files.")
