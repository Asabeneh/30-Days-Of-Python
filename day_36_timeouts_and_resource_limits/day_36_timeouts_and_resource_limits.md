# Day 36: Timeouts, Resource Limits, and Backpressure

[← Day 35](../day_35_users_and_permissions/day_35_users_and_permissions.md) · [Day index](../DAY_INDEX.md) · [Day 37 →](../day_37_processes__threads__and_queues/day_37_processes__threads__and_queues.md)

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

A security tool can fail by doing too much work. Timeouts, maximum sizes, and backpressure turn resource behavior into an explicit contract.

## Prerequisites

Complete Day 35 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 36

## The problem

Run a bounded local task and show how the caller reacts when the task exceeds the allowed time or output budget.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Lesson

### Vocabulary

A **timeout** limits elapsed time. A **resource limit** bounds work or memory. **Backpressure** slows producers when consumers cannot keep up.

## Worked examples

### Example 1: Set a timeout

The caller should not wait forever for a child.

```python
import subprocess

subprocess.run(["python", "-c", "print('ok')"], timeout=2)
```

**What to observe:**

The task completes within two seconds.

### Example 2: Handle timeout

A timeout is a distinct result that should be reported.

```python
try:
    subprocess.run(["python", "-c", "import time; time.sleep(2)"], timeout=0.1)
except subprocess.TimeoutExpired:
    print("timed out")
```

**What to observe:**

`timed out`

### Example 3: Bound bytes

A byte budget prevents a large result from filling memory.

```python
def bounded_bytes(data, limit):
    return data[:limit], len(data) > limit
```

**What to observe:**

The result includes both a preview and a truncation signal.

### Example 4: Use a queue bound

A bounded queue applies backpressure to producers.

```python
from queue import Queue

queue = Queue(maxsize=2)
queue.put("event")
print(queue.qsize())
```

**What to observe:**

The queue reports one pending event.

### Example 5: Choose a policy

A timeout should lead to an explicit status, not a silent empty result.

```python
result = {"status": "timed_out", "complete": False}
print(result)
```

**What to observe:**

The report says work was incomplete.

## Execution trace

The operation starts with finite time and output budgets; when a budget is reached, the tool records incomplete work and releases resources.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| timeout only the parent | child continues | terminate and clean up the child |
| no output cap | memory grows | stream or truncate |
| unbounded queue | producer overwhelms consumer | set `maxsize` |
| retry immediately | overload worsens | use bounded retries and backoff |
| report empty success | missing data is hidden | state timeout/truncation |

## Security application

Use short local sleeps and small synthetic outputs. Do not create load against another system or use resource experiments that could affect the host.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run every requested command, create the requested artifact, and record the limitation the exercise asks you to name.

## Finish line

Run `python -m course_days.day036`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A limit is part of correctness: incomplete work must be visible, and cleanup must happen when the limit is reached.

## Limitations

Limits can create false negatives. Production systems need capacity planning, cancellation semantics, and monitoring in addition to a number in code.

[← Day 35](../day_35_users_and_permissions/day_35_users_and_permissions.md) · [Day index](../DAY_INDEX.md) · [Day 37 →](../day_37_processes__threads__and_queues/day_37_processes__threads__and_queues.md)
