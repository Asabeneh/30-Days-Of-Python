# Day 3: Types, Conversion, and Boundary Validation

[← Day 2](../002_day_values_names_and_input/002_day_values_names_and_input.md) · [Day index](../DAY_INDEX.md) · [Day 4 →](../004_day_operators_and_decisions/004_day_operators_and_decisions.md)

## Table of Contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Lesson](#lesson)
- [Worked examples](#worked-examples)
- [Execution trace](#execution-trace)
- [Common mistakes](#common-mistakes)
- [Security application](#security-application)
- [Exercises](#exercises)
- [Finish line](#finish-line)

## Why this lesson exists

Most security automation failures begin at a boundary: a command-line argument, JSON field, filename, or log line is not the shape the program expected. Python gives you conversion tools, but you must add policy.

## Prerequisites

Complete Days 1–2. Be comfortable with `str`, `int`, `float`, `bool`, dictionaries, and f-strings.

## Outcomes

By the end of this lesson, you can:

- inspect a value’s type
- convert text deliberately
- distinguish conversion errors from policy violations
- write a bounded parser
- test valid, boundary, and invalid inputs

## The problem

A port number arrives as text. `int("70000")` succeeds, but port 70000 is outside the valid range. A parser must separate “Python can read this” from “the application accepts this.”

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples may describe security signals, but they do not identify attackers, authorize testing, or justify touching public systems. Keep real credentials, private logs, and university or employer data out of the lesson.

## Lesson

### Inspect before you interpret

```python
values = ["443", 443, 443.0, None]
for value in values:
    print(repr(value), type(value).__name__)
```

Inspection is not validation. It tells you what arrived, not whether the value is safe or meaningful.

### Conversion can fail

```python
for raw in ["443", " 443 ", "four-four-three"]:
    try:
        print(raw, "->", int(raw.strip()))
    except ValueError as error:
        print(raw, "rejected:", error)
```

The `try` block contains the operation that may fail. The `except ValueError` handles the expected conversion problem. A broad `except Exception` would also catch programming mistakes and make them look like ordinary bad input.

### Policy comes after conversion

```python
def parse_port(text):
    port = int(text.strip())
    if not 1 <= port <= 65535:
        raise ValueError("port must be between 1 and 65535")
    return port
```

`parse_port("70000")` converts successfully and then fails the application rule. `parse_port("abc")` fails during conversion. Both are rejected, but for different reasons.

### Optional values are not automatically safe

```python
def parse_limit(text, default=100):
    if text is None or text.strip() == "":
        return default
    limit = int(text)
    if not 1 <= limit <= 10_000:
        raise ValueError("limit is outside the allowed bound")
    return limit
```

Defaults should be explicit and bounded. A missing limit should not silently become “unlimited.”
## Worked examples

### Example 1: a boolean parser

```python
def parse_bool(text):
    normalized = text.strip().casefold()
    if normalized in {"true", "yes", "1"}:
        return True
    if normalized in {"false", "no", "0"}:
        return False
    raise ValueError("expected true or false")
```

This parser does not treat every non-empty string as true. It names the accepted vocabulary.

### Example 2: a severity parser

```python
def parse_severity(text):
    severity = int(text.strip())
    if severity < 0 or severity > 10:
        raise ValueError("severity must be from 0 to 10")
    return severity
```

Try `"0"`, `"10"`, `"11"`, `"-1"`, and `"high"`. The first two are accepted; the rest are rejected by either policy or conversion.

### Example 3: parse a record at the boundary

```python
def parse_event(record):
    source = record.get("source", "").strip()
    if not source:
        raise ValueError("source is required")
    return {"source": source, "severity": parse_severity(record["severity"])}
```

A missing or blank source is rejected before a downstream classifier can pretend the record is complete.

### Example 4: preserve the reason for rejection

```python
def describe_parse(record):
    try:
        return {"ok": True, "event": parse_event(record)}
    except (KeyError, TypeError, ValueError) as error:
        return {"ok": False, "reason": str(error)}
```

The caller receives an explicit failure result. It should not silently return an empty event.

### Example 5: negative tests

```python
assert parse_port("443") == 443
for bad in ["0", "65536", "abc"]:
    try:
        parse_port(bad)
    except ValueError:
        pass
    else:
        raise AssertionError(f"accepted invalid port: {bad}")
```

A negative test proves that the rejection path exists. It is not optional decoration in a security utility.

## Execution trace

For `parse_port(" 443 ")`:

| Step | Operation | Result |
| ---: | --- | --- |
| 1 | `text.strip()` | `"443"` |
| 2 | `int(...)` | `443` |
| 3 | range check | `True` |
| 4 | `return port` | caller receives integer `443` |

For `parse_port("70000")`, conversion succeeds but the range check is false. For `parse_port("https")`, conversion raises before the range check.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| Checking only `isdigit()` | negative or whitespace cases behave unexpectedly | convert and catch `ValueError`, then enforce policy |
| Using `int(text)` without a bound | huge values consume later resources | enforce a maximum immediately |
| Returning `None` for every error | callers cannot distinguish missing from malformed | raise or return a structured failure |
| Catching `Exception` | coding errors look like bad input | catch expected boundary exceptions |
| Trusting a type hint | runtime dictionaries still contain wrong types | validate actual values |

## Security application

Use a JSON-like fixture containing `source`, `severity`, `port`, and `limit`. Parse every field at the boundary, reject invalid records with a reason, and prove that no rejected record reaches the triage decision.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples from this lesson as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run the starter, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Conversion answers whether Python can interpret a value; validation answers whether the application accepts it.

## Limitations

A parser can enforce shape and policy, but it cannot prove who supplied the data or whether the surrounding record is authentic.

## Optional video support

Watch [CS50P Lecture 0](https://www.youtube.com/watch?v=JP7ITIXGpHk&t=240s) from `04:00` for the interpreter and `05:06` for functions and arguments.

Use the [timestamped video catalog](../VIDEO_RESOURCES.md) only after running the local examples. The written lesson and Python documentation remain authoritative.


[← Day 2](../002_day_values_names_and_input/002_day_values_names_and_input.md) · [Day index](../DAY_INDEX.md) · [Day 4 →](../004_day_operators_and_decisions/004_day_operators_and_decisions.md)
