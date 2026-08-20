# Day 87: Network Evidence

[← Day 86](../086_day_email_and_phishing_fixtures/086_day_email_and_phishing_fixtures.md) · [Day index](../DAY_INDEX.md) · [Day 88 →](../088_day_volatile_evidence_concepts/088_day_volatile_evidence_concepts.md)

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

Network evidence can explain sequence and protocol behavior, but it is sensitive and often incomplete. Fixture-first analysis lets learners practise fields, timestamps, direction, and truncation safely.

## Prerequisites

Complete Day 86. Use only the local fixtures and explicit loopback assessment scope supplied by the course.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using a tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Summarize synthetic flow records and identify what the fixture cannot show.

## Security boundary

This lesson is educational and authorized-lab-only. It does not authorize public scanning, credential guessing, exploitation, interception, persistence, or changes to systems you do not own.

## Lesson

### Vocabulary

A flow summarizes endpoints and bytes. Direction indicates source-to-destination orientation. A capture is packet-level evidence. Truncation limits interpretation.

## Worked examples

### Example 1: Model a flow

A flow record should name endpoints, time, and counts.

```python
flow = {
    "src": "127.0.0.1",
    "dst": "127.0.0.1",
    "src_port": 5000,
    "dst_port": 8000,
    "bytes": 120,
}
print(flow)
```

**What to observe:**

The record is loopback-only.

### Example 2: Normalize direction

A report should define which endpoint is considered source.

```python
direction = {"source": flow["src"], "destination": flow["dst"]}
print(direction)
```

**What to observe:**

Direction is explicit.

### Example 3: Aggregate safely

Totals can summarize without retaining every payload.

```python
flows = [120, 80]
print(sum(flows))
```

**What to observe:**

`200` bytes across synthetic records.

### Example 4: Mark truncation

Missing packets or payloads limit conclusions.

```python
print({"payload_present": False, "complete": False})
```

**What to observe:**

The limitation is visible.

### Example 5: Avoid identity claims

An endpoint is not a person.

```python
print({"endpoint": "127.0.0.1", "identity": "not established"})
```

**What to observe:**

The interpretation is bounded.

## Execution trace

The analyst loads a saved fixture, parses flow fields, normalizes direction and time, aggregates selected counts, and marks missing payload or capture gaps.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| capture live traffic | privacy and authorization fail | use fixtures |
| endpoint equals actor | identity is invented | state not established |
| missing payload ignored | analysis looks complete | report truncation |
| aggregate loses provenance | result cannot be checked | keep flow references |
| packet pattern equals intent | context is absent | use neutral language |

## Security application

Use only synthetic flow records. Do not sniff interfaces, intercept traffic, or reconstruct other people’s communications.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the requested evidence, expected behavior, edge case, and limitation.

## Finish line

Run `python -m course_days.day087`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Network evidence describes observed communication properties with scope and completeness limits.

## Limitations

Encryption, NAT, proxies, spoofing, and missing collection can make a flow misleading.

[← Day 86](../086_day_email_and_phishing_fixtures/086_day_email_and_phishing_fixtures.md) · [Day index](../DAY_INDEX.md) · [Day 88 →](../088_day_volatile_evidence_concepts/088_day_volatile_evidence_concepts.md)
