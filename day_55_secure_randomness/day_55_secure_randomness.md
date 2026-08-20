# Day 55: Secure Randomness and Token Design

[← Day 54](../day_54_hmac_and_authenticity/day_54_hmac_and_authenticity.md) · [Day index](../DAY_INDEX.md) · [Day 56 →](../day_56_password_verification/day_56_password_verification.md)

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

Security tokens, salts, nonces, and identifiers require unpredictable values. Ordinary pseudo-random helpers are useful for games and simulations but are not interchangeable with a cryptographic random source.

## Prerequisites

Complete Day 54. Run the repository checks and use only the local fixtures and explicitly authorized loopback services.

## Outcomes

By the end of this lesson, you can:

- explain the protocol or security property in plain language
- run and modify every worked example
- test a normal, boundary, and failure case
- identify the trust boundary and residual risk
- connect the concept to the numbered cybersecurity exercises

## The problem

Generate a short-lived training token, encode it safely, and explain its purpose and lifecycle.

## Security boundary

Use synthetic data, local fixtures, and loopback-only demonstrations. This lesson does not authorize scanning, interception, credential use, remote command execution, or changes to systems you do not own.

## Lesson

### Vocabulary

Entropy measures uncertainty. A nonce is intended for one use. A salt is a public random value mixed into password derivation. A token is a bearer value whose secrecy matters.

## Worked examples

### Example 1: Generate bytes

`secrets` is designed for security-sensitive randomness.

```python
import secrets

value = secrets.token_bytes(16)
print(len(value))
```

**What to observe:**

`16` bytes, without printing the secret.

### Example 2: Encode for a URL

Text transport needs a safe representation.

```python
token = secrets.token_urlsafe(16)
print(len(token))
```

**What to observe:**

A URL-safe token string length is visible, not its value.

### Example 3: Use a nonce once

The protocol should record use rather than reuse blindly.

```python
nonce = secrets.token_bytes(12)
used = {nonce}
print(nonce in used)
```

**What to observe:**

`True` after recording it.

### Example 4: Compare a token safely

A token check should not reveal the expected value.

```python
import hmac

provided = "training"
expected = "training"
print(hmac.compare_digest(provided, expected))
```

**What to observe:**

`True` without printing a real secret.

### Example 5: Set expiry

Randomness does not replace lifecycle policy.

```python
token_record = {"created": "now", "expires": "soon", "purpose": "training"}
print(token_record)
```

**What to observe:**

The token has purpose and expiry metadata.

## Execution trace

The secure generator creates unpredictable bytes, the protocol encodes them, records purpose and lifecycle without storing the secret in logs, and verification compares supplied material safely.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| use `random` for tokens | values may be predictable | use `secrets` |
| print token | bearer secret leaks | log presence or a safe identifier |
| reuse nonce | protocol assumptions fail | enforce uniqueness per key/context |
| no expiry | leaked token remains useful | set lifetime and revoke |
| low entropy | guessing becomes easier | choose adequate bytes for the threat model |

## Security application

Generate only disposable training tokens and delete them after the exercise. Never use a course token for a real account or service.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested local command, inspect its output, and record the limitation asked for by the exercise.

## Finish line

Run `python -m course_days.day055`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Secure randomness supplies unpredictable values; lifecycle and access policy decide whether those values remain useful to an attacker.

## Limitations

No random generator fixes a leaked token, weak authentication, replay, or poor key management.

[← Day 54](../day_54_hmac_and_authenticity/day_54_hmac_and_authenticity.md) · [Day index](../DAY_INDEX.md) · [Day 56 →](../day_56_password_verification/day_56_password_verification.md)
