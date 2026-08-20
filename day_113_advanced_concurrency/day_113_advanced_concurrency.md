# Day 113: Advanced Concurrency and Cancellation

[← Day 112](../day_112_performance_and_backpressure/day_112_performance_and_backpressure.md) · [Day index](../DAY_INDEX.md) · [Day 114 →](../day_114_failure_injection_and_recovery/day_114_failure_injection_and_recovery.md)

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

Concurrency at scale introduces cancellation, ordering, shared state, and cleanup problems. Reliable security tooling needs deterministic identifiers and explicit lifecycle control.

## Prerequisites

Complete Day 112. Work from a clean virtual environment and use only local synthetic fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using it
- run and modify all worked examples
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Coordinate bounded asynchronous tasks, cancel them cleanly, and preserve result identity.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, destructive actions, persistence, or processing of private data.

## Lesson

### Vocabulary

Cancellation requests work to stop. A future represents pending work. Idempotence means repeating an operation has the same safe effect. A race depends on timing.

## Worked examples

### Example 1: Name tasks

Every task needs an identifier.

```python
tasks = {"fixture-a": "pending", "fixture-b": "pending"}
print(tasks)
```

**What to observe:**

Results can be joined by id.

### Example 2: Limit concurrency

A semaphore caps simultaneous work.

```python
import asyncio

limit = asyncio.Semaphore(2)
print(limit)
```

**What to observe:**

The limit is explicit.

### Example 3: Handle cancellation

Cleanup belongs in `finally`.

```python
async def work():
    try:
        await asyncio.sleep(0)
    finally:
        print("cleanup")
```

**What to observe:**

Cleanup runs when the task ends or is cancelled.

### Example 4: Make operation idempotent

A repeated report write should not duplicate evidence.

```python
seen = {"fixture-a"}
print("fixture-a" in seen)
```

**What to observe:**

The identity check prevents duplicate handling.

### Example 5: Aggregate states

Mixed success needs a clear summary.

```python
print({"ok": 3, "failed": 1, "cancelled": 1})
```

**What to observe:**

The summary preserves failure states.

## Execution trace

The coordinator creates identified tasks, limits concurrency, handles cancellation and cleanup, aggregates state, and refuses to call a partial run complete.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| no cancellation | tasks keep running | propagate cancellation |
| shared mutable list | ordering/races | return identified results |
| duplicate retries | duplicate effects | require idempotence |
| ignore cancelled | incomplete run looks green | count cancelled |
| no cleanup | resources remain | use finally/context managers |

## Security application

Use `asyncio` with local sleeps and fixtures only. Do not create concurrent network clients for public systems.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the evidence, output, edge case, and limitation requested by each question.

## Finish line

Run `python -m course_days.day113`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Reliable concurrency is bounded, cancellable, and explicit about partial completion.

## Limitations

Concurrency correctness is difficult to prove with small tests; production systems need load, failure, and operational testing.

[← Day 112](../day_112_performance_and_backpressure/day_112_performance_and_backpressure.md) · [Day index](../DAY_INDEX.md) · [Day 114 →](../day_114_failure_injection_and_recovery/day_114_failure_injection_and_recovery.md)
