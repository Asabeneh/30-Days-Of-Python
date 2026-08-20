# Day 21: Virtual Environments and Reproducible Installs

[Previous](../020_day_project__log_triage_cli/020_day_project__log_triage_cli.md) | [Next](../022_day_cli_design/022_day_cli_design.md)

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

Complete Day 20, keep [SETUP.md](../SETUP.md) available, and read [SAFETY_AND_LAB_RULES.md](../SAFETY_AND_LAB_RULES.md).

## Outcomes

You can explain the concept, trace the starter, make one controlled change, test a normal and negative case, and document one security limitation.

## The problem

A security utility often fails at a boundary: installation, command-line input, configuration, data serialization, logging, review, dependencies, or design assumptions. Today makes one such boundary explicit.

## Security boundary

Use only synthetic data and local files. Do not add real credentials, private evidence, public targets, or network access to the starter. Stop if the exercise leaves its documented scope.

## Core lesson

The interpreter used by a project is part of the project’s assumptions. A virtual environment creates a local place for packages and scripts, but it does not make untrusted packages safe automatically.

```text
repository → .venv → installed tools → reproducible command
```

Record the Python version and install command. Prefer `python -m pip` so the pip process belongs to the interpreter you selected. A lock or constraints file improves repeatability, but it still needs review and updates.

Security connection: isolation limits accidental coupling. It does not replace dependency review, least privilege, or a clean source of packages.

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

> A virtual environment isolates a project’s dependencies, while a reproducible install makes the same starting point available to another learner.

## Finish line

Run `python -m course_days.day021`, pass the phase tests, complete Levels 1 and 2, and write one edge-case note.
