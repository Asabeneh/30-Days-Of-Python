# Day 6: Loops, Bounds, and Resource Safety

[Previous](../005_day_branching_and_triage/005_day_branching_and_triage.md) | [Next](../007_day_collections_and_iocs/007_day_collections_and_iocs.md)

## Table of Contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Lesson](#lesson)
- [Common mistakes](#common-mistakes)
- [Practice](#practice)
- [Mental model](#mental-model)
- [Finish line](#finish-line)

## Why this lesson exists

This lesson is part of the first phase for a learner who may have never written code. It introduces one idea at a time and connects it to a small, safe cybersecurity problem.

## Prerequisites

- Day 5 or “none” if this is Day 1.
- A working setup from [SETUP.md](../SETUP.md).
- The safety rules in [SAFETY_AND_LAB_RULES.md](../SAFETY_AND_LAB_RULES.md).

## Outcomes

By the end, you can explain the day's mental model, run the starter, predict at least one result, correct one deliberate mistake, and apply the idea to a synthetic security fixture.

## The problem

Security engineering is programming applied to systems, data, and decisions. If the underlying programming idea is vague, the security label only makes the confusion harder to see. This day gives the idea a small problem before adding tools.

## Security boundary

This lesson uses only local text and synthetic examples. Do not replace the fixture path with a university, employer, public website, or another person's data. The objective is to learn a programming idea and a safe evidence habit, not to discover targets.

## Lesson
## Why this lesson exists

Loops make it easy to process a collection, but an unbounded loop or an unexpectedly huge input can exhaust time or memory. Security automation must define how much work it is willing to do.

## The problem this solves

Scan only the first `limit` synthetic log lines and count matching events. If more data exists, report that the scan was bounded rather than pretending the whole source was examined.

```python
for index, line in enumerate(lines[:limit]):
    print(index, line)
```

The slice makes the boundary visible. In a streaming program, use a counter and stop deliberately. Test zero, one, and a limit smaller than the input.

## Finish line

You can trace a loop, state its stopping condition, and explain why bounded work is part of reliable security engineering.


## Common mistakes

The most useful debugging move is to reproduce the smallest failure, read the first error line, identify the value or assumption that differs from your expectation, and change one thing. Do not copy a large solution while the mental model is still unclear.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested commands, produce the requested artifact, and record the edge case or limitation asked for by the exercise. Use [hints](practice/hints.md) only after a real attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Mental model

> Repetition is useful only when its stopping condition and maximum work are clear.

## Finish line

Run `python -m course_days.day006`, pass the relevant tests, complete the Level 1 and Level 2 practice, and write one sentence about an edge case or security boundary.
