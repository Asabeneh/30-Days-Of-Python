# Day 92: Asset Inventory for Authorized Testing

[← Day 91](../day_91_rules_of_engagement/day_91_rules_of_engagement.md) · [Day index](../DAY_INDEX.md) · [Day 93 →](../day_93_safe_service_discovery/day_93_safe_service_discovery.md)

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

A test plan cannot be safe if the tester does not know what exists, who owns it, and which environment is in scope. Inventory is the foundation for bounded assessment.

## Prerequisites

Complete Day 91. Use only the local fixtures and explicit loopback assessment scope supplied by the course.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using a tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Create an inventory for a local application and classify each asset by owner, environment, data, and permitted action.

## Security boundary

This lesson is educational and authorized-lab-only. It does not authorize public scanning, credential guessing, exploitation, interception, persistence, or changes to systems you do not own.

## Lesson

### Vocabulary

An asset is a system or data resource. An owner is responsible for it. An environment is development, test, staging, or production. Scope is the allowed subset.

## Worked examples

### Example 1: Model an asset

Start with identity and owner.

```python
asset = {
    "id": "svc-92",
    "name": "training-api",
    "owner": "course",
    "environment": "test",
}
print(asset)
```

**What to observe:**

The asset is classified.

### Example 2: Record data

Data sensitivity affects test methods.

```python
asset["data"] = "synthetic case records"
print(asset)
```

**What to observe:**

The data is non-production.

### Example 3: Set scope

An inventory item must say what is permitted.

```python
asset["allowed"] = ["read health", "invalid local input"]
print(asset)
```

**What to observe:**

The allowed actions are narrow.

### Example 4: Mark exclusions

Explicit exclusions prevent accidental testing.

```python
asset["excluded"] = ["production", "real identities"]
print(asset)
```

**What to observe:**

The exclusions are visible.

### Example 5: Check inventory freshness

Stale inventory can make a test target wrong.

```python
asset["last_verified"] = "2026-08-20"
print(asset["last_verified"])
```

**What to observe:**

The date is recorded.

## Execution trace

The tester verifies asset identity, owner, environment, data classification, inclusion, exclusions, and freshness before planning any test.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| test by IP only | wrong asset is touched | use owner and asset id |
| environment omitted | production is hit | classify environment |
| stale list | retired target is tested | verify freshness |
| data unknown | privacy risk | classify data |
| inventory equals authorization | presence is not permission | require ROE |

## Security application

Use a repository inventory and local service fixture. Do not enumerate real networks or assets.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the requested evidence, expected behavior, edge case, and limitation.

## Finish line

Run `python -m course_days.day092`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> An inventory answers what exists and who owns it; rules of engagement decide what may be tested.

## Limitations

Inventories drift and may themselves contain sensitive infrastructure data.

[← Day 91](../day_91_rules_of_engagement/day_91_rules_of_engagement.md) · [Day index](../DAY_INDEX.md) · [Day 93 →](../day_93_safe_service_discovery/day_93_safe_service_discovery.md)
