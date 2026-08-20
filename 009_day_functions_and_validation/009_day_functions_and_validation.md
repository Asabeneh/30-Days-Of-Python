# Day 9: Functions, Contracts, and Validation

[Previous](../008_day_strings_and_canonicalization/008_day_strings_and_canonicalization.md) | [Next](../010_day_checkpoint_log_triage/010_day_checkpoint_log_triage.md)

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

- Day 8 or “none” if this is Day 1.
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

A long script hides decisions. A small function with a clear input and output contract can be tested with normal, invalid, and boundary cases.

## The problem this solves

Write a function that accepts a raw event line and returns either a structured record or a reason for rejection. Keep it deterministic so that the same input produces the same result.

```python
def is_nonempty_text(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())
```

A type hint documents the intended contract; it does not validate runtime input by itself. Tests and explicit checks still matter.

## Finish line

You can name a function's contract, keep validation deterministic, and write a test that proves both acceptance and rejection.


## Common mistakes

The most useful debugging move is to reproduce the smallest failure, read the first error line, identify the value or assumption that differs from your expectation, and change one thing. Do not copy a large solution while the mental model is still unclear.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested commands, produce the requested artifact, and record the edge case or limitation asked for by the exercise. Use [hints](practice/hints.md) only after a real attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Mental model

> A small pure function makes a security decision easier to test, review, and reuse.

## Finish line

Run `python -m course_days.day009`, pass the relevant tests, complete the Level 1 and Level 2 practice, and write one sentence about an edge case or security boundary.


<!-- video-resources:start -->
## Video support

**Optional recommendation:** [Learn Python - Full Course for Beginners [Tutorial]](https://www.youtube.com/watch?v=rfscVS0vtbw).

- Watch [00:00–01:45: Introduction](https://www.youtube.com/watch?v=rfscVS0vtbw&t=0s) for **what the course covers**. Then return to this lesson and run the local starter.
- Watch [01:45–06:40: Installing Python and PyCharm](https://www.youtube.com/watch?v=rfscVS0vtbw&t=105s) for **first installation**. Then return to this lesson and run the local starter.
- Watch [06:40–10:23: Setup and Hello World](https://www.youtube.com/watch?v=rfscVS0vtbw&t=400s) for **first runnable program**. Then return to this lesson and run the local starter.
- Watch [15:06–27:03: Variables and Data Types](https://www.youtube.com/watch?v=rfscVS0vtbw&t=906s) for **values and names**. Then return to this lesson and run the local starter.
- Watch [27:03–38:18: Working With Strings](https://www.youtube.com/watch?v=rfscVS0vtbw&t=1623s) for **text values**. Then return to this lesson and run the local starter.
- Watch [38:18–48:26: Working With Numbers](https://www.youtube.com/watch?v=rfscVS0vtbw&t=2298s) for **numeric operations**. Then return to this lesson and run the local starter.
- Watch [48:26–1:00:00: Getting Input From Users](https://www.youtube.com/watch?v=rfscVS0vtbw&t=2906s) for **input is text at the boundary**. Then return to this lesson and run the local starter.

Written alternative: [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/).
<!-- video-resources:end -->
