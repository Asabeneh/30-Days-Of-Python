# Day 23: Configuration, Environment Variables, and Secret Boundaries

[Previous](../022_day_cli_design/022_day_cli_design.md) | [Next](../024_day_json__csv__and_sqlite/024_day_json__csv__and_sqlite.md)

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

Complete Day 22, keep [SETUP.md](../SETUP.md) available, and read [SAFETY_AND_LAB_RULES.md](../SAFETY_AND_LAB_RULES.md).

## Outcomes

You can explain the concept, trace the starter, make one controlled change, test a normal and negative case, and document one security limitation.

## The problem

A security utility often fails at a boundary: installation, command-line input, configuration, data serialization, logging, review, dependencies, or design assumptions. Today makes one such boundary explicit.

## Security boundary

Use only synthetic data and local files. Do not add real credentials, private evidence, public targets, or network access to the starter. Stop if the exercise leaves its documented scope.

## Core lesson

Configuration is behavior data; a secret is an access capability. They may both arrive through environment variables, but they should not be treated the same way.

```python
import os

timeout = int(os.environ.get("APP_TIMEOUT", "5"))
api_key = os.environ.get("APP_API_KEY")
```

The default timeout is visible and testable. The key is optional in a local fixture and must never be printed. Validate configuration at startup and fail with a safe message.

Security connection: `.env` files and shell history can leak. The course uses fake values and teaches rotation concepts rather than asking learners to paste real keys.

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

> Configuration changes behavior; secrets grant access, so they must be separated, minimized, and kept out of source control.

## Finish line

Run the starter, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.
