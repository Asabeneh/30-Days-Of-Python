# Day 53: Hashes and Integrity

[← Day 52](../day_52_encoding_and_unicode/day_52_encoding_and_unicode.md) · [Day index](../DAY_INDEX.md) · [Day 54 →](../day_54_hmac_and_authenticity/day_54_hmac_and_authenticity.md)

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

A cryptographic hash is a compact fingerprint of bytes. It can detect accidental or unauthorized change only when the expected digest comes from a trusted comparison point.

## Prerequisites

Complete Day 52. Run the repository checks and use only the local fixtures and explicitly authorized loopback services.

## Outcomes

By the end of this lesson, you can:

- explain the protocol or security property in plain language
- run and modify every worked example
- test a normal, boundary, and failure case
- identify the trust boundary and residual risk
- connect the concept to the numbered cybersecurity exercises

## The problem

Hash a local fixture, change a copy, and show that the digest changes without calling the digest proof of authorship.

## Security boundary

Use synthetic data, local fixtures, and loopback-only demonstrations. This lesson does not authorize scanning, interception, credential use, remote command execution, or changes to systems you do not own.

## Lesson

### Vocabulary

A hash is a one-way digest. Integrity is the property of detecting change. A collision is two inputs with the same digest; secure hashes make finding one impractical under assumptions.

## Worked examples

### Example 1: Hash a value

The same bytes produce the same digest.

```python
import hashlib

print(hashlib.sha256(b"training").hexdigest())
```

**What to observe:**

A repeatable hexadecimal digest.

### Example 2: Compare bytes

The comparison must be exact and ideally constant-time where relevant.

```python
left = hashlib.sha256(b"a").digest()
right = hashlib.sha256(b"a").digest()
print(left == right)
```

**What to observe:**

`True`

### Example 3: Change one byte

Small input changes produce a different digest.

```python
one = hashlib.sha256(b"training").hexdigest()
two = hashlib.sha256(b"Training").hexdigest()
print(one == two)
```

**What to observe:**

`False`

### Example 4: Hash a file in chunks

Chunking avoids loading a large local fixture at once.

```python
digest = hashlib.sha256()
for chunk in [b"part-1", b"part-2"]:
    digest.update(chunk)
print(digest.hexdigest()[:12])
```

**What to observe:**

The chunked digest is deterministic.

### Example 5: State the trust point

A digest is useful only when the expected digest is trusted.

```python
evidence = {"sha256": "recorded-value", "source": "reviewed-baseline"}
print(evidence)
```

**What to observe:**

The baseline provenance is part of the evidence.

## Execution trace

The bytes are fed to the hash in order; the digest is compared to a trusted baseline; a mismatch becomes an integrity finding, not an identity claim.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| hash equals encryption | digest is treated as secret | explain one-way fingerprint |
| expected digest untrusted | attacker can replace both files | protect the baseline |
| hash text implicitly | reproducibility fails | specify encoding |
| use weak legacy hash | collision risks are higher | choose a current approved hash |
| digest equals authorship | source is overclaimed | separate integrity and authenticity |

## Security application

Hash only synthetic files and copies. Store the expected digest beside an explanation of how it was obtained; do not treat a course digest as proof of a real file’s origin.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested local command, inspect its output, and record the limitation asked for by the exercise.

## Finish line

Run `python -m course_days.day053`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A hash answers whether bytes match a trusted reference; it does not answer who created them.

## Limitations

Hash security depends on the algorithm, input handling, baseline protection, and threat model.

[← Day 52](../day_52_encoding_and_unicode/day_52_encoding_and_unicode.md) · [Day index](../DAY_INDEX.md) · [Day 54 →](../day_54_hmac_and_authenticity/day_54_hmac_and_authenticity.md)
