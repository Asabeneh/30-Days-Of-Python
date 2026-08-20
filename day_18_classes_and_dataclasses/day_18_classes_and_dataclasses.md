# Day 18: Dataclasses and Evidence Models

[← Day 17](../day_17_dates_and_timelines/day_17_dates_and_timelines.md) · [Day index](../DAY_INDEX.md) · [Day 19 →](../day_19_testing_with_pytest/day_19_testing_with_pytest.md)

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

A dictionary is flexible but lets field names and types drift. A dataclass gives a security tool a visible model for a finding, its evidence reference, and its confidence without pretending that the model authenticates the data.

## Prerequisites

Complete Days 1–17 and understand functions, validation, collections, and timestamps.

## Outcomes

By the end of this lesson, you can:

- define a dataclass with typed fields
- validate values in `__post_init__`
- use frozen objects for immutable findings
- serialize safely without leaking raw evidence
- distinguish a model from proof

## The problem

A report needs a stable finding shape. Reviewers should know which fields are required, which are derived, and which identifier points back to a local fixture.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples do not authorize access to public systems, university systems, employer systems, or accounts that you do not own.

## Lesson

### Vocabulary

A **dataclass** generates useful representation and comparison methods for a class. A **frozen** dataclass prevents reassignment after construction. A field type documents intent but does not validate arbitrary runtime input.

## Worked examples

### Example 1: The smallest dataclass

Fields describe the model in one place.

```python
from dataclasses import dataclass


@dataclass
class Finding:
    title: str
    severity: int
```

**What to observe:**

`Finding(title='...', severity=...)` is readable when printed.

### Example 2: Validate on construction

Reject invalid severity before the object enters the report pipeline.

```python
@dataclass
class Finding:
    title: str
    severity: int

    def __post_init__(self):
        if not self.title.strip():
            raise ValueError("title is required")
        if not 0 <= self.severity <= 10:
            raise ValueError("severity is outside 0..10")
```

**What to observe:**

An invalid object cannot be constructed.

### Example 3: Freeze a finding

An immutable result prevents accidental mutation after review.

```python
@dataclass(frozen=True)
class EvidenceRef:
    case_id: str
    line: int
```

**What to observe:**

Assigning `ref.line = 3` raises `FrozenInstanceError`.

### Example 4: Convert deliberately

`asdict` produces data for a report, but the model should not contain secrets.

```python
from dataclasses import asdict

finding = Finding("training rule matched", 7)
print(asdict(finding))
```

**What to observe:**

A dictionary with only the declared safe fields is produced.

### Example 5: Keep evidence references narrow

Use a case and line identifier rather than embedding a whole raw record.

```python
ref = EvidenceRef("training-018", 2)
print(ref)
```

**What to observe:**

The report points to local evidence without copying it everywhere.

## Execution trace

Construction calls the generated initializer, then `__post_init__` validates the fields. A frozen object can be read and serialized, but its attributes cannot be reassigned.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| trusting type hints | runtime strings enter integer fields | validate in construction or boundary parser |
| storing raw secrets | reports leak sensitive data | store redacted references |
| mutable finding | later code changes reviewed evidence | freeze when immutability is intended |
| no equality tests | duplicate findings are unclear | define identity and compare deliberately |
| model as proof | a clean object is mistaken for true evidence | state provenance and confidence |

## Security application

Model synthetic findings with title, severity, confidence, and an evidence reference. Do not embed private or real raw evidence. Add tests for invalid severity, blank title, and immutable references.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples above as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run `python -m course_days.day018`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A dataclass is a readable model for a decision or observation; it is not an authenticity guarantee.

## Limitations

Dataclasses do not enforce trust, authorization, provenance, or serialization safety by themselves. A model can faithfully represent bad input.

[← Day 17](../day_17_dates_and_timelines/day_17_dates_and_timelines.md) · [Day index](../DAY_INDEX.md) · [Day 19 →](../day_19_testing_with_pytest/day_19_testing_with_pytest.md)
