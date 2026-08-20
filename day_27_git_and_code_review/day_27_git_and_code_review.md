# Day 27: Git and Code Review for Security Changes

[← Day 26](../day_26_structured_logging/day_26_structured_logging.md) · [Day index](../DAY_INDEX.md) · [Day 28 →](../day_28_dependency_hygiene_and_sboms/day_28_dependency_hygiene_and_sboms.md)

## Table of Contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Lesson](#lesson)
- [Vocabulary](#vocabulary)
- [Worked examples](#worked-examples)
- [Execution trace](#execution-trace)
- [Common mistakes](#common-mistakes)
- [Security application](#security-application)
- [Exercises](#exercises)
- [Finish line](#finish-line)

## Why this lesson exists

Version control is part of engineering evidence. A small reviewable commit helps a team understand what changed, why it changed, and how to revert it.

## Prerequisites

Complete Day 26 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 27

## The problem

Review a change to a parser or security rule without trusting the author’s description alone.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Lesson

### Vocabulary

A **diff** is a line-level change. A **commit** is a recorded snapshot. A **review** checks behavior, tests, scope, and risk before integration.

## Worked examples

### Example 1: Inspect status

Start with the repository state before modifying anything.

```python
git status --short
git branch --show-current
```

**What to observe:**

You see changed files and the active branch.

### Example 2: Read a diff

A diff shows additions, deletions, and context.

```python
git diff -- course_days/day027.py
```

**What to observe:**

The reviewer can focus on the actual changed lines.

### Example 3: Make a focused commit

A commit should tell one coherent story.

```python
git add course_days/day027.py tests/test_day027.py
git commit -m "Validate evidence source"
```

**What to observe:**

The source and its tests move together.

### Example 4: Review security questions

A checklist prevents “tests pass” from being the only question.

```python
questions = [
    "What input is new?",
    "What is the trust boundary?",
    "What can leak?",
    "What is the rollback?",
]
print(len(questions))
```

**What to observe:**

Four review questions are visible.

### Example 5: Compare before and after

A reviewer should inspect behavior, not only formatting.

```python
before = {"accepted": ["443"], "rejected": ["70000"]}
after = {"accepted": ["443"], "rejected": ["70000", "abc"]}
print(after)
```

**What to observe:**

The added rejection is an observable behavior change.

## Execution trace

The review moves from status to diff to tests to threat questions to a focused commit. The repository becomes a record of engineering decisions.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| review only the title | dangerous line is missed | inspect the diff |
| giant mixed commit | rollback is risky | split coherent changes |
| no negative test | security claim is unproved | add rejection tests |
| commit secrets | history retains them | scan and remove before commit |
| approve based on authority | reviewer skips evidence | require reproducible checks |

## Security application

Practice on the course branch and synthetic fixtures. Never commit tokens, private logs, or generated evidence. If a secret enters Git history, stop and follow the repository security policy.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run every requested command, create the requested artifact, and record the limitation the exercise asks you to name.

## Finish line

Run `python -m course_days.day027`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A code review is a structured challenge to the change’s assumptions, not a vote on the author.

## Limitations

Git records changes but does not make secrets disappear from history or guarantee that a review found every flaw.

[← Day 26](../day_26_structured_logging/day_26_structured_logging.md) · [Day index](../DAY_INDEX.md) · [Day 28 →](../day_28_dependency_hygiene_and_sboms/day_28_dependency_hygiene_and_sboms.md)
