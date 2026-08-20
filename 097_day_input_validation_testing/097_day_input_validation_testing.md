# Day 97: Input Validation Testing

[← Day 96](../096_day_authorization_testing/096_day_authorization_testing.md) · [Day index](../DAY_INDEX.md) · [Day 98 →](../098_day_bounded_fuzzing/098_day_bounded_fuzzing.md)

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

Validation tests should prove that boundaries reject malformed, missing, oversized, and unexpected input while accepting valid data. The goal is predictable behavior, not payload theater.

## Prerequisites

Complete Day 96. Use only the local fixtures and explicit loopback assessment scope supplied by the course.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using a tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Create a table-driven validation suite for a synthetic case request.

## Security boundary

This lesson is educational and authorized-lab-only. It does not authorize public scanning, credential guessing, exploitation, interception, persistence, or changes to systems you do not own.

## Lesson

### Vocabulary

A boundary case is near an allowed limit. A negative case is invalid. A property is a behavior that should hold across many inputs.

## Worked examples

### Example 1: Define valid input

Start with the smallest accepted request.

```python
valid = {"case_id": "training-97", "limit": 10}
print(valid)
```

**What to observe:**

The valid shape is known.

### Example 2: List invalid cases

Test categories rather than one magic string.

```python
invalid = [{}, {"limit": -1}, {"case_id": "x" * 10000}]
print(len(invalid))
```

**What to observe:**

Three invalid classes are present.

### Example 3: Test a boundary

Allowed endpoints need explicit tests.

```python
for limit in [1, 100]:
    print(limit, 1 <= limit <= 100)
```

**What to observe:**

Both endpoints are accepted by this policy.

### Example 4: Test a just-outside value

Off-by-one bugs appear adjacent to the boundary.

```python
for limit in [0, 101]:
    print(limit, 1 <= limit <= 100)
```

**What to observe:**

Both are rejected.

### Example 5: Return safe errors

Tests should check error shape without exposing raw input.

```python
error = {"status": 400, "field": "limit", "message": "outside allowed range"}
print(error)
```

**What to observe:**

The error is actionable and minimal.

## Execution trace

The suite arranges one case, validates it, compares accepted/rejected outcome and safe error schema, and repeats across a table of boundaries and malformed shapes.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| only valid tests | bad input reaches service | add categories |
| huge payload in test | test itself consumes resources | small bounded representative |
| assert raw error | secret input leaks | assert safe fields |
| no property | one sample passes by accident | state invariant |
| input test becomes exploit | scope changes | keep contract-focused |

## Security application

Use synthetic requests and a local handler. Test validation, not exploitation or bypass of a real application.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the requested evidence, expected behavior, edge case, and limitation.

## Finish line

Run `python -m course_days.day097`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Input validation testing turns the boundary contract into repeatable evidence.

## Limitations

Tests can miss parser differentials, framework behavior, encoding edge cases, and integration failures.

[← Day 96](../096_day_authorization_testing/096_day_authorization_testing.md) · [Day index](../DAY_INDEX.md) · [Day 98 →](../098_day_bounded_fuzzing/098_day_bounded_fuzzing.md)
