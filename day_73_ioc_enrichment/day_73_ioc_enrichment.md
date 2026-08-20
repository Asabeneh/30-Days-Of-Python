# Day 73: IOC Enrichment and Provenance

[← Day 72](../day_72_log_normalization/day_72_log_normalization.md) · [Day index](../DAY_INDEX.md) · [Day 74 →](../day_74_detection_thresholds/day_74_detection_thresholds.md)

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

An indicator can be a domain, hash, address, or filename. Enrichment adds context, but it can also create privacy, accuracy, and false-confidence problems.

## Prerequisites

Complete Day 72. Use only the local course fixtures, loopback services, and synthetic records described by the lesson.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using the tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state the trust boundary and residual risk
- complete the numbered cybersecurity exercises

## The problem

Enrich synthetic indicators from a local lookup table and keep source, time, and confidence attached to each result.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, interception, exploit delivery, real-user profiling, or changes to systems you do not own.

## Lesson

### Vocabulary

An IOC is an observed indicator. Enrichment adds context. Provenance records source and time. Confidence describes evidence quality.

## Worked examples

### Example 1: Classify a candidate

A candidate shape is not a verdict.

```python
candidate = {"value": "example.invalid", "kind": "domain", "status": "candidate"}
print(candidate)
```

**What to observe:**

The label remains neutral.

### Example 2: Use local enrichment

A local table avoids contacting external services.

```python
lookup = {"example.invalid": {"owner": "training", "confidence": "high"}}
print(lookup.get(candidate["value"]))
```

**What to observe:**

Synthetic context is returned.

### Example 3: Attach provenance

The result should say where the context came from.

```python
result = {**candidate, **lookup[candidate["value"]], "source": "course-fixture"}
print(result)
```

**What to observe:**

The fields explain the enrichment.

### Example 4: Handle no result

Absence of enrichment is not evidence of safety.

```python
print({"value": "unknown.invalid", "status": "not_found", "safe": None})
```

**What to observe:**

The unknown state is explicit.

### Example 5: Bound cache

Repeated lookups should not grow without a policy.

```python
cache_policy = {"max_entries": 100, "ttl_seconds": 3600}
print(cache_policy)
```

**What to observe:**

Resource and staleness limits are visible.

## Execution trace

The indicator is parsed, looked up only in the approved local source, merged with provenance, and returned with a neutral status and confidence.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| enrichment equals malicious | context becomes accusation | retain candidate and confidence |
| external lookup by default | privacy and scope expand | use local fixtures or explicit approval |
| no timestamp | stale context looks current | record observation time |
| no source | result cannot be audited | preserve provenance |
| not found equals safe | blind spot becomes reassurance | use unknown |

## Security application

Use local synthetic indicators and a fixture lookup table. Do not resolve, scan, or query public reputation services.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples as a starting point, then record the requested output, edge case, and limitation.

## Finish line

Run `python -m course_days.day073`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Enrichment adds context to an observation; it does not create certainty or permission to act.

## Limitations

External data can be stale, biased, unavailable, or wrong, and enrichment may itself expose sensitive indicators.

[← Day 72](../day_72_log_normalization/day_72_log_normalization.md) · [Day index](../DAY_INDEX.md) · [Day 74 →](../day_74_detection_thresholds/day_74_detection_thresholds.md)
