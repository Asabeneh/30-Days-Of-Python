# Day 63: Authentication and Authorization

[← Day 62](../062_day_request_parsing_and_validation/062_day_request_parsing_and_validation.md) · [Day index](../DAY_INDEX.md) · [Day 64 →](../064_day_injection_and_parameterized_queries/064_day_injection_and_parameterized_queries.md)

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

Authentication asks who or what is calling. Authorization asks whether that identity may perform this action on this resource. Confusing them creates security gaps.

## Prerequisites

Complete Day 62. Use only the local course fixtures, loopback services, and synthetic records described by the lesson.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using the tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state the trust boundary and residual risk
- complete the numbered cybersecurity exercises

## The problem

Model a local case-read request with a fictional identity, role, resource owner, and explicit authorization decision.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, interception, exploit delivery, real-user profiling, or changes to systems you do not own.

## Lesson

### Vocabulary

Authentication establishes an identity claim. Authorization evaluates a policy. A role is a group of permissions. An object-level check compares the requested resource to the caller’s allowed scope.

## Worked examples

### Example 1: Represent identity

The identity object should not contain a password.

```python
identity = {"subject": "student-63", "roles": ["analyst"]}
print(identity)
```

**What to observe:**

The subject and roles are explicit.

### Example 2: Define a permission

Permissions should name action and resource.

```python
permission = {"action": "read", "resource": "case"}
print(permission)
```

**What to observe:**

A policy can compare these fields.

### Example 3: Check role policy

A role check is only one layer.

```python
allowed_roles = {"analyst", "mentor"}
print(set(identity["roles"]) & allowed_roles)
```

**What to observe:**

The intersection is non-empty for the fictional identity.

### Example 4: Check the object

The caller must be allowed to access this specific case.

```python
request = {"subject": "student-63", "case_id": "training-63"}
owned = {"student-63": {"training-63"}}
print(request["case_id"] in owned[request["subject"]])
```

**What to observe:**

The object decision is explicit.

### Example 5: Fail closed

Missing identity or permission should not become anonymous access.

```python
if not identity or not permission:
    raise PermissionError("authorization required")
```

**What to observe:**

The request stops before the service.

## Execution trace

The request presents an identity claim, authentication verifies it outside the business rule, authorization checks action and object scope, and only then does the service run.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| identity equals permission | every authenticated user can act | check action and object |
| role-only check | horizontal access leak | compare resource scope |
| client-side authorization | direct API call bypasses it | enforce server-side |
| fail open | missing identity gets access | fail closed |
| log credentials | authentication material leaks | log subject and outcome only |

## Security application

Use fictional identities and cases. Do not implement login collection or connect to a real identity provider in the lesson.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples as a starting point, then record the requested output, edge case, and limitation.

## Finish line

Run `python -m course_days.day063`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Authentication names a caller; authorization limits what that caller may do here and now.

## Limitations

A code sample cannot prove identity, protect sessions, or replace an organization’s access-control policy.

[← Day 62](../062_day_request_parsing_and_validation/062_day_request_parsing_and_validation.md) · [Day index](../DAY_INDEX.md) · [Day 64 →](../064_day_injection_and_parameterized_queries/064_day_injection_and_parameterized_queries.md)
