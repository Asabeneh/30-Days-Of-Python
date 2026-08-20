# Day 15: Iterators, Generators, and Bounded Streaming

[Previous](../014_day_files_and_safe_paths/014_day_files_and_safe_paths.md) | [Next](../016_day_regular_expressions/016_day_regular_expressions.md)

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

A list loads all values into memory. An iterator produces values one at a time. Generators are useful for large logs, but a lazy pipeline still needs bounds, error handling, and observability.

### Problem first

Process synthetic lines without building a second copy of the entire input.

```python
def matching_lines(lines, needle):
    for line in lines:
        if needle in line:
            yield line
```

### Execution trace

Calling `matching_lines` creates a generator without running its body. Each `next` request resumes the function until it yields a matching line. When the source is exhausted, Python raises `StopIteration` internally and the loop ends.

### Security connection

Generators improve memory behavior but do not make untrusted input safe. Add maximum records, maximum line length, timeouts, and counters so the operator knows how much was processed.


### Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| Using a broad catch-all | A real failure looks like an empty success | Catch expected boundary errors and preserve unexpected failures |
| Skipping the raw value | A reviewer cannot reproduce the decision | Keep raw input next to normalized or parsed fields |
| Assuming a type hint is validation | Malformed runtime data still enters the function | Validate at the boundary and test rejection |
| Optimizing before measuring | The code becomes harder to explain | Build the simplest correct version, then measure |

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested commands, produce the requested artifact, and record the edge case or limitation asked for by the exercise. Use [hints](practice/hints.md) only after a real attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Mental model

> Iterators, Generators, and Bounded Streaming is valuable when the boundary, assumptions, failure behavior, and evidence are visible.

## Finish line

Run the starter, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.
