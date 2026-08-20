# Day 13: Exceptions, Error Taxonomy, and Safe Failure

[Previous](../012_day_modules_and_packages/012_day_modules_and_packages.md) | [Next](../014_day_files_and_safe_paths/014_day_files_and_safe_paths.md)

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

Python becomes useful in cybersecurity when its behavior is predictable, testable, and explainable. This day introduces a professional engineering idea through a small local problem before asking you to combine it with other tools.

## Prerequisites

You should be able to run the previous day, write a small function, and use the setup in [SETUP.md](../SETUP.md). If a term is unfamiliar, return to the previous lesson rather than copying a later pattern.

## Outcomes

By the end, you can explain the core concept, trace the starter, predict a changed result, write a normal and negative test, and state what the exercise does not prove about a real system.

## The problem

Security data is untrusted, incomplete, and easy to misinterpret. The problem today is to make one transformation or decision explicit enough that another learner can run it, test it, and review its assumptions.

## Security boundary

Use only the synthetic fixtures supplied by the course or a local file you created. Do not substitute public targets, university systems, employer systems, real credentials, or private evidence. Read `lab/scope.md` before changing the exercise.

## Core lesson

Exceptions are structured signals that an operation did not produce its normal result. Catch only errors you can handle, preserve useful context, and do not turn every failure into a successful-looking empty result.

### Problem first

A malformed event should be rejected with a reason, while an unexpected programming error should remain visible during development.

```python
def parse_severity(text: str) -> int:
    try:
        value = int(text)
    except ValueError as error:
        raise ValueError("severity must be an integer") from error
    if not 0 <= value <= 10:
        raise ValueError("severity is outside the allowed range")
    return value
```

### Execution trace

Python enters the `try` block, calls `int`, and either returns a number or raises `ValueError`. The `except` block translates the low-level failure into a message that describes the input contract. The original error remains attached through exception chaining.

### Security connection

Broad `except Exception` blocks can hide outages and evidence. Catch expected input errors at the boundary, log safely, and let unexpected failures fail loudly in tests. Never include secrets or raw private data in error messages.


### Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| Using a broad catch-all | A real failure looks like an empty success | Catch expected boundary errors and preserve unexpected failures |
| Skipping the raw value | A reviewer cannot reproduce the decision | Keep raw input next to normalized or parsed fields |
| Assuming a type hint is validation | Malformed runtime data still enters the function | Validate at the boundary and test rejection |
| Optimizing before measuring | The code becomes harder to explain | Build the simplest correct version, then measure |

## Practice

### Level 1 — Mechanical

Run `python -m course_days.day013`. Predict one output, change one input, and explain the difference.

### Level 2 — Applied

Complete [practice/prompts.md](practice/prompts.md) using the supplied synthetic fixture. State the input contract and acceptance criteria before coding.

### Level 3 — Synthesis

Add one edge case, one negative test, and one paragraph distinguishing observation, inference, and residual risk.

Review [practice/hints.md](practice/hints.md) only after a real attempt and [practice/solutions.md](practice/solutions.md) only to compare decisions.

## Mental model

> Exceptions, Error Taxonomy, and Safe Failure is valuable when the boundary, assumptions, failure behavior, and evidence are visible.

## Finish line

Run the starter, pass the phase tests, complete Levels 1 and 2, and explain one edge case aloud or in writing.
