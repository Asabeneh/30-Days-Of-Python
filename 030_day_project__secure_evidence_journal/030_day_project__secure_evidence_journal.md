# Day 30: Project: Secure Evidence Journal

[← Day 29](../029_day_threat_modeling/029_day_threat_modeling.md) · [Day index](../DAY_INDEX.md) · [Day 31 →](../031_day_processes_and_system_calls/031_day_processes_and_system_calls.md)

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

A project makes the engineering habits visible in one artifact. The Secure Evidence Journal stores synthetic observations, preserves provenance, redacts sensitive fields, and records confidence without pretending to be a case-management system.

## Prerequisites

Complete Day 29 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 30

## The problem

Build a local JSON Lines journal that accepts synthetic entries, validates them, assigns an identifier, and exports a safe report.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Lesson

### Vocabulary

A **journal entry** is one immutable observation. **Provenance** says where and when it came from. **Confidence** describes the strength of an interpretation, not the guilt of a person.

## Worked examples

### Example 1: Define a record

Start with fields that make an observation reviewable.

```python
entry = {
    "case_id": "training-030",
    "source": "fixture-a",
    "observed_at": "2026-08-20T10:00:00+00:00",
    "note": "login_failed",
}
```

**What to observe:**

The entry contains synthetic provenance and a neutral note.

### Example 2: Validate required fields

Missing source or timezone makes later review weaker.

```python
required = {"case_id", "source", "observed_at", "note"}
missing = required - entry.keys()
print(missing)
```

**What to observe:**

An empty set means the required keys exist.

### Example 3: Redact before export

A report should contain only the fields it needs.

```python
safe = {key: entry[key] for key in ["case_id", "source", "observed_at"]}
print(safe)
```

**What to observe:**

The note is omitted from this summary view.

### Example 4: Write JSON Lines

One JSON object per line is easy to append and process incrementally.

```python
import json

line = json.dumps(entry, sort_keys=True)
print(line)
```

**What to observe:**

The record has a stable text representation.

### Example 5: State limitations

A journal records observations; it does not establish truth.

```python
limitations = ["synthetic only", "no identity proof", "no chain of custody"]
print("; ".join(limitations))
```

**What to observe:**

The report communicates scope honestly.

## Execution trace

The project pipeline is validate → preserve raw safe fields → derive an identifier → append JSON Lines → export a redacted report → test and reset. Every step should be inspectable.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| edit raw evidence | provenance is lost | append corrections as new entries |
| store secrets | journal becomes sensitive | redact and minimize |
| claim confidence is truth | interpretation becomes accusation | describe confidence and basis |
| no reset | fixtures accumulate | document cleanup |
| no schema version | future readers guess | include a version field |

## Security application

The journal uses only local synthetic entries, a dedicated output path, and a reset command. The README must include setup, schema, threat model, sample report, limitations, and tests.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run every requested command, create the requested artifact, and record the limitation the exercise asks you to name.

## Finish line

Run `python -m course_days.day030`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> An evidence journal preserves what was observed and how it was transformed; it does not manufacture certainty.

## Limitations

This project is not a forensic evidence system, legal record, or production case-management platform. Real evidence requires policy, access control, retention, and chain of custody.

[← Day 29](../029_day_threat_modeling/029_day_threat_modeling.md) · [Day index](../DAY_INDEX.md) · [Day 31 →](../031_day_processes_and_system_calls/031_day_processes_and_system_calls.md)
