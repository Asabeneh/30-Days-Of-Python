# Day 14: Files, Paths, and Safe Evidence Boundaries

[← Day 13](../013_day_exceptions_and_error_taxonomy/013_day_exceptions_and_error_taxonomy.md) · [Day index](../DAY_INDEX.md) · [Day 15 →](../015_day_iterators_and_generators/015_day_iterators_and_generators.md)

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

Files are useful evidence sources and dangerous trust boundaries. A path supplied by a user can escape the intended directory, a large file can consume resources, and a report can overwrite something important.

## Prerequisites

Complete Days 1–13 and know how to catch a boundary exception.

## Outcomes

By the end of this lesson, you can:

- use `pathlib.Path` for readable path operations
- resolve and constrain a path to a base directory
- read text with an explicit encoding
- bound file size and line length
- write reports atomically in a fixture directory

## The problem

The checkpoint should read one supplied fixture and write one generated report without following `../` outside the training directory. The safety property must be testable.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples do not authorize access to public systems, university systems, employer systems, or accounts that you do not own.

## Lesson

### Vocabulary

A **path** is a description of a location. A **resolved path** is the normalized location after following relative components and links. A **trust boundary** is where data changes from an external or less-trusted source into a sensitive operation.

## Worked examples

### Example 1: Build a path

Joining path components is clearer with `Path` than string concatenation.

```python
from pathlib import Path

base = Path("training-fixtures")
path = base / "events.log"
print(path)
```

**What to observe:**

`training-fixtures/events.log` on POSIX-style output.

### Example 2: Resolve and constrain

Compare resolved paths rather than searching for a literal `..`.

```python
def safe_path(base, user_value):
    base = base.resolve()
    candidate = (base / user_value).resolve()
    if candidate != base and base not in candidate.parents:
        raise ValueError("path escapes fixture directory")
    return candidate
```

**What to observe:**

`../secret.txt` is rejected after resolution.

### Example 3: Read with an encoding

Text decoding is part of the file contract.

```python
text = path.read_text(encoding="utf-8")
print(text.splitlines()[:2])
```

**What to observe:**

The first two lines are read as Unicode text.

### Example 4: Check size before reading

A tool can refuse a fixture that exceeds its documented bound.

```python
maximum = 1_000_000
if path.stat().st_size > maximum:
    raise ValueError("fixture is too large")
```

**What to observe:**

The file is rejected before its full content enters memory.

### Example 5: Write a controlled report

Create output only beneath the chosen report directory.

```python
report_dir = Path("training-output")
report_dir.mkdir(exist_ok=True)
(report_dir / "summary.txt").write_text("complete\n", encoding="utf-8")
```

**What to observe:**

The output is local and resettable.

## Execution trace

For base `/course/training-fixtures` and user value `../secret.txt`, the candidate resolves to `/course/secret.txt`. The candidate is not inside the resolved base, so the function raises before opening it.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| string prefix check | `/base-other` looks like `/base` | compare resolved path parents |
| string concatenation | separators and `..` behave unexpectedly | use `Path` |
| no encoding | platform-dependent decoding | specify UTF-8 or the documented encoding |
| read before size check | memory spikes | inspect metadata first |
| overwrite source | evidence is destroyed | write to a dedicated output directory |

## Security application

Use only `shared/fixtures` or a temporary directory under the repository. Add tests for a normal relative path, `../` escape, absolute path, oversized fixture, and output cleanup.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples above as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run `python -m course_days.day014`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A file operation is safe only when location, size, encoding, mode, and cleanup are explicit.

## Limitations

Path checks can be affected by symlinks, permissions, races, and platform differences. A local helper is not a replacement for a hardened production file service.

[← Day 13](../013_day_exceptions_and_error_taxonomy/013_day_exceptions_and_error_taxonomy.md) · [Day index](../DAY_INDEX.md) · [Day 15 →](../015_day_iterators_and_generators/015_day_iterators_and_generators.md)
