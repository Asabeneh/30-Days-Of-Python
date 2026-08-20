# Day 44: DNS Concepts and Safe Resolution

[← Day 43](../day_43_udp_and_framing/day_43_udp_and_framing.md) · [Day index](../DAY_INDEX.md) · [Day 45 →](../day_45_http_requests_and_responses/day_45_http_requests_and_responses.md)

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

Names are translated into addresses through a resolver path that can vary by cache, configuration, and time. Security tooling should distinguish lookup results from ownership or trust.

## Prerequisites

Complete Day 43. Run the repository checks and use only the local fixtures and explicitly authorized loopback services.

## Outcomes

By the end of this lesson, you can:

- explain the protocol or security property in plain language
- run and modify every worked example
- test a normal, boundary, and failure case
- identify the trust boundary and residual risk
- connect the concept to the numbered cybersecurity exercises

## The problem

Resolve a documentation name or local fixture safely and record the resolver result without probing the returned host.

## Security boundary

Use synthetic data, local fixtures, and loopback-only demonstrations. This lesson does not authorize scanning, interception, credential use, remote command execution, or changes to systems you do not own.

## Lesson

### Vocabulary

DNS maps names to records. A resolver performs lookup. A cache stores results for a period. TTL expresses a caching interval.

## Worked examples

### Example 1: Resolve a local name

Use the standard library for a single explicit lookup.

```python
import socket

print(socket.gethostbyname("localhost"))
```

**What to observe:**

Usually `127.0.0.1` in a local environment.

### Example 2: Inspect multiple results

One name can map to multiple addresses.

```python
print(socket.getaddrinfo("localhost", 0, type=socket.SOCK_STREAM))
```

**What to observe:**

The result contains address families and endpoints.

### Example 3: Preserve the name

The original name is important provenance.

```python
record = {"name": "localhost", "resolved": ["127.0.0.1"], "observed": True}
print(record)
```

**What to observe:**

The name and result stay together.

### Example 4: Bound a lookup

A tool should not treat resolution as a permission to connect.

```python
policy = {"allowed_names": {"localhost"}}
print("localhost" in policy["allowed_names"])
```

**What to observe:**

Only an explicitly allowed training name passes policy.

### Example 5: State time

Results need an observation time because DNS can change.

```python
from datetime import datetime, timezone

print(datetime.now(timezone.utc).isoformat())
```

**What to observe:**

An aware UTC timestamp.

## Execution trace

The name is selected, policy checks it, the resolver returns records, and the tool records time and source. No connection follows automatically.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| resolution equals ownership | name is treated as trusted | record it as an observation |
| connect after lookup | lookup becomes an unapproved action | separate phases |
| assume one address | load balancing and IPv6 are missed | handle multiple results |
| cache forever | stale result is treated as current | record time and TTL when available |
| log private names | internal data leaks | minimize output |

## Security application

Use `localhost` or documented synthetic names only. Do not enumerate DNS names, perform zone transfers, or connect to resolved endpoints.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested local command, inspect its output, and record the limitation asked for by the exercise.

## Finish line

Run `python -m course_days.day044`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> DNS is a time-bound naming observation, not identity, authorization, or proof of ownership.

## Limitations

Resolvers, caches, hosts files, and network policy affect results; a Python lookup cannot prove the full DNS path.

[← Day 43](../day_43_udp_and_framing/day_43_udp_and_framing.md) · [Day index](../DAY_INDEX.md) · [Day 45 →](../day_45_http_requests_and_responses/day_45_http_requests_and_responses.md)
