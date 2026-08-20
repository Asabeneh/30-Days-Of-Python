# Day 110: Project: Secure Delivery Pipeline

[← Day 109](../109_day_security_metrics/109_day_security_metrics.md) · [Day index](../DAY_INDEX.md) · [Day 111 →](../111_day_security_tool_architecture/111_day_security_tool_architecture.md)

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

This project composes SDLC requirements, CI gates, static analysis, provenance, secret detection, isolation, identity, drift, and metrics into a delivery decision that can be inspected and repeated.

## Prerequisites

Complete Day 109. Work from a clean virtual environment and use only local synthetic fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using it
- run and modify all worked examples
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Design a local pipeline that either produces a reviewed artifact or stops with a clear reason.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, destructive actions, persistence, or processing of private data.

## Lesson

### Vocabulary

A delivery pipeline is a sequence of build and verification stages. A release decision is the final policy result. Evidence artifacts support review.

## Worked examples

### Example 1: Define stages

The pipeline should show where controls run.

```python
stages = ["requirements", "tests", "lint", "secrets", "sbom", "artifact", "review"]
print(stages)
```

**What to observe:**

The sequence is visible.

### Example 2: Aggregate gates

A required failure blocks release.

```python
gates = {"tests": True, "lint": True, "secrets": False}
print(all(gates.values()))
```

**What to observe:**

`False` blocks delivery.

### Example 3: Create provenance

The artifact needs source and component context.

```python
artifact = {"commit": "abc123", "components": ["python"], "digest": "reviewed"}
print(artifact)
```

**What to observe:**

The output is traceable.

### Example 4: Review drift

Effective configuration is part of delivery evidence.

```python
print({"config_baseline": "v2", "drift": False})
```

**What to observe:**

The pipeline records configuration state.

### Example 5: Write decision

A decision must say why it passed or stopped.

```python
decision = {"release": False, "reason": "secret candidate requires review"}
print(decision)
```

**What to observe:**

The stop is explainable.

## Execution trace

The pipeline loads requirements, runs checks, captures artifacts, evaluates provenance/configuration/secrets, and returns a release decision with reason and owner.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| gate only tests | supply chain is ignored | include provenance and secrets |
| secrets report value | leak worsens | redact |
| pass on unknown | blind spot becomes release | fail closed or mark blocked |
| no owner | blocked work stalls | assign remediation |
| artifact without source | cannot reproduce | record commit/build |

## Security application

Use local tools and synthetic records. Do not build a production deployment or upload private pipeline artifacts.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the evidence, output, edge case, and limitation requested by each question.

## Finish line

Run `python -m course_days.day110`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Secure delivery is evidence aggregation plus a policy decision; a green test suite is only one input.

## Limitations

A local pipeline does not prove production security, compliant provenance, or absence of malicious dependencies.

[← Day 109](../109_day_security_metrics/109_day_security_metrics.md) · [Day index](../DAY_INDEX.md) · [Day 111 →](../111_day_security_tool_architecture/111_day_security_tool_architecture.md)
