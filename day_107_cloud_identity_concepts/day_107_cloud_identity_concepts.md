# Day 107: Cloud Identity Concepts

[← Day 106](../day_106_containers_and_isolation/day_106_containers_and_isolation.md) · [Day index](../DAY_INDEX.md) · [Day 108 →](../day_108_configuration_drift/day_108_configuration_drift.md)

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

Cloud security often fails when an identity receives more permission than its task needs or when roles, resources, and trust relationships are unclear. This lesson stays conceptual and local.

## Prerequisites

Complete Day 106. Work from a clean virtual environment and use only local synthetic fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using it
- run and modify all worked examples
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Model a least-privilege role for a synthetic report worker without connecting to a cloud account.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, destructive actions, persistence, or processing of private data.

## Lesson

### Vocabulary

An identity is a principal. A role is a set of permissions. A resource is an object. Least privilege grants only required actions. A trust policy controls who may assume a role.

## Worked examples

### Example 1: Name a principal

Use a fictional workload identity.

```python
principal = {"name": "training-report-worker", "type": "workload"}
print(principal)
```

**What to observe:**

The identity is explicit.

### Example 2: List actions

Permissions should be specific.

```python
policy = {
    "actions": ["read_case_fixture", "write_report"],
    "resources": ["training-only"],
}
print(policy)
```

**What to observe:**

The actions and resources are bounded.

### Example 3: Deny broad actions

A negative permission makes the boundary visible.

```python
print({"not_allowed": ["admin", "delete_source", "public_network"]})
```

**What to observe:**

The role is narrow.

### Example 4: Record trust

Role assumption has a caller condition.

```python
trust = {"allowed_principal": "training-runner", "environment": "test"}
print(trust)
```

**What to observe:**

The trust relationship is explicit.

### Example 5: Review unused access

Permissions should be reduced when no longer needed.

```python
print({"review": "remove unused actions", "cadence": "documented"})
```

**What to observe:**

The lifecycle is part of least privilege.

## Execution trace

The designer names principal, actions, resources, trust conditions, and lifecycle review before any cloud configuration is applied.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| admin role for convenience | blast radius grows | narrow actions/resources |
| resource wildcard | access crosses cases | scope resource identifiers |
| identity equals trust | any caller assumes role | define trust policy |
| credentials in code | secrets leak | use platform identity mechanisms |
| never review | stale access persists | schedule review |

## Security application

Use fictional policy objects only. Do not log into or modify a cloud account for this lesson.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the evidence, output, edge case, and limitation requested by each question.

## Finish line

Run `python -m course_days.day107`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Cloud identity is a relationship among principal, action, resource, and trust conditions.

## Limitations

Provider semantics vary; production identity design needs platform specialists and actual ownership.

[← Day 106](../day_106_containers_and_isolation/day_106_containers_and_isolation.md) · [Day index](../DAY_INDEX.md) · [Day 108 →](../day_108_configuration_drift/day_108_configuration_drift.md)
