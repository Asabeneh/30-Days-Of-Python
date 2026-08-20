# Day 106: Containers and Isolation Concepts

[← Day 105](../105_day_secret_detection/105_day_secret_detection.md) · [Day index](../DAY_INDEX.md) · [Day 107 →](../107_day_cloud_identity_concepts/107_day_cloud_identity_concepts.md)

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

Containers package a process and its dependencies, but they are not magical security boundaries. Images, privileges, mounts, networks, and secrets still need explicit policy.

## Prerequisites

Complete Day 105. Work from a clean virtual environment and use only local synthetic fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using it
- run and modify all worked examples
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Describe a least-privilege local container configuration without running untrusted images or altering the host.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, destructive actions, persistence, or processing of private data.

## Lesson

### Vocabulary

An image is a packaged filesystem and metadata. A container is a running instance. A mount shares host data. Isolation reduces but does not eliminate risk.

## Worked examples

### Example 1: Name the image source

Source and digest matter for reproducibility.

```python
image = {"name": "course-app", "source": "local build", "digest": "reviewed"}
print(image)
```

**What to observe:**

The image provenance is visible.

### Example 2: Drop privileges

A process should not run as root without a reason.

```python
runtime = {"user": "non-root", "read_only_fs": True}
print(runtime)
```

**What to observe:**

The default is restrictive.

### Example 3: Limit mounts

Mounts cross the container-host boundary.

```python
mounts = [{"source": "training-output", "target": "/output", "read_only": False}]
print(mounts)
```

**What to observe:**

Only the intended directory is shared.

### Example 4: Disable unnecessary network

A local tool may not need outbound access.

```python
network = {"mode": "none", "reason": "fixture-only"}
print(network)
```

**What to observe:**

The capability is removed.

### Example 5: State residual risk

Isolation is a layer, not a guarantee.

```python
print({"unknown": ["kernel", "runtime", "image dependencies"]})
```

**What to observe:**

The report remains cautious.

## Execution trace

The deployment declares image provenance, user, filesystem, mounts, network, resources, and secrets; the runtime receives only capabilities required by the local task.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| image tag as provenance | tag can move | record digest/source |
| root by default | compromise impact grows | non-root |
| mount home directory | host data exposed | narrow mount |
| network by default | outbound scope expands | disable or allowlist |
| container equals sandbox | controls are overtrusted | defense in depth |

## Security application

Use diagrams or configuration snippets only; do not run unreviewed images or mount private host paths.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the evidence, output, edge case, and limitation requested by each question.

## Finish line

Run `python -m course_days.day106`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Isolation is a capability budget around a process, not an excuse to skip source, image, host, and network review.

## Limitations

Container security depends on runtime, kernel, orchestrator, image, and host configuration.

[← Day 105](../105_day_secret_detection/105_day_secret_detection.md) · [Day index](../DAY_INDEX.md) · [Day 107 →](../107_day_cloud_identity_concepts/107_day_cloud_identity_concepts.md)
