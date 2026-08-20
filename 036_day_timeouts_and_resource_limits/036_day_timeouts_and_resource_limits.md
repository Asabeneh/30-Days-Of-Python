# Day 36: Timeouts, Signals, and Resource Limits

[Previous](../035_day_users_and_permissions/035_day_users_and_permissions.md) | [Next](../037_day_processes__threads__and_queues/037_day_processes__threads__and_queues.md)

## Table of Contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Core lesson](#core-lesson)
- [Common mistakes](#common-mistakes)
- [Practice](#practice)
- [Mental model](#mental-model)
- [Finish line](#finish-line)

## Why this lesson exists

A Python security tool interacts with a host that has processes, permissions, paths, resource limits, and concurrent work. This lesson makes one host-level boundary visible and testable.

## Prerequisites

Complete Day 35, keep [SETUP.md](../SETUP.md) available, and read [SAFETY_AND_LAB_RULES.md](../SAFETY_AND_LAB_RULES.md).

## Outcomes

You can explain the concept, trace the starter, make one controlled change, test a normal and negative case, and state what the local fixture does not represent.

## The problem

Host automation can collect useful evidence or cause unexpected load and data exposure. The problem today is to make the target, permission, resource, and cleanup assumptions explicit before writing a broader tool.

## Security boundary

Use only the repository and supplied synthetic fixtures. Do not inspect other users, services, university systems, employer systems, or public targets. Keep collection bounded and stop if scope changes.

## Core lesson

A timeout is a policy decision about how long a task may consume resources. It is not a guarantee that every child process has stopped unless the design handles cleanup.

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=2) as pool:
    future = pool.submit(lambda: "done")
    print(future.result(timeout=2))
```

Handle timeout, cancellation, and cleanup paths. Avoid swallowing the timeout and reporting a successful empty result.

Security connection: bounded work protects the analyst workstation and the service being observed.

### Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| Assuming a name proves identity | A process or file is attributed without evidence | Record the exact observation and its limits |
| Using free-form commands | Shell metacharacters change behavior | Pass argument lists and allowlist programs |
| Ignoring limits | A collector can run forever or consume memory | Add bounds, timeouts, and cancellation |
| Treating differences as verdicts | A baseline change is called compromise | Report the difference and seek context |

## Practice

### Level 1 — Mechanical

Run the starter, predict one output, change one input, and explain the result.

### Level 2 — Applied

Build a local fixture utility with a documented maximum scope and at least one rejection test.

### Level 3 — Synthesis

Add a timeout, resource bound, or evidence limitation and explain how it changes the tool's safety.

Use [practice/prompts.md](practice/prompts.md), then [hints](practice/hints.md), then [solutions](practice/solutions.md).

## Mental model

> A tool that cannot stop safely is an availability risk, even when its intended task is defensive.

## Finish line

Run `python -m course_days.day036`, pass the phase tests, complete Levels 1 and 2, and write one edge-case note.
