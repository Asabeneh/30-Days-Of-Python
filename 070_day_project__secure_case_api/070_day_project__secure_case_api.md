# Day 70: Project: Secure Case API

[← Day 69](../069_day_supply_chain_and_exceptional_conditions/069_day_supply_chain_and_exceptional_conditions.md) · [Day index](../DAY_INDEX.md) · [Day 71 →](../071_day_telemetry_and_event_schemas/071_day_telemetry_and_event_schemas.md)

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

This project applies request validation, authorization, injection defense, output handling, browser controls, outbound policy, secure defaults, and dependency thinking to a single local API design.

## Prerequisites

Complete Day 69. Use only the local course fixtures, loopback services, and synthetic records described by the lesson.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using the tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state the trust boundary and residual risk
- complete the numbered cybersecurity exercises

## The problem

Build a local API for synthetic cases with read-only routes, explicit authorization, bounded JSON, safe errors, and a threat model.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, interception, exploit delivery, real-user profiling, or changes to systems you do not own.

## Lesson

### Vocabulary

A route maps an HTTP method and path to behavior. An object-level authorization check compares the caller to the requested case. An API contract specifies request and response fields.

## Worked examples

### Example 1: Define routes

A small allowlist is easier to review.

```python
routes = {
    "GET /cases/{id}": "read synthetic case",
    "POST /cases": "disabled in training",
}
print(routes)
```

**What to observe:**

The supported surface is explicit.

### Example 2: Validate a body

The API accepts only fields needed for the action.

```python
allowed = {"case_id", "limit"}
body = {"case_id": "training-70", "limit": 10}
print(set(body) <= allowed)
```

**What to observe:**

The body fits the schema.

### Example 3: Authorize an object

The caller must have scope over this case.

```python
permissions = {"student-70": {"training-70"}}
print("training-70" in permissions["student-70"])
```

**What to observe:**

The object check is separate from identity.

### Example 4: Use safe SQL

The repository layer must parameterize values.

```python
query = "SELECT id, title FROM cases WHERE id = ?"
print(query)
```

**What to observe:**

The query is fixed.

### Example 5: Return safe errors

The API response should not expose traceback or secret fields.

```python
response = {"status": 400, "error": "invalid request", "request_id": "training-70"}
print(response)
```

**What to observe:**

The response is useful but minimal.

## Execution trace

The request enters through a bounded parser, passes auth and object checks, reaches a parameterized repository call, and returns a schema-controlled response with safe errors.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| broad route surface | more unreviewed behavior | allowlist routes |
| auth without object check | case data crosses tenants | check resource scope |
| raw SQL | injection risk | parameterize |
| return model internals | secret fields leak | serialize allowlisted fields |
| public bind | training API is exposed | loopback-only |

## Security application

The API is local, synthetic, read-only, and resettable. The project README must contain its route contract, scope, threat model, tests, example requests, and limitations.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples as a starting point, then record the requested output, edge case, and limitation.

## Finish line

Run `python -m course_days.day070`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A secure API is a sequence of explicit contracts: route, input, identity, authorization, storage, output, and failure.

## Limitations

This project is not production-ready and does not implement a complete identity provider, deployment hardening, or privacy program.

[← Day 69](../069_day_supply_chain_and_exceptional_conditions/069_day_supply_chain_and_exceptional_conditions.md) · [Day index](../DAY_INDEX.md) · [Day 71 →](../071_day_telemetry_and_event_schemas/071_day_telemetry_and_event_schemas.md)
