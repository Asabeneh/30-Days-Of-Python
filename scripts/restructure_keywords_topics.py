# ruff: noqa: E501
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def section(text: str, heading: str) -> str:
    match = re.search(
        rf"^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )
    return match.group(1).strip() if match else ""


def add_topics_overview(text: str, overview: str, marker: str) -> str:
    if "## Topics" in text:
        return text
    return text.replace(marker, "## Topics\n\n" + overview + "\n\n" + marker, 1)


for path in sorted(ROOT.glob("day_*/*.md")):
    day = int(path.parent.name.split("_", 2)[1])
    text = path.read_text(encoding="utf-8")
    title_match = re.search(r"^# Day \d+: (.+)$", text, flags=re.MULTILINE)
    title = title_match.group(1) if title_match else f"Day {day}"

    if day <= 10:
        text = text.replace(
            "## Vocabulary in ordinary language",
            "## Keywords and terms in ordinary language",
            1,
        )
        text = text.replace("## Vocabulary", "## Keywords and terms", 1)
        if day in {2, 4}:
            marker_match = re.search(r"^## \d+\. ", text, flags=re.MULTILINE)
            marker = marker_match.group(0) if marker_match else "## Worked examples\n"
            if marker.startswith("## ") and marker.endswith(" "):
                marker = marker + ""
            if marker != "## Worked examples\n":
                line_start = text.find(marker)
                line_end = text.find("\n", line_start) + 1
                marker_text = text[line_start:line_end]
            else:
                marker_text = marker
            overview = f"This lesson teaches **{title}** as a sequence of topics. Read the topics in order: first understand the basic idea, then learn the syntax, then study variations and boundaries, and finally apply the idea to a bounded cybersecurity fixture."
            text = add_topics_overview(text, overview, marker_text)
        elif day == 1:
            overview = "This lesson moves through four topics: what a Python program is, how the interpreter runs it, how to read an error, and how to practise safely. Each topic introduces one idea before the next one depends on it."
            text = add_topics_overview(text, overview, "## Worked examples\n")
        else:
            text = text.replace("## Lesson", "## Topics", 1)
            if "## Topics" not in text:
                overview = f"This lesson teaches **{title}** through a sequence of small topics. Read each topic, run its example, predict one change, and then connect the idea to the bounded fixture."
                text = add_topics_overview(text, overview, "## Worked examples\n")
    else:
        if "## Keywords and terms" not in text:
            vocabulary = section(text, "Lesson")
            if vocabulary.startswith("### Vocabulary"):
                vocabulary = vocabulary.removeprefix("### Vocabulary").strip()
            why = section(text, "Why this lesson exists")
            problem = section(text, "The problem")
            replacement = (
                "## Keywords and terms\n\n"
                + vocabulary
                + "\n\n## Topics\n\n"
                + f"### What is {title}?\n\n"
                + (why or f"This lesson introduces {title} in small, testable steps.")
                + "\n\n"
                + f"### Why is {title} useful?\n\n"
                + (
                    problem
                    or "The topic gives a program a clearer way to solve a defined problem."
                )
                + "\n\n"
                + "### How will Python use this idea?\n\n"
                + "Read the worked examples next. For each one, identify the input, the operation, the result, and the boundary that prevents the example from doing more than the lesson allows."
                + "\n\n"
                + "### What are the security limits?\n\n"
                + "The examples remain local, synthetic, bounded, and authorized. A successful program run demonstrates behavior on the fixture; it does not prove authenticity, compromise, or permission to act on a real target."
                + "\n\n## Worked examples"
            )
            text = re.sub(
                r"^## Lesson\s*\n.*?(?=^## Worked examples\s*$)",
                replacement + "\n",
                text,
                flags=re.MULTILINE | re.DOTALL,
                count=1,
            )

    path.write_text(text, encoding="utf-8")

print(
    "Separated Keywords and terms from explicit Topics sections across the Python course."
)
