# Day 46: TLS and Certificate Validation

[← Day 45](../045_day_http_requests_and_responses/045_day_http_requests_and_responses.md) · [Day index](../DAY_INDEX.md) · [Day 47 →](../047_day_packet_capture_fixtures/047_day_packet_capture_fixtures.md)

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

Encryption in transit is useful only when the client validates who it is communicating with. A learner should understand certificates and hostname checks without writing a bypass.

## Prerequisites

Complete Day 45. Run the repository checks and use only the local fixtures and explicitly authorized loopback services.

## Outcomes

By the end of this lesson, you can:

- explain the protocol or security property in plain language
- run and modify every worked example
- test a normal, boundary, and failure case
- identify the trust boundary and residual risk
- connect the concept to the numbered cybersecurity exercises

## The problem

Inspect the standard library’s secure client defaults and explain why disabling certificate verification is not a fix.

## Security boundary

Use synthetic data, local fixtures, and loopback-only demonstrations. This lesson does not authorize scanning, interception, credential use, remote command execution, or changes to systems you do not own.

## Lesson

### Vocabulary

TLS provides confidentiality and integrity for a negotiated connection. A certificate binds a public key to an identity under a trust model. Hostname verification checks the requested name.

## Worked examples

### Example 1: Create a default context

The standard client context enables ordinary verification defaults.

```python
import ssl

context = ssl.create_default_context()
print(context.check_hostname, context.verify_mode)
```

**What to observe:**

Hostname checking is enabled and certificates are required.

### Example 2: Name the target

The requested hostname is part of validation.

```python
target = {"hostname": "training.local", "purpose": "loopback demo"}
print(target)
```

**What to observe:**

The identity expectation is explicit.

### Example 3: Reject a mismatch conceptually

A certificate for another name should not be accepted silently.

```python
expected = "training.local"
presented = "other.local"
print(expected == presented)
```

**What to observe:**

`False`; the client should fail rather than continue.

### Example 4: Separate trust stores

Trust decisions depend on which CA roots the client uses.

```python
trust_policy = {"system_roots": True, "custom_roots": []}
print(trust_policy)
```

**What to observe:**

The trust source is documented.

### Example 5: Do not disable verification

A bypass converts an identity failure into an undetected connection.

```python
safe = {"verify_certificates": True, "verify_hostname": True}
print(safe)
```

**What to observe:**

Both checks remain enabled.

## Execution trace

The client chooses a trust store, negotiates TLS, validates the chain and hostname, and only then treats the connection as authenticated for the stated identity.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| `CERT_NONE` in production | identity is not checked | keep verification enabled |
| trust any hostname | wrong service can impersonate | verify hostname |
| encryption equals authentication | endpoint identity is assumed | describe the trust model |
| ignore expiration | stale credentials remain trusted | check validity |
| print certificate details carelessly | internal names leak | minimize logs |

## Security application

Use documentation and a local controlled certificate if needed. Do not add a verification bypass or connect to arbitrary public targets.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested local command, inspect its output, and record the limitation asked for by the exercise.

## Finish line

Run `python -m course_days.day046`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> TLS protects a connection only under an explicit certificate and hostname trust decision.

## Limitations

TLS configuration is complex, trust stores vary, and certificate validation does not authorize actions after connection.

[← Day 45](../045_day_http_requests_and_responses/045_day_http_requests_and_responses.md) · [Day index](../DAY_INDEX.md) · [Day 47 →](../047_day_packet_capture_fixtures/047_day_packet_capture_fixtures.md)
