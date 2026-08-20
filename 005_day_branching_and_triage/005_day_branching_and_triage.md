# Day 5: Branching and a First Triage Classifier

[Previous](../004_day_operators_and_decisions/004_day_operators_and_decisions.md) | [Next](../006_day_loops_and_bounded_work/006_day_loops_and_bounded_work.md)

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

- Day 4 or “none” if this is Day 1.
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

Triage requires decisions, but a classifier should make a narrow, explainable decision rather than inventing certainty. Branches let us make that behavior explicit.

## The problem this solves

Given a synthetic event, choose `ignore`, `review`, or `urgent_review` using documented conditions. Return the reason as well as the label so another person can inspect the decision.

```python
def classify(severity: int, in_scope: bool) -> tuple[str, str]:
    if not in_scope:
        return "ignore", "outside the lab scope"
    if severity >= 9:
        return "urgent_review", "high severity"
    if severity >= 5:
        return "review", "moderate severity"
    return "ignore", "low severity"
```

The order matters. A later branch is never reached if an earlier branch returns. Test boundary values such as 4, 5, 8, and 9.

## Observation is not conclusion

A label such as `urgent_review` means a human should inspect the event under the course policy. It does not mean “the system is compromised.” The reason and raw evidence keep the claim narrow.

## Finish line

You can write an ordered classifier, test boundaries, return a reason, and explain why a triage label is not proof of an incident.


## Common mistakes

The most useful debugging move is to reproduce the smallest failure, read the first error line, identify the value or assumption that differs from your expectation, and change one thing. Do not copy a large solution while the mental model is still unclear.

## Practice

1. **Level 1 — mechanical:** Run the starter, predict one output, change one input, and explain the difference.
2. **Level 2 — applied:** Complete the practice prompt using only concepts taught so far and the supplied synthetic fixture.
3. **Level 3 — synthesis:** Add one edge case, one negative test, and one short note explaining a security limitation.

Open [practice/prompts.md](practice/prompts.md) before [practice/hints.md](practice/hints.md). Review [practice/solutions.md](practice/solutions.md) only after a real attempt.

## Mental model

> A branch turns evidence into a decision, but a decision is not the same as proof of compromise.

## Finish line

Run `python -m course_days.day005`, pass the relevant tests, complete the Level 1 and Level 2 practice, and write one sentence about an edge case or security boundary.
