# Day 74: Detection Thresholds and Evaluation

[← Day 73](../day_73_ioc_enrichment/day_73_ioc_enrichment.md) · [Day index](../DAY_INDEX.md) · [Day 75 →](../day_75_mitre_att_ck_mapping/day_75_mitre_att_ck_mapping.md)

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

A detection rule is a policy over incomplete telemetry. Thresholds control false positives and false negatives, so a learner should evaluate them against labeled synthetic fixtures instead of trusting intuition.

## Prerequisites

Complete Day 73. Use only the local course fixtures, loopback services, and synthetic records described by the lesson.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using the tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state the trust boundary and residual risk
- complete the numbered cybersecurity exercises

## The problem

Choose and evaluate a threshold for synthetic failed-login events, then explain what the metric does not show.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, interception, exploit delivery, real-user profiling, or changes to systems you do not own.

## Lesson

### Vocabulary

A threshold is a rule boundary. A true positive matches a labeled condition. A false positive alerts on benign data. Recall and precision summarize different error trade-offs.

## Worked examples

### Example 1: Count events

A simple detector starts with observable counts.

```python
events = ["failed", "failed", "ok"]
failures = events.count("failed")
print(failures)
```

**What to observe:**

`2` failures.

### Example 2: Apply a threshold

The threshold turns count into an alert decision.

```python
threshold = 3
print(failures >= threshold)
```

**What to observe:**

`False` for two failures.

### Example 3: Create labels

Evaluation requires an expected label in synthetic data.

```python
cases = [{"alert": True, "expected": True}, {"alert": True, "expected": False}]
print(cases)
```

**What to observe:**

The two cases support error counting.

### Example 4: Count errors

Confusion-matrix counts make trade-offs visible.

```python
tp, fp, fn, tn = 1, 1, 0, 2
print({"tp": tp, "fp": fp, "fn": fn, "tn": tn})
```

**What to observe:**

The outcomes are explicit.

### Example 5: State threshold limits

A rule may miss slow or distributed behavior.

```python
print(
    {"blind_spot": "below-threshold distributed activity", "status": "known limitation"}
)
```

**What to observe:**

The detector is not overclaimed.

## Execution trace

The detector aggregates bounded events, applies a threshold, compares output with synthetic labels, counts errors, and documents blind spots before deployment.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| threshold from intuition | false alarms or misses | evaluate labeled fixtures |
| precision only | misses are ignored | examine recall too |
| label is attacker truth | synthetic label is overtrusted | document labeling assumptions |
| no time window | counts accumulate forever | define window and reset |
| alert equals incident | automation overreacts | require triage |

## Security application

Use only synthetic labeled fixtures. Do not tune a detector against real people or claim its threshold identifies attackers.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples as a starting point, then record the requested output, edge case, and limitation.

## Finish line

Run `python -m course_days.day074`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A detection threshold is a policy that trades false positives and negatives under a defined window and dataset.

## Limitations

Metrics depend on labels, distribution, drift, and operational cost; they are not universal quality scores.

[← Day 73](../day_73_ioc_enrichment/day_73_ioc_enrichment.md) · [Day index](../DAY_INDEX.md) · [Day 75 →](../day_75_mitre_att_ck_mapping/day_75_mitre_att_ck_mapping.md)
