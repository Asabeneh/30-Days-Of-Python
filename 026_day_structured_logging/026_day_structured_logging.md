# Day 26: Structured Logging, Redaction, and Audit Events

[Previous](../025_day_type_hints_and_static_checks/025_day_type_hints_and_static_checks.md) | [Next](../027_day_git_and_code_review/027_day_git_and_code_review.md)

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

Security engineering becomes dependable when its inputs, dependencies, failure behavior, and evidence are visible. This day builds one professional Python habit through a bounded local exercise.

## Prerequisites

Complete Day 25, keep [SETUP.md](../SETUP.md) available, and read [SAFETY_AND_LAB_RULES.md](../SAFETY_AND_LAB_RULES.md).

## Outcomes

You can explain the concept, trace the starter, make one controlled change, test a normal and negative case, and document one security limitation.

## The problem

A security utility often fails at a boundary: installation, command-line input, configuration, data serialization, logging, review, dependencies, or design assumptions. Today makes one such boundary explicit.

## Security boundary

Use only synthetic data and local files. Do not add real credentials, private evidence, public targets, or network access to the starter. Stop if the exercise leaves its documented scope.

## Core lesson

A structured log event is data with fields such as timestamp, action, outcome, and actor. Redaction is a policy, not a string replacement that can be applied carelessly.

```python
SENSITIVE_KEYS = {"password", "token", "secret"}


def redact(event):
    return {
        key: "[REDACTED]" if key in SENSITIVE_KEYS else value
        for key, value in event.items()
    }
```

Preserve enough context to investigate while minimizing sensitive data. Neutralize line breaks when writing human-readable logs, and separate audit events from debug output.

Security connection: logs can support detection and become a data-exposure channel at the same time.

### Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| Treating tools as magic | The learner cannot reproduce the result | State the interpreter, input, command, and expected output |
| Trusting representation | Malformed data enters the decision layer | Validate fields and types at the boundary |
| Logging everything | Secrets or private data appear in output | Minimize, redact, and test logging behavior |
| Confusing a control with proof | A checklist is called “secure” | Name the test and the residual risk |

## Practice

### Level 1 — Mechanical

Run the starter, predict one output, change one value, and explain the result.

### Level 2 — Applied

Build a small local utility that uses today's idea with synthetic input. State its contract and acceptance criteria before coding.

### Level 3 — Synthesis

Add one failure case, one test, and a short threat-model note naming an asset, boundary, threat, control, and residual risk.

Use [practice/prompts.md](practice/prompts.md), then progressive [hints](practice/hints.md), then explained [solutions](practice/solutions.md).

## Mental model

> Logs should help reconstruction without becoming a second place where secrets and personal data leak.

## Finish line

Run `python -m course_days.day026`, pass the phase tests, complete Levels 1 and 2, and write one edge-case note.
