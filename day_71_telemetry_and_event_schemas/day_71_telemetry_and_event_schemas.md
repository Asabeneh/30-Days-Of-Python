# Day 71: Telemetry and Event Schemas

[← Day 70](../day_70_project__secure_case_api/day_70_project__secure_case_api.md) · [Day index](../DAY_INDEX.md) · [Day 72 →](../day_72_log_normalization/day_72_log_normalization.md)

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

Detection depends on events that different systems represent differently. A schema gives analysts stable fields while preserving source, time, and uncertainty.

## Prerequisites

Complete Day 70. Use only the local course fixtures, loopback services, and synthetic records described by the lesson.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using the tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state the trust boundary and residual risk
- complete the numbered cybersecurity exercises

## The problem

Define a normalized event schema for synthetic authentication activity and reject records that cannot support the required fields.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, interception, exploit delivery, real-user profiling, or changes to systems you do not own.

## Lesson

### Vocabulary

Telemetry is collected operational data. A schema defines fields and types. Normalization maps source-specific fields into common fields. Provenance identifies the source.

## Worked examples

### Example 1: Define an event

Start with fields needed for a decision.

```python
event = {
    "event_type": "auth_failure",
    "source": "training-auth",
    "actor": "student",
    "observed_at": "now",
}
print(event)
```

**What to observe:**

The event has stable names.

### Example 2: Map source fields

Normalization makes source differences explicit.

```python
source_record = {"user": "student", "action": "login_failed"}
normalized = {"actor": source_record["user"], "event_type": "auth_failure"}
print(normalized)
```

**What to observe:**

The mapping is visible.

### Example 3: Validate time

A detection without time cannot be placed in a sequence.

```python
if not event.get("observed_at"):
    raise ValueError("timestamp required")
```

**What to observe:**

The event is rejected when time is missing.

### Example 4: Preserve source

Normalized data must retain where it came from.

```python
normalized["provenance"] = {"source": "training-auth", "raw_id": "fixture-1"}
print(normalized)
```

**What to observe:**

The mapping is auditable.

### Example 5: Version a schema

Fields evolve; a version tells readers how to interpret them.

```python
normalized["schema_version"] = 1
print(normalized["schema_version"])
```

**What to observe:**

The version is explicit.

## Execution trace

The source record is mapped, required fields are checked, raw provenance is retained, and the versioned normalized event enters detection logic.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| drop source | analyst cannot trace mapping | preserve provenance |
| no schema version | fields drift silently | version and document |
| missing time accepted | sequence rules fail | reject or mark unknown |
| normalize away raw | audit loses context | retain safe references |
| event equals truth | collection errors become facts | record confidence |

## Security application

Use synthetic authentication events and local JSON fixtures only. Do not ingest real user telemetry.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples as a starting point, then record the requested output, edge case, and limitation.

## Finish line

Run `python -m course_days.day071`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A schema creates stable analytical fields without erasing source or uncertainty.

## Limitations

A normalized event can still be incomplete, delayed, duplicated, or wrong.

[← Day 70](../day_70_project__secure_case_api/day_70_project__secure_case_api.md) · [Day index](../DAY_INDEX.md) · [Day 72 →](../day_72_log_normalization/day_72_log_normalization.md)
