# Day 99: Findings and Retesting

[← Day 98](../098_day_bounded_fuzzing/098_day_bounded_fuzzing.md) · [Day index](../DAY_INDEX.md) · [Day 100 →](../100_day_project__authorized_local_assessment/100_day_project__authorized_local_assessment.md)

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

A finding becomes useful when it states affected component, reproduction, impact, evidence, severity rationale, remediation, and retest result. Retesting should verify the original behavior without expanding scope.

## Prerequisites

Complete Day 98. Use only the local fixtures and explicit loopback assessment scope supplied by the course.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using a tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Write a synthetic finding, propose a fix, and record a retest that changes the status from open to verified or remains open.

## Security boundary

This lesson is educational and authorized-lab-only. It does not authorize public scanning, credential guessing, exploitation, interception, persistence, or changes to systems you do not own.

## Lesson

### Vocabulary

A finding is a documented issue. Reproduction is a minimal repeatable test. Remediation changes the control. Retest checks whether the original condition remains.

## Worked examples

### Example 1: State a finding

Start with a concise title and affected route.

```python
finding = {
    "title": "training endpoint accepts invalid limit",
    "route": "/cases",
    "status": "open",
}
print(finding)
```

**What to observe:**

The issue is scoped.

### Example 2: Give reproduction

A minimal case is easier to review.

```python
reproduction = {"input": {"limit": -1}, "expected": 400, "observed": 200}
print(reproduction)
```

**What to observe:**

The behavior is concrete.

### Example 3: Assess impact

Impact must match evidence.

```python
finding["impact"] = {"scope": "synthetic API", "effect": "invalid data reaches service"}
print(finding)
```

**What to observe:**

The impact is bounded.

### Example 4: Record remediation

A fix should name control and owner.

```python
remediation = {"control": "range validation", "owner": "student", "status": "planned"}
print(remediation)
```

**What to observe:**

The action is actionable.

### Example 5: Retest

Retesting repeats the original case and records outcome.

```python
retest = {"input": {"limit": -1}, "observed": 400, "status": "verified"}
print(retest)
```

**What to observe:**

The fixed behavior is documented.

## Execution trace

The finding records original evidence, remediation, and retest using the same bounded case. The status changes only when the expected behavior is observed.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| vague title | owner cannot act | name component and behavior |
| no reproduction | finding cannot be checked | give minimal input and expected result |
| severity without rationale | priority is arbitrary | explain impact and exposure |
| retest different case | fix is not verified | repeat original behavior |
| claim fixed from code review | runtime behavior unknown | run a safe retest |

## Security application

Use only synthetic local findings. Do not publish or weaponize a real vulnerability; follow the repository security policy for reports.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the requested evidence, expected behavior, edge case, and limitation.

## Finish line

Run `python -m course_days.day099`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A finding is a reproducible claim with bounded impact, owned remediation, and an evidence-linked retest.

## Limitations

Retesting can miss variants and does not prove absence of all related bugs.

[← Day 98](../098_day_bounded_fuzzing/098_day_bounded_fuzzing.md) · [Day index](../DAY_INDEX.md) · [Day 100 →](../100_day_project__authorized_local_assessment/100_day_project__authorized_local_assessment.md)
