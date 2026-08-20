# Day 34: Subprocesses Without Shell Injection

[Previous](../033_day_paths_and_file_metadata/033_day_paths_and_file_metadata.md) | [Next](../035_day_users_and_permissions/035_day_users_and_permissions.md)

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

Complete Day 33, keep [SETUP.md](../SETUP.md) available, and read [SAFETY_AND_LAB_RULES.md](../SAFETY_AND_LAB_RULES.md).

## Outcomes

You can explain the concept, trace the starter, make one controlled change, test a normal and negative case, and state what the local fixture does not represent.

## The problem

Host automation can collect useful evidence or cause unexpected load and data exposure. The problem today is to make the target, permission, resource, and cleanup assumptions explicit before writing a broader tool.

## Security boundary

Use only the repository and supplied synthetic fixtures. Do not inspect other users, services, university systems, employer systems, or public targets. Keep collection bounded and stop if scope changes.

## Core lesson

`subprocess.run` can pass arguments as a list without asking a shell to interpret them.

```python
import subprocess

result = subprocess.run(
    ["python", "--version"], capture_output=True, text=True, timeout=3, check=True
)
```

`check=True` turns a non-zero exit into an exception; `timeout` bounds waiting. Never concatenate untrusted text into a shell command, and never use `shell=True` as a shortcut for input handling.

Security connection: allowlisting a program and its arguments is safer than trying to remove dangerous characters from a free-form command.

### Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| Assuming a name proves identity | A process or file is attributed without evidence | Record the exact observation and its limits |
| Using free-form commands | Shell metacharacters change behavior | Pass argument lists and allowlist programs |
| Ignoring limits | A collector can run forever or consume memory | Add bounds, timeouts, and cancellation |
| Treating differences as verdicts | A baseline change is called compromise | Report the difference and seek context |

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested commands, produce the requested artifact, and record the edge case or limitation asked for by the exercise. Use [hints](practice/hints.md) only after a real attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Mental model

> A subprocess boundary is safer when arguments are separated, programs are allowlisted, and timeouts are enforced.

## Finish line

Run the starter, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.
