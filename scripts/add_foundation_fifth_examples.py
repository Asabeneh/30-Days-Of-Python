# ruff: noqa: E501
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = {
    2: """### Example 5: Name, value, and type can disagree with your assumption

```python
severity = \"7\"
print(repr(severity), type(severity).__name__)
severity = int(severity)
print(repr(severity), type(severity).__name__)
```

The first output describes text. The second describes an integer. The name stayed the same, but the value and type changed. A name does not guarantee what it contains; inspect and validate at the boundary.
""",
    3: """### Example 5: A valid conversion can still fail policy

```python
raw = \"99\"
value = int(raw)
print(value)
print(0 <= value <= 10)
```

Conversion succeeds, but the range check is false. Keep conversion errors and policy errors separate so the final report explains what happened.
""",
    5: """### Example 5: The order of branches changes the result

```python
severity = 9
if severity >= 7:
    label = \"review\"
elif severity >= 9:
    label = \"urgent\"
print(label)
```

This prints `review`, because Python stops at the first true branch. Put the urgent test first when urgent is meant to be a more specific category.
""",
    6: """### Example 5: A limit changes completeness, not truth

```python
items = [\"a\", \"b\", \"c\"]
limit = 2
processed = items[:limit]
print(processed)
print(len(processed) == len(items))
```

The program processed two items and reports that processing was not complete. A bounded result should never be described as a complete inspection when the limit stopped the work.
""",
    7: """### Example 5: Keep observation order and uniqueness separately

```python
observed = [\"login_failed\", \"logout\", \"login_failed\"]
unique = set(observed)
print(len(observed))
print(len(unique))
```

The list preserves three observations and the set contains two unique values. Security reports often need both facts: frequency and uniqueness answer different questions.
""",
    8: """### Example 5: Preserve raw text beside a comparison value

```python
raw = \" Login-Failed \"
comparison = raw.strip().casefold()
print(repr(raw))
print(comparison == \"login-failed\")
```

The raw string preserves what the fixture contained. The comparison value supports a deliberate match. Do not overwrite evidence merely because a normalized form is convenient.
""",
    9: """### Example 5: A function can reject an unsafe boundary

```python
def bounded_limit(value):
    if not 1 <= value <= 100:
        raise ValueError(\"limit must be from 1 through 100\")
    return value

print(bounded_limit(10))
```

The successful call returns `10`. A call with `0` or `101` raises the documented error. The contract makes the resource boundary visible to every caller.
""",
    10: """### Example 5: Invalid input remains visible in the summary

```python
results = [\"review\", \"routine\", \"invalid\"]
counts = {\"review\": 0, \"routine\": 0, \"invalid\": 0}
for result in results:
    counts[result] += 1
print(counts)
```

The summary keeps `invalid` separate from `routine`. A malformed record should not silently become a reassuring result.
""",
}

for day, addition in EXAMPLES.items():
    path = next(ROOT.glob(f"day_{day}_*/*.md"))
    text = path.read_text(encoding="utf-8")
    if "### Example 5:" not in text:
        marker = "## Execution trace\n"
        if marker not in text:
            raise SystemExit(f"Missing execution trace heading: {path}")
        text = text.replace(marker, addition + "\n" + marker, 1)
        path.write_text(text, encoding="utf-8")
print("Added explicit fifth worked examples to foundation lessons.")
