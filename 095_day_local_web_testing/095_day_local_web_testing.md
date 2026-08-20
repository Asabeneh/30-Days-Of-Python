# Day 95: Local Web Testing

[← Day 94](../094_day_cve_and_severity_reasoning/094_day_cve_and_severity_reasoning.md) · [Day index](../DAY_INDEX.md) · [Day 96 →](../096_day_authorization_testing/096_day_authorization_testing.md)

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

Testing a web service safely means checking explicit contracts on a local target, recording expected and unexpected behavior, and stopping at the rules of engagement.

## Prerequisites

Complete Day 94. Use only the local fixtures and explicit loopback assessment scope supplied by the course.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using a tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Test a local health endpoint for status, content type, and invalid input using a small fixture-driven test suite.

## Security boundary

This lesson is educational and authorized-lab-only. It does not authorize public scanning, credential guessing, exploitation, interception, persistence, or changes to systems you do not own.

## Lesson

### Vocabulary

A test case has setup, action, expected result, and cleanup. A negative test sends invalid input. A regression test protects a fixed behavior.

## Worked examples

### Example 1: Define a case

A test case should be a data object.

```python
case = {"name": "health", "method": "GET", "path": "/health", "expected": 200}
print(case)
```

**What to observe:**

The test contract is explicit.

### Example 2: Check content type

Status alone does not prove response contract.

```python
response = {"status": 200, "content_type": "application/json"}
print(response)
```

**What to observe:**

The response includes both fields.

### Example 3: Add negative input

Invalid input should be rejected predictably.

```python
negative = {"path": "/cases", "body": {"limit": -1}, "expected": 400}
print(negative)
```

**What to observe:**

The boundary case is explicit.

### Example 4: Record cleanup

Testing must leave the local service reset.

```python
cleanup = {"created_records": 0, "output_deleted": True}
print(cleanup)
```

**What to observe:**

No test data remains.

### Example 5: Keep scope

Tests should carry target and approval.

```python
metadata = {"target": "127.0.0.1:8000", "approved": True}
print(metadata)
```

**What to observe:**

The target is local and approved.

## Execution trace

The runner loads cases, confirms target scope, performs one local request at a time, validates status/headers/body, records failures, and resets generated state.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| test public endpoint | unauthorized activity | loopback-only |
| only happy path | validation failures hide | add negative tests |
| no cleanup | state changes persist | reset fixture |
| exploit instead of verify | risk grows | test contract minimally |
| no evidence | finding cannot reproduce | record request and expected result safely |

## Security application

Use local service fixtures, synthetic identities, and harmless invalid inputs. No exploitation, credential guessing, or public scanning.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the requested evidence, expected behavior, edge case, and limitation.

## Finish line

Run `python -m course_days.day095`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Authorized testing is controlled experimentation against a known contract and target, with cleanup and evidence.

## Limitations

A passing local test says little about production deployment, authentication integration, or unknown attack paths.

[← Day 94](../094_day_cve_and_severity_reasoning/094_day_cve_and_severity_reasoning.md) · [Day index](../DAY_INDEX.md) · [Day 96 →](../096_day_authorization_testing/096_day_authorization_testing.md)
