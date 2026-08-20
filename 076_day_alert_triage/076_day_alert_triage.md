# Day 76: Alert Triage and Analyst Decisions

[← Day 75](../075_day_mitre_att_ck_mapping/075_day_mitre_att_ck_mapping.md) · [Day index](../DAY_INDEX.md) · [Day 77 →](../077_day_baselines_and_anomalies/077_day_baselines_and_anomalies.md)

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

An alert is a queue item, not a conclusion. Triage organizes evidence, severity, confidence, scope, next step, and closure reason so analysts do not confuse urgency with certainty.

## Prerequisites

Complete Day 75. Use only the local course fixtures, loopback services, and synthetic records described by the lesson.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using the tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state the trust boundary and residual risk
- complete the numbered cybersecurity exercises

## The problem

Triage synthetic alerts into review states with an explicit evidence checklist and no automatic accusation.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, interception, exploit delivery, real-user profiling, or changes to systems you do not own.

## Lesson

### Vocabulary

Triage prioritizes work. Severity describes impact or urgency. Confidence describes evidence quality. Disposition records what happened to the alert.

## Worked examples

### Example 1: Create an alert

An alert needs an identifier and evidence reference.

```python
alert = {"id": "alert-76", "rule": "failed-login-threshold", "evidence": ["fixture:4"]}
print(alert)
```

**What to observe:**

The alert points to evidence.

### Example 2: Score separately

Severity and confidence answer different questions.

```python
alert.update({"severity": "medium", "confidence": "low"})
print(alert)
```

**What to observe:**

A medium-impact, low-confidence alert is possible.

### Example 3: Choose a disposition

Triage needs controlled states.

```python
allowed = {"new", "investigating", "benign", "escalated", "closed"}
print("investigating" in allowed)
```

**What to observe:**

The state is from a finite vocabulary.

### Example 4: Record next step

The next action should be authorized and bounded.

```python
alert["next_step"] = "review synthetic timeline"
print(alert)
```

**What to observe:**

The plan is local and specific.

### Example 5: Close with reason

Closure should preserve why a case ended.

```python
alert.update({"disposition": "benign_training_fixture", "closed_by": "student"})
print(alert)
```

**What to observe:**

The outcome is explainable.

## Execution trace

Triage reads the alert and evidence, separates severity from confidence, selects a state, records a bounded next step, and preserves a disposition and reviewer.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| alert equals incident | unnecessary response | require evidence and triage |
| severity equals confidence | urgency and certainty blur | store separately |
| no closure reason | lessons are lost | require disposition |
| investigate without scope | analyst overreaches | name authorized next step |
| copy raw data everywhere | privacy expands | reference evidence minimally |

## Security application

Use synthetic alerts and a local queue. Do not triage real individuals or initiate response actions from this lesson.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples as a starting point, then record the requested output, edge case, and limitation.

## Finish line

Run `python -m course_days.day076`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Triage is an evidence-organizing decision process that turns a signal into a documented next step.

## Limitations

Triage quality depends on context, staffing, data quality, and escalation policy outside the code.

[← Day 75](../075_day_mitre_att_ck_mapping/075_day_mitre_att_ck_mapping.md) · [Day index](../DAY_INDEX.md) · [Day 77 →](../077_day_baselines_and_anomalies/077_day_baselines_and_anomalies.md)
