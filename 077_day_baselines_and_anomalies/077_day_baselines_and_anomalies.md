# Day 77: Baselines and Anomaly Reasoning

[← Day 76](../076_day_alert_triage/076_day_alert_triage.md) · [Day index](../DAY_INDEX.md) · [Day 78 →](../078_day_threat_intelligence_provenance/078_day_threat_intelligence_provenance.md)

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

An anomaly is a deviation from a model, not proof of maliciousness. Baselines need a time window, feature definition, missing-data policy, and a plan for normal change.

## Prerequisites

Complete Day 76. Use only the local course fixtures, loopback services, and synthetic records described by the lesson.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using the tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state the trust boundary and residual risk
- complete the numbered cybersecurity exercises

## The problem

Compute a simple synthetic baseline and flag a value for review while preserving the model’s assumptions.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, interception, exploit delivery, real-user profiling, or changes to systems you do not own.

## Lesson

### Vocabulary

A baseline summarizes normal reference data. An anomaly score measures deviation. A false positive is benign deviation. Concept drift means normal behavior changes over time.

## Worked examples

### Example 1: Compute an average

A simple baseline starts with a transparent statistic.

```python
values = [10, 11, 9, 10]
mean = sum(values) / len(values)
print(mean)
```

**What to observe:**

`10.0`

### Example 2: Measure deviation

The difference is a signal, not a verdict.

```python
observed = 15
print(observed - mean)
```

**What to observe:**

A deviation of 5.

### Example 3: Choose a rule

The rule must name its threshold.

```python
threshold = 3
print(abs(observed - mean) > threshold)
```

**What to observe:**

`True` for review.

### Example 4: Handle missing data

No sample should not silently become zero.

```python
sample = None
print({"status": "not_observed" if sample is None else "observed"})
```

**What to observe:**

Missingness is explicit.

### Example 5: Document drift

A baseline needs refresh and review.

```python
model = {"window": "training fixture", "refresh": "manual review", "owner": "student"}
print(model)
```

**What to observe:**

The model lifecycle is visible.

## Execution trace

The detector defines a reference window, computes a feature, measures deviation, applies a threshold, and emits a review signal with model version and missing-data status.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| anomaly equals attack | benign change is accused | use needs-review |
| no window | old behavior dominates | define a reference period |
| missing equals normal | blind spot disappears | mark unknown |
| no refresh | drift creates noise | version and review model |
| feature leaks privacy | unnecessary collection | minimize and aggregate |

## Security application

Use synthetic counts and no real user behavior. Document the feature, window, threshold, false-positive risk, and reset procedure.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples as a starting point, then record the requested output, edge case, and limitation.

## Finish line

Run `python -m course_days.day077`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> An anomaly detector identifies difference from a model; human or policy review determines meaning.

## Limitations

Simple statistics can fail under seasonality, dependence, adversarial adaptation, and changing operations.

[← Day 76](../076_day_alert_triage/076_day_alert_triage.md) · [Day index](../DAY_INDEX.md) · [Day 78 →](../078_day_threat_intelligence_provenance/078_day_threat_intelligence_provenance.md)
