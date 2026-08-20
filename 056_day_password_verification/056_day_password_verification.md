# Day 56: Password Verification and Slow Derivation

[← Day 55](../055_day_secure_randomness/055_day_secure_randomness.md) · [Day index](../DAY_INDEX.md) · [Day 57 →](../057_day_symmetric_and_asymmetric_crypto/057_day_symmetric_and_asymmetric_crypto.md)

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

Passwords are human-chosen and often guessable. Systems should store a verifier derived with an approved password-hashing scheme, not the password or a fast raw hash.

## Prerequisites

Complete Day 55. Run the repository checks and use only the local fixtures and explicitly authorized loopback services.

## Outcomes

By the end of this lesson, you can:

- explain the protocol or security property in plain language
- run and modify every worked example
- test a normal, boundary, and failure case
- identify the trust boundary and residual risk
- connect the concept to the numbered cybersecurity exercises

## The problem

Compare a training password against a stored verifier while keeping the password out of source, logs, and output.

## Security boundary

Use synthetic data, local fixtures, and loopback-only demonstrations. This lesson does not authorize scanning, interception, credential use, remote command execution, or changes to systems you do not own.

## Lesson

### Vocabulary

A password hash uses a salt and work factor. A salt prevents identical passwords from sharing a digest. A verifier lets the system check a candidate without storing the password.

## Worked examples

### Example 1: Use a salt conceptually

The salt is public metadata but changes the derived output.

```python
salt = b"training-salt"
password = b"example"
print(len(salt), len(password))
```

**What to observe:**

The values have different roles.

### Example 2: Do not use a raw SHA

A fast general hash is not a password verifier.

```python
import hashlib

print(hashlib.sha256(b"example").hexdigest()[:12])
```

**What to observe:**

This digest is shown only to explain why the wrong primitive is tempting.

### Example 3: Use a standard password library

Approved libraries encode salt and cost decisions.

```python
# Pseudocode shape: use the selected library’s documented API.
verifier = {"algorithm": "approved-password-kdf", "cost": "reviewed"}
print(verifier)
```

**What to observe:**

The implementation choice is documented rather than improvised.

### Example 4: Compare without logging

The candidate should exist only for the verification call.

```python
candidate = "input-from-user"
print({"candidate_received": bool(candidate)})
```

**What to observe:**

Only presence is reported.

### Example 5: Handle failure equally

A failed verification should not reveal which account detail was wrong.

```python
print({"authenticated": False, "reason": "generic"})
```

**What to observe:**

The response avoids account enumeration.

## Execution trace

The system receives a candidate, applies the stored verifier’s salt and cost, compares the derived result, and returns a generic outcome. The password never enters a report or source file.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| store plaintext | one leak exposes every password | store a verifier |
| use raw SHA | guessing is too cheap | use an approved password KDF |
| fixed salt | identical passwords correlate | use a unique salt per password |
| log candidates | credentials leak | never log password material |
| detailed login errors | account enumeration | use a generic failure response |

## Security application

Use only a fictional training password and a standard library or documented course dependency. Do not implement a password cracker or test against real accounts.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested local command, inspect its output, and record the limitation asked for by the exercise.

## Finish line

Run `python -m course_days.day056`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Password verification is a deliberately expensive comparison with protected lifecycle, not a reversible encryption operation.

## Limitations

Work factors age, breaches happen, and authentication needs rate limits, MFA, recovery, and monitoring in addition to password storage.

[← Day 55](../055_day_secure_randomness/055_day_secure_randomness.md) · [Day index](../DAY_INDEX.md) · [Day 57 →](../057_day_symmetric_and_asymmetric_crypto/057_day_symmetric_and_asymmetric_crypto.md)
