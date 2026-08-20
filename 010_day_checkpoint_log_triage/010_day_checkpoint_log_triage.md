# Day 10: Checkpoint: Build a Safe Log-Triage Classifier

[Previous](../009_day_functions_and_validation/009_day_functions_and_validation.md) | [Next](../011_day_function_contracts/011_day_function_contracts.md)

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

- Day 9 or “none” if this is Day 1.
- A working setup from [SETUP.md](../SETUP.md).
- The safety rules in [SAFETY_AND_LAB_RULES.md](../SAFETY_AND_LAB_RULES.md).

## Outcomes

By the end, you can explain the day's mental model, run the starter, predict at least one result, correct one deliberate mistake, and apply the idea to a synthetic security fixture.

## The problem

Security engineering is programming applied to systems, data, and decisions. If the underlying programming idea is vague, the security label only makes the confusion harder to see. This day gives the idea a small problem before adding tools.

## Security boundary

This lesson uses only local text and synthetic examples. Do not replace the fixture path with a university, employer, public website, or another person's data. The objective is to learn a programming idea and a safe evidence habit, not to discover targets.

## Lesson
## Why this exists

This checkpoint asks you to combine the first phase without hiding the reasoning inside a large framework. You will build a small classifier for synthetic authentication events. It will parse a line, preserve the raw input, apply bounded validation, classify a narrow condition, and print an explainable result.

## Project requirements

Your classifier must accept only the documented synthetic format, reject malformed lines with a reason, never read outside the supplied fixture directory, and distinguish `ignore`, `review`, and `urgent_review`. It must include tests for a valid event, an invalid event, a boundary severity, and an out-of-scope event.

## Finish line

You can explain the full data flow from fixture to report, show the test that proves a rejection, and state what your classifier cannot conclude.


## Common mistakes

The most useful debugging move is to reproduce the smallest failure, read the first error line, identify the value or assumption that differs from your expectation, and change one thing. Do not copy a large solution while the mental model is still unclear.

## Practice

1. **Level 1 — mechanical:** Run the starter, predict one output, change one input, and explain the difference.
2. **Level 2 — applied:** Complete the practice prompt using only concepts taught so far and the supplied synthetic fixture.
3. **Level 3 — synthesis:** Add one edge case, one negative test, and one short note explaining a security limitation.

Open [practice/prompts.md](practice/prompts.md) before [practice/hints.md](practice/hints.md). Review [practice/solutions.md](practice/solutions.md) only after a real attempt.

## Mental model

> A useful first tool is a small, tested, explainable classifier that reports evidence without pretending to know more than it observed.

## Finish line

Run `python -m course_days.day010`, pass the relevant tests, complete the Level 1 and Level 2 practice, and write one sentence about an edge case or security boundary.
