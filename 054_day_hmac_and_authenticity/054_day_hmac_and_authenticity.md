# Day 54: HMAC and Message Authenticity

[← Day 53](../053_day_hashes_and_integrity/053_day_hashes_and_integrity.md) · [Day index](../DAY_INDEX.md) · [Day 55 →](../055_day_secure_randomness/055_day_secure_randomness.md)

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

A keyed message authentication code adds a secret key to integrity checking. It can show that a verifier with the same key accepts a message, but it does not provide non-repudiation and depends on key protection.

## Prerequisites

Complete Day 53. Run the repository checks and use only the local fixtures and explicitly authorized loopback services.

## Outcomes

By the end of this lesson, you can:

- explain the protocol or security property in plain language
- run and modify every worked example
- test a normal, boundary, and failure case
- identify the trust boundary and residual risk
- connect the concept to the numbered cybersecurity exercises

## The problem

Authenticate a synthetic record with an HMAC, verify it before parsing, and reject a changed message.

## Security boundary

Use synthetic data, local fixtures, and loopback-only demonstrations. This lesson does not authorize scanning, interception, credential use, remote command execution, or changes to systems you do not own.

## Lesson

### Vocabulary

HMAC is a keyed integrity/authenticity construction. A tag is the resulting authenticator. Constant-time comparison reduces timing leakage in comparisons.

## Worked examples

### Example 1: Create a tag

The same key and bytes produce the same tag.

```python
import hmac, hashlib

key = b"training-key"
message = b"case=54"
tag = hmac.new(key, message, hashlib.sha256).hexdigest()
print(tag[:12])
```

**What to observe:**

A deterministic tag prefix.

### Example 2: Verify with compare_digest

Do not use ordinary early-exit comparison for a secret tag.

```python
expected = hmac.new(key, message, hashlib.sha256).hexdigest()
print(hmac.compare_digest(tag, expected))
```

**What to observe:**

`True`

### Example 3: Detect tampering

A changed message produces a different tag.

```python
changed = b"case=55"
actual = hmac.new(key, changed, hashlib.sha256).hexdigest()
print(hmac.compare_digest(tag, actual))
```

**What to observe:**

`False`

### Example 4: Verify before parse

Do not let unverified bytes control a parser or action.

```python
if not hmac.compare_digest(tag, expected):
    raise ValueError("authentication failed")
record = message.decode("utf-8")
```

**What to observe:**

Only an authenticated message is decoded.

### Example 5: Name key scope

A key should have an owner and purpose.

```python
key_policy = {
    "purpose": "training bundle",
    "holder": "test process",
    "rotation": "reset each run",
}
print(key_policy)
```

**What to observe:**

The key lifecycle is documented.

## Execution trace

The sender computes a tag over exact bytes; the receiver recomputes it with the expected key, compares safely, and only then parses or acts on the message.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| compare with `==` | timing behavior is less deliberate | use `compare_digest` |
| verify after parse | attacker controls parser input | verify first |
| reuse key everywhere | compromise spreads | define key scope and rotation |
| expose key in logs | authenticity is lost | minimize and protect keys |
| call HMAC non-repudiation | shared key cannot identify one signer | state the property accurately |

## Security application

Use a fake key stored in the test fixture or generated per run. Never paste a real credential or send HMAC material to an external service.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested local command, inspect its output, and record the limitation asked for by the exercise.

## Finish line

Run `python -m course_days.day054`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> HMAC authenticates bytes to parties that share a protected key; verification must precede interpretation.

## Limitations

HMAC does not solve key distribution, compromise, replay, or non-repudiation.

[← Day 53](../053_day_hashes_and_integrity/053_day_hashes_and_integrity.md) · [Day index](../DAY_INDEX.md) · [Day 55 →](../055_day_secure_randomness/055_day_secure_randomness.md)
