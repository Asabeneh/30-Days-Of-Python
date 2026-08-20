# Day 62: Request Parsing and Validation

[← Day 61](../061_day_local_service_architecture/061_day_local_service_architecture.md) · [Day index](../DAY_INDEX.md) · [Day 63 →](../063_day_authentication_and_authorization/063_day_authentication_and_authorization.md)

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

Web input arrives as bytes, headers, path segments, query values, and bodies. Parsing creates structure; validation decides whether that structure is acceptable.

## Prerequisites

Complete Day 61. Use only the local course fixtures, loopback services, and synthetic records described by the lesson.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using the tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state the trust boundary and residual risk
- complete the numbered cybersecurity exercises

## The problem

Validate a synthetic JSON request with required fields, bounds, and unknown-field policy before it reaches a service function.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, interception, exploit delivery, real-user profiling, or changes to systems you do not own.

## Lesson

### Vocabulary

Parsing extracts structure. Validation checks type and policy. A schema describes shape. Canonical errors avoid leaking implementation details.

## Worked examples

### Example 1: Parse JSON

Parsing creates ordinary values but does not validate them.

```python
import json

raw = '{"case_id": "training-062", "limit": 10}'
record = json.loads(raw)
print(record)
```

**What to observe:**

A dictionary is produced.

### Example 2: Require an object

The endpoint should reject a list when an object is expected.

```python
if not isinstance(record, dict):
    raise ValueError("body must be an object")
```

**What to observe:**

The wrong top-level shape fails early.

### Example 3: Check required fields

A missing field is different from an empty value.

```python
required = {"case_id", "limit"}
print(required - record.keys())
```

**What to observe:**

An empty set means keys exist.

### Example 4: Bound a field

Limits prevent resource abuse and ambiguous behavior.

```python
limit = int(record["limit"])
if not 1 <= limit <= 100:
    raise ValueError("limit outside allowed range")
```

**What to observe:**

10 is accepted; 0 and 101 are rejected.

### Example 5: Reject unknown fields

A strict schema prevents accidental policy bypass through ignored data.

```python
allowed = {"case_id", "limit"}
unknown = set(record) - allowed
print(unknown)
```

**What to observe:**

The caller can choose to reject unknown keys.

## Execution trace

The raw body is parsed, top-level type is checked, keys are compared to schema, values are converted and bounded, and only the validated model enters the service layer.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| parse equals validate | malformed data reaches policy | validate separately |
| ignore unknown fields | caller smuggles unsupported intent | reject or document them |
| huge string accepted | memory or storage abuse | bound length |
| generic `except` | programmer bugs look like input errors | catch expected parse errors |
| error echoes body | sensitive input leaks | return field-level safe errors |

## Security application

Use local JSON fixtures and test malformed JSON, missing fields, wrong types, unknown fields, and oversized values.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples as a starting point, then record the requested output, edge case, and limitation.

## Finish line

Run `python -m course_days.day062`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Parsing answers what structure arrived; validation answers whether the application will accept it.

## Limitations

Validation cannot prove that the caller is authorized or that the data is truthful.

[← Day 61](../061_day_local_service_architecture/061_day_local_service_architecture.md) · [Day index](../DAY_INDEX.md) · [Day 63 →](../063_day_authentication_and_authorization/063_day_authentication_and_authorization.md)
