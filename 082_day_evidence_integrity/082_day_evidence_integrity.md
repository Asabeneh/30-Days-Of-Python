# Day 82: Evidence Integrity and Handling

[← Day 81](../081_day_response_lifecycle/081_day_response_lifecycle.md) · [Day index](../DAY_INDEX.md) · [Day 83 →](../083_day_filesystem_timelines/083_day_filesystem_timelines.md)

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

Evidence must remain attributable and unchanged enough for another reviewer to check it. Hashes, manifests, access records, and working copies support integrity but do not create a legal chain of custody by themselves.

## Prerequisites

Complete Day 81. Use only the local fixtures and explicit loopback assessment scope supplied by the course.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using a tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Create a local manifest for synthetic files and record who, when, where, and how each item was handled.

## Security boundary

This lesson is educational and authorized-lab-only. It does not authorize public scanning, credential guessing, exploitation, interception, persistence, or changes to systems you do not own.

## Lesson

### Vocabulary

Integrity means detecting change. Provenance records origin and transformation. A working copy is an analysis copy. A manifest lists evidence and digests.

## Worked examples

### Example 1: Hash a file

A digest detects later content changes.

```python
import hashlib

data = b"synthetic evidence"
print(hashlib.sha256(data).hexdigest()[:12])
```

**What to observe:**

A repeatable digest prefix.

### Example 2: Create a manifest

The manifest binds names to digests and scope.

```python
manifest = {"case": "training-82", "files": {"event.txt": "digest"}, "scope": "local"}
print(manifest)
```

**What to observe:**

The evidence set is explicit.

### Example 3: Record handling

Every transfer or transformation should be recorded.

```python
log = {"item": "event.txt", "actor": "student", "action": "copied", "time": "now"}
print(log)
```

**What to observe:**

The handling event is visible.

### Example 4: Verify before analysis

Work should stop when a digest changes unexpectedly.

```python
expected = "abc"
actual = "xyz"
print({"integrity_ok": expected == actual})
```

**What to observe:**

`False` means review is required.

### Example 5: Separate original and copy

Analysis should not overwrite the source.

```python
paths = {"original": "evidence/original", "working": "analysis/copy"}
print(paths)
```

**What to observe:**

The handling boundary is clear.

## Execution trace

The item is acquired into a controlled location, hashed, entered in the manifest, copied for analysis, and rechecked before conclusions are written.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| hash after editing | original state is unknown | hash at acquisition |
| store digest beside attacker-controlled file | baseline can change | protect manifest |
| no handling log | provenance is unclear | record actions and times |
| analyze original | evidence is altered | use a working copy |
| call hash legal proof | technical control overclaimed | state limits |

## Security application

Use synthetic files and a local manifest. Do not collect, copy, or analyze private evidence.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the requested evidence, expected behavior, edge case, and limitation.

## Finish line

Run `python -m course_days.day082`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Evidence integrity is a set of repeatable controls that make change and handling visible.

## Limitations

Integrity controls do not prove truth, identity, or legal admissibility without organizational process.

[← Day 81](../081_day_response_lifecycle/081_day_response_lifecycle.md) · [Day index](../DAY_INDEX.md) · [Day 83 →](../083_day_filesystem_timelines/083_day_filesystem_timelines.md)
