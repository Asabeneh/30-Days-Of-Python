# Day 78: Threat Intelligence Provenance

[← Day 77](../day_77_baselines_and_anomalies/day_77_baselines_and_anomalies.md) · [Day index](../DAY_INDEX.md) · [Day 79 →](../day_79_analyst_reporting/day_79_analyst_reporting.md)

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

Threat intelligence is useful only when analysts can judge source, freshness, confidence, and handling restrictions. Copying an indicator without context creates false authority.

## Prerequisites

Complete Day 77. Use only the local course fixtures, loopback services, and synthetic records described by the lesson.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using the tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state the trust boundary and residual risk
- complete the numbered cybersecurity exercises

## The problem

Represent a synthetic intelligence report and decide whether its indicator is suitable for a local training rule.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, interception, exploit delivery, real-user profiling, or changes to systems you do not own.

## Lesson

### Vocabulary

Intelligence is analyzed information. Provenance records source and transformation. Freshness describes age. Confidence reflects evidence quality. Handling restrictions limit sharing.

## Worked examples

### Example 1: Model a report

Start with source and observation time.

```python
report = {
    "source": "training-lab",
    "observed_at": "2026-08-20",
    "indicator": "example.invalid",
}
print(report)
```

**What to observe:**

The origin is explicit.

### Example 2: Add confidence

Confidence is not the same as severity.

```python
report.update({"confidence": "medium", "severity": "unknown"})
print(report)
```

**What to observe:**

The fields remain separate.

### Example 3: Track transformation

A normalized indicator should say what changed.

```python
report["transformation"] = "lowercase domain for comparison"
print(report)
```

**What to observe:**

The transformation is auditable.

### Example 4: Apply freshness

Old data may need review before use.

```python
report["freshness"] = {"status": "training-only", "expires": "documented"}
print(report)
```

**What to observe:**

Freshness policy is visible.

### Example 5: Respect handling

A source restriction is part of safe use.

```python
report["handling"] = "do not redistribute"
print(report["handling"])
```

**What to observe:**

The learner sees a sharing boundary.

## Execution trace

The analyst records source, time, indicator, transformation, confidence, freshness, and handling before deciding whether a local rule can use the information.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| source name as proof | provenance is shallow | record method and time |
| old indicator as current | stale detection | apply freshness |
| confidence equals truth | uncertainty disappears | preserve confidence |
| redistribute restricted data | handling breach | respect restrictions |
| query indicator externally | scope and privacy expand | use local fixtures |

## Security application

Use only synthetic reports and indicators. Do not paste private intelligence or query public reputation services.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples as a starting point, then record the requested output, edge case, and limitation.

## Finish line

Run `python -m course_days.day078`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Intelligence is contextual evidence with provenance and handling rules, not a magic label.

## Limitations

Sources can be wrong, biased, stale, compromised, or unsuitable for the learner’s legal and operational context.

[← Day 77](../day_77_baselines_and_anomalies/day_77_baselines_and_anomalies.md) · [Day index](../DAY_INDEX.md) · [Day 79 →](../day_79_analyst_reporting/day_79_analyst_reporting.md)
