# Day 34: Safe Subprocess Allowlisting

[← Day 33](../day_33_paths_and_file_metadata/day_33_paths_and_file_metadata.md) · [Day index](../DAY_INDEX.md) · [Day 35 →](../day_35_users_and_permissions/day_35_users_and_permissions.md)

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

Day 31 showed how to start a process; this day turns that knowledge into a safer design. A command runner should allow a small set of known operations instead of accepting arbitrary executable input.

## Prerequisites

Complete Day 33 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 34

## The problem

Build a local command adapter that supports one or two harmless inventory commands and rejects everything else.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Lesson

### Vocabulary

An **allowlist** permits named safe cases. A **denylist** tries to enumerate unsafe cases. An **argv list** keeps arguments separate from shell parsing.

## Worked examples

### Example 1: Allow one command

Map a friendly operation to a fixed argv list.

```python
COMMANDS = {"python-version": ["python", "--version"]}
print(COMMANDS["python-version"])
```

**What to observe:**

The user chooses a key, not an executable string.

### Example 2: Reject unknown keys

Fail before starting a process.

```python
def command_for(name):
    try:
        return COMMANDS[name].copy()
    except KeyError as error:
        raise ValueError("operation is not allowed") from error
```

**What to observe:**

An unknown operation is rejected.

### Example 3: Constrain arguments

Even an allowed executable may accept unsafe arguments.

```python
def python_check(script):
    if script != "import sys; print(sys.version_info[:2])":
        raise ValueError("script is not allowed")
    return ["python", "-c", script]
```

**What to observe:**

Only the exact local check is accepted.

### Example 4: Set environment

Do not inherit more environment than necessary.

```python
safe_env = {"PATH": "/usr/bin:/bin"}
print(sorted(safe_env))
```

**What to observe:**

The child receives a deliberately small environment.

### Example 5: Bound output

Capture only a limited amount of output before reporting truncation.

```python
def preview(text, limit=4096):
    return text[:limit], len(text) > limit
```

**What to observe:**

The caller can display `truncated=True`.

## Execution trace

The friendly operation maps to fixed data, the adapter validates the key and arguments, starts with an explicit cwd/environment, and caps output and lifetime.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| denylist | a new dangerous command bypasses it | allowlist |
| executable from input | arbitrary code runs | map names to fixed argv |
| inherited environment | secrets enter child | pass a minimal environment |
| inherited privileges | child can do too much | drop privilege or refuse |
| output stored forever | sensitive output persists | cap, redact, and clean up |

## Security application

The adapter may run only harmless local inventory commands. It must reject shell metacharacters, remote destinations, arbitrary scripts, and unknown operation names.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run every requested command, create the requested artifact, and record the limitation the exercise asks you to name.

## Finish line

Run `python -m course_days.day034`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Safe automation narrows the language accepted at the process boundary until only the intended operation remains.

## Limitations

Allowlisting is a design control, not proof that the allowed command is safe on every platform or with every dependency.

[← Day 33](../day_33_paths_and_file_metadata/day_33_paths_and_file_metadata.md) · [Day index](../DAY_INDEX.md) · [Day 35 →](../day_35_users_and_permissions/day_35_users_and_permissions.md)
