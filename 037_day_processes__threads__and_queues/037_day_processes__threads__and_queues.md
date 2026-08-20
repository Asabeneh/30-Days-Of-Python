# Day 37: Processes, Threads, and Queues

[← Day 36](../036_day_timeouts_and_resource_limits/036_day_timeouts_and_resource_limits.md) · [Day index](../DAY_INDEX.md) · [Day 38 →](../038_day_async_i_o/038_day_async_i_o.md)

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

Concurrency can reduce waiting time, but it also creates shared state, ordering, cancellation, and resource problems. A security tool should prefer predictable bounded concurrency over maximum parallelism.

## Prerequisites

Complete Day 36 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 37

## The problem

Process several local fixture items with a small worker pool and preserve a safe result for each item.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Lesson

### Vocabulary

A **thread** shares memory within one process. A **process** has a separate memory space. A **queue** coordinates producers and consumers. A **race condition** occurs when outcome depends on timing.

## Worked examples

### Example 1: Use a thread pool

Threads suit small I/O waits in a local fixture.

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(str.upper, ["a", "b"]))
print(results)
```

**What to observe:**

`['A', 'B']`

### Example 2: Use a process pool carefully

Separate processes have higher overhead and clearer memory boundaries.

```python
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(abs, [-2, 3]))
print(results)
```

**What to observe:**

`[2, 3]`

### Example 3: Bound work

The worker count is an explicit resource choice.

```python
max_workers = min(4, 2)
print(max_workers)
```

**What to observe:**

The tool never creates an unbounded number of workers.

### Example 4: Queue a result

A queue can separate collection from processing.

```python
from queue import Queue

queue = Queue()
queue.put({"status": "accepted"})
print(queue.get())
```

**What to observe:**

The result moves through the queue.

### Example 5: Preserve errors

A worker failure must be returned or raised, not silently discarded.

```python
def safe_call(function, value):
    try:
        return {"ok": True, "value": function(value)}
    except Exception as error:
        return {"ok": False, "error": type(error).__name__}
```

**What to observe:**

The caller can count failed work.

## Execution trace

The coordinator creates a bounded set of workers, submits local work, collects results, and shuts down the pool. Ordering and failure behavior are part of the report contract.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| one worker per item | resource exhaustion | cap workers |
| shared mutable state | results depend on timing | return values or protect state |
| swallow worker errors | incomplete report looks successful | preserve error records |
| assume order | output changes run to run | attach identifiers and sort explicitly |
| no shutdown | threads/processes remain | use a context manager |

## Security application

Run concurrency only over local synthetic records. Do not use it to increase scanning, guessing, or request volume against another system.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run every requested command, create the requested artifact, and record the limitation the exercise asks you to name.

## Finish line

Run `python -m course_days.day037`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Concurrency is a coordination problem with a resource budget, not a magic speed switch.

## Limitations

Concurrency bugs can be nondeterministic and platform-dependent. Tests should use small deterministic fixtures and explicit synchronization.

[← Day 36](../036_day_timeouts_and_resource_limits/036_day_timeouts_and_resource_limits.md) · [Day index](../DAY_INDEX.md) · [Day 38 →](../038_day_async_i_o/038_day_async_i_o.md)
