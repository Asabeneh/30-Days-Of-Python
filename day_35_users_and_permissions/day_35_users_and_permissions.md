# Day 35: Users, Permissions, and Least Privilege

[← Day 34](../day_34_safe_subprocesses/day_34_safe_subprocesses.md) · [Day index](../DAY_INDEX.md) · [Day 36 →](../day_36_timeouts_and_resource_limits/day_36_timeouts_and_resource_limits.md)

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

A process runs with an identity and permissions. Security automation must understand the difference between needing access and being entitled to broaden access.

## Prerequisites

Complete Day 34 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 35

## The problem

Inspect the current local user and a fixture’s permission metadata without changing the machine’s security settings.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Lesson

### Vocabulary

An **identity** is the account associated with a process. **Permission** controls an operation. **Least privilege** grants only what the task needs.

## Worked examples

### Example 1: Read the current user

A diagnostic can identify context without exposing credentials.

```python
import getpass

print(getpass.getuser())
```

**What to observe:**

A username, not a password.

### Example 2: Inspect a mode

POSIX mode bits can be displayed as metadata.

```python
from pathlib import Path

print(oct(Path("shared/fixtures/events.log").stat().st_mode))
```

**What to observe:**

An octal mode representation.

### Example 3: Check readability

The program can test a capability before attempting work.

```python
path = Path("shared/fixtures/events.log")
print(path.is_file())
```

**What to observe:**

The fixture exists as a file; actual access can still fail.

### Example 4: Avoid privilege escalation

A tool should report insufficient access rather than silently asking for more.

```python
def require_readable(path):
    if not path.is_file():
        raise PermissionError("fixture is not a readable regular file")
    return path
```

**What to observe:**

The caller receives a clear failure path.

### Example 5: Document permissions

A README should say what permissions the tool expects.

```python
requirements = {"read": "fixture files", "write": "training-output", "admin": "none"}
print(requirements)
```

**What to observe:**

The tool explicitly needs no administrator access.

## Execution trace

The process identity is inherited from the launcher; the tool inspects capability, performs only the required operation, and reports a permission error instead of escalating.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| run as administrator | a bug has greater impact | use ordinary user privileges |
| chmod broadly | unrelated files become exposed | change only a disposable fixture if authorized |
| log username plus secrets | identity data leaks | minimize context |
| assume platform mode | Windows and POSIX differ | state platform assumptions |
| permission equals legitimacy | access is treated as authorization | require explicit scope |

## Security application

Use the current sandbox and synthetic fixture only. Do not alter system users, groups, ACLs, or permissions as part of the exercise.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run every requested command, create the requested artifact, and record the limitation the exercise asks you to name.

## Finish line

Run `python -m course_days.day035`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Identity and capability describe what a process can do; authorization describes what it is allowed to do.

## Limitations

Permission APIs vary by operating system, containers, filesystems, and ACLs. A local check is not a complete access-control review.

[← Day 34](../day_34_safe_subprocesses/day_34_safe_subprocesses.md) · [Day index](../DAY_INDEX.md) · [Day 36 →](../day_36_timeouts_and_resource_limits/day_36_timeouts_and_resource_limits.md)
