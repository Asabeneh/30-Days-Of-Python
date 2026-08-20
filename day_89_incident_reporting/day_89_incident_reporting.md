# Day 89: Incident Reporting

[← Day 88](../day_88_volatile_evidence_concepts/day_88_volatile_evidence_concepts.md) · [Day index](../DAY_INDEX.md) · [Day 90 →](../day_90_project__synthetic_breach_investigation/day_90_project__synthetic_breach_investigation.md)

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

A report converts technical observations into a shared decision record. It should be concise enough to use and detailed enough to reproduce, with separate facts, assessment, actions, and limitations.

## Prerequisites

Complete Day 88. Use only the local fixtures and explicit loopback assessment scope supplied by the course.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using a tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Write a synthetic incident report with an executive summary, timeline, evidence references, impact assessment, and next steps.

## Security boundary

This lesson is educational and authorized-lab-only. It does not authorize public scanning, credential guessing, exploitation, interception, persistence, or changes to systems you do not own.

## Lesson

### Vocabulary

An executive summary communicates impact and status. A timeline orders observations. An impact assessment states affected scope. An action item has an owner and due state.

## Worked examples

### Example 1: Write a summary

Lead with scope, status, and confidence.

```python
summary = {"status": "investigating", "scope": "training fixture", "confidence": "low"}
print(summary)
```

**What to observe:**

The summary is cautious.

### Example 2: Build a timeline

Use evidence references rather than unsupported prose.

```python
timeline = [{"time": "10:00Z", "event": "fixture alert", "ref": "line-2"}]
print(timeline)
```

**What to observe:**

The event is traceable.

### Example 3: Assess impact

Impact is a bounded claim.

```python
impact = {"systems": 0, "real_users": 0, "training_records": 3}
print(impact)
```

**What to observe:**

The scope is explicit.

### Example 4: Assign action

Reports should result in owned follow-up.

```python
action = {"task": "add parser test", "owner": "student", "state": "open"}
print(action)
```

**What to observe:**

The action is concrete.

### Example 5: State limitations

A report protects readers from overtrust.

```python
limitations = ["synthetic", "no identity proof", "no live collection"]
print(limitations)
```

**What to observe:**

The limitations are visible.

## Execution trace

The report gathers validated observations, orders them, assesses bounded impact, records authorized actions, assigns owners, and preserves limitations and evidence references.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| bury status | leaders cannot act | start with summary |
| mix fact and interpretation | claims are hard to review | label sections |
| no impact boundary | scope expands in retelling | quantify what is known |
| no owner | action stalls | assign follow-up |
| omit uncertainty | report becomes verdict | state confidence and gaps |

## Security application

Use synthetic events and fictional ownership. Do not report a real person, organization, or incident.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the requested evidence, expected behavior, edge case, and limitation.

## Finish line

Run `python -m course_days.day089`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A report is a shared, evidence-linked decision record with explicit scope and uncertainty.

## Limitations

Reports can be copied out of context and cannot replace incident command or legal review.

[← Day 88](../day_88_volatile_evidence_concepts/day_88_volatile_evidence_concepts.md) · [Day index](../DAY_INDEX.md) · [Day 90 →](../day_90_project__synthetic_breach_investigation/day_90_project__synthetic_breach_investigation.md)
