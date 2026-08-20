# Day 51: Trust Boundaries and Threat Models for Crypto

[← Day 50](../050_day_project__local_service_monitor/050_day_project__local_service_monitor.md) · [Day index](../DAY_INDEX.md) · [Day 52 →](../052_day_encoding_and_unicode/052_day_encoding_and_unicode.md)

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

Cryptography is not a decoration around data. Before choosing a primitive, identify what must remain secret, what must be tamper-evident, who holds keys, and what happens when verification fails.

## Prerequisites

Complete Day 50. Run the repository checks and use only the local fixtures and explicitly authorized loopback services.

## Outcomes

By the end of this lesson, you can:

- explain the protocol or security property in plain language
- run and modify every worked example
- test a normal, boundary, and failure case
- identify the trust boundary and residual risk
- connect the concept to the numbered cybersecurity exercises

## The problem

Threat-model a local case bundle before selecting hashes, HMAC, encryption, or signatures.

## Security boundary

Use synthetic data, local fixtures, and loopback-only demonstrations. This lesson does not authorize scanning, interception, credential use, remote command execution, or changes to systems you do not own.

## Lesson

### Vocabulary

A trust boundary separates assumptions. Confidentiality hides content. Integrity detects change. Authenticity ties data to a key or signer. A threat model records assets and adversaries.

## Worked examples

### Example 1: Name properties

Different goals require different controls.

```python
needs = {"secret": "confidentiality", "changed": "integrity", "sender": "authenticity"}
print(needs)
```

**What to observe:**

The requirements are not collapsed into one word: secure.

### Example 2: Model a key holder

Key location and access matter as much as the algorithm.

```python
key_plan = {
    "holder": "local test process",
    "storage": "not in source",
    "rotation": "documented",
}
print(key_plan)
```

**What to observe:**

The trust assumption is visible.

### Example 3: Define failure

Verification failure needs a safe default.

```python
failure_policy = {"on_bad_tag": "reject", "continue": False}
print(failure_policy)
```

**What to observe:**

Bad data is not processed.

### Example 4: State threat

A threat names an action and asset.

```python
threat = {
    "action": "modify_case_bundle",
    "asset": "integrity",
    "control": "verify_mac_before_parse",
}
print(threat)
```

**What to observe:**

The control maps to the threat.

### Example 5: Record residual risk

No primitive solves key compromise or wrong trust decisions.

```python
print("residual: compromised key or wrong key selection defeats verification")
```

**What to observe:**

The limitation remains visible.

## Execution trace

The model starts with properties and key holders, chooses a failure policy, maps threat to control, and states what remains. Only then should code select a primitive.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| say “encrypted” | property is unclear | name confidentiality/integrity/authenticity |
| hard-code key | secret enters source | externalize key handling |
| parse before verify | attacker controls parser input | verify before trusting content |
| bad tag becomes warning | tampered data continues | reject safely |
| algorithm first | requirements are missed | threat-model first |

## Security application

Use only training keys and synthetic bundles. Never use a university, employer, or personal key in exercises.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested local command, inspect its output, and record the limitation asked for by the exercise.

## Finish line

Run `python -m course_days.day051`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Cryptography implements a property under key and trust assumptions; the assumptions are part of the security design.

## Limitations

A correct primitive with a compromised key, wrong mode, or bad lifecycle can fail completely.

[← Day 50](../050_day_project__local_service_monitor/050_day_project__local_service_monitor.md) · [Day index](../DAY_INDEX.md) · [Day 52 →](../052_day_encoding_and_unicode/052_day_encoding_and_unicode.md)
