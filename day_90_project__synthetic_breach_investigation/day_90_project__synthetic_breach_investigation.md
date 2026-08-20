# Day 90: Project: Synthetic Breach Investigation

[← Day 89](../day_89_incident_reporting/day_89_incident_reporting.md) · [Day index](../DAY_INDEX.md) · [Day 91 →](../day_91_rules_of_engagement/day_91_rules_of_engagement.md)

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

This project combines response lifecycle, evidence handling, timelines, artifacts, email, network context, volatility planning, and reporting into one safe investigation of invented data.

## Prerequisites

Complete Day 89. Use only the local fixtures and explicit loopback assessment scope supplied by the course.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using a tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Investigate a synthetic case bundle and produce a report that distinguishes observations, hypotheses, and missing evidence.

## Security boundary

This lesson is educational and authorized-lab-only. It does not authorize public scanning, credential guessing, exploitation, interception, persistence, or changes to systems you do not own.

## Lesson

### Vocabulary

A case bundle is a bounded set of artifacts. A hypothesis is an explanation to test. A finding links evidence to a cautious conclusion.

## Worked examples

### Example 1: Open the case index

Start with scope and artifact list.

```python
case = {
    "id": "training-090",
    "artifacts": ["timeline.json", "email.txt", "flow.json"],
    "scope": "synthetic",
}
print(case)
```

**What to observe:**

The bundle is bounded.

### Example 2: Verify artifacts

Check manifest or digest before analysis.

```python
verified = {"timeline.json": True, "email.txt": True, "flow.json": True}
print(verified)
```

**What to observe:**

All fixture artifacts pass the training check.

### Example 3: Build hypotheses

Hypotheses should be falsifiable and cautious.

```python
hypotheses = [
    {"text": "fixture rule triggered", "confidence": "medium"},
    {"text": "real compromise", "confidence": "not assessed"},
]
print(hypotheses)
```

**What to observe:**

The second hypothesis is not asserted.

### Example 4: Reference evidence

Every assessment should cite a local artifact.

```python
finding = {"assessment": "needs review", "evidence": ["timeline.json:2", "flow.json:1"]}
print(finding)
```

**What to observe:**

The report is traceable.

### Example 5: Close the case

Closure records learning and residual uncertainty.

```python
closure = {
    "state": "closed-training",
    "lesson": "add timestamp test",
    "unknowns": ["identity"],
}
print(closure)
```

**What to observe:**

The case closes without pretending certainty.

## Execution trace

The investigator preserves the bundle, verifies artifacts, builds hypotheses, tests them against local evidence, writes a report, and closes with lessons and unknowns.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| start with a story | evidence is selected to fit | start with index |
| alter artifacts | reproducibility fails | work on copies |
| hypothesis becomes fact | report overclaims | label confidence |
| no unknowns | blind spots disappear | list missing evidence |
| live response | scope and risk expand | synthetic-only |

## Security application

The project must remain synthetic, local, resettable, and non-operational. No real breach data, credentials, or response action is permitted.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the requested evidence, expected behavior, edge case, and limitation.

## Finish line

Run `python -m course_days.day090`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Investigation is a disciplined movement from preserved evidence to testable hypotheses to a bounded report.

## Limitations

The project cannot teach all forensic disciplines, law, attribution, or production incident command.

[← Day 89](../day_89_incident_reporting/day_89_incident_reporting.md) · [Day index](../DAY_INDEX.md) · [Day 91 →](../day_91_rules_of_engagement/day_91_rules_of_engagement.md)
