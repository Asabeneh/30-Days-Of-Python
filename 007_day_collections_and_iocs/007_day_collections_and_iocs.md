# Day 7: Collections and an Indicator Catalog

[Previous](../006_day_loops_and_bounded_work/006_day_loops_and_bounded_work.md) | [Next](../008_day_strings_and_canonicalization/008_day_strings_and_canonicalization.md)

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

- Day 6 or “none” if this is Day 1.
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

Security data is often a collection of events and indicators. Choosing the wrong collection can lose order, allow duplicates, or make context hard to retrieve.

## The problem this solves

Build a small catalog where an indicator maps to its type, source, and confidence. Use a set to deduplicate observed values and a list when event order matters.

```python
observed = ["203.0.113.8", "203.0.113.8", "198.51.100.7"]
unique = set(observed)
record = {"indicator": "203.0.113.8", "kind": "ip", "confidence": "low"}
```

A set loses ordering. A dictionary lookup is fast but requires a key policy. Document those trade-offs before optimizing.

## Finish line

You can select a collection for its semantics, deduplicate an indicator, preserve event order, and retain context for a review.


## Common mistakes

The most useful debugging move is to reproduce the smallest failure, read the first error line, identify the value or assumption that differs from your expectation, and change one thing. Do not copy a large solution while the mental model is still unclear.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested commands, produce the requested artifact, and record the edge case or limitation asked for by the exercise. Use [hints](practice/hints.md) only after a real attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Mental model

> Lists preserve order, sets enforce uniqueness, and dictionaries connect a key to context.

## Finish line

Run `python -m course_days.day007`, pass the relevant tests, complete the Level 1 and Level 2 practice, and write one sentence about an edge case or security boundary.
