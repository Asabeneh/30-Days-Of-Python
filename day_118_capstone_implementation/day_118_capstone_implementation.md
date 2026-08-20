# Day 118: Capstone Implementation

[← Day 117](../day_117_capstone_planning/day_117_capstone_planning.md) · [Day index](../DAY_INDEX.md) · [Day 119 →](../day_119_capstone_security_review/day_119_capstone_security_review.md)

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

Implementation is where design decisions meet real code. The learner should build incrementally, keep the core testable, and preserve the evidence needed for a final demonstration.

## Prerequisites

Complete Day 117. Work from a clean virtual environment and use only local synthetic fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using it
- run and modify all worked examples
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Implement the capstone in small vertical slices and record testable outputs at each milestone.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, destructive actions, persistence, or processing of private data.

## Lesson

### Vocabulary

A vertical slice crosses input, core behavior, and output. A checkpoint is evidence at a milestone. Refactoring changes structure while preserving behavior.

## Worked examples

### Example 1: Build the first slice

A tiny end-to-end path reveals integration mistakes early.

```python
slice = {"input": "one fixture event", "decision": "review", "output": "one report row"}
print(slice)
```

**What to observe:**

The first slice is demonstrable.

### Example 2: Add a failing test

A test can state the next behavior before implementation.

```python
expected = {"invalid_severity": "rejected"}
print(expected)
```

**What to observe:**

The contract guides code.

### Example 3: Keep a checkpoint

Save outputs after each milestone.

```python
checkpoint = {"milestone": "parser", "tests": 4, "artifact": "sample-report.json"}
print(checkpoint)
```

**What to observe:**

Progress is measurable.

### Example 4: Refactor safely

A refactor should preserve observable contracts.

```python
before = {"status": 200, "body_fields": ["case_id"]}
after = before.copy()
print(before == after)
```

**What to observe:**

The expected behavior remains equal.

### Example 5: Document a limitation

Implementation notes should prevent misuse.

```python
print({"limitation": "fixture-only", "not": "production detector"})
```

**What to observe:**

The scope remains visible.

## Execution trace

The learner implements one slice, writes tests, records output, refactors under test protection, and documents limitations before adding the next feature.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| build all layers at once | debugging is overwhelming | vertical slices |
| no tests until end | regressions hide | test each milestone |
| copy output as proof | behavior is not understood | explain and reproduce |
| ignore cleanup | artifacts accumulate | reset after each run |
| overbuild | capstone loses focus | cut scope |

## Security application

Use the planned local fixtures and safe modules. Do not expand the capstone into scanning, credential handling, or remote automation.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the evidence, output, edge case, and limitation requested by each question.

## Finish line

Run `python -m course_days.day118`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Implementation is a sequence of small, tested, explainable slices that preserve the capstone argument.

## Limitations

A local capstone can contain defects; review and retesting are part of the work.

[← Day 117](../day_117_capstone_planning/day_117_capstone_planning.md) · [Day index](../DAY_INDEX.md) · [Day 119 →](../day_119_capstone_security_review/day_119_capstone_security_review.md)
