# Day 91: Rules of Engagement

[← Day 90](../day_90_project__synthetic_breach_investigation/day_90_project__synthetic_breach_investigation.md) · [Day index](../DAY_INDEX.md) · [Day 92 →](../day_92_asset_inventory/day_92_asset_inventory.md)

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

Authorized testing starts with permission, scope, timing, targets, techniques, stop conditions, and reporting—not with a tool command.

## Prerequisites

Complete Day 90. Use only the local fixtures and explicit loopback assessment scope supplied by the course.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using a tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Write a rules-of-engagement document for a local test service and show how a proposed action is checked before execution.

## Security boundary

This lesson is educational and authorized-lab-only. It does not authorize public scanning, credential guessing, exploitation, interception, persistence, or changes to systems you do not own.

## Lesson

### Vocabulary

Rules of engagement define permitted activity. Scope identifies targets. A stop condition ends testing. An escalation path handles unexpected impact.

## Worked examples

### Example 1: Define target

Name one local target and owner.

```python
roe = {
    "target": "127.0.0.1:8000",
    "owner": "course learner",
    "environment": "disposable",
}
print(roe)
```

**What to observe:**

The target is loopback and owned.

### Example 2: Define allowed tests

Technique names should be narrow and bounded.

```python
roe["allowed"] = ["health request", "invalid local input"]
print(roe)
```

**What to observe:**

The test set is explicit.

### Example 3: Define prohibited actions

A prohibition prevents scope drift.

```python
roe["prohibited"] = ["credential guessing", "data deletion", "public scanning"]
print(roe)
```

**What to observe:**

The dangerous expansions are named.

### Example 4: Define stop conditions

Stop when an impact signal appears.

```python
roe["stop_if"] = ["service instability", "unexpected target", "private data"]
print(roe)
```

**What to observe:**

The tester has a stop rule.

### Example 5: Approve a command

A command is eligible only after all checks pass.

```python
proposal = {"target": "127.0.0.1:8000", "action": "health request"}
print(proposal["target"] == roe["target"] and proposal["action"] in roe["allowed"])
```

**What to observe:**

`True` for the permitted proposal.

## Execution trace

The tester reads scope, compares target and action to allowlists, checks time and stop conditions, records approval, then performs only the local test and reports outcome.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| permission implied | target is guessed | require written scope |
| scope by hostname only | redirects or aliases expand | define exact target |
| no stop condition | impact continues | stop and escalate |
| test first, document later | authorization is unclear | write ROE first |
| keep credentials | sensitive data enters lab | use synthetic accounts |

## Security application

Use the local disposable service only. This lesson does not authorize vulnerability scanning, password attacks, exploitation, or public testing.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the requested evidence, expected behavior, edge case, and limitation.

## Finish line

Run `python -m course_days.day091`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Authorization is a prerequisite and a constraint; a tool command is never permission.

## Limitations

Rules of engagement can be incomplete or superseded by policy; obtain current approval and stop when uncertain.

[← Day 90](../day_90_project__synthetic_breach_investigation/day_90_project__synthetic_breach_investigation.md) · [Day index](../DAY_INDEX.md) · [Day 92 →](../day_92_asset_inventory/day_92_asset_inventory.md)
