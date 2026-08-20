# Day 39: Host Inventories and Baseline Data

[← Day 38](../day_38_async_i_o/day_38_async_i_o.md) · [Day index](../DAY_INDEX.md) · [Day 40 →](../day_40_project__host_baseline_auditor/day_40_project__host_baseline_auditor.md)

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

An inventory describes what a tool observed about a host or fixture at one point in time. Baselines help identify change, but only when collection scope, normalization, and comparison are clear.

## Prerequisites

Complete Day 38 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 39

## The problem

Create a local host-like inventory from synthetic data and compare two snapshots without claiming that a difference is malicious.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Lesson

### Vocabulary

An **inventory** is a structured list of observed properties. A **baseline** is a reference snapshot. **Drift** is a difference between observations.

## Worked examples

### Example 1: Model a host

A dictionary can represent a small inventory before a dataclass is introduced.

```python
host = {"name": "training-host", "os": "fixture", "services": ["python"]}
print(host)
```

**What to observe:**

The host is explicitly synthetic.

### Example 2: Normalize a service list

Sorting makes comparison deterministic.

```python
services = ["ssh", "python", "ssh"]
normalized = sorted(set(services))
print(normalized)
```

**What to observe:**

`['python', 'ssh']`

### Example 3: Compare snapshots

A set difference shows observed change.

```python
before = {"python", "ssh"}
after = {"python", "web"}
print("added", after - before)
print("removed", before - after)
```

**What to observe:**

`web` is added and `ssh` is removed.

### Example 4: Record collection scope

A baseline without scope is hard to interpret.

```python
snapshot = {"scope": "course fixture only", "observed": {"python"}}
print(snapshot["scope"])
```

**What to observe:**

The scope travels with the observation.

### Example 5: State confidence

A difference needs a review state, not an automatic accusation.

```python
finding = {"change": "service added", "status": "needs_review", "confidence": "medium"}
print(finding)
```

**What to observe:**

The change is a review item.

## Execution trace

Collection normalizes local observations into a snapshot; comparison computes differences; a human or policy decides what the difference means.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| baseline without date | change cannot be placed in time | record timestamp |
| normalize away detail | evidence is lost | keep raw plus comparison form |
| difference equals attack | drift is overinterpreted | use needs-review status |
| collect beyond scope | inventory becomes surveillance | define allowed properties |
| no baseline provenance | reference may be untrusted | record source and method |

## Security application

Use synthetic host dictionaries and repository fixtures. Do not enumerate the actual host, network, processes, or accounts beyond what the lesson explicitly permits.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run every requested command, create the requested artifact, and record the limitation the exercise asks you to name.

## Finish line

Run `python -m course_days.day039`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A baseline makes change visible; judgment and provenance determine what the change means.

## Limitations

Baselines can be incomplete, stale, or wrong. A difference is a lead for review, not a compromise verdict.

[← Day 38](../day_38_async_i_o/day_38_async_i_o.md) · [Day index](../DAY_INDEX.md) · [Day 40 →](../day_40_project__host_baseline_auditor/day_40_project__host_baseline_auditor.md)
