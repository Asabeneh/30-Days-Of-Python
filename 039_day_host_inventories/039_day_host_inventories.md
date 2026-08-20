# Day 39: Host Inventories and Configuration Baselines

[Previous](../038_day_async_i_o/038_day_async_i_o.md) | [Next](../040_day_project__host_baseline_auditor/040_day_project__host_baseline_auditor.md)

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

Complete Day 38, keep [SETUP.md](../SETUP.md) available, and read [SAFETY_AND_LAB_RULES.md](../SAFETY_AND_LAB_RULES.md).

## Outcomes

You can explain the concept, trace the starter, make one controlled change, test a normal and negative case, and state what the local fixture does not represent.

## The problem

Host automation can collect useful evidence or cause unexpected load and data exposure. The problem today is to make the target, permission, resource, and cleanup assumptions explicit before writing a broader tool.

## Security boundary

Use only the repository and supplied synthetic fixtures. Do not inspect other users, services, university systems, employer systems, or public targets. Keep collection bounded and stop if scope changes.

## Core lesson

A baseline is a comparison model, not a verdict. Store the expected state with provenance, compare normalized records, and report added, removed, and changed values.

```python
def diff(expected: dict[str, str], observed: dict[str, str]) -> dict[str, list[str]]:
    return {
        "added": sorted(set(observed) - set(expected)),
        "removed": sorted(set(expected) - set(observed)),
    }
```

A difference can be a planned change, a measurement error, or a security issue. Ask for context.

Security connection: detection quality depends on a trustworthy baseline and a way to update it deliberately.

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

> A baseline compares observed configuration with an expected state without pretending that difference alone proves compromise.

## Finish line

Run `python -m course_days.day039`, pass the phase tests, complete Levels 1 and 2, and write one edge-case note.
