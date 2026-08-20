# Day 83: Filesystem Timelines

[← Day 82](../day_82_evidence_integrity/day_82_evidence_integrity.md) · [Day index](../DAY_INDEX.md) · [Day 84 →](../day_84_sqlite_artifacts/day_84_sqlite_artifacts.md)

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

File metadata and content changes can help reconstruct a sequence. Timestamps are clues with clock, filesystem, and copying limitations—not an automatic story of who acted.

## Prerequisites

Complete Day 82. Use only the local fixtures and explicit loopback assessment scope supplied by the course.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using a tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Build a synthetic timeline from file events and identify gaps and ambiguous ordering.

## Security boundary

This lesson is educational and authorized-lab-only. It does not authorize public scanning, credential guessing, exploitation, interception, persistence, or changes to systems you do not own.

## Lesson

### Vocabulary

A filesystem timestamp is metadata about an operation or state. A timeline orders observations. Clock skew and copying can change interpretation.

## Worked examples

### Example 1: Represent events

A timeline entry needs item, time, and source.

```python
events = [{"path": "a.txt", "kind": "modified", "time": "10:00Z"}]
print(events)
```

**What to observe:**

The event is a bounded observation.

### Example 2: Sort parsed times

Use aware timestamps rather than text sorting.

```python
from datetime import datetime

events = ["2026-08-20T10:02:00+00:00", "2026-08-20T10:01:00+00:00"]
print(sorted(map(datetime.fromisoformat, events)))
```

**What to observe:**

The earlier instant comes first.

### Example 3: Record source

A copied file and an original need different provenance.

```python
events[0]["source"] = "synthetic-fixture"
print(events[0])
```

**What to observe:**

The source is attached.

### Example 4: Flag clock uncertainty

An event can be ordered while its exact meaning remains uncertain.

```python
print({"ordered": True, "clock_confidence": "low"})
```

**What to observe:**

The report avoids overconfidence.

### Example 5: Identify a gap

Missing events are part of the timeline conclusion.

```python
print({"gap": "10:03–10:10Z", "explanation": "not observed"})
```

**What to observe:**

The gap is explicit.

## Execution trace

The parser reads bounded metadata, converts timezones, sorts observations, attaches source and confidence, and reports missing windows rather than inventing actions.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| timestamp equals action | metadata is overinterpreted | say observed time only |
| text sort | offsets misorder events | parse aware time |
| copied file treated as original | provenance is lost | record source and transformations |
| no gaps | incomplete collection looks complete | report not observed |
| identify a person | file metadata is not identity proof | avoid attribution |

## Security application

Use only synthetic files and timestamps. Do not inspect a real home directory, university system, or workplace disk.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the requested evidence, expected behavior, edge case, and limitation.

## Finish line

Run `python -m course_days.day083`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A timeline orders observations and exposes gaps; it does not establish causation or identity.

## Limitations

Filesystem semantics vary across platforms, filesystems, clocks, and copy tools.

[← Day 82](../day_82_evidence_integrity/day_82_evidence_integrity.md) · [Day index](../DAY_INDEX.md) · [Day 84 →](../day_84_sqlite_artifacts/day_84_sqlite_artifacts.md)
