# Day 49: Network Baselines and Change Detection

[← Day 48](../048_day_rate_limits_and_retries/048_day_rate_limits_and_retries.md) · [Day index](../DAY_INDEX.md) · [Day 50 →](../050_day_project__local_service_monitor/050_day_project__local_service_monitor.md)

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

A baseline can make local service behavior easier to understand. It can also create false alarms when normal timing, DNS, or deployment changes are treated as threats.

## Prerequisites

Complete Day 48. Run the repository checks and use only the local fixtures and explicitly authorized loopback services.

## Outcomes

By the end of this lesson, you can:

- explain the protocol or security property in plain language
- run and modify every worked example
- test a normal, boundary, and failure case
- identify the trust boundary and residual risk
- connect the concept to the numbered cybersecurity exercises

## The problem

Compare two synthetic connection summaries and classify the difference as observed drift requiring review.

## Security boundary

Use synthetic data, local fixtures, and loopback-only demonstrations. This lesson does not authorize scanning, interception, credential use, remote command execution, or changes to systems you do not own.

## Lesson

### Vocabulary

A baseline is a reference observation. A feature is a measured property. Drift is a difference. A false positive is an alert for benign change.

## Worked examples

### Example 1: Create features

A baseline compares normalized features rather than raw log order.

```python
baseline = {"port": 8000, "protocol": "tcp", "latency_ms": 20}
print(baseline)
```

**What to observe:**

The feature set is explicit.

### Example 2: Normalize a measurement

Rounding can reduce noise, but should be documented.

```python
latencies = [19, 21, 20]
print(round(sum(latencies) / len(latencies), 1))
```

**What to observe:**

`20.0` milliseconds.

### Example 3: Compare fields

Each changed field gets its own finding.

```python
before = {"port": 8000}
after = {"port": 8080}
print({"field": "port", "before": before["port"], "after": after["port"]})
```

**What to observe:**

The difference is reviewable.

### Example 4: Add context

A deployment window can explain benign drift.

```python
context = {"change_window": True, "owner_note": "training update"}
print(context)
```

**What to observe:**

Context reduces overclaiming.

### Example 5: State confidence

A baseline finding should be a lead, not a verdict.

```python
print({"status": "needs_review", "confidence": "low"})
```

**What to observe:**

The label is neutral.

## Execution trace

The collector normalizes local observations, compares them to a dated baseline, attaches context, and reports changed or missing features without deciding intent.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| baseline never updated | normal change alerts forever | version and review it |
| raw timing comparison | noise creates alerts | define normalization |
| drift equals intrusion | evidence is overinterpreted | use needs-review |
| no collection scope | monitoring expands silently | list approved features |
| ignore missing data | blind spot becomes normal | report not observed |

## Security application

Use synthetic connection summaries and local fixtures only. Document the baseline date, feature definitions, review owner, and residual false-positive risk.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested local command, inspect its output, and record the limitation asked for by the exercise.

## Finish line

Run `python -m course_days.day049`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A baseline highlights change relative to a reference; it does not explain why the change occurred.

## Limitations

Baselines are sensitive to deployment, clock, configuration, and measurement quality.

[← Day 48](../048_day_rate_limits_and_retries/048_day_rate_limits_and_retries.md) · [Day index](../DAY_INDEX.md) · [Day 50 →](../050_day_project__local_service_monitor/050_day_project__local_service_monitor.md)
