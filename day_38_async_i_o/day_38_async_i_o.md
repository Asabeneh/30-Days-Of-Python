# Day 38: Async I/O and Bounded Awaiting

[← Day 37](../day_37_processes__threads__and_queues/day_37_processes__threads__and_queues.md) · [Day index](../DAY_INDEX.md) · [Day 39 →](../day_39_host_inventories/day_39_host_inventories.md)

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

Asynchronous code lets one task wait while another makes progress, but it introduces cancellation, ordering, and concurrency limits. It is useful for cooperative local I/O, not a reason to remove authorization.

## Prerequisites

Complete Day 37 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 38

## The problem

Run several local coroutines with a semaphore and collect successes, failures, and cancellation cleanly.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Lesson

### Vocabulary

A **coroutine** is an awaitable computation. `await` yields control. A **task** schedules a coroutine. A **semaphore** limits concurrent entry.

## Worked examples

### Example 1: Define a coroutine

Calling an async function creates a coroutine; awaiting runs it.

```python
import asyncio


async def label(value):
    await asyncio.sleep(0)
    return value.upper()


print(asyncio.run(label("ok")))
```

**What to observe:**

`OK`

### Example 2: Gather tasks

`gather` waits for several awaitables.

```python
async def main():
    values = await asyncio.gather(label("a"), label("b"))
    print(values)


asyncio.run(main())
```

**What to observe:**

`['A', 'B']`

### Example 3: Bound concurrency

A semaphore keeps only a small number of tasks inside a resource section.

```python
limit = asyncio.Semaphore(2)


async def bounded_work(value):
    async with limit:
        await asyncio.sleep(0)
        return value
```

**What to observe:**

At most two calls enter the section at once.

### Example 4: Handle cancellation

Cancellation is a normal lifecycle event that needs cleanup.

```python
async def safe_task():
    try:
        await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("cancelled")
        raise
```

**What to observe:**

The task reports cancellation and re-raises it.

### Example 5: Preserve result identity

Attach an identifier because completion order may differ from input order.

```python
results = {"fixture-a": {"status": "ok"}}
print(results)
```

**What to observe:**

The caller can merge results deterministically.

## Execution trace

The event loop schedules awaitable work; the semaphore limits concurrent operations; cancellation and exceptions become explicit result states.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| call async function without await | coroutine never runs | await or schedule it |
| unbounded gather | too many tasks | use a semaphore and batch |
| ignore cancellation | cleanup is skipped | use `try/finally` and re-raise |
| assume completion order | records mismatch | keep identifiers |
| mix blocking I/O | event loop stalls | isolate or use async-compatible APIs |

## Security application

Use `asyncio.sleep` and local fixtures only. Do not turn an async example into a high-volume network client or use it against unapproved endpoints.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run every requested command, create the requested artifact, and record the limitation the exercise asks you to name.

## Finish line

Run `python -m course_days.day038`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Async I/O is cooperative scheduling with explicit limits, cancellation, and result identity.

## Limitations

Async code does not make operations harmless, faster in every workload, or safe to direct at a public system.

[← Day 37](../day_37_processes__threads__and_queues/day_37_processes__threads__and_queues.md) · [Day index](../DAY_INDEX.md) · [Day 39 →](../day_39_host_inventories/day_39_host_inventories.md)
