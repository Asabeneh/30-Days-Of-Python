# Day 108: Configuration Drift

[← Day 107](../day_107_cloud_identity_concepts/day_107_cloud_identity_concepts.md) · [Day index](../DAY_INDEX.md) · [Day 109 →](../day_109_security_metrics/day_109_security_metrics.md)

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

A secure configuration can become insecure after a manual change, deployment override, dependency update, or environment difference. Drift detection compares an approved baseline to effective state.

## Prerequisites

Complete Day 107. Work from a clean virtual environment and use only local synthetic fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using it
- run and modify all worked examples
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Compare synthetic baseline and runtime configuration, classify drift, and assign a review action.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, destructive actions, persistence, or processing of private data.

## Lesson

### Vocabulary

Drift is a difference from an approved state. Effective configuration is what the process actually uses. A baseline is a reviewed reference.

## Worked examples

### Example 1: Create a baseline

A baseline includes version and owner.

```python
baseline = {"version": 2, "debug": False, "body_limit": 1000000, "owner": "course"}
print(baseline)
```

**What to observe:**

The approved state is visible.

### Example 2: Read runtime state

Effective state may differ from source configuration.

```python
runtime = {"version": 2, "debug": True, "body_limit": 1000000}
print(runtime)
```

**What to observe:**

Runtime debug is drifted.

### Example 3: Compare keys

Each difference needs field and before/after values.

```python
changes = {
    k: (baseline[k], runtime.get(k)) for k in baseline if baseline[k] != runtime.get(k)
}
print(changes)
```

**What to observe:**

`debug` differs.

### Example 4: Classify severity

A change’s effect determines priority.

```python
finding = {"field": "debug", "severity": "high", "status": "needs_review"}
print(finding)
```

**What to observe:**

The drift is actionable.

### Example 5: Avoid auto-remediation

Report first when the fix could affect service.

```python
print({"remediate": False, "next": "owner review"})
```

**What to observe:**

The tool does not change the system.

## Execution trace

The auditor loads a versioned baseline, captures effective state, computes field-level differences, classifies impact, and sends a review item without silently changing configuration.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| source config only | override is missed | inspect effective state |
| auto-fix all drift | outage or data loss | report and approve |
| no version | baseline meaning is unclear | version it |
| ignore missing field | control disappears | mark unknown |
| log secrets | configuration leaks | redact |

## Security application

Use synthetic dictionaries and local files. Do not inspect or remediate real deployment configuration.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the evidence, output, edge case, and limitation requested by each question.

## Finish line

Run `python -m course_days.day108`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Drift detection compares approved intent with effective reality and makes change visible.

## Limitations

Configuration is dynamic and provider-specific; drift reports need owner review and deployment context.

[← Day 107](../day_107_cloud_identity_concepts/day_107_cloud_identity_concepts.md) · [Day index](../DAY_INDEX.md) · [Day 109 →](../day_109_security_metrics/day_109_security_metrics.md)
