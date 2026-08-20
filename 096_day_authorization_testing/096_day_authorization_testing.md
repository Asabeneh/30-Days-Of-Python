# Day 96: Authorization Testing

[← Day 95](../095_day_local_web_testing/095_day_local_web_testing.md) · [Day index](../DAY_INDEX.md) · [Day 97 →](../097_day_input_validation_testing/097_day_input_validation_testing.md)

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

Authorization bugs often occur when a caller can access another object or perform an action outside its role. Testing should use synthetic identities and cases, not real accounts.

## Prerequisites

Complete Day 95. Use only the local fixtures and explicit loopback assessment scope supplied by the course.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using a tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Test object-level and action-level authorization with a small matrix of fictional users, roles, and cases.

## Security boundary

This lesson is educational and authorized-lab-only. It does not authorize public scanning, credential guessing, exploitation, interception, persistence, or changes to systems you do not own.

## Lesson

### Vocabulary

A subject is a fictional caller identity. An object is a resource. An action is an operation. An authorization matrix lists allowed and denied combinations.

## Worked examples

### Example 1: Create identities

Use labels rather than credentials.

```python
identities = {"alice": {"role": "analyst"}, "bob": {"role": "viewer"}}
print(identities)
```

**What to observe:**

The identities are synthetic.

### Example 2: Create objects

Ownership or scope is a separate record.

```python
ownership = {"alice": {"case-1"}, "bob": {"case-2"}}
print(ownership)
```

**What to observe:**

Each subject has object scope.

### Example 3: Test an allow

The expected result is part of the case.

```python
case = {"subject": "alice", "action": "read", "object": "case-1", "expected": True}
print(case)
```

**What to observe:**

The allowed case is explicit.

### Example 4: Test horizontal denial

A caller should not read another subject’s object.

```python
case = {"subject": "alice", "action": "read", "object": "case-2", "expected": False}
print(case)
```

**What to observe:**

The cross-object case is denied.

### Example 5: Test action denial

A role may read but not delete.

```python
policy = {"viewer": {"read"}}
print("delete" in policy["viewer"])
```

**What to observe:**

The action is denied.

## Execution trace

The matrix supplies subject, role, action, and object; the service evaluates role and object scope; the test compares the result with expected allow/deny without using real authentication.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| role-only tests | object leak missed | add horizontal cases |
| UI-only denial | API bypass | test service boundary |
| real accounts | privacy and access risk | synthetic identities |
| expected unspecified | failure is ambiguous | write matrix first |
| denial leaks object | error reveals data | safe error responses |

## Security application

Use fictional identities and local cases. Do not test a real account or attempt to bypass access controls on a public service.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the requested evidence, expected behavior, edge case, and limitation.

## Finish line

Run `python -m course_days.day096`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Authorization testing asks whether each subject/action/object combination matches the written policy.

## Limitations

A small matrix cannot cover every policy path, tenant rule, or deployment integration.

[← Day 95](../095_day_local_web_testing/095_day_local_web_testing.md) · [Day index](../DAY_INDEX.md) · [Day 97 →](../097_day_input_validation_testing/097_day_input_validation_testing.md)
