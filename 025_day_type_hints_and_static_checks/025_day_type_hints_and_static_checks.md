# Day 25: Type Hints and Static Checks

[← Day 24](../024_day_json__csv__and_sqlite/024_day_json__csv__and_sqlite.md) · [Day index](../DAY_INDEX.md) · [Day 26 →](../026_day_structured_logging/026_day_structured_logging.md)

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

Type hints make a function’s intended data flow visible to humans and tools. They improve review, but they do not validate runtime JSON, CSV, or CLI input.

## Prerequisites

Complete Day 24 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 25

## The problem

A reviewer needs to see which functions accept raw text, which accept validated events, and which return reports or errors.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Lesson

### Vocabulary

A **type annotation** describes intended types. A **static checker** analyzes code without running it. A `TypedDict` describes dictionary keys but does not enforce them at runtime.

## Worked examples

### Example 1: Annotate a function

Annotations document the contract at the call site.

```python
def label(severity: int) -> str:
    return "high" if severity >= 7 else "normal"
```

**What to observe:**

Readers can see the input and output relationship.

### Example 2: Use a TypedDict

A typed dictionary documents required fields.

```python
from typing import TypedDict


class Event(TypedDict):
    source: str
    severity: int
```

**What to observe:**

The checker can reason about `event['source']`.

### Example 3: Optional values

`None` must be handled before using a value as text.

```python
def source_name(source: str | None) -> str:
    return source or "unknown"
```

**What to observe:**

Missing source becomes an explicit display value.

### Example 4: Protocols by behavior

A protocol can describe the method a dependency must provide.

```python
from typing import Protocol


class Reader(Protocol):
    def read(self, limit: int) -> list[str]: ...
```

**What to observe:**

Tests can provide a small fake reader.

### Example 5: Runtime validation still matters

A dictionary from JSON can violate the annotation.

```python
raw: Event = {
    "source": "auth",
    "severity": "7",
}  # type checker warning; runtime may still create it
```

**What to observe:**

The annotation does not convert the string or reject it.

## Execution trace

Static analysis reads the declared contract, but external data crosses into Python at runtime. Validate first, then construct the typed internal record.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| type hints as validation | malformed input still runs | validate at runtime |
| `Any` everywhere | checker provides no signal | narrow types at boundaries |
| ignore every error | real design gaps disappear | explain justified ignores |
| wrong `Optional` handling | `None` reaches string methods | branch or validate |
| annotations without tests | type shape is right but behavior wrong | keep behavioral tests |

## Security application

Run the checker on local course modules and add runtime tests for malformed synthetic data. Do not paste real data into a static-analysis service.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run every requested command, create the requested artifact, and record the limitation the exercise asks you to name.

## Finish line

Run `python -m course_days.day025`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Type hints are a review map; runtime validation is the gate that external data must pass.

## Limitations

Static checks cannot prove correctness, security, authorization, or package safety. They are one layer of evidence.

[← Day 24](../024_day_json__csv__and_sqlite/024_day_json__csv__and_sqlite.md) · [Day index](../DAY_INDEX.md) · [Day 26 →](../026_day_structured_logging/026_day_structured_logging.md)
