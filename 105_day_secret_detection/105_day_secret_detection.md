# Day 105: Secret Detection and Remediation

[← Day 104](../104_day_sbom_and_provenance/104_day_sbom_and_provenance.md) · [Day index](../DAY_INDEX.md) · [Day 106 →](../106_day_containers_and_isolation/106_day_containers_and_isolation.md)

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

Secrets often enter repositories through convenience. Detection is one layer; prevention, removal from history, rotation, and safe reporting complete the response.

## Prerequisites

Complete Day 104. Work from a clean virtual environment and use only local synthetic fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using it
- run and modify all worked examples
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Scan synthetic files for token-like values, report locations without printing secrets, and write a remediation plan.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, destructive actions, persistence, or processing of private data.

## Lesson

### Vocabulary

A secret is sensitive authentication material. Detection finds candidates. Rotation invalidates a credential and issues a replacement. False positives are benign matches.

## Worked examples

### Example 1: Use a candidate pattern

Patterns identify candidates, not confirmed secrets.

```python
import re

pattern = re.compile(r"token=[^\s]+")
print(bool(pattern.search("token=training-secret")))
```

**What to observe:**

A candidate is found.

### Example 2: Redact the match

The report should not reproduce the value.

```python
text = "token=training-secret"
print(re.sub(r"(token=)[^\s]+", r"\1[REDACTED]", text))
```

**What to observe:**

The marker replaces the value.

### Example 3: Record location

File and line are useful without full content.

```python
finding = {"file": "fixture.txt", "line": 1, "kind": "token-like"}
print(finding)
```

**What to observe:**

The location is safe enough for training.

### Example 4: Plan rotation

Removing a string from the working tree does not revoke a real credential.

```python
plan = ["revoke", "issue replacement", "remove from history if needed", "review access"]
print(plan)
```

**What to observe:**

The response steps are explicit.

### Example 5: Handle false positives

A pattern may match a placeholder or test value.

```python
print({"candidate": "training-secret", "confirmed": False, "review": True})
```

**What to observe:**

The result is not overclaimed.

## Execution trace

The scanner reads bounded files, identifies candidate patterns, redacts values before reporting, records location and confidence, and directs real secret response toward revocation and access review.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| print match | secret leaks in report | redact before output |
| delete only | credential remains valid | revoke and rotate |
| scan private tree | scope violation | use fixtures |
| pattern equals secret | false positives | review candidates |
| forget history | old commit retains value | assess history and access |

## Security application

Use placeholders only. If a real credential is ever exposed, stop, notify the owner privately, and follow the repository security policy; do not paste it into issues or reports.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the evidence, output, edge case, and limitation requested by each question.

## Finish line

Run `python -m course_days.day105`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Secret detection finds candidates; remediation removes utility through revocation, rotation, history handling, and access review.

## Limitations

Detection patterns miss formats and can create false positives; real secret response requires the credential owner.

[← Day 104](../104_day_sbom_and_provenance/104_day_sbom_and_provenance.md) · [Day index](../DAY_INDEX.md) · [Day 106 →](../106_day_containers_and_isolation/106_day_containers_and_isolation.md)
