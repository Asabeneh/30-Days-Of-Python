# Day 24: JSON, CSV, SQLite, and Schema Validation

[Previous](../023_day_configuration_and_secrets/023_day_configuration_and_secrets.md) | [Next](../025_day_type_hints_and_static_checks/025_day_type_hints_and_static_checks.md)

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

Security engineering becomes dependable when its inputs, dependencies, failure behavior, and evidence are visible. This day builds one professional Python habit through a bounded local exercise.

## Prerequisites

Complete Day 23, keep [SETUP.md](../SETUP.md) available, and read [SAFETY_AND_LAB_RULES.md](../SAFETY_AND_LAB_RULES.md).

## Outcomes

You can explain the concept, trace the starter, make one controlled change, test a normal and negative case, and document one security limitation.

## The problem

A security utility often fails at a boundary: installation, command-line input, configuration, data serialization, logging, review, dependencies, or design assumptions. Today makes one such boundary explicit.

## Security boundary

Use only synthetic data and local files. Do not add real credentials, private evidence, public targets, or network access to the starter. Stop if the exercise leaves its documented scope.

## Core lesson

JSON and CSV are representations, not trusted object models. SQLite gives structured queries, but a database does not validate that a record's meaning is correct.

```python
import json

record = json.loads('{"severity": 5}')
if not isinstance(record.get("severity"), int):
    raise ValueError("severity must be an integer")
```

Validate required fields, types, ranges, and unknown-field policy at the boundary. Use parameterized SQL rather than string concatenation.

Security connection: deserialization and injection occur when data is allowed to become behavior without a narrow contract.

### Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| Treating tools as magic | The learner cannot reproduce the result | State the interpreter, input, command, and expected output |
| Trusting representation | Malformed data enters the decision layer | Validate fields and types at the boundary |
| Logging everything | Secrets or private data appear in output | Minimize, redact, and test logging behavior |
| Confusing a control with proof | A checklist is called “secure” | Name the test and the residual risk |

## Practice

### Level 1 — Mechanical

Run the starter, predict one output, change one value, and explain the result.

### Level 2 — Applied

Build a small local utility that uses today's idea with synthetic input. State its contract and acceptance criteria before coding.

### Level 3 — Synthesis

Add one failure case, one test, and a short threat-model note naming an asset, boundary, threat, control, and residual risk.

Use [practice/prompts.md](practice/prompts.md), then progressive [hints](practice/hints.md), then explained [solutions](practice/solutions.md).

## Mental model

> Serialization moves data across a boundary; validate the structure before trusting the fields.

## Finish line

Run `python -m course_days.day024`, pass the phase tests, complete Levels 1 and 2, and write one edge-case note.
