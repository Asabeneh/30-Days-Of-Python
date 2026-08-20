# Day 52: Encoding, Unicode, and Canonical Bytes

[← Day 51](../day_51_trust_boundaries_and_threat_models/day_51_trust_boundaries_and_threat_models.md) · [Day index](../DAY_INDEX.md) · [Day 53 →](../day_53_hashes_and_integrity/day_53_hashes_and_integrity.md)

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

Cryptographic functions operate on bytes, while learners usually see text. Inconsistent encoding or normalization can make two parties hash different data that looks identical.

## Prerequisites

Complete Day 51. Run the repository checks and use only the local fixtures and explicitly authorized loopback services.

## Outcomes

By the end of this lesson, you can:

- explain the protocol or security property in plain language
- run and modify every worked example
- test a normal, boundary, and failure case
- identify the trust boundary and residual risk
- connect the concept to the numbered cybersecurity exercises

## The problem

Convert synthetic text into agreed bytes, preserve the original representation, and explain where normalization belongs.

## Security boundary

Use synthetic data, local fixtures, and loopback-only demonstrations. This lesson does not authorize scanning, interception, credential use, remote command execution, or changes to systems you do not own.

## Lesson

### Vocabulary

Text is Unicode. Bytes are numeric data. Encoding maps text to bytes. Canonicalization chooses one representation for comparison or signing.

## Worked examples

### Example 1: Encode UTF-8

The encoding must be explicit at the boundary.

```python
text = "café"
data = text.encode("utf-8")
print(data)
```

**What to observe:**

UTF-8 bytes are displayed.

### Example 2: Decode with the same rule

The inverse operation requires the compatible encoding.

```python
print(data.decode("utf-8"))
```

**What to observe:**

`café`

### Example 3: Hash bytes, not a vague string

The digest input must be reproducible.

```python
import hashlib

print(hashlib.sha256(data).hexdigest()[:12])
```

**What to observe:**

A stable prefix for the exact bytes.

### Example 4: Normalize deliberately

Unicode normalization changes bytes and must be part of the protocol.

```python
import unicodedata

canonical = unicodedata.normalize("NFC", text)
print(canonical)
```

**What to observe:**

The canonical text is explicit.

### Example 5: Preserve raw and canonical

Evidence needs provenance even when comparison uses a canonical form.

```python
record = {"raw": text, "canonical": canonical, "encoding": "utf-8"}
print(record)
```

**What to observe:**

Both representations remain available.

## Execution trace

The protocol chooses text normalization and encoding, produces bytes, applies the cryptographic operation to those bytes, and records the choices so another implementation can reproduce them.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| hash implicit encoding | digests differ by platform | encode explicitly |
| normalize without record | original evidence changes | preserve raw and rule |
| decode arbitrary bytes | errors or replacement characters | define error policy |
| compare display text | visually similar data differs | compare agreed canonical bytes |
| treat bytes as secret | representation is mistaken for confidentiality | apply access controls |

## Security application

Use synthetic strings including non-ASCII characters and test round trips. Do not include personal names or private files.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested local command, inspect its output, and record the limitation asked for by the exercise.

## Finish line

Run `python -m course_days.day052`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Cryptography sees bytes; secure protocols must specify how human-facing text becomes those bytes.

## Limitations

Canonicalization can be lossy and Unicode security is complex; protocol designers must define exact rules.

[← Day 51](../day_51_trust_boundaries_and_threat_models/day_51_trust_boundaries_and_threat_models.md) · [Day index](../DAY_INDEX.md) · [Day 53 →](../day_53_hashes_and_integrity/day_53_hashes_and_integrity.md)
