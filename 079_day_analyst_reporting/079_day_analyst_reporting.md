# Day 79: Analyst Reporting and Evidence-Based Writing

[← Day 78](../078_day_threat_intelligence_provenance/078_day_threat_intelligence_provenance.md) · [Day index](../DAY_INDEX.md) · [Day 80 →](../080_day_project__mini_detection_pipeline/080_day_project__mini_detection_pipeline.md)

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

A security report must let another person reproduce the reasoning. Separating observation, analysis, assessment, action, and limitation reduces accidental overclaiming.

## Prerequisites

Complete Day 78. Use only the local course fixtures, loopback services, and synthetic records described by the lesson.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using the tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state the trust boundary and residual risk
- complete the numbered cybersecurity exercises

## The problem

Write a short synthetic alert report that distinguishes facts from interpretation and names the next authorized step.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, interception, exploit delivery, real-user profiling, or changes to systems you do not own.

## Lesson

### Vocabulary

An observation is what was recorded. Analysis connects observations. Assessment states a cautious interpretation. A limitation identifies missing or weak evidence.

## Worked examples

### Example 1: Write an observation

Use neutral, timestamped language.

```python
observation = (
    "Three failed logins occurred in the training fixture between 10:00 and 10:02 UTC."
)
print(observation)
```

**What to observe:**

The sentence states a bounded fact.

### Example 2: Write analysis

Analysis explains why the fact matters without inventing a person.

```python
analysis = "The count crosses the training rule threshold; the fixture has no identity validation."
print(analysis)
```

**What to observe:**

The uncertainty remains visible.

### Example 3: Write assessment

Use confidence and scope.

```python
assessment = {
    "status": "needs_review",
    "confidence": "low",
    "scope": "synthetic fixture",
}
print(assessment)
```

**What to observe:**

The conclusion is limited.

### Example 4: Name next step

The action must be authorized and concrete.

```python
next_step = "review the local timeline and confirm fixture provenance"
print(next_step)
```

**What to observe:**

The next step is bounded.

### Example 5: List limitations

A report is stronger when it says what it cannot show.

```python
limitations = ["no real identity data", "no endpoint context", "synthetic timestamps"]
print(limitations)
```

**What to observe:**

The reader can judge confidence.

## Execution trace

The report moves from source-backed observation to analysis, cautious assessment, authorized next step, and limitations. A reader can tell fact from inference.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| adjective as evidence | ‘suspicious’ replaces facts | write observable detail |
| no source | claim cannot be checked | cite case and line |
| certainty language | thin evidence becomes verdict | state confidence |
| action without authorization | report triggers harm | name allowed next step |
| omit limitations | reader overtrusts result | include blind spots |

## Security application

Use a synthetic case and local references. Do not write accusations about real people, organizations, or public indicators.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples as a starting point, then record the requested output, edge case, and limitation.

## Finish line

Run `python -m course_days.day079`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Good reporting preserves the chain from observation to interpretation and makes uncertainty actionable.

## Limitations

Writing quality cannot repair bad collection, biased labels, or missing evidence; it makes those gaps visible.

[← Day 78](../078_day_threat_intelligence_provenance/078_day_threat_intelligence_provenance.md) · [Day index](../DAY_INDEX.md) · [Day 80 →](../080_day_project__mini_detection_pipeline/080_day_project__mini_detection_pipeline.md)
