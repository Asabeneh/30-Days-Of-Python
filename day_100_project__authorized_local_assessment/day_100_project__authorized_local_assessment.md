# Day 100: Project: Authorized Local Assessment

[← Day 99](../day_99_findings_and_retesting/day_99_findings_and_retesting.md) · [Day index](../DAY_INDEX.md) · [Day 101 →](../day_101_secure_sdlc/day_101_secure_sdlc.md)

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

This project is the culmination of safe testing: scope, inventory, ROE, local web tests, validation checks, bounded fuzzing, findings, remediation, and retesting in one controlled assessment.

## Prerequisites

Complete Day 99. Use only the local fixtures and explicit loopback assessment scope supplied by the course.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using a tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Assess one disposable local service and produce an evidence-based report without scanning, exploitation, or real credentials.

## Security boundary

This lesson is educational and authorized-lab-only. It does not authorize public scanning, credential guessing, exploitation, interception, persistence, or changes to systems you do not own.

## Lesson

### Vocabulary

An assessment is a scoped evaluation. A test plan states cases and expected results. A finding is an observed contract failure. A closeout records limits and cleanup.

## Worked examples

### Example 1: Load authorization

The project begins with the signed or explicit local scope record.

```python
scope = {
    "target": "127.0.0.1:8000",
    "allowed": ["health", "validation"],
    "stop": ["instability"],
}
print(scope)
```

**What to observe:**

The target and limits are visible.

### Example 2: Run inventory

Check the target against the approved asset list.

```python
asset = {"target": "127.0.0.1:8000", "environment": "disposable", "owner": "course"}
print(asset["target"] == scope["target"])
```

**What to observe:**

The asset matches scope.

### Example 3: Run contract tests

Use a small table of safe cases.

```python
tests = [
    {"path": "/health", "expected": 200},
    {"path": "/cases", "input": {"limit": -1}, "expected": 400},
]
print(tests)
```

**What to observe:**

The cases are explicit.

### Example 4: Create finding

Only observed deviations become findings.

```python
finding = {"status": "none", "evidence": ["health-1", "validation-1"]}
print(finding)
```

**What to observe:**

No issue is invented when tests pass.

### Example 5: Close and reset

The assessment ends with cleanup and limitations.

```python
closeout = {
    "reports_deleted": True,
    "service_stopped": True,
    "public_target": False,
    "limitations": ["local only"],
}
print(closeout)
```

**What to observe:**

The environment is reset.

## Execution trace

The assessment verifies authorization, matches one asset, executes only planned local cases, records evidence and findings, retests fixes, and closes with cleanup and limitations.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| scope after testing | authorization is unclear | load it first |
| add scanning feature | project exceeds ROE | one local service |
| report every difference | noise and overclaiming | require reproducible evidence |
| no retest | remediation is unverified | repeat original case |
| forget cleanup | local state persists | reset and document |

## Security application

The project is loopback-only, disposable, synthetic, read-only where possible, finite, and governed by explicit stop conditions. It must never test a public or third-party target.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the requested evidence, expected behavior, edge case, and limitation.

## Finish line

Run `python -m course_days.day100`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> An authorized assessment is a controlled experiment whose strongest result is reproducible evidence within a documented boundary.

## Limitations

This project cannot establish production security, legal compliance, exploitability, or absence of unknown vulnerabilities.

[← Day 99](../day_99_findings_and_retesting/day_99_findings_and_retesting.md) · [Day index](../DAY_INDEX.md) · [Day 101 →](../day_101_secure_sdlc/day_101_secure_sdlc.md)
