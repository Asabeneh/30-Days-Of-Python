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

<!-- video-resources:start -->
## Video support

**Inline recommendation:** [Getting Started with Python in VS Code (Official Video)](https://www.youtube.com/watch?v=D2cwvpJSBX4).

- Watch [00:00–06:30: Python in VS Code setup](https://www.youtube.com/watch?v=D2cwvpJSBX4&t=0s) for **editor, interpreter, and workspace**. Then return to this lesson and run the local starter.
- Watch [06:30–08:27: Code navigation and debugging](https://www.youtube.com/watch?v=D2cwvpJSBX4&t=390s) for **navigation and debugger**. Then return to this lesson and run the local starter.
- Watch [08:27–10:19: Debugging](https://www.youtube.com/watch?v=D2cwvpJSBX4&t=507s) for **breakpoints and stepping**. Then return to this lesson and run the local starter.

Written alternative: [https://code.visualstudio.com/docs/python/python-tutorial](https://code.visualstudio.com/docs/python/python-tutorial).
<!-- video-resources:end -->

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

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested commands, produce the requested artifact, and record the edge case or limitation asked for by the exercise. Use [hints](practice/hints.md) only after a real attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Mental model

> A virtual environment isolates a project’s dependencies, while a reproducible install makes the same starting point available to another learner.

## Finish line

Run the starter, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.
