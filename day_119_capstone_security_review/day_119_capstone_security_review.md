# Day 119: Capstone Security Review

[← Day 118](../day_118_capstone_implementation/day_118_capstone_implementation.md) · [Day index](../DAY_INDEX.md) · [Day 120 →](../day_120_final_demonstration/day_120_final_demonstration.md)

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

A final review asks whether the capstone’s claims are supported, whether the controls are correctly placed, and whether the demonstration could mislead a user.

## Prerequisites

Complete Day 118. Work from a clean virtual environment and use only local synthetic fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using it
- run and modify all worked examples
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Review a capstone with a checklist covering inputs, secrets, authorization, resources, evidence, tests, and limitations.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, destructive actions, persistence, or processing of private data.

## Lesson

### Vocabulary

A security review challenges assumptions. A control is effective only when it protects the intended boundary. A residual risk is a known remaining weakness.

## Worked examples

### Example 1: Review inputs

List every external or fixture-controlled input.

```python
inputs = ["fixture path", "JSON record", "CLI limit"]
print(inputs)
```

**What to observe:**

The review surface is explicit.

### Example 2: Review secrets

Search for values and unsafe logging paths.

```python
secret_controls = {"source": False, "logs": False, "fixtures": False}
print(secret_controls)
```

**What to observe:**

No secret source is intended.

### Example 3: Review authorization

A tool must state who can invoke each action.

```python
auth = {"local_user": True, "remote_admin": False, "target": "fixture"}
print(auth)
```

**What to observe:**

The authority is bounded.

### Example 4: Review resources

Limits should cover input, output, time, and concurrency.

```python
limits = {"lines": 100, "bytes": 1000000, "seconds": 10, "workers": 2}
print(limits)
```

**What to observe:**

The resource policy is visible.

### Example 5: Write residual risk

A review ends with what remains and who accepts it.

```python
risk = {
    "item": "synthetic rules miss real patterns",
    "owner": "course",
    "accepted": True,
}
print(risk)
```

**What to observe:**

The limitation is owned.

## Execution trace

The reviewer walks input to output, checks controls at boundaries, runs tests and negative cases, inspects artifacts and secrets, and records residual risks rather than declaring absolute security.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| review only code | setup and deployment ignored | inspect whole path |
| green tests equals safe | threats are untested | use threat model |
| no negative cases | rejection paths fail | add boundary tests |
| hide residual risk | users overtrust | state owner and acceptance |
| review author alone | blind spots persist | use another reviewer |

## Security application

Review the local capstone only. Do not use the review to justify testing an external target or collecting real data.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the evidence, output, edge case, and limitation requested by each question.

## Finish line

Run `python -m course_days.day119`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Security review is a reasoned challenge to the system’s claims, controls, evidence, and limits.

## Limitations

A review is bounded by reviewer skill, time, tools, and available evidence; it is not a guarantee.

[← Day 118](../day_118_capstone_implementation/day_118_capstone_implementation.md) · [Day index](../DAY_INDEX.md) · [Day 120 →](../day_120_final_demonstration/day_120_final_demonstration.md)
