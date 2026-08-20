# Day 114: Failure Injection and Recovery

[← Day 113](../113_day_advanced_concurrency/113_day_advanced_concurrency.md) · [Day index](../DAY_INDEX.md) · [Day 115 →](../115_day_privacy_and_retention/115_day_privacy_and_retention.md)

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

A resilient tool is not one that never fails; it is one whose failure modes are expected, bounded, observable, and recoverable without corrupting evidence.

## Prerequisites

Complete Day 113. Work from a clean virtual environment and use only local synthetic fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using it
- run and modify all worked examples
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Inject controlled timeout, malformed data, and write failures into a local pipeline and verify recovery behavior.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, destructive actions, persistence, or processing of private data.

## Lesson

### Vocabulary

Failure injection deliberately creates a test condition. Recovery restores an acceptable state. A retryable failure differs from a permanent failure. A circuit breaker stops repeated attempts.

## Worked examples

### Example 1: Inject a timeout

A fake function makes the failure reproducible.

```python
def fake_timeout():
    raise TimeoutError("training timeout")


try:
    fake_timeout()
except TimeoutError as error:
    print(type(error).__name__)
```

**What to observe:**

The timeout is classified.

### Example 2: Recover with fallback

A fallback must not claim full success.

```python
result = {"status": "degraded", "complete": False}
print(result)
```

**What to observe:**

The degraded state is visible.

### Example 3: Stop repeated attempts

A breaker prevents repeated failure amplification.

```python
breaker = {"state": "open", "reason": "repeated training failures"}
print(breaker)
```

**What to observe:**

Further work is stopped.

### Example 4: Preserve partial output

A checkpoint can make recovery resumable.

```python
checkpoint = {"processed": 7, "last_id": "fixture-7"}
print(checkpoint)
```

**What to observe:**

The progress is explicit.

### Example 5: Test recovery

The test asserts state and cleanup, not only no exception.

```python
assert result["status"] == "degraded"
print("recovery contract passed")
```

**What to observe:**

The recovery behavior is tested.

## Execution trace

The injected failure enters a known category, the pipeline stops or falls back according to policy, records partial state, cleans resources, and reports incomplete work.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| catch all | failure looks successful | classify |
| retry permanent error | repeated damage | stop |
| fallback as full data | users overtrust | mark degraded |
| no checkpoint | restart duplicates work | persist safe progress |
| inject in production | outage | disposable fixture only |

## Security application

Inject failures only into pure local components or disposable fixtures. Never deliberately disrupt a real service.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the evidence, output, edge case, and limitation requested by each question.

## Finish line

Run `python -m course_days.day114`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Resilience is explicit failure state plus bounded recovery and cleanup.

## Limitations

Failure injection in a toy pipeline cannot prove production resilience or recovery-time objectives.

[← Day 113](../113_day_advanced_concurrency/113_day_advanced_concurrency.md) · [Day index](../DAY_INDEX.md) · [Day 115 →](../115_day_privacy_and_retention/115_day_privacy_and_retention.md)
