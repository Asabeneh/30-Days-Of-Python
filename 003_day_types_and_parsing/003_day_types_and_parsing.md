# Day 3: Types, Conversion, and Parsing Boundaries

[Previous](../002_day_values_names_and_input/002_day_values_names_and_input.md) | [Next](../004_day_operators_and_decisions/004_day_operators_and_decisions.md)

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

- Day 2 or “none” if this is Day 1.
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

Python will happily hold many kinds of values, but a security decision often depends on distinguishing text, numbers, booleans, missing values, and malformed values. Parsing is where ambiguity becomes either a clear result or a clear rejection.

## The problem this solves

A status field may be `"200"`, `200`, `"unknown"`, or missing. These are not interchangeable. Use `type(value)` while learning, then write a small parser that returns a documented result or a useful error.

```python
status_text = "200"
status_code = int(status_text)
print(type(status_text).__name__, type(status_code).__name__)
```

The conversion is a boundary: before it, the value is text; after it, the program is allowed to use numeric comparisons. The conversion can fail, so it must be tested.

## Strings, numbers, and booleans

Strings represent text. Integers represent whole numbers. Floats approximate decimal values. Booleans represent `True` or `False`, but a non-empty string such as `"False"` is still truthy. Never use `bool(text)` as a security parser for yes/no input.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| `bool("False")` | The result is `True` | Parse accepted words explicitly |
| Mixing strings and integers | `TypeError` or wrong ordering | Convert at the boundary and name the type |
| Silently converting failures | Bad data disappears | Return a rejection with the raw field and reason |

## Finish line

You can identify the type of a value, convert a valid field, reject malformed input, and explain why visible text and typed data are different.


## Common mistakes

The most useful debugging move is to reproduce the smallest failure, read the first error line, identify the value or assumption that differs from your expectation, and change one thing. Do not copy a large solution while the mental model is still unclear.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested commands, produce the requested artifact, and record the edge case or limitation asked for by the exercise. Use [hints](practice/hints.md) only after a real attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Mental model

> A parser translates text into a type while making invalid and ambiguous input visible.

## Finish line

Run `python -m course_days.day003`, pass the relevant tests, complete the Level 1 and Level 2 practice, and write one sentence about an edge case or security boundary.


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
