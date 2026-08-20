# Day 80: Project: Mini Detection Pipeline

[← Day 79](../day_79_analyst_reporting/day_79_analyst_reporting.md) · [Day index](../DAY_INDEX.md) · [Day 81 →](../day_81_response_lifecycle/day_81_response_lifecycle.md)

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

The project composes telemetry schemas, normalization, enrichment, thresholds, mappings, triage, baselines, provenance, and reporting into a small defensive pipeline with honest limits.

## Prerequisites

Complete Day 79. Use only the local course fixtures, loopback services, and synthetic records described by the lesson.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using the tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state the trust boundary and residual risk
- complete the numbered cybersecurity exercises

## The problem

Build a local pipeline that ingests synthetic events, normalizes them, applies one detection rule, creates a triage item, and writes an evidence-based report.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, interception, exploit delivery, real-user profiling, or changes to systems you do not own.

## Lesson

### Vocabulary

A pipeline is an ordered transformation. A detection rule emits a signal. Triage adds context and disposition. A report preserves evidence and limitations.

## Worked examples

### Example 1: Define stages

A project is easier to debug when every stage has one purpose.

```python
stages = ["ingest", "normalize", "enrich", "detect", "triage", "report"]
print(" -> ".join(stages))
```

**What to observe:**

The pipeline is explicit.

### Example 2: Normalize an event

The event must carry provenance.

```python
event = {
    "event_type": "auth_failure",
    "source": "fixture",
    "actor": "student",
    "line": 2,
}
print(event)
```

**What to observe:**

A normalized synthetic event.

### Example 3: Apply a rule

A rule produces a signal, not a conclusion.

```python
signal = {"rule": "three-failures", "matched": True, "confidence": "low"}
print(signal)
```

**What to observe:**

The signal is cautious.

### Example 4: Create triage

Triage records evidence and next step.

```python
alert = {
    "signal": signal,
    "evidence": [event],
    "status": "new",
    "next_step": "review fixture",
}
print(alert)
```

**What to observe:**

The alert is actionable but bounded.

### Example 5: Write limitations

The report should prevent overinterpretation.

```python
report = {
    "scope": "synthetic only",
    "complete": True,
    "limitations": ["no identity proof", "no production context"],
}
print(report)
```

**What to observe:**

The report is transparent.

## Execution trace

The pipeline validates input, normalizes fields, enriches from local data, applies a bounded rule, creates a triage item, and writes a report with provenance, completeness, and limitations.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| pipeline drops raw reference | signal cannot be checked | retain evidence ids |
| enrichment becomes truth | context overrules observation | keep confidence |
| alert auto-escalates | false positive causes harm | require triage |
| no schema version | future data breaks | version events |
| no reset | fixtures and reports accumulate | document cleanup |

## Security application

The pipeline must use only repository fixtures, local lookup tables, finite inputs, and neutral labels. Its README must include threat model, tests, sample report, and reset.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples as a starting point, then record the requested output, edge case, and limitation.

## Finish line

Run `python -m course_days.day080`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A detection pipeline turns bounded observations into reviewable signals while preserving provenance and uncertainty at every stage.

## Limitations

This is not a SIEM, threat-intelligence platform, or real-world detection service; production needs governance, access control, retention, and monitoring.

[← Day 79](../day_79_analyst_reporting/day_79_analyst_reporting.md) · [Day index](../DAY_INDEX.md) · [Day 81 →](../day_81_response_lifecycle/day_81_response_lifecycle.md)
