# Day 109: Security Metrics and Measurement

[← Day 108](../day_108_configuration_drift/day_108_configuration_drift.md) · [Day index](../DAY_INDEX.md) · [Day 110 →](../day_110_project__secure_delivery_pipeline/day_110_project__secure_delivery_pipeline.md)

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

Metrics influence decisions. A good metric defines unit, population, time window, data quality, and action; a bad metric rewards gaming or hides uncertainty.

## Prerequisites

Complete Day 108. Work from a clean virtual environment and use only local synthetic fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using it
- run and modify all worked examples
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Design three synthetic metrics for test quality, detection review, and remediation without using real organizational data.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, destructive actions, persistence, or processing of private data.

## Lesson

### Vocabulary

A metric is a defined measurement. A denominator is the population used. Coverage measures what was observed. A leading indicator predicts work; a lagging indicator records outcome.

## Worked examples

### Example 1: Define a ratio

A metric must state numerator and denominator.

```python
passed = 18
total = 20
print(passed / total)
```

**What to observe:**

`0.9`, or 90% if reported clearly.

### Example 2: Name the population

A percentage without population is misleading.

```python
metric = {
    "name": "tests_passed",
    "population": "required checks",
    "window": "one commit",
}
print(metric)
```

**What to observe:**

The context travels with the number.

### Example 3: Add data quality

Missing telemetry affects confidence.

```python
metric["data_quality"] = "complete"
print(metric)
```

**What to observe:**

The quality field is explicit.

### Example 4: Avoid vanity metrics

A high count may not mean safer behavior.

```python
print({"metric": "alerts_closed", "warning": "closure speed can hide quality"})
```

**What to observe:**

The interpretation is cautious.

### Example 5: Attach action

Measurement should change a decision.

```python
metric["action"] = "review failed gates"
print(metric)
```

**What to observe:**

The metric has purpose.

## Execution trace

The metric definition identifies population, unit, time window, data quality, and decision; only then are values calculated and interpreted.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| count without denominator | progress is unclear | define population |
| optimize number | behavior is gamed | pair measures with review |
| missing equals zero | quality looks better | report missingness |
| no time window | trends mix periods | define window |
| metric equals security | complexity is hidden | state limitations |

## Security application

Use invented values and document that they are examples. Do not claim the metrics describe a real team or organization.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the evidence, output, edge case, and limitation requested by each question.

## Finish line

Run `python -m course_days.day109`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A security metric is a measurement contract tied to a decision, not a badge of safety.

## Limitations

Metrics can be biased, incomplete, and gamed; qualitative review remains essential.

[← Day 108](../day_108_configuration_drift/day_108_configuration_drift.md) · [Day index](../DAY_INDEX.md) · [Day 110 →](../day_110_project__secure_delivery_pipeline/day_110_project__secure_delivery_pipeline.md)
