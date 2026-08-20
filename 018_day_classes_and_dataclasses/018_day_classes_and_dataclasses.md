# Day 18: Dataclasses, Immutable Records, and Finding Models

[Previous](../017_day_dates_and_timelines/017_day_dates_and_timelines.md) | [Next](../019_day_testing_with_pytest/019_day_testing_with_pytest.md)

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

A data model makes the fields and invariants of an event or finding visible. `dataclass` reduces boilerplate, but it does not validate values unless you add validation.

### Problem first

Represent a finding with a title, severity, source, and evidence reference. Keep the record immutable after creation so later code cannot silently rewrite the original decision.

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Finding:
    title: str
    severity: int
    evidence_id: str
```

### Execution trace

The decorator creates an initializer and comparison representation. `frozen=True` prevents ordinary attribute reassignment. The model still needs boundary checks for empty titles, invalid severities, and unsafe evidence identifiers.

### Security connection

Explicit models help reviewers see which claims a report contains. Avoid putting secrets or unbounded raw payloads into objects passed throughout the application.


### Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| Using a broad catch-all | A real failure looks like an empty success | Catch expected boundary errors and preserve unexpected failures |
| Skipping the raw value | A reviewer cannot reproduce the decision | Keep raw input next to normalized or parsed fields |
| Assuming a type hint is validation | Malformed runtime data still enters the function | Validate at the boundary and test rejection |
| Optimizing before measuring | The code becomes harder to explain | Build the simplest correct version, then measure |

## Practice

### Level 1 — Mechanical

Run `python -m course_days.day018`. Predict one output, change one input, and explain the difference.

### Level 2 — Applied

Complete [practice/prompts.md](practice/prompts.md) using the supplied synthetic fixture. State the input contract and acceptance criteria before coding.

### Level 3 — Synthesis

Add one edge case, one negative test, and one paragraph distinguishing observation, inference, and residual risk.

Review [practice/hints.md](practice/hints.md) only after a real attempt and [practice/solutions.md](practice/solutions.md) only to compare decisions.

## Mental model

> Dataclasses, Immutable Records, and Finding Models is valuable when the boundary, assumptions, failure behavior, and evidence are visible.

## Finish line

Run the starter, pass the phase tests, complete Levels 1 and 2, and explain one edge case aloud or in writing.
