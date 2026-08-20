# Day 9: Functions, Contracts, and Validation

[← Day 8](../008_day_strings_and_canonicalization/008_day_strings_and_canonicalization.md) · [Day index](../DAY_INDEX.md) · [Day 10 →](../010_day_checkpoint_log_triage/010_day_checkpoint_log_triage.md)

## Table of Contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Lesson](#lesson)
- [Worked examples](#worked-examples)
- [Execution trace](#execution-trace)
- [Common mistakes](#common-mistakes)
- [Security application](#security-application)
- [Exercises](#exercises)
- [Finish line](#finish-line)

## Why this lesson exists

Functions let you name a decision, reuse it, and test it without repeating setup. In security engineering, a function contract makes assumptions visible at the boundary.

## Prerequisites

Complete Days 1–8. You should be comfortable with types, conditions, loops, collections, and strings.

## Outcomes

By the end of this lesson, you can:

- define and call functions
- pass arguments and return values
- keep side effects at the boundary
- express preconditions and postconditions
- test normal, boundary, and invalid cases

## The problem

A log-triage program becomes difficult to review when parsing, classification, printing, and file access are mixed together. Separate functions make each claim smaller and testable.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples may describe security signals, but they do not identify attackers, authorize testing, or justify touching public systems. Keep real credentials, private logs, and university or employer data out of the lesson.

## Lesson

### Defining a function

```python
def add(left, right):
    return left + right


print(add(2, 3))
```

`def` creates a function. `left` and `right` are parameters. `return` sends a value back to the caller. Calling `add(2, 3)` binds the arguments and runs the body.

### A function can be pure

```python
def severity_label(severity):
    if not 0 <= severity <= 10:
        raise ValueError("severity must be between 0 and 10")
    return "high" if severity >= 7 else "normal"
```

This function does not print, open files, or use the network. For the same valid input, it returns the same result. Pure functions are easier to test and reason about.

### Contracts describe behavior

A useful contract answers:

- What inputs are accepted?
- What does the function return?
- What happens when input is invalid?
- Does it change files, global state, or external systems?

Write the contract before the implementation. It gives a reviewer something precise to check.

### Arguments and defaults

```python
def summarize(events, limit=100):
    if limit < 0:
        raise ValueError("limit must not be negative")
    selected = events[:limit]
    return {"processed": len(selected), "truncated": len(events) > limit}
```

Defaults are part of the policy. A default limit of `100` is safer than an accidental unbounded read.

### Keep effects at the edge

```python
def format_finding(label, reason):
    return f"label={label} reason={reason}"


message = format_finding("review", "high severity")
print(message)
```

Formatting is separate from printing. A caller can save, test, or display the returned message.
## Worked examples

### Example 1: keyword arguments

```python
def connect_summary(host, port, *, timeout=3):
    return {"host": host, "port": port, "timeout": timeout}


print(connect_summary("127.0.0.1", 8000, timeout=1))
```

The `*` makes `timeout` keyword-only, which can make security-sensitive options harder to pass accidentally.

### Example 2: validation at the function boundary

```python
def require_source(value):
    if not isinstance(value, str):
        raise TypeError("source must be text")
    value = value.strip()
    if not value:
        raise ValueError("source must not be blank")
    return value
```

The function checks both type and policy. The caller receives a clear failure instead of a later obscure error.

### Example 3: returning structured evidence

```python
def inspect_event(event):
    source = require_source(event.get("source"))
    severity = int(event["severity"])
    return {"source": source, "severity": severity, "observed": True}
```

This still needs a severity range check. A function can be useful while remaining incomplete; document the contract rather than pretending it is finished.

### Example 4: a testable caller

```python
def classify_and_format(event):
    label = severity_label(event["severity"])
    return format_finding(label, event["reason"])
```

Because the helper functions return values, tests can exercise them without capturing terminal output.

### Example 5: one side effect at the edge

```python
def write_report(path, text):
    path.write_text(text + "
", encoding="utf-8")
```

File writing is a side effect. It belongs in a small function with an explicit path policy and test fixture, not inside a pure classifier.

## Execution trace

For `severity_label(8)`:

| Step | Operation | Result |
| ---: | --- | --- |
| 1 | bind `severity` | `8` |
| 2 | validate range | true |
| 3 | evaluate `severity >= 7` | true |
| 4 | return | `"high"` |

The caller receives a value. The function does not decide that a real incident occurred.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| forgetting `return` | caller receives `None` | return the intended value |
| mutable default argument | calls share unexpected state | use `None` or an immutable default |
| hidden print or file write | unit tests become awkward | keep effects at the boundary |
| vague contract | callers guess allowed input | state preconditions and failures |
| validating only in the caller | another caller bypasses checks | validate at the function boundary |

## Security application

Refactor the Day 5 classifier into pure functions for parsing, policy, explanation, and output formatting. Add tests that prove each function’s contract. Keep file access and terminal output in the CLI boundary.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples from this lesson as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run the starter, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A function is a named contract: explicit inputs enter, a defined result leaves, and side effects are visible at the boundary.

## Limitations

A pure function can still implement a bad policy, receive unauthenticated data, or be called unsafely. Contracts improve review; they do not replace threat modeling.

## Optional video support

Watch [CS50P Lecture 0](https://www.youtube.com/watch?v=JP7ITIXGpHk&t=306s) from `05:06` for functions, arguments, and side effects.

Use the [timestamped video catalog](../VIDEO_RESOURCES.md) only after running the local examples. The written lesson and Python documentation remain authoritative.


[← Day 8](../008_day_strings_and_canonicalization/008_day_strings_and_canonicalization.md) · [Day index](../DAY_INDEX.md) · [Day 10 →](../010_day_checkpoint_log_triage/010_day_checkpoint_log_triage.md)
