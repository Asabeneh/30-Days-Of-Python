# Day 47: Packet-Capture Fixtures and Layered Parsing

[← Day 46](../day_46_tls_and_certificate_validation/day_46_tls_and_certificate_validation.md) · [Day index](../DAY_INDEX.md) · [Day 48 →](../day_48_rate_limits_and_retries/day_48_rate_limits_and_retries.md)

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

Packet captures are rich evidence, but a beginner can easily mistake a decoded field for complete context. A fixture-first parser makes layers, offsets, and truncation visible.

## Prerequisites

Complete Day 46. Run the repository checks and use only the local fixtures and explicitly authorized loopback services.

## Outcomes

By the end of this lesson, you can:

- explain the protocol or security property in plain language
- run and modify every worked example
- test a normal, boundary, and failure case
- identify the trust boundary and residual risk
- connect the concept to the numbered cybersecurity exercises

## The problem

Parse a saved, synthetic packet summary rather than sniffing a live interface.

## Security boundary

Use synthetic data, local fixtures, and loopback-only demonstrations. This lesson does not authorize scanning, interception, credential use, remote command execution, or changes to systems you do not own.

## Lesson

### Vocabulary

A packet is a sequence of bytes. A protocol layer interprets part of it. A capture fixture is saved evidence with collection limits and metadata.

## Worked examples

### Example 1: Represent a frame

A fixture can describe layers without needing live capture.

```python
frame = {"number": 1, "layers": ["ethernet", "ip", "tcp"], "captured": True}
print(frame)
```

**What to observe:**

The layer list is explicit.

### Example 2: Parse a bounded header

Never index bytes without checking length.

```python
data = b"GET /"
if len(data) < 4:
    raise ValueError("truncated")
print(data[:4])
```

**What to observe:**

`b'GET '`

### Example 3: Preserve offsets

Offsets let a reviewer locate a field in a fixture.

```python
field = {"name": "payload", "start": 40, "length": 5}
print(field)
```

**What to observe:**

The evidence location is retained.

### Example 4: Mark truncation

A capture may omit bytes by design.

```python
capture = {"captured_bytes": 64, "original_bytes": 120, "truncated": True}
print(capture)
```

**What to observe:**

The result cannot be interpreted as a complete payload.

### Example 5: Separate observation

A decoded flag is not automatically malicious.

```python
finding = {"flag": "SYN", "label": "observed", "confidence": "low"}
print(finding)
```

**What to observe:**

The neutral label preserves uncertainty.

## Execution trace

The parser validates fixture length, decodes one layer, records offsets and truncation, and returns observations with provenance rather than a story about an attacker.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| sniff live interface | scope and privacy fail | use saved fixtures |
| assume full payload | truncated data is overread | check lengths and flags |
| decode without layer | fields are misaligned | parse in order |
| packet equals event | context is missing | record only observation |
| store sensitive capture | evidence leaks | use synthetic fixtures and minimize |

## Security application

Use only supplied packet summaries or synthetic byte strings. Do not capture other people’s traffic or build a live interception tool.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested local command, inspect its output, and record the limitation asked for by the exercise.

## Finish line

Run `python -m course_days.day047`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A packet parser transforms bounded bytes into layered observations with offsets and completeness metadata.

## Limitations

A capture can be truncated, malformed, encrypted, spoofed, or detached from application context.

[← Day 46](../day_46_tls_and_certificate_validation/day_46_tls_and_certificate_validation.md) · [Day index](../DAY_INDEX.md) · [Day 48 →](../day_48_rate_limits_and_retries/day_48_rate_limits_and_retries.md)
