# Day 13: Exceptions and Error Taxonomy

[← Day 12](../012_day_modules_and_packages/012_day_modules_and_packages.md) · [Day index](../DAY_INDEX.md) · [Day 14 →](../014_day_files_and_safe_paths/014_day_files_and_safe_paths.md)

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

Errors are part of a security tool’s output. If a program hides a malformed record, a permission failure, and a programming bug under one `except`, operators cannot know what happened or what to do next.

## Prerequisites

Complete Days 1–12 and be comfortable with modules, functions, and conversion errors.

## Outcomes

By the end of this lesson, you can:

- read a traceback from the bottom up
- raise a precise exception at a boundary
- catch only what the caller can handle
- preserve context with exception chaining
- separate rejected input from unavailable resources

## The problem

The log parser sees a missing field, the fixture path is outside the allowed directory, and the report file cannot be written. These are different failures and require different messages and tests.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples do not authorize access to public systems, university systems, employer systems, or accounts that you do not own.

## Lesson

### Vocabulary

An **exception** is an object describing an abnormal condition. **Raising** transfers control to a handler. **Catching** says the current layer knows how to recover or report. An exception chain preserves the original cause.

## Worked examples

### Example 1: Catch the expected conversion error

Handle malformed user input at the CLI boundary.

```python
try:
    severity = int(raw)
except ValueError:
    print("severity must be an integer")
```

**What to observe:**

The user sees a useful message instead of a traceback.

### Example 2: Raise a policy error

A successful conversion can still violate a domain rule.

```python
def require_limit(value):
    if not 1 <= value <= 1000:
        raise ValueError("limit must be 1..1000")
    return value
```

**What to observe:**

`require_limit(1001)` raises a precise policy error.

### Example 3: Use separate exception types

A caller can react differently to invalid data and a missing file.

```python
class InvalidRecord(ValueError):
    pass


class FixtureNotFound(FileNotFoundError):
    pass
```

**What to observe:**

The type communicates the recovery path.

### Example 4: Chain a cause

Translate a low-level exception while preserving why it happened.

```python
try:
    value = int(raw)
except ValueError as error:
    raise InvalidRecord("severity is malformed") from error
```

**What to observe:**

The message is domain-specific and the original `ValueError` remains available.

### Example 5: Do not hide failures

A catch-all returning an empty list looks like a successful scan with no findings.

```python
try:
    records = load_fixture(path)
except FixtureNotFound:
    return {"status": "unavailable"}
```

**What to observe:**

The caller can distinguish unavailable input from an empty result.

## Execution trace

For `int("high")`, Python raises `ValueError`; the boundary catches it and raises `InvalidRecord` with the original error chained. A programming error such as a misspelled variable should remain visible instead of being converted into `invalid input`.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| `except Exception` everywhere | real bugs disappear | catch only recoverable types |
| `except: pass` | evidence silently vanishes | report or re-raise with context |
| one error for all cases | operators cannot choose a response | define a small error taxonomy |
| leaking raw input | secrets appear in messages | use safe field names and redaction |
| retrying every error | malformed data is processed repeatedly | retry only transient resource failures |

## Security application

Add a rejection report for malformed synthetic records and a separate unavailable-fixture result. Never include the full raw line or a secret in the exception message.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples above as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run `python -m course_days.day013`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> An exception is information about a failed assumption; classify it so the correct layer can recover, report, or stop.

## Limitations

Exception messages can be sensitive and exception types are not a complete observability strategy. Production systems also need structured logs, metrics, and ownership.

[← Day 12](../012_day_modules_and_packages/012_day_modules_and_packages.md) · [Day index](../DAY_INDEX.md) · [Day 14 →](../014_day_files_and_safe_paths/014_day_files_and_safe_paths.md)
