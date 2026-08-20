# Day 60: Project: Tamper-Evident Case Bundle

[← Day 59](../059_day_secure_errors_and_logging/059_day_secure_errors_and_logging.md) · [Day index](../DAY_INDEX.md) · [Day 61 →](../061_day_local_service_architecture/061_day_local_service_architecture.md)

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

This project combines encoding, hashes, HMAC, serialization, error policy, and provenance into a local case bundle that can detect modification without pretending to be legal chain of custody.

## Prerequisites

Complete Day 59. Run the repository checks and use only the local fixtures and explicitly authorized loopback services.

## Outcomes

By the end of this lesson, you can:

- explain the protocol or security property in plain language
- run and modify every worked example
- test a normal, boundary, and failure case
- identify the trust boundary and residual risk
- connect the concept to the numbered cybersecurity exercises

## The problem

Build a bundle of synthetic JSON records with canonical bytes, a manifest digest, an HMAC tag, and a verification command.

## Security boundary

Use synthetic data, local fixtures, and loopback-only demonstrations. This lesson does not authorize scanning, interception, credential use, remote command execution, or changes to systems you do not own.

## Lesson

### Vocabulary

A manifest lists bundle members. Canonical bytes make hashing reproducible. Tamper-evident means change is detectable under a protected verification key.

## Worked examples

### Example 1: Create canonical JSON

Stable key ordering and encoding make bytes reproducible.

```python
import json

record = {"severity": 7, "case_id": "training-060"}
canonical = json.dumps(record, sort_keys=True, separators=(",", ":")).encode("utf-8")
print(canonical)
```

**What to observe:**

The canonical bytes have no incidental spaces.

### Example 2: Digest a member

The manifest can store a digest for each member.

```python
import hashlib

member_hash = hashlib.sha256(canonical).hexdigest()
print(member_hash[:12])
```

**What to observe:**

A stable digest prefix.

### Example 3: Build a manifest

The manifest names scope and members.

```python
manifest = {
    "version": 1,
    "members": {"record.json": member_hash},
    "scope": "training-only",
}
print(manifest)
```

**What to observe:**

The bundle structure is visible.

### Example 4: Authenticate the manifest

HMAC protects the manifest under the training key.

```python
import hmac

key = b"training-bundle-key"
manifest_bytes = json.dumps(manifest, sort_keys=True).encode()
tag = hmac.new(key, manifest_bytes, hashlib.sha256).hexdigest()
print(tag[:12])
```

**What to observe:**

The tag is stored separately from the secret key.

### Example 5: Verify before reading

Verification must precede interpreting members as trusted.

```python
ok = hmac.compare_digest(tag, hmac.new(key, manifest_bytes, hashlib.sha256).hexdigest())
print(ok)
```

**What to observe:**

`True` for the unchanged training manifest.

## Execution trace

The project canonicalizes data, hashes each member, authenticates the manifest, writes a bounded bundle, and verifies the tag and member digests before reporting a result.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| hash noncanonical JSON | equivalent data hashes differently | define canonical bytes |
| store key with bundle | attacker gets verification key | separate key lifecycle |
| parse before verify | tampered content controls code | verify manifest first |
| claim legal evidence | technical check is overclaimed | state training limitations |
| no version | future parser guesses | version the bundle schema |

## Security application

The bundle is local, synthetic, resettable, and verified with a disposable training key. The README must document exact bytes, key handling, tamper test, cleanup, and limitations.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested local command, inspect its output, and record the limitation asked for by the exercise.

## Finish line

Run `python -m course_days.day060`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A tamper-evident bundle makes changes detectable under a defined byte and key policy; it does not make data true.

## Limitations

This is not a production evidence system, secure archival service, or legal chain-of-custody implementation.

[← Day 59](../059_day_secure_errors_and_logging/059_day_secure_errors_and_logging.md) · [Day index](../DAY_INDEX.md) · [Day 61 →](../061_day_local_service_architecture/061_day_local_service_architecture.md)
