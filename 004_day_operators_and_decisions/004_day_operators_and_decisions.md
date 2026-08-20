# Day 4: Operators, Comparisons, Truthiness, and Precedence

[Previous](../003_day_types_and_parsing/003_day_types_and_parsing.md) | [Next](../005_day_branching_and_triage/005_day_branching_and_triage.md)

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

- Day 3 or “none” if this is Day 1.
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

A single character can change a security decision. `and` versus `or`, `>` versus `>=`, or an unexpected precedence rule can turn a safe allowlist into an accidental bypass.

## The problem this solves

You need to express a policy such as “the event is in scope and either high severity or repeated.” Write the conditions in named pieces before combining them. Parentheses make intent visible.

```python
in_scope = True
severity = 8
repeated = False
needs_review = in_scope and (severity >= 7 or repeated)
print(needs_review)
```

Trace each comparison first. Then combine the resulting booleans. Do not rely on a reader remembering precedence.

## Truthiness is not authorization

Empty strings, empty collections, zero, and `None` are falsy. That can be convenient for ordinary control flow, but security policy should usually compare an explicit value or use a named predicate. `if token:` does not prove that a token is valid, unexpired, or authorized.

## Finish line

You can predict a compound boolean expression, add parentheses to express intent, and distinguish a truthy value from a verified security fact.


## Common mistakes

The most useful debugging move is to reproduce the smallest failure, read the first error line, identify the value or assumption that differs from your expectation, and change one thing. Do not copy a large solution while the mental model is still unclear.

## Practice

1. **Level 1 — mechanical:** Run the starter, predict one output, change one input, and explain the difference.
2. **Level 2 — applied:** Complete the practice prompt using only concepts taught so far and the supplied synthetic fixture.
3. **Level 3 — synthesis:** Add one edge case, one negative test, and one short note explaining a security limitation.

Open [practice/prompts.md](practice/prompts.md) before [practice/hints.md](practice/hints.md). Review [practice/solutions.md](practice/solutions.md) only after a real attempt.

## Mental model

> A security decision is only as correct as the exact expression and assumptions that produce it.

## Finish line

Run `python -m course_days.day004`, pass the relevant tests, complete the Level 1 and Level 2 practice, and write one sentence about an edge case or security boundary.
