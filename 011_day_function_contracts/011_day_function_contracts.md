# Day 11: Function Contracts and Explicit Security Decisions

[← Day 10](../010_day_checkpoint_log_triage/010_day_checkpoint_log_triage.md) · [Day index](../DAY_INDEX.md) · [Day 12 →](../012_day_modules_and_packages/012_day_modules_and_packages.md)

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

A function is where an idea becomes a reusable promise. Security utilities become trustworthy when their inputs, outputs, failures, and side effects are visible enough for another person to review.

## Prerequisites

Complete Days 1–10. You should be able to write a function, return a value, and test a boundary.

## Outcomes

By the end of this lesson, you can:

- write a precondition and postcondition
- distinguish a return value from a side effect
- use keyword-only arguments and immutable defaults
- preserve failure information
- test a contract rather than an implementation detail

## The problem

The phase-one classifier works, but its rules are hidden inside a script. A reviewer needs a small function whose contract says exactly which severity values are accepted, which label is returned, and what happens when the input is invalid.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples do not authorize access to public systems, university systems, employer systems, or accounts that you do not own.

## Lesson

### Vocabulary

A **precondition** describes what must be true before a call. A **postcondition** describes what the caller can rely on after a successful return. A **side effect** changes something outside the returned value, such as a file, log, database, or network service.

## Worked examples

### Example 1: The smallest contract

A function can make its accepted input and returned value obvious.

```python
def double(value):
    return value * 2


print(double(4))
```

**What to observe:**

8

### Example 2: A bounded contract

Validation belongs at the boundary so every caller receives the same rule.

```python
def severity_label(severity):
    if not isinstance(severity, int):
        raise TypeError("severity must be an integer")
    if not 0 <= severity <= 10:
        raise ValueError("severity must be between 0 and 10")
    return "high" if severity >= 7 else "normal"
```

**What to observe:**

`severity_label(7)` returns `high`; `severity_label(11)` raises `ValueError`.

### Example 3: Keyword-only safety options

Keyword-only parameters make an important option visible at the call site.

```python
def read_preview(path, *, max_bytes=4096):
    if max_bytes <= 0:
        raise ValueError("max_bytes must be positive")
    return path.read_bytes()[:max_bytes]
```

**What to observe:**

The caller must write `max_bytes=...`; an accidental positional limit is harder to review.

### Example 4: Return instead of print

Returning a structured value lets tests and callers inspect the decision without capturing terminal output.

```python
def finding(label, reason):
    return {"label": label, "reason": reason}


result = finding("review", "high severity")
print(result["label"])
```

**What to observe:**

`review`

### Example 5: Keep effects at the edge

File access is a side effect and should be separated from a pure parser.

```python
def format_report(event):
    return f"source={event['source']} severity={event['severity']}"
```

**What to observe:**

The function returns text and does not open a file or contact a service.

## Execution trace

For `severity_label(8)`, Python binds the argument, checks its type, checks the range, evaluates `8 >= 7`, and returns `high`. For `severity_label("8")`, the type precondition fails before policy logic runs.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| no return | caller receives `None` | return the promised value |
| broad `except` | programming errors become ordinary bad input | catch only expected boundary errors |
| mutable default | calls share hidden state | use `None` or an immutable default |
| hidden file write | a pure function changes evidence | keep effects in a small boundary function |
| undocumented range | callers guess the policy | state preconditions and test boundaries |

## Security application

Refactor one phase-one rule into a pure function and add a contract table. The exercise must use only synthetic events and must distinguish the observation `rule matched` from the conclusion `attack occurred`.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples above as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run `python -m course_days.day011`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A function contract is a small trust boundary: explicit input enters, a defined result leaves, and side effects are visible.

## Limitations

A contract improves review but cannot prove that the caller supplied authentic data or that the policy is correct for a production environment.

[← Day 10](../010_day_checkpoint_log_triage/010_day_checkpoint_log_triage.md) · [Day index](../DAY_INDEX.md) · [Day 12 →](../012_day_modules_and_packages/012_day_modules_and_packages.md)
