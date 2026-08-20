# Day 61: Local Service Architecture

[← Day 60](../060_day_project__tamper_evident_case_bundle/060_day_project__tamper_evident_case_bundle.md) · [Day index](../DAY_INDEX.md) · [Day 62 →](../062_day_request_parsing_and_validation/062_day_request_parsing_and_validation.md)

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

A web service is a pipeline of request parsing, validation, authorization, business logic, and response construction. Drawing those boundaries before coding makes security behavior testable.

## Prerequisites

Complete Day 60. Use only the local course fixtures, loopback services, and synthetic records described by the lesson.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using the tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state the trust boundary and residual risk
- complete the numbered cybersecurity exercises

## The problem

Sketch a local case API that accepts a request, validates it, checks authorization, and returns a safe response without touching a real account.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, interception, exploit delivery, real-user profiling, or changes to systems you do not own.

## Lesson

### Vocabulary

A request is untrusted input. A handler coordinates work. A service layer applies policy. A repository stores data. A response is an output boundary.

## Worked examples

### Example 1: Draw the flow

Make the stages visible before implementation.

```python
stages = ["request", "parse", "validate", "authorize", "service", "response"]
print(" -> ".join(stages))
```

**What to observe:**

The request path is explicit.

### Example 2: Use a typed request

A boundary object separates raw data from internal fields.

```python
request = {"case_id": "training-061", "action": "read"}
print(request)
```

**What to observe:**

The raw input is still subject to validation.

### Example 3: Return a result

Handlers should return data and status rather than print.

```python
response = {"status": 200, "body": {"case_id": "training-061"}}
print(response)
```

**What to observe:**

The response is structured.

### Example 4: Name a trust boundary

The service should state where authorization is checked.

```python
boundary = {
    "untrusted": "HTTP body",
    "trusted_after": "validated authorization decision",
}
print(boundary)
```

**What to observe:**

The policy location is visible.

### Example 5: Keep local scope

A training service needs an explicit target and reset.

```python
scope = {"host": "127.0.0.1", "data": "synthetic", "reset": "delete training DB"}
print(scope)
```

**What to observe:**

The service is bounded.

## Execution trace

The request enters as bytes or text, becomes a parsed object, passes schema and authorization checks, reaches a service function, and returns a minimal response. No stage should silently skip the previous boundary.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| auth in UI only | direct calls bypass it | enforce at service boundary |
| handler does everything | tests and review are hard | separate layers |
| return raw exception | internal data leaks | safe error response |
| global mutable state | tests affect each other | explicit dependencies |
| local API becomes public | scope expands | bind to loopback and document |

## Security application

Build only a local synthetic API. Do not add account management, public deployment, credential collection, or real case data.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples as a starting point, then record the requested output, edge case, and limitation.

## Finish line

Run `python -m course_days.day061`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A service is a sequence of trust-boundary transitions; each transition must validate, authorize, and preserve evidence.

## Limitations

Architecture diagrams are hypotheses until tests and deployment configuration enforce the boundaries.

[← Day 60](../060_day_project__tamper_evident_case_bundle/060_day_project__tamper_evident_case_bundle.md) · [Day index](../DAY_INDEX.md) · [Day 62 →](../062_day_request_parsing_and_validation/062_day_request_parsing_and_validation.md)
