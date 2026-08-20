# Day 58: Safe Serialization and Deserialization

[← Day 57](../057_day_symmetric_and_asymmetric_crypto/057_day_symmetric_and_asymmetric_crypto.md) · [Day index](../DAY_INDEX.md) · [Day 59 →](../059_day_secure_errors_and_logging/059_day_secure_errors_and_logging.md)

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

Serialization turns objects into data for storage or transport. Some formats are data-only; others can execute behavior when loaded. Security code must choose a format and validate its schema.

## Prerequisites

Complete Day 57. Run the repository checks and use only the local fixtures and explicitly authorized loopback services.

## Outcomes

By the end of this lesson, you can:

- explain the protocol or security property in plain language
- run and modify every worked example
- test a normal, boundary, and failure case
- identify the trust boundary and residual risk
- connect the concept to the numbered cybersecurity exercises

## The problem

Serialize a synthetic case record with JSON and reject unexpected fields before it reaches policy.

## Security boundary

Use synthetic data, local fixtures, and loopback-only demonstrations. This lesson does not authorize scanning, interception, credential use, remote command execution, or changes to systems you do not own.

## Lesson

### Vocabulary

Serialization encodes an object. Deserialization reconstructs data. A schema defines allowed fields and types. A data-only format does not execute code by itself.

## Worked examples

### Example 1: Serialize JSON

JSON keeps the example data-oriented.

```python
import json

record = {"case_id": "training-058", "severity": 3}
text = json.dumps(record, sort_keys=True)
print(text)
```

**What to observe:**

A deterministic JSON string.

### Example 2: Parse JSON

Parsing creates ordinary Python values that still require validation.

```python
loaded = json.loads(text)
print(type(loaded).__name__, loaded["severity"])
```

**What to observe:**

A dictionary and integer.

### Example 3: Allow only fields

A schema boundary prevents unexpected data from silently entering policy.

```python
allowed = {"case_id", "severity"}
print(set(loaded) <= allowed)
```

**What to observe:**

`True` for the example.

### Example 4: Reject unsafe shapes

A list where a dictionary is expected should fail explicitly.

```python
if not isinstance(loaded, dict):
    raise ValueError("record must be an object")
```

**What to observe:**

The policy rejects the wrong shape.

### Example 5: Avoid executable loaders

Do not load untrusted Python object formats in a security boundary.

```python
policy = {"accepted": ["json"], "rejected": ["executable-object-format"]}
print(policy)
```

**What to observe:**

The format decision is documented.

## Execution trace

The loader parses data into primitive values, checks top-level type, allowed keys, field types, sizes, and required fields, then constructs the internal model.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| load executable objects | untrusted data can run behavior | use data-only format |
| trust JSON shape | malformed data reaches code | validate schema |
| accept unlimited nesting | parser resource abuse | bound depth and size |
| serialize secrets | reports leak material | minimize fields |
| ignore version | format drift breaks tools | version the schema |

## Security application

Use only JSON fixtures under the repository. Add tests for unknown keys, oversized strings, wrong types, missing fields, and malformed JSON.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested local command, inspect its output, and record the limitation asked for by the exercise.

## Finish line

Run `python -m course_days.day058`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Serialization is a data boundary; choose a non-executable format and validate before constructing trusted internal objects.

## Limitations

JSON itself does not solve authorization, secrets, resource limits, or business-logic validation.

[← Day 57](../057_day_symmetric_and_asymmetric_crypto/057_day_symmetric_and_asymmetric_crypto.md) · [Day index](../DAY_INDEX.md) · [Day 59 →](../059_day_secure_errors_and_logging/059_day_secure_errors_and_logging.md)
