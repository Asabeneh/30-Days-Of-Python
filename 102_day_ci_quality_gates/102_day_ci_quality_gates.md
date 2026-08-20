# Day 102: CI Quality Gates

[← Day 101](../101_day_secure_sdlc/101_day_secure_sdlc.md) · [Day index](../DAY_INDEX.md) · [Day 103 →](../103_day_static_analysis/103_day_static_analysis.md)

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

Continuous integration makes quality checks repeatable on every change. A gate should be fast, explainable, and proportionate, while a failure should stop unsafe delivery rather than be ignored.

## Prerequisites

Complete Day 101. Work from a clean virtual environment and use only local synthetic fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using it
- run and modify all worked examples
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Design a local CI-like sequence that formats, lints, compiles, tests, checks links, and records artifacts.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, destructive actions, persistence, or processing of private data.

## Lesson

### Vocabulary

A quality gate is a required check. CI runs checks in an automated environment. An artifact is an output such as a test report. A false negative lets a defect pass.

## Worked examples

### Example 1: List gates

The gate sequence is a policy object.

```python
gates = ["format", "lint", "compile", "test", "links"]
print(gates)
```

**What to observe:**

The required checks are visible.

### Example 2: Represent a result

Each check needs status and evidence.

```python
result = {"name": "pytest", "status": "passed", "artifact": "test-report.txt"}
print(result)
```

**What to observe:**

The result is reviewable.

### Example 3: Fail closed

A failed required gate should not report success.

```python
required = ["lint", "tests"]
results = {"lint": "passed", "tests": "failed"}
print(all(results[name] == "passed" for name in required))
```

**What to observe:**

`False` blocks delivery.

### Example 4: Separate flaky from failed

A retry policy should not hide a persistent failure.

```python
print({"status": "flaky", "needs_review": True, "release": False})
```

**What to observe:**

The gate remains conservative.

### Example 5: Store safe artifacts

Reports should not contain secrets or private environment values.

```python
artifact_policy = {"tests": True, "environment_dump": False, "secrets": False}
print(artifact_policy)
```

**What to observe:**

The output policy is explicit.

## Execution trace

The pipeline runs deterministic checks, captures minimal artifacts, aggregates statuses, and refuses delivery when a required gate fails or is unknown.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| gate only locally | CI differs from developer | reproduce environment |
| ignore failure | unsafe change ships | fail closed |
| dump environment | secrets leak | minimize artifacts |
| flaky equals pass | defects hide | quarantine and review |
| too many slow checks | feedback is ignored | stage and prioritize |

## Security application

Run gates only on the course repository. Never upload private logs or credentials to a CI artifact.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the evidence, output, edge case, and limitation requested by each question.

## Finish line

Run `python -m course_days.day102`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A quality gate is a decision boundary: required evidence passes or delivery stops.

## Limitations

CI results can be wrong when dependencies, runners, tests, or configuration differ from production.

[← Day 101](../101_day_secure_sdlc/101_day_secure_sdlc.md) · [Day index](../DAY_INDEX.md) · [Day 103 →](../103_day_static_analysis/103_day_static_analysis.md)
