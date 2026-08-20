# Day 111: Security Tool Architecture

[← Day 110](../110_day_project__secure_delivery_pipeline/110_day_project__secure_delivery_pipeline.md) · [Day index](../DAY_INDEX.md) · [Day 112 →](../112_day_performance_and_backpressure/112_day_performance_and_backpressure.md)

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

A mature security tool needs clear modules for collection, parsing, policy, storage, reporting, and orchestration. Architecture prevents a proof-of-concept from becoming an unreviewable tool.

## Prerequisites

Complete Day 110. Work from a clean virtual environment and use only local synthetic fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using it
- run and modify all worked examples
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Design module boundaries and dependency directions for a local detection utility.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, destructive actions, persistence, or processing of private data.

## Lesson

### Vocabulary

Architecture describes components and relationships. Dependency direction says which layer may call which. An adapter translates external systems into internal interfaces.

## Worked examples

### Example 1: Name layers

Layering makes responsibility reviewable.

```python
layers = ["cli", "orchestration", "policy", "domain", "adapters"]
print(layers)
```

**What to observe:**

The layers are ordered.

### Example 2: Define an interface

A protocol lets tests substitute a fixture reader.

```python
class Reader:
    def read(self, limit: int) -> list[str]:
        raise NotImplementedError
```

**What to observe:**

The caller depends on behavior.

### Example 3: Keep policy pure

Policy should not open files or make network calls.

```python
def decide(event):
    return event.get("severity", 0) >= 7
```

**What to observe:**

The decision is testable.

### Example 4: Use an adapter

The adapter owns external representation.

```python
adapter = {"source": "fixture", "target": "domain event"}
print(adapter)
```

**What to observe:**

The translation boundary is explicit.

### Example 5: Document dependencies

A diagram is only useful if it states direction.

```python
edges = [("cli", "orchestration"), ("orchestration", "policy"), ("adapters", "domain")]
print(edges)
```

**What to observe:**

The architecture can be reviewed.

## Execution trace

Input enters through adapters/CLI, becomes domain data, passes pure policy, and returns through reporting; external effects remain at edges.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| policy imports network | tests have side effects | keep policy pure |
| circular layers | changes spread | define direction |
| adapter leaks raw fields | domain trusts source | normalize |
| global configuration | hidden coupling | inject dependencies |
| diagram without tests | architecture is aspirational | test boundaries |

## Security application

Use local fixtures and dependency injection. Do not add remote connectors or agentic execution.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the evidence, output, edge case, and limitation requested by each question.

## Finish line

Run `python -m course_days.day111`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Good architecture makes trust boundaries and effects visible in module relationships.

## Limitations

Architecture cannot guarantee correct policy, safe deployment, or team ownership.

[← Day 110](../110_day_project__secure_delivery_pipeline/110_day_project__secure_delivery_pipeline.md) · [Day index](../DAY_INDEX.md) · [Day 112 →](../112_day_performance_and_backpressure/112_day_performance_and_backpressure.md)
