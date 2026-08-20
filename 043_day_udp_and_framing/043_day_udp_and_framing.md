# Day 43: UDP and Message Framing

[← Day 42](../042_day_tcp_clients_and_servers/042_day_tcp_clients_and_servers.md) · [Day index](../DAY_INDEX.md) · [Day 44 →](../044_day_dns_concepts/044_day_dns_concepts.md)

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

UDP sends independent datagrams without a connection guarantee. It can be useful for bounded local telemetry, but loss, duplication, reordering, and spoofing must be part of the design.

## Prerequisites

Complete Day 42. Run the repository checks and use only the local fixtures and explicitly authorized loopback services.

## Outcomes

By the end of this lesson, you can:

- explain the protocol or security property in plain language
- run and modify every worked example
- test a normal, boundary, and failure case
- identify the trust boundary and residual risk
- connect the concept to the numbered cybersecurity exercises

## The problem

Parse a local datagram fixture and explain why a missing response is not automatically an attack.

## Security boundary

Use synthetic data, local fixtures, and loopback-only demonstrations. This lesson does not authorize scanning, interception, credential use, remote command execution, or changes to systems you do not own.

## Lesson

### Vocabulary

A datagram is one UDP packet payload. UDP is connectionless and does not guarantee delivery. A sequence number supports application-level ordering.

## Worked examples

### Example 1: Create a UDP socket

The type distinguishes UDP from TCP.

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(sock.type)
sock.close()
```

**What to observe:**

The socket type is datagram.

### Example 2: Encode a datagram

The payload has an explicit byte representation.

```python
message = b"event=1\n"
print(len(message))
```

**What to observe:**

The length is known before sending.

### Example 3: Add a sequence number

A receiver can detect missing or repeated application messages.

```python
packet = {"sequence": 4, "payload": "heartbeat"}
print(packet)
```

**What to observe:**

The sequence is metadata, not proof of sender identity.

### Example 4: Bound a datagram

Reject oversized data before parsing or storing it.

```python
MAX = 1200
if len(message) > MAX:
    raise ValueError("datagram too large")
```

**What to observe:**

Oversized training data is rejected.

### Example 5: Describe uncertainty

A timeout is a transport result, not a conclusion.

```python
result = {"status": "no_response", "complete": False}
print(result)
```

**What to observe:**

The report preserves uncertainty.

## Execution trace

The sender creates a bounded byte payload; the receiver obtains one datagram or a timeout; the application validates framing, sequence, and schema before interpreting it.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| assume delivery | missing data disappears | report loss or timeout |
| trust source address | spoofing is possible | authenticate at the application layer |
| accept unlimited payload | memory or parser abuse | cap size |
| use UDP for secrets | no confidentiality by default | use an appropriate authenticated protocol |
| call loss malicious | network conditions are ignored | preserve alternative explanations |

## Security application

Use serialized local fixtures rather than sending traffic. If a live demonstration is used, keep both endpoints on loopback and document cleanup.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested local command, inspect its output, and record the limitation asked for by the exercise.

## Finish line

Run `python -m course_days.day043`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> UDP provides datagrams, not reliability or identity; the application must state what loss means.

## Limitations

A local UDP test does not represent an internet path, and a packet observation does not prove intent.

[← Day 42](../042_day_tcp_clients_and_servers/042_day_tcp_clients_and_servers.md) · [Day index](../DAY_INDEX.md) · [Day 44 →](../044_day_dns_concepts/044_day_dns_concepts.md)
