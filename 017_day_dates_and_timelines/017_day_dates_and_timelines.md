# Day 17: Timestamps, Timezones, and Incident Timelines

[← Day 16](../016_day_regular_expressions/016_day_regular_expressions.md) · [Day index](../DAY_INDEX.md) · [Day 18 →](../018_day_classes_and_dataclasses/018_day_classes_and_dataclasses.md)

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

Security evidence is often ordered by time, but timestamps arrive in different formats and offsets. A timeline is only as reliable as its parsing, timezone policy, and provenance.

## Prerequisites

Complete Days 1–16 and be able to parse strings at a boundary.

## Outcomes

By the end of this lesson, you can:

- parse ISO timestamps
- require timezone-aware values
- compare events in a common timezone
- preserve the raw timestamp
- identify clock and ordering limitations

## The problem

Two synthetic records show `10:00+00:00` and `11:00+01:00`. They represent the same instant. A naive string sort can suggest the wrong order.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples do not authorize access to public systems, university systems, employer systems, or accounts that you do not own.

## Lesson

### Vocabulary

A **naive datetime** has no timezone. An **aware datetime** includes enough offset information to identify an instant. **Normalization** converts values into a common representation while **provenance** preserves how the value originally arrived.

## Worked examples

### Example 1: Parse UTC

The `Z` suffix means UTC when converted to `+00:00`.

```python
from datetime import datetime

value = datetime.fromisoformat("2026-08-20T10:00:00+00:00")
print(value.tzinfo is not None)
```

**What to observe:**

`True`

### Example 2: Reject a naive value

A timestamp without an offset cannot be safely compared across sources.

```python
value = datetime.fromisoformat("2026-08-20T10:00:00")
if value.tzinfo is None:
    raise ValueError("timestamp needs a timezone")
```

**What to observe:**

The explicit error prevents an ambiguous timeline.

### Example 3: Compare offsets

Aware datetimes compare instants, not only displayed clock text.

```python
first = datetime.fromisoformat("2026-08-20T10:00:00+00:00")
second = datetime.fromisoformat("2026-08-20T11:00:00+01:00")
print(first == second)
```

**What to observe:**

`True`

### Example 4: Normalize to UTC

A common display timezone makes a report easier to read.

```python
from datetime import timezone

print(second.astimezone(timezone.utc))
```

**What to observe:**

The result displays the same instant in UTC.

### Example 5: Keep provenance

Store the original string beside the parsed value.

```python
record = {"raw_timestamp": "2026-08-20T11:00:00+01:00", "parsed": second}
```

**What to observe:**

The reviewer can check the transformation.

## Execution trace

The two example timestamps compare equal because their offsets describe the same instant. If one value is naive, Python should reject it before sorting rather than inventing a timezone.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| sorting strings | offset events appear misordered | parse aware datetimes |
| assuming local time | results differ by machine | require or document timezone |
| dropping raw values | transformation cannot be audited | preserve provenance |
| treating order as causation | timeline overclaims | describe sequence and uncertainty |
| accepting future or impossible dates | fixture quality is hidden | document clock policy and test it |

## Security application

Build a synthetic timeline from fixture events, normalize to UTC, preserve raw timestamps, and report when two events have equal instants or when input lacks a timezone.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples above as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run `python -m course_days.day017`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A timeline is an ordered interpretation of timestamped observations, not a complete story of causation.

## Limitations

Clock skew, delayed collection, missing events, and forged timestamps can make a correct sort misleading. Production investigations need corroboration and chain-of-custody procedures.

[← Day 16](../016_day_regular_expressions/016_day_regular_expressions.md) · [Day index](../DAY_INDEX.md) · [Day 18 →](../018_day_classes_and_dataclasses/018_day_classes_and_dataclasses.md)
