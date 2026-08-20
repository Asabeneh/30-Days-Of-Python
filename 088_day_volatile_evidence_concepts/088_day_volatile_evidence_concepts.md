# Day 88: Volatile Evidence Concepts

[← Day 87](../087_day_network_evidence/087_day_network_evidence.md) · [Day index](../DAY_INDEX.md) · [Day 89 →](../089_day_incident_reporting/089_day_incident_reporting.md)

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

Some evidence changes quickly: process lists, memory, open connections, and temporary state. The safe lesson is to reason about volatility and collection order without collecting from a real host.

## Prerequisites

Complete Day 87. Use only the local fixtures and explicit loopback assessment scope supplied by the course.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using a tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Create a synthetic evidence-priority plan and explain why collection order matters.

## Security boundary

This lesson is educational and authorized-lab-only. It does not authorize public scanning, credential guessing, exploitation, interception, persistence, or changes to systems you do not own.

## Lesson

### Vocabulary

Volatile evidence changes quickly. A snapshot is one observation. Collection order is the sequence in which evidence is preserved. A live response has operational risk.

## Worked examples

### Example 1: Rank volatility

Prioritize evidence that changes fastest in the plan.

```python
order = ["memory-like state", "process list", "connections", "disk fixture"]
print(order)
```

**What to observe:**

The plan is ordered by conceptual volatility.

### Example 2: Model a snapshot

A snapshot needs time and scope.

```python
snapshot = {"kind": "processes", "captured_at": "now", "host": "synthetic"}
print(snapshot)
```

**What to observe:**

The context is preserved.

### Example 3: Record absence

A missing collection is not an empty state.

```python
print({"kind": "memory", "status": "not_collected", "reason": "fixture only"})
```

**What to observe:**

The limitation is honest.

### Example 4: State collection impact

Live collection can alter the system or expose data.

```python
risk = {"impact": "process list changes", "mitigation": "synthetic fixture"}
print(risk)
```

**What to observe:**

The safety trade-off is explicit.

### Example 5: Preserve order

A response plan should explain why order was chosen.

```python
plan = {"order": order, "rationale": "preserve volatile state first"}
print(plan)
```

**What to observe:**

The reasoning is reviewable.

## Execution trace

The plan ranks evidence, records scope and time, names unavailable sources, and documents collection impact before any live action is considered.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| collect everything first | volatile state changes | plan order |
| live collection casually | system impact | use fixture or authority |
| missing equals empty | blind spot is hidden | mark not collected |
| no timestamp | state cannot be placed | record time |
| memory dump without policy | privacy and access risk | do not collect in lesson |

## Security application

Use synthetic snapshots only. Do not inspect processes, memory, connections, or accounts on a real host.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the requested evidence, expected behavior, edge case, and limitation.

## Finish line

Run `python -m course_days.day088`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Volatility is a planning property: preserve changing observations first when authorized, and disclose what was not collected.

## Limitations

Real volatile evidence collection requires specialized authority, tools, minimization, and legal or organizational procedures.

[← Day 87](../087_day_network_evidence/087_day_network_evidence.md) · [Day index](../DAY_INDEX.md) · [Day 89 →](../089_day_incident_reporting/089_day_incident_reporting.md)
