# Day 2: Values, Names, Input, and Output

[Previous](../001_day_setup_and_safe_practice/001_day_setup_and_safe_practice.md) | [Next](../003_day_types_and_parsing/003_day_types_and_parsing.md)

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

- Day 1 or “none” if this is Day 1.
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

Security programs constantly move values between text, numbers, flags, and records. If a learner cannot explain which value is stored under which name, a later log parser or access decision becomes guesswork.

## The problem this solves

A log line arrives as text. You need to keep the raw line for evidence while storing a cleaned field for analysis. Names make those roles visible. Assignment does not mean mathematical equality; it binds a name to a value.

```python
raw_line = "2026-08-20 login_failed user=maya"
source = "synthetic-auth.log"
print(source, raw_line)
```

Trace the order: Python evaluates the right side, creates or rebinds the name on the left, then prints the current values. Rebinding a name does not rewrite an earlier string stored elsewhere.

## Input is text until you prove otherwise

`input()` always returns a string. If you expect a number, convert it and handle failure. If you expect an event field, check the format and required pieces. Keep raw and parsed forms separate so an analyst can inspect what the parser actually saw.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| Confusing `=` with `==` | Assignment appears inside a condition | Use assignment to bind; comparisons come later |
| Overwriting raw evidence | The original line cannot be reviewed | Keep `raw_line` separate from normalized fields |
| Assuming input is numeric | Arithmetic raises `TypeError` | Convert explicitly and report invalid input |

## Finish line

You can name values precisely, preserve raw input, convert a known field, and explain why external text is not automatically trustworthy.


## Common mistakes

The most useful debugging move is to reproduce the smallest failure, read the first error line, identify the value or assumption that differs from your expectation, and change one thing. Do not copy a large solution while the mental model is still unclear.

## Practice

1. **Level 1 — mechanical:** Run the starter, predict one output, change one input, and explain the difference.
2. **Level 2 — applied:** Complete the practice prompt using only concepts taught so far and the supplied synthetic fixture.
3. **Level 3 — synthesis:** Add one edge case, one negative test, and one short note explaining a security limitation.

Open [practice/prompts.md](practice/prompts.md) before [practice/hints.md](practice/hints.md). Review [practice/solutions.md](practice/solutions.md) only after a real attempt.

## Mental model

> A variable is a name bound to a value; external input is data that must earn trust through validation.

## Finish line

Run `python -m course_days.day002`, pass the relevant tests, complete the Level 1 and Level 2 practice, and write one sentence about an edge case or security boundary.
