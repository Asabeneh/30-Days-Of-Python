# ruff: noqa: E501
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXPANSIONS = {
    3: """## 1. Read a value's type before choosing an operation

Start with five values that look different when Python displays them:

```python
samples = ["7", 7, 7.0, True, None]
for sample in samples:
    print(repr(sample), type(sample).__name__)
```

Expected output:

```text
'7' str
7 int
7.0 float
True bool
None NoneType
```

The quotation marks around `"7"` make it text. The absence of quotation marks around `7` makes it an integer. `None` is a special value meaning that a value is deliberately absent. It is not the same as the text `"None"`.

Before you call a function such as `int`, `float`, or `str`, ask what meaning the result should have. `int("7")` creates the number seven. `str(7)` creates text containing the character seven. Conversion changes the type but does not prove that the input is honest or allowed.

## 2. Convert first, validate second

Conversion answers “Can Python interpret these characters as this type?” Validation answers “Is the resulting value allowed by this program?” Keep the questions separate:

```python
raw = "99"
severity = int(raw)
print(severity)
print(0 <= severity <= 10)
```

Output:

```text
99
False
```

The conversion succeeded. The policy check failed. If `raw` were `"high"`, conversion itself would fail with `ValueError`. These are different problems and should receive different explanations.

A safe boundary function can make the policy visible:

```python
def parse_severity(raw):
    cleaned = raw.strip()
    value = int(cleaned)
    if not 0 <= value <= 10:
        raise ValueError("severity must be between 0 and 10")
    return value
```

Do not catch an error merely to make the program look successful. Decide whether the caller should reject the record, ask again, or label the value unknown.

## 3. Boolean conversion is not language understanding

This surprising example is worth running:

```python
print(bool("false"))
print(bool(""))
print(bool(0))
print(bool(1))
```

Output:

```text
True
False
False
True
```

`bool` asks whether a value is truthy. It does not translate English words. The non-empty string `"false"` is truthy. If a program receives words, define the accepted words explicitly:

```python
def parse_yes_no(raw):
    word = raw.strip().casefold()
    if word in {"yes", "true", "1"}:
        return True
    if word in {"no", "false", "0"}:
        return False
    raise ValueError("expected an accepted yes/no value")
```

An allowlist is easier to review than a guess. It also gives malformed input a clear outcome.

## 4. Missing, malformed, and out-of-range are different

Use a small table to reason about inputs:

| Input | Conversion | Policy result |
| --- | --- | --- |
| `""` | empty text | missing or rejected, by policy |
| `"high"` | conversion fails | malformed |
| `"99"` | produces integer 99 | out of range |
| `"7"` | produces integer 7 | accepted for a 0–10 rule |

Write a prediction for each before testing. In a security tool, these distinctions help a reviewer understand whether the source was incomplete, incorrectly formatted, or simply outside the documented range. None of the categories proves malicious intent.
""",
    5: """## 1. An `if` statement asks one question

The smallest decision has one condition and one indented body:

```python
severity = 8
if severity >= 7:
    print("review")
```

Output:

```text
review
```

The colon ends the condition. The indentation shows which statement belongs to the `if`. If the condition is false, Python skips the indented statement. Indentation is part of Python's syntax, not decoration.

## 2. Add an alternative with `else`

```python
severity = 4
if severity >= 7:
    label = "review"
else:
    label = "routine"
print(label)
```

Output: `routine`. Exactly one of the two blocks runs. The `else` is not another test; it is the fallback when the `if` condition is false.

## 3. Use `elif` for several ranges

```python
severity = 9
if severity >= 9:
    label = "urgent"
elif severity >= 7:
    label = "review"
else:
    label = "routine"
print(label)
```

Output: `urgent`. Python checks from top to bottom and stops at the first true branch. Put the most specific or highest-priority rule first. If `severity >= 7` came first, a severity of 9 would never reach the urgent branch.

## 4. Separate the questions before combining them

Long conditions are easier to debug when you name their parts:

```python
severity = 8
source = "training-auth"
source_is_present = source != ""
severity_is_high = severity >= 7
needs_review = severity_is_high and source_is_present
print(severity_is_high)
print(source_is_present)
print(needs_review)
```

If the final result surprises you, print the smaller Boolean values. This is a beginner-friendly debugging technique and a useful security-review habit.

## 5. Truthiness needs a policy

Python treats several values as false in a condition, including `0`, `""`, empty collections, and `None`. That can be convenient, but “empty” and “zero” may have different meanings in a security record. Use an explicit comparison when the difference matters:

```python
attempts = 0
if attempts == 0:
    print("no attempts recorded")
```

This says exactly what the program means.
""",
    6: """## 1. A `for` loop repeats a known sequence

A loop repeats work. Start with a short list:

```python
events = ["login_failed", "logout", "access_denied"]
for event in events:
    print(event)
```

Python takes the first item, stores it under `event`, runs the indented body, then repeats for the next item. The loop ends when the sequence has no more items.

## 2. `range` creates a predictable counting sequence

```python
for record_number in range(1, 4):
    print(record_number)
```

Output:

```text
1
2
3
```

The stop value `4` is not included. This “stop before” rule is common and worth testing with a tiny range before using a larger one.

## 3. A `while` loop needs a changing condition

```python
attempt = 1
while attempt <= 3:
    print(attempt)
    attempt += 1
```

The update `attempt += 1` is what allows the loop to finish. If you remove it, the condition remains true forever. Never test an unknown loop against a real large input until you have proved that the loop has a limit.

## 4. Bounds protect time and memory

A bound is a maximum amount of permitted work:

```python
items = ["a", "b", "c", "d"]
limit = 3
processed = 0
for item in items:
    if processed >= limit:
        break
    print(item)
    processed += 1
print(f"processed={processed}")
```

Output:

```text
a
b
c
processed=3
```

The loop did not claim that the fourth item was safe or unsafe. It stopped because the exercise allowed only three records. In security automation, a bounded result should say whether processing was complete.

## 5. `break` and `continue` change the path

`break` ends the loop. `continue` skips the rest of the current iteration and moves to the next item. Use both only when the reason is clear. A hidden `continue` can accidentally skip evidence; a hidden `break` can make a report incomplete.
""",
    7: """## 1. Lists preserve order and duplicates

```python
events = ["login_failed", "logout", "login_failed"]
print(events[0])
print(len(events))
```

Output:

```text
login_failed
3
```

The first item has index 0. The duplicate is meaningful: the event was observed twice. Use a list when order and repeated observations matter.

## 2. Sets answer membership questions

```python
known_events = {"login_failed", "access_denied", "login_failed"}
print(len(known_events))
print("logout" in known_events)
```

Output:

```text
2
False
```

The set removes duplicates. It is useful for asking whether a value has appeared or belongs to an allowlist. It cannot preserve the original sequence or prove that an event is malicious.

## 3. Dictionaries label fields

```python
record = {
    "event": "login_failed",
    "severity": 7,
    "source": "training-auth",
}
print(record["event"])
print(record.get("confidence"))
```

Output:

```text
login_failed
None
```

Square brackets require the key to exist. `.get` returns `None` when the optional key is absent. Decide deliberately whether a missing required key should be rejected instead.

## 4. Tuples group fixed values

```python
endpoint = ("127.0.0.1", 8000)
host, port = endpoint
print(host)
print(port)
```

A tuple can communicate that the two values belong together. The loopback address and port are local training values, not an instruction to connect to a remote service.

## 5. Mutation is a visible change

```python
items = ["a", "b"]
items.append("c")
print(items)
```

The list changes from two items to three. When two names refer to the same mutable list, one function can change what another function sees. Later lessons will use copying and contracts to make ownership clearer.
""",
    8: """## 1. Strings are sequences of characters

```python
text = "Login-Failed"
print(len(text))
print(text[0])
print(text[-1])
```

Output:

```text
12
L
d
```

Indexing starts at zero. A string is not a security verdict; it is text that needs a documented interpretation.

## 2. Use methods for deliberate transformations

```python
raw = "  Login-Failed  "
cleaned = raw.strip()
comparison_value = cleaned.casefold()
print(repr(raw))
print(repr(comparison_value))
```

Output:

```text
'  Login-Failed  '
'login-failed'
```

Keep the raw value when provenance matters. Create a normalized comparison value for matching. Do not overwrite the original automatically when an investigation may need to show what was received.

## 3. Slicing selects a portion

```python
value = "training-001"
print(value[:8])
print(value[9:])
```

A slice creates a new string. Learn the start-inclusive, stop-exclusive rule with small examples. Never use slicing as a secret-redaction strategy unless you have proved the entire value format and the required protection.

## 4. Split and join have contracts

```python
line = "severity=7 source=training-auth"
parts = line.split()
print(parts)
print("|".join(parts))
```

Output:

```text
['severity=7', 'source=training-auth']
severity=7|source=training-auth
```

Splitting is not validation. A malformed line may have too few parts, repeated keys, or unexpected separators. Check the result before using it.

## 5. Canonicalization can change meaning

Lowercasing an event label may be appropriate for a case-insensitive comparison. It may be wrong for a password, signature, encoded value, or evidence field where every character matters. Record which field was normalized and why.
""",
    9: """## 1. A function packages one job

```python
def add_one(value):
    return value + 1

answer = add_one(4)
print(answer)
```

`def` starts a function definition. `value` is a parameter name. `return` sends a value back to the caller. `add_one(4)` calls the function with the argument `4`.

## 2. Parameters make a rule reusable

```python
def is_high_severity(severity):
    return severity >= 7

print(is_high_severity(6))
print(is_high_severity(7))
```

Output:

```text
False
True
```

The function does not print a verdict about a real incident. It returns a Boolean about the value supplied by the caller.

## 3. Validate at the boundary

```python
def parse_severity(text):
    cleaned = text.strip()
    value = int(cleaned)
    if not 0 <= value <= 10:
        raise ValueError("severity must be between 0 and 10")
    return value
```

The contract is visible: text enters, an integer from 0 through 10 leaves, and malformed or out-of-range input raises an error. A function contract is not authorization; it is only a promise about program behavior.

## 4. Return values instead of hiding decisions in prints

```python
def make_finding(label, reason):
    return {"label": label, "reason": reason}

finding = make_finding("review", "synthetic high severity")
print(finding["label"])
```

Returning structured data makes a function easier to test. Printing inside every helper makes composition and testing harder.

## 5. Scope determines where a name exists

```python
label = "outside"

def show_label():
    label = "inside"
    print(label)

show_label()
print(label)
```

Output:

```text
inside
outside
```

The function's local `label` is different from the outer `label`. Prefer passing values as parameters and returning results instead of depending on hidden global state.
""",
    10: """## 1. A pipeline is a sequence of small stages

A log-triage program becomes easier to explain when it has separate stages:

| Stage | Question |
| --- | --- |
| Read | Which local fixture is permitted? |
| Parse | Can the text become fields? |
| Convert | Can the severity become an integer? |
| Validate | Is the value inside the allowed range? |
| Classify | Which documented label applies? |
| Report | What happened, and was processing complete? |

Do not hide all six questions inside one giant function. A beginner can test one stage at a time, and a reviewer can identify where a failure occurred.

## 2. Parse a simple key-value line

```python
line = "severity=8 source=training-auth event=login_failed"
fields = {}
for part in line.split():
    key, value = part.split("=", 1)
    fields[key] = value
print(fields)
```

Output:

```text
{'severity': '8', 'source': 'training-auth', 'event': 'login_failed'}
```

Notice that severity is still text. Parsing fields and converting values are separate tasks. The `1` in `split("=", 1)` prevents a later equals sign from being split into too many pieces.

## 3. Classify without making accusations

```python
def classify(severity_text, source, known_events, event):
    try:
        severity = int(severity_text)
    except ValueError:
        return "invalid"
    if not 0 <= severity <= 10:
        return "out-of-range"
    if source == "":
        return "missing-source"
    if event not in known_events:
        return "unknown-event"
    if severity >= 7:
        return "review"
    return "routine"
```

The labels describe what the local rule found. They do not identify an attacker or prove compromise.

## 4. Count outcomes explicitly

```python
counts = {"review": 0, "routine": 0, "invalid": 0}
label = "review"
counts[label] += 1
print(counts)
```

Initialize every expected category so zero values remain visible. A report that omits `invalid=0` can be harder to compare with another run.

## 5. Report completeness

A finite limit is not the same as complete processing. If the fixture contains more records than the permitted limit, say so:

```python
limit = 2
processed = 0
complete = True
for line in ["a", "b", "c"]:
    if processed >= limit:
        complete = False
        break
    processed += 1
print(processed, complete)
```

Output:

```text
2 False
```

The safe report tells the reader what the program actually processed.
""",
}

for day, addition in EXPANSIONS.items():
    matches = list(ROOT.glob(f"day_{day:02d}_*/*.md"))
    if len(matches) != 1:
        raise SystemExit(f"Expected one lesson for Day {day}, found {matches}")
    path = matches[0]
    text = path.read_text(encoding="utf-8")
    marker = "## Worked examples\n"
    if marker not in text:
        raise SystemExit(f"Missing worked-example heading: {path}")
    if addition.splitlines()[0] not in text:
        text = text.replace(marker, addition + "\n" + marker, 1)
        path.write_text(text, encoding="utf-8")
print("Added topic-by-topic beginner explanations to Days 3 and 5–10.")
