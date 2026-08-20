# Day 115: Privacy and Retention

[← Day 114](../day_114_failure_injection_and_recovery/day_114_failure_injection_and_recovery.md) · [Day index](../DAY_INDEX.md) · [Day 116 →](../day_116_research_and_source_evaluation/day_116_research_and_source_evaluation.md)

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

Security tooling often collects more personal data than it needs. Privacy engineering asks what is necessary, how long it is kept, who can access it, and how it is deleted.

## Prerequisites

Complete Day 114. Work from a clean virtual environment and use only local synthetic fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using it
- run and modify all worked examples
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Design a retention policy for synthetic case records and implement minimization and deletion metadata.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, destructive actions, persistence, or processing of private data.

## Lesson

### Vocabulary

Data minimization collects only what is needed. Retention is how long data is kept. A deletion record proves an action without preserving the deleted content.

## Worked examples

### Example 1: Classify fields

Not every field has the same sensitivity.

```python
fields = {"case_id": "low", "message": "medium", "token": "secret"}
print(fields)
```

**What to observe:**

Sensitivity is explicit.

### Example 2: Minimize report

A report can omit raw message and token.

```python
report = {"case_id": "training-115", "status": "review"}
print(report)
```

**What to observe:**

Only necessary fields remain.

### Example 3: Set retention

Retention needs purpose and period.

```python
policy = {"purpose": "training", "retention_days": 7, "owner": "course"}
print(policy)
```

**What to observe:**

The policy is concrete.

### Example 4: Record deletion

The record can prove deletion without retaining content.

```python
deletion = {"case_id": "training-115", "deleted_at": "now", "content": "not stored"}
print(deletion)
```

**What to observe:**

The audit record is minimized.

### Example 5: Restrict access

Access policy is part of privacy.

```python
print({"readers": ["student"], "public": False})
```

**What to observe:**

The data is not public.

## Execution trace

The system classifies and minimizes fields, applies retention, restricts access, deletes content at the end of purpose, and keeps only a safe deletion record.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| collect just in case | privacy scope grows | minimize |
| retention forever | breach impact grows | define purpose and period |
| deletion without proof | control is unreviewable | keep safe metadata |
| hash equals anonymize | identifiers remain linkable | assess re-identification |
| public sample data | private fields leak | synthetic fixtures |

## Security application

Use synthetic case data only. Do not process personal logs, names, messages, or credentials.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the evidence, output, edge case, and limitation requested by each question.

## Finish line

Run `python -m course_days.day115`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Privacy is a lifecycle of collection, purpose, access, retention, minimization, and deletion.

## Limitations

Privacy obligations vary by jurisdiction and organization; a short policy is not legal advice.

[← Day 114](../day_114_failure_injection_and_recovery/day_114_failure_injection_and_recovery.md) · [Day index](../DAY_INDEX.md) · [Day 116 →](../day_116_research_and_source_evaluation/day_116_research_and_source_evaluation.md)
