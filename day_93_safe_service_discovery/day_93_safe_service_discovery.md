# Day 93: Safe Service Discovery

[← Day 92](../day_92_asset_inventory/day_92_asset_inventory.md) · [Day index](../DAY_INDEX.md) · [Day 94 →](../day_94_cve_and_severity_reasoning/day_94_cve_and_severity_reasoning.md)

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

Discovery can be useful in a disposable lab and dangerous on an unowned network. The safe pattern is to use a supplied target list and verify one endpoint rather than scan ranges.

## Prerequisites

Complete Day 92. Use only the local fixtures and explicit loopback assessment scope supplied by the course.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using a tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Check one approved local service from an explicit inventory and report unavailable versus closed without scanning.

## Security boundary

This lesson is educational and authorized-lab-only. It does not authorize public scanning, credential guessing, exploitation, interception, persistence, or changes to systems you do not own.

## Lesson

### Vocabulary

Discovery identifies reachable services. An allowlist is a fixed target set. A health check is a known request. A timeout limits waiting.

## Worked examples

### Example 1: Read targets

Discovery begins with approved inventory, not guesses.

```python
targets = [{"host": "127.0.0.1", "port": 8000, "purpose": "training"}]
print(targets)
```

**What to observe:**

The target is explicit.

### Example 2: Validate endpoint

Reject targets outside the lab policy.

```python
target = targets[0]
print(target["host"] == "127.0.0.1")
```

**What to observe:**

Only loopback passes this example.

### Example 3: Check one service

A connection attempt is still an authorized action.

```python
check = {"target": "127.0.0.1:8000", "timeout": 1, "request": "health"}
print(check)
```

**What to observe:**

The operation is bounded.

### Example 4: Classify result

Unavailable and refused are different observations.

```python
print({"status": "unavailable", "meaning": "no conclusion about cause"})
```

**What to observe:**

The interpretation is neutral.

### Example 5: Stop after inventory

Do not turn one check into a range scan.

```python
print({"targets_checked": 1, "range_scan": False})
```

**What to observe:**

Scope is recorded.

## Execution trace

The tool loads an approved target, validates the host and port, performs one finite health check, records the transport result, and exits without expanding the target set.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| scan subnet | unauthorized reconnaissance | use one supplied target |
| retry many ports | scope expands | fixed endpoint |
| timeout means closed | cause is overclaimed | report unknown/unavailable |
| follow redirects | target changes | revalidate or disable |
| no log of scope | review cannot verify | record target count |

## Security application

Use loopback and a disposable service only. No range scans, port sweeps, banner grabbing, or public targets.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the requested evidence, expected behavior, edge case, and limitation.

## Finish line

Run `python -m course_days.day093`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Safe discovery is an approved inventory check with a finite target and neutral result interpretation.

## Limitations

A failed connection can be caused by policy, routing, service state, or timeout; it does not reveal intent.

[← Day 92](../day_92_asset_inventory/day_92_asset_inventory.md) · [Day index](../DAY_INDEX.md) · [Day 94 →](../day_94_cve_and_severity_reasoning/day_94_cve_and_severity_reasoning.md)
