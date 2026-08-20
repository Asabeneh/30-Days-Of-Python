# Day 26: Structured Logging and Redaction

[← Day 25](../day_25_type_hints_and_static_checks/day_25_type_hints_and_static_checks.md) · [Day index](../DAY_INDEX.md) · [Day 27 →](../day_27_git_and_code_review/day_27_git_and_code_review.md)

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

Logs are evidence for operators and input for future tools. Unstructured messages are hard to query; unredacted messages can leak secrets.

## Prerequisites

Complete Day 25 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 26

## The problem

Emit a machine-readable event with a stable schema while ensuring token, password, and private message values do not appear.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Lesson

### Vocabulary

A **log record** has fields such as time, level, event, and context. **Structured logging** emits fields rather than only prose. **Redaction** removes or masks sensitive values.

## Worked examples

### Example 1: Use logging levels

Levels communicate importance to operators.

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("triage_started")
```

**What to observe:**

The logger emits a timestamped informational record.

### Example 2: Log fields carefully

A structured dictionary keeps safe context separate from a secret.

```python
record = {"event": "token_check", "case_id": "training", "token_present": True}
print(record)
```

**What to observe:**

Only presence is logged.

### Example 3: Redact known keys

A field policy is more reliable than searching for one literal secret.

```python
SENSITIVE = {"password", "token", "api_key"}


def redact(record):
    return {k: "[REDACTED]" if k in SENSITIVE else v for k, v in record.items()}
```

**What to observe:**

Sensitive keys receive the marker.

### Example 4: Prevent newline injection

A user-controlled message can forge visual log lines.

```python
def one_line(text):
    return text.replace("\r", "\\r").replace("\n", "\\n")
```

**What to observe:**

Newlines are represented instead of creating new records.

### Example 5: Add correlation context

A case identifier connects records without copying raw evidence.

```python
log_record = {
    "case_id": "training-026",
    "event": "record_rejected",
    "reason": "bad severity",
}
```

**What to observe:**

The record can be searched by case and event.

## Execution trace

A record is assembled, sensitive keys are transformed, free text is made single-line, and only then is it emitted. Redaction must happen before formatting or serialization.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| log full request | secrets enter retained logs | log selected safe fields |
| redact after formatting | alternate representations leak | redact structured data first |
| user newline unescaped | fake records appear | neutralize line breaks |
| no retention rule | evidence remains forever | define retention and access |
| use logs as truth | collection error is ignored | record source and confidence |

## Security application

Create structured logs only from synthetic events. Test that secret values and newline payloads never appear in output, and document retention and access assumptions.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run every requested command, create the requested artifact, and record the limitation the exercise asks you to name.

## Finish line

Run `python -m course_days.day026`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A log is a durable data boundary; make its schema, redaction, provenance, and retention explicit.

## Limitations

Redaction is not perfect if secrets appear in exception traces, process arguments, memory, or nested fields. Minimize collection as well as masking.

[← Day 25](../day_25_type_hints_and_static_checks/day_25_type_hints_and_static_checks.md) · [Day index](../DAY_INDEX.md) · [Day 27 →](../day_27_git_and_code_review/day_27_git_and_code_review.md)
