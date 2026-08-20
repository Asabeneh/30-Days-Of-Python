# Day 14: Files, Paths, Encodings, and Safe Cleanup

[Previous](../013_day_exceptions_and_error_taxonomy/013_day_exceptions_and_error_taxonomy.md) | [Next](../015_day_iterators_and_generators/015_day_iterators_and_generators.md)

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

Files are resources and paths are data. A path supplied by a user or a log record must not automatically be allowed to escape the intended evidence directory.

### Problem first

Read one synthetic evidence file below a known directory and reject a path that would resolve outside it.

```python
from pathlib import Path


def safe_path(base: Path, requested: str) -> Path:
    candidate = (base / requested).resolve()
    base_resolved = base.resolve()
    if candidate != base_resolved and base_resolved not in candidate.parents:
        raise ValueError("path escapes the evidence directory")
    return candidate
```

### Execution trace

The candidate is resolved before comparison, which makes `..` and redundant separators visible. The comparison checks the resolved path, not the spelling the user typed. This is a boundary check, not a complete authorization system.

### Security connection

Use context managers for cleanup, explicit encodings, bounded reads, and fixture directories. Do not follow symlinks or collect arbitrary files unless the lab scope explicitly allows it.


### Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| Using a broad catch-all | A real failure looks like an empty success | Catch expected boundary errors and preserve unexpected failures |
| Skipping the raw value | A reviewer cannot reproduce the decision | Keep raw input next to normalized or parsed fields |
| Assuming a type hint is validation | Malformed runtime data still enters the function | Validate at the boundary and test rejection |
| Optimizing before measuring | The code becomes harder to explain | Build the simplest correct version, then measure |

## Practice

### Level 1 — Mechanical

Run `python -m course_days.day014`. Predict one output, change one input, and explain the difference.

### Level 2 — Applied

Complete [practice/prompts.md](practice/prompts.md) using the supplied synthetic fixture. State the input contract and acceptance criteria before coding.

### Level 3 — Synthesis

Add one edge case, one negative test, and one paragraph distinguishing observation, inference, and residual risk.

Review [practice/hints.md](practice/hints.md) only after a real attempt and [practice/solutions.md](practice/solutions.md) only to compare decisions.

## Mental model

> Files, Paths, Encodings, and Safe Cleanup is valuable when the boundary, assumptions, failure behavior, and evidence are visible.

## Finish line

Run the starter, pass the phase tests, complete Levels 1 and 2, and explain one edge case aloud or in writing.
