# Day 57: Symmetric and Asymmetric Cryptography

[← Day 56](../056_day_password_verification/056_day_password_verification.md) · [Day index](../DAY_INDEX.md) · [Day 58 →](../058_day_safe_serialization/058_day_safe_serialization.md)

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

Encryption protects confidentiality under a key model. Symmetric systems use a shared secret; asymmetric systems use a public/private pair. Choosing one requires knowing who must encrypt, decrypt, sign, or verify.

## Prerequisites

Complete Day 56. Run the repository checks and use only the local fixtures and explicitly authorized loopback services.

## Outcomes

By the end of this lesson, you can:

- explain the protocol or security property in plain language
- run and modify every worked example
- test a normal, boundary, and failure case
- identify the trust boundary and residual risk
- connect the concept to the numbered cybersecurity exercises

## The problem

Map security requirements to a key model and use library-level pseudocode without inventing cryptography.

## Security boundary

Use synthetic data, local fixtures, and loopback-only demonstrations. This lesson does not authorize scanning, interception, credential use, remote command execution, or changes to systems you do not own.

## Lesson

### Vocabulary

Symmetric encryption uses one secret key for both directions. Asymmetric cryptography uses a public key and private key. A signature proves possession of a private key under a verification model.

## Worked examples

### Example 1: Map the key roles

Start with who needs which operation.

```python
roles = {
    "encrypt_to_recipient": "recipient public key",
    "decrypt": "recipient private key",
    "sign": "sender private key",
    "verify": "sender public key",
}
print(roles)
```

**What to observe:**

The roles are explicit.

### Example 2: Symmetric key scope

A shared key requires secure distribution to every participant.

```python
plan = {
    "key": "shared secret",
    "holders": ["sender", "receiver"],
    "purpose": "training bundle",
}
print(plan)
```

**What to observe:**

The distribution assumption is visible.

### Example 3: Public versus private

A public key can be distributed; the private key must remain controlled.

```python
keys = {"public": "shareable identifier", "private": "protected secret"}
print(keys)
```

**What to observe:**

The example never contains real key material.

### Example 4: Authenticated encryption

Confidentiality without integrity is incomplete for many messages.

```python
requirements = ["confidentiality", "integrity", "nonce uniqueness"]
print(requirements)
```

**What to observe:**

The required properties are listed before implementation.

### Example 5: Reject homemade crypto

Use a reviewed library and documented construction.

```python
decision = {"implementation": "approved library", "custom_cipher": False}
print(decision)
```

**What to observe:**

The project avoids inventing primitives.

## Execution trace

The design identifies parties and properties, chooses key roles, selects an approved construction, verifies before parsing, and documents key storage, rotation, and failure behavior.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| encryption equals authenticity | sender is assumed | add authentication/signature model |
| public key is secret | distribution becomes impossible | protect private key |
| reuse nonce | construction assumptions break | follow library protocol |
| roll own cipher | subtle flaws | use reviewed libraries |
| key in source | repository leak compromises data | externalize key management |

## Security application

Keep this lesson design-level and use training libraries only. Do not encrypt personal records, build a covert channel, or exchange keys with an external system.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested local command, inspect its output, and record the limitation asked for by the exercise.

## Finish line

Run `python -m course_days.day057`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Cryptographic design begins with parties, properties, and key roles; the primitive is only one part of the system.

## Limitations

Real cryptographic deployments require expert review, key management, algorithm agility, side-channel analysis, and operational controls.

[← Day 56](../056_day_password_verification/056_day_password_verification.md) · [Day index](../DAY_INDEX.md) · [Day 58 →](../058_day_safe_serialization/058_day_safe_serialization.md)
