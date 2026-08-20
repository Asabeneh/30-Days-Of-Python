# Day 50: Project: Local Service Monitor

[← Day 49](../049_day_network_baselines/049_day_network_baselines.md) · [Day index](../DAY_INDEX.md) · [Day 51 →](../051_day_trust_boundaries_and_threat_models/051_day_trust_boundaries_and_threat_models.md)

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

This project combines sockets, HTTP parsing, TLS reasoning, timeouts, retries, and baselines into a local monitor that reports bounded observations instead of acting like an internet scanner.

## Prerequisites

Complete Day 49. Run the repository checks and use only the local fixtures and explicitly authorized loopback services.

## Outcomes

By the end of this lesson, you can:

- explain the protocol or security property in plain language
- run and modify every worked example
- test a normal, boundary, and failure case
- identify the trust boundary and residual risk
- connect the concept to the numbered cybersecurity exercises

## The problem

Build a monitor for one supplied loopback service with explicit timeout, retry, endpoint, and cleanup rules.

## Security boundary

Use synthetic data, local fixtures, and loopback-only demonstrations. This lesson does not authorize scanning, interception, credential use, remote command execution, or changes to systems you do not own.

## Lesson

### Vocabulary

A monitor observes availability and response properties. It does not prove health, ownership, or security. An **SLO** is a documented reliability target.

## Worked examples

### Example 1: Define scope

The monitor should carry its one approved endpoint.

```python
scope = {"host": "127.0.0.1", "port": 8000, "path": "/health", "max_attempts": 2}
print(scope)
```

**What to observe:**

The endpoint and budgets are visible.

### Example 2: Record a check

A result should separate transport from application outcome.

```python
result = {"connected": True, "status": 200, "latency_ms": 12}
print(result)
```

**What to observe:**

The fields describe what was observed.

### Example 3: Handle timeout

Timeout is incomplete evidence.

```python
print({"connected": False, "status": None, "reason": "timeout", "complete": False})
```

**What to observe:**

The report avoids a false healthy/unhealthy claim.

### Example 4: Compare baseline

A threshold is a review policy, not proof of compromise.

```python
baseline_ms = 20
observed_ms = 45
print({"latency_changed": observed_ms > baseline_ms * 2})
```

**What to observe:**

The difference is a local review signal.

### Example 5: Reset cleanly

A project must say how to stop and remove generated reports.

```python
cleanup = ["stop local server", "delete training-output"]
print(cleanup)
```

**What to observe:**

The reset plan is explicit.

## Execution trace

The monitor validates scope, performs a finite local check, handles timeout/retry, parses a bounded response, compares safe features, and writes a report with completeness and limitations.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| scan a range | project becomes reconnaissance | one supplied endpoint only |
| no timeout | monitor hangs | finite timeout |
| retry forever | load amplification | finite retry budget |
| call latency attack | timing is ambiguous | report as observation |
| no cleanup | local service persists | document reset |

## Security application

The checkpoint must be loopback-only, read-only, finite, synthetic, and tested with a fake service or fixture. No public host, credential, or scanning feature is allowed.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested local command, inspect its output, and record the limitation asked for by the exercise.

## Finish line

Run `python -m course_days.day050`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A monitor is a bounded observation pipeline with a documented endpoint and uncertainty-aware report.

## Limitations

A local monitor cannot establish availability for all users, application correctness, or security posture.

[← Day 49](../049_day_network_baselines/049_day_network_baselines.md) · [Day index](../DAY_INDEX.md) · [Day 51 →](../051_day_trust_boundaries_and_threat_models/051_day_trust_boundaries_and_threat_models.md)
