# Day 69: Supply Chain and Exceptional Conditions

[← Day 68](../day_68_misconfiguration_and_defaults/day_68_misconfiguration_and_defaults.md) · [Day index](../DAY_INDEX.md) · [Day 70 →](../day_70_project__secure_case_api/day_70_project__secure_case_api.md)

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

A secure application depends on packages, build steps, services, and assumptions outside one source file. Exceptional conditions include dependency failure, missing updates, and unexpected runtime behavior.

## Prerequisites

Complete Day 68. Use only the local course fixtures, loopback services, and synthetic records described by the lesson.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using the tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state the trust boundary and residual risk
- complete the numbered cybersecurity exercises

## The problem

Review a synthetic dependency record and design a failure path that does not silently downgrade security.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, interception, exploit delivery, real-user profiling, or changes to systems you do not own.

## Lesson

### Vocabulary

A supply chain includes code, packages, maintainers, build systems, and artifacts. An exceptional condition is a failure outside the ordinary happy path. Fail closed means refusing a sensitive action when a required control is unavailable.

## Worked examples

### Example 1: Inventory a component

Record source, version, purpose, and review date.

```python
component = {
    "name": "training-lib",
    "version": "1.0",
    "source": "reviewed-index",
    "reviewed": "2026-08-20",
}
print(component)
```

**What to observe:**

The provenance fields are visible.

### Example 2: Separate required and optional

Security controls should not silently become optional.

```python
dependency = {"name": "verifier", "required_for": "integrity", "optional": False}
print(dependency)
```

**What to observe:**

The requirement is explicit.

### Example 3: Handle unavailable verification

If verification cannot run, do not mark data trusted.

```python
verification = {"status": "unavailable", "trusted": False}
print(verification)
```

**What to observe:**

The state is incomplete.

### Example 4: Pin a policy

A review record should identify what was actually tested.

```python
policy = {"lockfile": True, "hashes": "reviewed", "updates": "scheduled"}
print(policy)
```

**What to observe:**

The process is documented.

### Example 5: Preserve evidence

An error record should identify the component without dumping environment secrets.

```python
print({"component": component["name"], "event": "verification_failed"})
```

**What to observe:**

The log is minimal.

## Execution trace

The program identifies dependencies and their provenance, attempts a required control, records whether it was available, and refuses to mark the artifact trusted when the control failed.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| install any package | unreviewed code enters | verify source and purpose |
| latest without review | behavior changes silently | pin and test updates |
| unavailable scanner equals pass | blind spot is reported as clean | fail closed or mark unknown |
| log environment | tokens and paths leak | minimize component evidence |
| no update owner | known issues persist | assign review lifecycle |

## Security application

Use only the repository’s declared development tools and synthetic component records. Do not install packages from arbitrary commands or execute downloaded artifacts.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples as a starting point, then record the requested output, edge case, and limitation.

## Finish line

Run `python -m course_days.day069`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A supply-chain control is trustworthy only when its source, version, availability, and failure state are visible.

## Limitations

No inventory eliminates maintainer compromise, build tampering, or unknown vulnerabilities; it supports informed review.

[← Day 68](../day_68_misconfiguration_and_defaults/day_68_misconfiguration_and_defaults.md) · [Day index](../DAY_INDEX.md) · [Day 70 →](../day_70_project__secure_case_api/day_70_project__secure_case_api.md)
