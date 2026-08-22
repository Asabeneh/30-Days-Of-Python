# ruff: noqa: E501
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def explain(line: str) -> str:
    stripped = line.strip()
    if not stripped:
        return "Blank line: it separates ideas for the human reader."
    if stripped.startswith("#"):
        return "Comment: Python ignores this text while running the program."
    if stripped.startswith("def "):
        return "Function definition: Python records a reusable block with this name."
    if stripped.startswith("return "):
        return "Return statement: the function sends this value back to its caller."
    if stripped.startswith("if ") or stripped.startswith("elif "):
        return "Condition: Python evaluates this question and chooses whether the block runs."
    if stripped == "else:":
        return "Fallback branch: this block runs when earlier conditions were false."
    if stripped.startswith("raise "):
        return (
            "Explicit failure: the program refuses an input that violates the contract."
        )
    if stripped.startswith("for ") or stripped.startswith("while "):
        return "Loop header: Python prepares to repeat the indented block."
    if stripped.startswith("import ") or stripped.startswith("from "):
        return "Import statement: the program asks for code from a module."
    if "print(" in stripped:
        return "Output call: Python evaluates the argument and writes a representation to the terminal."
    if "(" in stripped and ")" in stripped and "=" not in stripped:
        return "Function call: Python evaluates the arguments and runs the named operation."
    if (
        "=" in stripped
        and "==" not in stripped
        and ">=" not in stripped
        and "<=" not in stripped
        and "!=" not in stripped
    ):
        return "Assignment: Python evaluates the right side and stores the result under the name on the left."
    return "Expression or data declaration: read the names, values, and operators and predict the result."


def quote_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


for path in sorted(ROOT.glob("day_*/*.md")):
    day = int(path.parent.name.split("_", 2)[1])
    if day < 11:
        continue
    text = path.read_text(encoding="utf-8")
    if "## Read the first example line by line" in text:
        continue
    match = re.search(r"```python\n(.*?)\n```", text, flags=re.DOTALL)
    if not match:
        raise SystemExit(f"No Python example found: {path}")
    code = match.group(1).splitlines()
    code = code[:16]
    title_match = re.search(r"^# Day \d+: (.+)$", text, flags=re.MULTILINE)
    title = title_match.group(1) if title_match else "today's topic"
    rows = [
        "## Read the first example line by line",
        "",
        f"The first runnable example introduces **{title}**. Copy it into a new file and run it before changing anything. Then use this table to read the same code slowly. A line-by-line explanation does not replace practice: it shows you what to look for when a program behaves differently from your prediction.",
        "",
        "| Line | Code | What Python is doing |",
        "| ---: | --- | --- |",
    ]
    for number, line in enumerate(code, 1):
        rows.append(
            f"| {number} | `{quote_cell(line.strip())}` | {quote_cell(explain(line))} |"
        )
    rows.extend(
        [
            "",
            "After the run, write down the value created by each assignment, the condition tested by each branch, and the output that appeared. Change one input only. If the result changes, identify the line that used that input. If the result does not change, explain why the input was not part of the decision. This is the same tracing habit used later when reviewing security automation.",
            "",
        ]
    )
    addition = "\n".join(rows)
    marker = "## Execution trace\n"
    if marker not in text:
        raise SystemExit(f"Missing execution trace heading: {path}")
    text = text.replace(marker, addition + marker, 1)
    path.write_text(text, encoding="utf-8")
print("Added line-by-line guides to Days 11–120.")
