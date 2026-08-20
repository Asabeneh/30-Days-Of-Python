# Day 68: Misconfiguration and Secure Defaults

[← Day 67](../day_67_ssrf_and_outbound_controls/day_67_ssrf_and_outbound_controls.md) · [Day index](../DAY_INDEX.md) · [Day 69 →](../day_69_supply_chain_and_exceptional_conditions/day_69_supply_chain_and_exceptional_conditions.md)

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

Many security failures are ordinary configuration choices: debug enabled, permissive origins, verbose errors, weak cookies, unlimited bodies, or development keys.

## Prerequisites

Complete Day 67. Use only the local course fixtures, loopback services, and synthetic records described by the lesson.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using the tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state the trust boundary and residual risk
- complete the numbered cybersecurity exercises

## The problem

Create a configuration review that identifies unsafe defaults without changing a real service.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, interception, exploit delivery, real-user profiling, or changes to systems you do not own.

## Lesson

### Vocabulary

A secure default is safe when the user does nothing. A misconfiguration is a deployed setting that violates intended security or reliability policy.

## Worked examples

### Example 1: Represent settings

A review needs names and effective values.

```python
settings = {
    "debug": False,
    "body_limit": 1_000_000,
    "allow_origins": ["https://training.local"],
}
print(settings)
```

**What to observe:**

The effective settings are inspectable.

### Example 2: Flag debug

Debug can reveal internals and must be false outside local development.

```python
if settings["debug"]:
    print("review: debug enabled")
```

**What to observe:**

The review creates a finding.

### Example 3: Check a bounded body

A finite body limit is a resource control.

```python
print(0 < settings["body_limit"] <= 10_000_000)
```

**What to observe:**

The value is checked against policy.

### Example 4: Review defaults

An empty allowlist should not silently mean allow all.

```python
origins = settings.get("allow_origins", [])
print(origins)
```

**What to observe:**

Missing configuration is visible.

### Example 5: Make failure safe

Invalid security configuration should stop startup in a controlled way.

```python
if not origins:
    raise RuntimeError("no trusted origin configured")
```

**What to observe:**

The service does not start with an ambiguous policy.

## Execution trace

The reviewer loads effective configuration, compares each setting to a policy, reports unsafe or missing values, and fails closed when a required security choice is absent.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| development default in production | debug or test keys remain | separate environments |
| empty means all | missing origin opens access | fail closed |
| config review only once | deployment drifts | review effective runtime settings |
| print full config | secrets leak | redact sensitive values |
| no owner | findings remain open | assign remediation |

## Security application

Use a static synthetic settings dictionary. Do not inspect or change a production deployment.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples as a starting point, then record the requested output, edge case, and limitation.

## Finish line

Run `python -m course_days.day068`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A secure default reduces harm when configuration is omitted; an explicit policy still needs review and enforcement.

## Limitations

Configuration scanners can miss code paths, secret stores, deployment overrides, and runtime behavior.

[← Day 67](../day_67_ssrf_and_outbound_controls/day_67_ssrf_and_outbound_controls.md) · [Day index](../DAY_INDEX.md) · [Day 69 →](../day_69_supply_chain_and_exceptional_conditions/day_69_supply_chain_and_exceptional_conditions.md)
