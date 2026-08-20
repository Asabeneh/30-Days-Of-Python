# Day 112: Performance and Backpressure

[← Day 111](../111_day_security_tool_architecture/111_day_security_tool_architecture.md) · [Day index](../DAY_INDEX.md) · [Day 113 →](../113_day_advanced_concurrency/113_day_advanced_concurrency.md)

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

Performance is a security property when slow or oversized work can exhaust a service. Measure first, then choose bounded queues, batching, streaming, and rejection policies.

## Prerequisites

Complete Day 111. Work from a clean virtual environment and use only local synthetic fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using it
- run and modify all worked examples
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Process a synthetic stream with a bounded queue and explain what happens when the consumer is slower than the producer.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, destructive actions, persistence, or processing of private data.

## Lesson

### Vocabulary

Throughput is work per time. Latency is time per operation. Backpressure limits producers. A queue is a buffer. Rejection is an explicit resource policy.

## Worked examples

### Example 1: Measure a count

Begin with a simple workload measurement.

```python
processed = 100
seconds = 2
print(processed / seconds)
```

**What to observe:**

50 records per second.

### Example 2: Bound a queue

A finite queue prevents unlimited memory growth.

```python
from queue import Queue

queue = Queue(maxsize=3)
print(queue.maxsize)
```

**What to observe:**

The capacity is explicit.

### Example 3: Reject or wait

When full, the producer needs a policy.

```python
policy = {"full_queue": "wait briefly then reject", "report": "backpressure"}
print(policy)
```

**What to observe:**

The behavior is documented.

### Example 4: Batch work

Batches can reduce overhead but increase latency and memory.

```python
batch = [1, 2, 3]
print({"size": len(batch), "max": 100})
```

**What to observe:**

The batch has a bound.

### Example 5: Report incomplete work

Dropped or rejected work must be visible.

```python
print({"accepted": 98, "rejected": 2, "complete": False})
```

**What to observe:**

The result does not look perfect.

## Execution trace

The producer creates bounded work, the queue applies backpressure, the consumer processes within a resource budget, and the report records accepted, rejected, and incomplete items.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| benchmark synthetic only | real workload differs | state assumptions |
| unbounded queue | memory exhaustion | cap capacity |
| drop silently | detection gaps | report rejection |
| batch unlimited | latency/memory grows | cap batch |
| optimize before measure | complexity without benefit | measure first |

## Security application

Use small synthetic workloads and local timing. Do not generate load against any external system.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the evidence, output, edge case, and limitation requested by each question.

## Finish line

Run `python -m course_days.day112`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Performance safety is bounded work plus honest accounting of what was rejected or delayed.

## Limitations

Benchmarks vary by hardware, input, Python version, and contention; capacity needs production measurement.

[← Day 111](../111_day_security_tool_architecture/111_day_security_tool_architecture.md) · [Day index](../DAY_INDEX.md) · [Day 113 →](../113_day_advanced_concurrency/113_day_advanced_concurrency.md)
