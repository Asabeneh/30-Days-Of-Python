# Day 59: Secure Errors and Logging

[← Day 58](../058_day_safe_serialization/058_day_safe_serialization.md) · [Day index](../DAY_INDEX.md) · [Day 60 →](../060_day_project__tamper_evident_case_bundle/060_day_project__tamper_evident_case_bundle.md)

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

Crypto and network failures are sensitive. An error should help an operator recover without revealing keys, passwords, raw tokens, internal paths, or attacker-controlled formatting.

## Prerequisites

Complete Day 58. Run the repository checks and use only the local fixtures and explicitly authorized loopback services.

## Outcomes

By the end of this lesson, you can:

- explain the protocol or security property in plain language
- run and modify every worked example
- test a normal, boundary, and failure case
- identify the trust boundary and residual risk
- connect the concept to the numbered cybersecurity exercises

## The problem

Design error categories and structured logs for a local case bundle without exposing secret material.

## Security boundary

Use synthetic data, local fixtures, and loopback-only demonstrations. This lesson does not authorize scanning, interception, credential use, remote command execution, or changes to systems you do not own.

## Lesson

### Vocabulary

An error category groups a failure for a caller. A safe message is actionable but minimized. A correlation identifier links events without copying sensitive data.

## Worked examples

### Example 1: Define safe categories

Categories help callers choose behavior.

```python
categories = {
    "input": "reject",
    "timeout": "retry-or-stop",
    "integrity": "stop",
    "bug": "escalate",
}
print(categories)
```

**What to observe:**

The policy differs by failure.

### Example 2: Redact fields

Redaction happens on structured data before formatting.

```python
safe = {"event": "decrypt_failed", "case_id": "training", "key": "[REDACTED]"}
print(safe)
```

**What to observe:**

The key is not output.

### Example 3: Use correlation

A short case id helps search without exposing a raw payload.

```python
record = {"case_id": "training-059", "error": "integrity_check_failed"}
print(record)
```

**What to observe:**

The record is searchable and minimal.

### Example 4: Avoid exception echo

User-controlled text should not become an unescaped log record.

```python
message = "bad\nvalue".replace("\n", "\\n")
print(message)
```

**What to observe:**

The line break is visible as text.

### Example 5: Separate user message and debug detail

Different audiences need different fields and access.

```python
public = {"status": "rejected", "reason": "invalid record"}
debug = {"internal": "training-only detail"}
print(public)
```

**What to observe:**

The safe output is intentionally smaller.

## Execution trace

The boundary catches a known category, creates a minimal safe record, attaches a correlation id, and stores restricted detail separately or omits it.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| log key or plaintext | cryptographic material leaks | redact and minimize |
| echo attacker text | fake records or injection | encode control characters |
| same message for all | operators cannot act | categorize failures |
| detail in exception | traceback leaks paths and values | safe public error plus restricted detail |
| retry integrity failure | tampered data is processed | stop and review |

## Security application

Use synthetic errors and fake keys only. Tests must assert that key-like strings, passwords, and raw payloads cannot appear in safe logs.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested local command, inspect its output, and record the limitation asked for by the exercise.

## Finish line

Run `python -m course_days.day059`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Secure error handling preserves enough information to act while withholding material that increases harm.

## Limitations

Logging policy depends on retention, access, correlation, and incident procedures outside the Python function.

[← Day 58](../058_day_safe_serialization/058_day_safe_serialization.md) · [Day index](../DAY_INDEX.md) · [Day 60 →](../060_day_project__tamper_evident_case_bundle/060_day_project__tamper_evident_case_bundle.md)
