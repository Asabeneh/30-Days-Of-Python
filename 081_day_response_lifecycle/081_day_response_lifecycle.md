# Day 81: The Response Lifecycle

[← Day 80](../080_day_project__mini_detection_pipeline/080_day_project__mini_detection_pipeline.md) · [Day index](../DAY_INDEX.md) · [Day 82 →](../082_day_evidence_integrity/082_day_evidence_integrity.md)

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

Response work is a controlled lifecycle, not a collection of exciting commands. Preparation, detection, analysis, containment, recovery, and lessons learned each have different evidence and authority requirements.

## Prerequisites

Complete Day 80. Use only the local fixtures and explicit loopback assessment scope supplied by the course.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using a tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Represent a synthetic alert from intake through closure while keeping actions bounded and approvals visible.

## Security boundary

This lesson is educational and authorized-lab-only. It does not authorize public scanning, credential guessing, exploitation, interception, persistence, or changes to systems you do not own.

## Lesson

### Vocabulary

An incident is a suspected adverse event requiring coordinated handling. Containment limits impact. Eradication removes a cause. Recovery restores service. A retrospective improves the system.

## Worked examples

### Example 1: Define states

A finite lifecycle prevents hidden transitions.

```python
states = ["new", "triage", "contained", "recovered", "closed"]
print(states)
```

**What to observe:**

The allowed lifecycle is visible.

### Example 2: Record an owner

A response item needs responsibility.

```python
case = {"id": "training-81", "owner": "student", "state": "new"}
print(case)
```

**What to observe:**

The case has an owner and state.

### Example 3: Require authorization

A containment action is not implied by an alert.

```python
action = {"name": "disable_fixture_account", "approved": False}
print(action)
```

**What to observe:**

The action remains pending.

### Example 4: Preserve evidence

Response should reference evidence rather than alter it.

```python
case["evidence_refs"] = ["fixture:event-2"]
print(case)
```

**What to observe:**

The case points to local evidence.

### Example 5: Close with lessons

Closure includes outcome and improvement.

```python
closure = {
    "state": "closed",
    "root_cause": "training fixture",
    "lesson": "add parser test",
}
print(closure)
```

**What to observe:**

The closeout is explainable.

## Execution trace

The case moves only through allowed states; every action has an owner, authority, evidence reference, and outcome. A signal does not automatically authorize containment.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| alert equals incident | response starts without validation | triage first |
| no owner | work stalls | assign responsibility |
| alter evidence | investigation loses provenance | preserve and work on copies |
| contain without approval | service impact | define authority |
| close without learning | defect repeats | record retrospective action |

## Security application

Use only a synthetic case and describe actions without performing them on real systems. The project must state who may approve each state transition.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the requested evidence, expected behavior, edge case, and limitation.

## Finish line

Run `python -m course_days.day081`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Response is a governed lifecycle that moves evidence and decisions through explicit states.

## Limitations

Real response depends on law, policy, contracts, communications, and business continuity beyond this lesson.

[← Day 80](../080_day_project__mini_detection_pipeline/080_day_project__mini_detection_pipeline.md) · [Day index](../DAY_INDEX.md) · [Day 82 →](../082_day_evidence_integrity/082_day_evidence_integrity.md)
