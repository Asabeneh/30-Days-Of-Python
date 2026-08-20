# Day 16: Regular Expressions and Careful Indicator Extraction

[← Day 15](../day_15_iterators_and_generators/day_15_iterators_and_generators.md) · [Day index](../DAY_INDEX.md) · [Day 17 →](../day_17_dates_and_timelines/day_17_dates_and_timelines.md)

## Table of Contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Lesson](#lesson)
- [Vocabulary](#vocabulary)
- [Worked examples](#worked-examples)
- [Execution trace](#execution-trace)
- [Common mistakes](#common-mistakes)
- [Security application](#security-application)
- [Exercises](#exercises)
- [Finish line](#finish-line)

## Why this lesson exists

Regular expressions are useful for finding candidate shapes in text, such as an IP-like token or an event ID. They are not complete validators and must never turn a match into an accusation.

## Prerequisites

Complete Days 1–15 and understand strings, generators, and bounded processing.

## Outcomes

By the end of this lesson, you can:

- write a small regex with named groups
- use `finditer` to preserve positions
- distinguish candidate extraction from validation
- avoid catastrophic patterns and excessive input
- retain raw context and confidence

## The problem

A synthetic log line contains several tokens. Extract candidates with their positions, then validate the candidate using ordinary Python logic. The report must preserve the original line number without storing unnecessary raw data.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples do not authorize access to public systems, university systems, employer systems, or accounts that you do not own.

## Lesson

### Vocabulary

A **pattern** describes text shape. A **match** is evidence that the shape occurred. A **capture group** returns part of a match. A **validator** applies domain rules that a pattern alone may not express.

## Worked examples

### Example 1: Find a simple field

A named group makes the captured value readable.

```python
import re

pattern = re.compile(r"user=(?P<user>[a-z0-9_-]+)")
match = pattern.search("user=alice status=ok")
print(match.group("user"))
```

**What to observe:**

`alice`

### Example 2: Find every candidate

`finditer` provides each match and its position.

```python
for match in re.finditer(r"id=(?P<id>\d+)", "id=12 id=99"):
    print(match.group("id"), match.start())
```

**What to observe:**

`12 0` and `99 6` with positions relative to the string.

### Example 3: Validate an IP-like candidate

A simple shape can be checked with numeric policy afterward.

```python
def valid_ipv4(text):
    parts = text.split(".")
    return len(parts) == 4 and all(
        part.isdigit() and 0 <= int(part) <= 255 for part in parts
    )
```

**What to observe:**

`203.0.113.8` is accepted; `999.1.1.1` is rejected.

### Example 4: Avoid a greedy match

A narrow character class prevents a pattern from swallowing unrelated text.

```python
pattern = re.compile(r"token=(?P<token>[^\s]+)")
print(pattern.search("token=abc next=value").group("token"))
```

**What to observe:**

`abc`; the match stops at whitespace.

### Example 5: Bound the input

A regex should not process an unbounded line supplied by an unknown source.

```python
line = line[:2000]
if len(line) == 2000:
    truncated = True
```

**What to observe:**

The report can say that matching occurred on a bounded preview.

## Execution trace

For `user=alice`, the pattern first locates the literal `user=`, captures allowed characters into `user`, and returns the group. For a candidate IP, extraction finds text first and validation checks four numeric octets afterward.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| pattern is a validator | malformed candidate is trusted | validate with domain logic |
| greedy `.*` | one match consumes too much | use narrow classes and test boundaries |
| no input bound | expensive matching on huge data | cap line length |
| losing positions | reviewer cannot locate evidence | store line and character positions |
| printing full sensitive line | data leaks into output | report a redacted excerpt or identifier |

## Security application

Extract candidate IP-like values only from the synthetic fixture. Preserve line number and character position, validate octets, and label the result `candidate` rather than `malicious`.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples above as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run `python -m course_days.day016`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A regex finds a shape; a validator adds domain rules; neither one proves intent, ownership, or compromise.

## Limitations

Regex syntax can become complex and expensive. Prefer small patterns, bounds, tests, and a standard library parser when a protocol already defines one.

[← Day 15](../day_15_iterators_and_generators/day_15_iterators_and_generators.md) · [Day index](../DAY_INDEX.md) · [Day 17 →](../day_17_dates_and_timelines/day_17_dates_and_timelines.md)
