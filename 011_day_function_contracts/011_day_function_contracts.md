# Day 11: Function Contracts and Explicit Security Decisions

[Previous](../010_day_checkpoint_log_triage/010_day_checkpoint_log_triage.md) | [Next](../012_day_modules_and_packages/012_day_modules_and_packages.md)

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

A function is a named contract: it receives defined inputs, performs a bounded transformation, and returns a documented result. In security code, vague contracts create hidden assumptions.

### Problem first

A triage helper should not silently accept any object and guess what it means. It should receive an event mapping, require the fields it needs, and return a small result that a caller can test.

```python
def severity_label(severity: int) -> str:
    if not 0 <= severity <= 10:
        raise ValueError("severity must be between 0 and 10")
    return "high" if severity >= 7 else "normal"
```

### Execution trace

For `severity_label(8)`, Python binds `severity` to `8`, checks the range, evaluates `8 >= 7` as `True`, and returns the string `"high"`. The caller receives a value; the function does not print, mutate global state, or decide that an incident occurred.

### Security connection

A narrow function is easier to review. Keep policy decisions pure where possible, return reasons alongside labels, and let the caller decide how to display or store the result. Type hints describe intent but do not replace runtime validation.


### Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| Using a broad catch-all | A real failure looks like an empty success | Catch expected boundary errors and preserve unexpected failures |
| Skipping the raw value | A reviewer cannot reproduce the decision | Keep raw input next to normalized or parsed fields |
| Assuming a type hint is validation | Malformed runtime data still enters the function | Validate at the boundary and test rejection |
| Optimizing before measuring | The code becomes harder to explain | Build the simplest correct version, then measure |

## Practice

### Level 1 — Mechanical

Run `python -m course_days.day011`. Predict one output, change one input, and explain the difference.

### Level 2 — Applied

Complete [practice/prompts.md](practice/prompts.md) using the supplied synthetic fixture. State the input contract and acceptance criteria before coding.

### Level 3 — Synthesis

Add one edge case, one negative test, and one paragraph distinguishing observation, inference, and residual risk.

Review [practice/hints.md](practice/hints.md) only after a real attempt and [practice/solutions.md](practice/solutions.md) only to compare decisions.

## Mental model

> Function Contracts and Explicit Security Decisions is valuable when the boundary, assumptions, failure behavior, and evidence are visible.

## Finish line

Run the starter, pass the phase tests, complete Levels 1 and 2, and explain one edge case aloud or in writing.
