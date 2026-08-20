# Day 17: Dates, Time Zones, and Defensible Timelines

[Previous](../016_day_regular_expressions/016_day_regular_expressions.md) | [Next](../018_day_classes_and_dataclasses/018_day_classes_and_dataclasses.md)

## Table of Contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Core lesson](#core-lesson)
- [Common mistakes](#common-mistakes)
- [Practice](#practice)
- [Mental model](#mental-model)
- [Finish line](#finish-line)

## Why this lesson exists

Python becomes useful in cybersecurity when its behavior is predictable, testable, and explainable. This day introduces a professional engineering idea through a small local problem before asking you to combine it with other tools.

## Prerequisites

You should be able to run the previous day, write a small function, and use the setup in [SETUP.md](../SETUP.md). If a term is unfamiliar, return to the previous lesson rather than copying a later pattern.

## Outcomes

By the end, you can explain the core concept, trace the starter, predict a changed result, write a normal and negative test, and state what the exercise does not prove about a real system.

## The problem

Security data is untrusted, incomplete, and easy to misinterpret. The problem today is to make one transformation or decision explicit enough that another learner can run it, test it, and review its assumptions.

## Security boundary

Use only the synthetic fixtures supplied by the course or a local file you created. Do not substitute public targets, university systems, employer systems, real credentials, or private evidence. Read `lab/scope.md` before changing the exercise.

## Core lesson

Incident timelines fail when timestamps are compared as unstructured strings or silently interpreted in a local timezone. Use timezone-aware datetimes and retain the original text.

### Problem first

Parse ISO-8601 timestamps from synthetic events and sort them consistently in UTC.

```python
from datetime import datetime, timezone


def parse_timestamp(text: str) -> datetime:
    value = datetime.fromisoformat(text.replace("Z", "+00:00"))
    if value.tzinfo is None:
        raise ValueError("timestamp must include a timezone")
    return value.astimezone(timezone.utc)
```

### Execution trace

The `Z` suffix is translated to an explicit UTC offset. A timezone-aware value is converted to UTC, allowing events from different offsets to be ordered. The original timestamp should remain in the evidence record.

### Security connection

A sorted list is not automatically a true story. Clock drift, missing events, collection delays, and source reliability belong in the report's limitations.


### Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| Using a broad catch-all | A real failure looks like an empty success | Catch expected boundary errors and preserve unexpected failures |
| Skipping the raw value | A reviewer cannot reproduce the decision | Keep raw input next to normalized or parsed fields |
| Assuming a type hint is validation | Malformed runtime data still enters the function | Validate at the boundary and test rejection |
| Optimizing before measuring | The code becomes harder to explain | Build the simplest correct version, then measure |

## Practice

### Level 1 — Mechanical

Run `python -m course_days.day017`. Predict one output, change one input, and explain the difference.

### Level 2 — Applied

Complete [practice/prompts.md](practice/prompts.md) using the supplied synthetic fixture. State the input contract and acceptance criteria before coding.

### Level 3 — Synthesis

Add one edge case, one negative test, and one paragraph distinguishing observation, inference, and residual risk.

Review [practice/hints.md](practice/hints.md) only after a real attempt and [practice/solutions.md](practice/solutions.md) only to compare decisions.

## Mental model

> Dates, Time Zones, and Defensible Timelines is valuable when the boundary, assumptions, failure behavior, and evidence are visible.

## Finish line

Run the starter, pass the phase tests, complete Levels 1 and 2, and explain one edge case aloud or in writing.
