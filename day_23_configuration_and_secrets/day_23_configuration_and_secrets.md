# Day 23: Configuration, Environment Variables, and Secrets

[← Day 22](../day_22_cli_design/day_22_cli_design.md) · [Day index](../DAY_INDEX.md) · [Day 24 →](../day_24_json__csv__and_sqlite/day_24_json__csv__and_sqlite.md)

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

Configuration changes between development, testing, and deployment. Secrets must be supplied through a controlled mechanism, not copied into source code or printed while debugging.

## Prerequisites

Complete Day 22 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 23

## The problem

The tool needs a timeout and a case identifier, while an optional API token must be present without ever appearing in a report.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Lesson

### Vocabulary

Configuration is non-code input that controls behavior. A **secret** is sensitive authentication material. A **default** is a fallback, not proof that a value is valid.

## Worked examples

### Example 1: Read a default

A harmless setting can use an explicit fallback.

```python
import os

timeout = int(os.getenv("APP_TIMEOUT", "3"))
print(timeout)
```

**What to observe:**

`3` when the variable is absent.

### Example 2: Validate configuration

Reject values outside the operational policy.

```python
def read_timeout(raw):
    value = int(raw)
    if not 1 <= value <= 60:
        raise ValueError("timeout must be 1..60 seconds")
    return value
```

**What to observe:**

A timeout of `0` or `61` fails early.

### Example 3: Detect a secret without printing it

Presence is often enough for diagnostics.

```python
token = os.getenv("TRAINING_TOKEN")
print({"token_present": token is not None})
```

**What to observe:**

`{'token_present': False}` or `True`; the token value is never printed.

### Example 4: Separate config from code

A dictionary makes the final configuration inspectable.

```python
config = {
    "timeout": read_timeout(os.getenv("APP_TIMEOUT", "3")),
    "case_id": os.getenv("CASE_ID", "training"),
}
print(config)
```

**What to observe:**

Only non-sensitive configuration appears.

### Example 5: Fail closed for required secrets

A tool that requires authentication should not silently continue without it.

```python
if token is None and require_token:
    raise RuntimeError("required token is missing")
```

**What to observe:**

The caller receives an explicit setup failure.

## Execution trace

The program reads environment text, converts it, enforces bounds, and stores a safe configuration object. Secret values remain outside logs, reports, and source control.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| secret in source | it enters Git history | use an external secret mechanism |
| `print(os.environ)` | all environment secrets leak | print selected safe metadata |
| default for a required token | authentication silently fails | fail closed |
| no bounds | timeout or batch becomes abusive | validate limits |
| configuration scattered | behavior is hard to audit | load once into a typed object |

## Security application

Use fake training values only. Add tests proving a token value is absent from output and that a timeout outside `1..60` is rejected.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run every requested command, create the requested artifact, and record the limitation the exercise asks you to name.

## Finish line

Run `python -m course_days.day023`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Configuration is input with policy; a secret’s presence is not permission to reveal or misuse it.

## Limitations

Environment variables can leak through process listings, CI logs, crash reports, and shell history. Production secret management needs platform controls.

[← Day 22](../day_22_cli_design/day_22_cli_design.md) · [Day index](../DAY_INDEX.md) · [Day 24 →](../day_24_json__csv__and_sqlite/day_24_json__csv__and_sqlite.md)
