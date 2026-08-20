# Day 104: SBOM and Provenance

[← Day 103](../day_103_static_analysis/day_103_static_analysis.md) · [Day index](../DAY_INDEX.md) · [Day 105 →](../day_105_secret_detection/day_105_secret_detection.md)

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

Delivery teams need to know which components produced an artifact. An SBOM-like inventory and provenance record help answer what was built, from which source, with which tools, and under which review.

## Prerequisites

Complete Day 103. Work from a clean virtual environment and use only local synthetic fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using it
- run and modify all worked examples
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Create a small provenance record for a synthetic course artifact without claiming that metadata proves safety.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, destructive actions, persistence, or processing of private data.

## Lesson

### Vocabulary

An SBOM inventories software components. Provenance records origin and build steps. An artifact is a produced file or image. Reproducibility means rebuilding from the same declared inputs.

## Worked examples

### Example 1: List components

The inventory begins with names and versions.

```python
sbom = [{"name": "python", "version": "3.x"}, {"name": "course-tool", "version": "1.0"}]
print(sbom)
```

**What to observe:**

The components are named.

### Example 2: Record source

Source commit links output to a change.

```python
provenance = {"commit": "abc123", "branch": "course-redesign"}
print(provenance)
```

**What to observe:**

The source reference is explicit.

### Example 3: Record builder

The environment affects output.

```python
provenance.update({"builder": "local-ci", "python": "3.x"})
print(provenance)
```

**What to observe:**

The builder context is visible.

### Example 4: Hash an artifact

A digest identifies the bytes that were produced.

```python
import hashlib

print(hashlib.sha256(b"training-artifact").hexdigest()[:12])
```

**What to observe:**

A stable fingerprint is recorded.

### Example 5: State unknowns

Inventory is evidence, not a security guarantee.

```python
print({"unknown": ["transitive build behavior", "future vulnerability"]})
```

**What to observe:**

The report remains honest.

## Execution trace

The artifact is linked to source, builder, components, build steps, and digest; reviewers can compare records without treating the record as proof of a harmless supply chain.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| only direct dependencies | transitive code is missed | inventory full graph |
| no source commit | artifact cannot be traced | record provenance |
| hash equals trust | origin is overclaimed | protect source and process |
| stale SBOM | current artifact differs | generate per build |
| include secrets | metadata leaks | sanitize records |

## Security application

Use synthetic artifact names and local records. Do not publish private build metadata or install unreviewed packages.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the evidence, output, edge case, and limitation requested by each question.

## Finish line

Run `python -m course_days.day104`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Provenance makes a build’s inputs and steps inspectable; it does not guarantee every component is secure.

## Limitations

SBOM formats, signing, and provenance standards need organizational tooling and verification.

[← Day 103](../day_103_static_analysis/day_103_static_analysis.md) · [Day index](../DAY_INDEX.md) · [Day 105 →](../day_105_secret_detection/day_105_secret_detection.md)
