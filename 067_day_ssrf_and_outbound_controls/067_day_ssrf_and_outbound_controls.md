# Day 67: SSRF and Outbound Request Controls

[← Day 66](../066_day_csrf__cookies__and_cors/066_day_csrf__cookies__and_cors.md) · [Day index](../DAY_INDEX.md) · [Day 68 →](../068_day_misconfiguration_and_defaults/068_day_misconfiguration_and_defaults.md)

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

A server that fetches a URL based on user input can become a network pivot. The defense is an explicit outbound policy: allowed schemes, hosts, ports, resolution behavior, redirects, and response limits.

## Prerequisites

Complete Day 66. Use only the local course fixtures, loopback services, and synthetic records described by the lesson.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using the tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state the trust boundary and residual risk
- complete the numbered cybersecurity exercises

## The problem

Design a local URL fetch policy that accepts one documentation fixture and rejects loopback, private, unsupported, or unknown destinations.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, interception, exploit delivery, real-user profiling, or changes to systems you do not own.

## Lesson

### Vocabulary

SSRF is unintended server-side access through attacker-influenced requests. An egress policy controls outbound destinations. A redirect can change the effective destination.

## Worked examples

### Example 1: Parse a URL

A URL has components that the policy must inspect.

```python
from urllib.parse import urlparse

parts = urlparse("https://training.local/docs")
print(parts.scheme, parts.hostname, parts.path)
```

**What to observe:**

Scheme, host, and path are separate values.

### Example 2: Allow schemes

Reject schemes that the fetcher does not need.

```python
if parts.scheme not in {"https"}:
    raise ValueError("scheme is not allowed")
```

**What to observe:**

Only HTTPS passes this policy example.

### Example 3: Allow a host

A host allowlist is narrower than a denylist.

```python
allowed_hosts = {"training.local"}
print(parts.hostname in allowed_hosts)
```

**What to observe:**

The documentation host is explicit.

### Example 4: Bound redirects

A response should not silently move to a new destination.

```python
policy = {"follow_redirects": False, "max_redirects": 0}
print(policy)
```

**What to observe:**

Redirect behavior is explicit.

### Example 5: Bound response bytes

Even an allowed endpoint can return excessive data.

```python
MAX_BYTES = 1_000_000
print(MAX_BYTES)
```

**What to observe:**

The response budget is finite.

## Execution trace

The server parses the URL, validates scheme/host/port, resolves and rechecks according to policy, uses a bounded client, and refuses unexpected redirects or destinations.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| blocklist only | new private target bypasses it | allowlist destinations |
| validate before redirect only | redirect escapes policy | revalidate every hop or disable redirects |
| hostname string check | DNS changes or alternate forms bypass | resolve and enforce carefully |
| allow all HTTPS | HTTPS does not define destination trust | allow known hosts |
| no response bound | memory and time abuse | cap bytes and timeout |

## Security application

Use a saved local fixture or a fake HTTP client. Do not make outbound requests to cloud metadata, private networks, or public systems.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples as a starting point, then record the requested output, edge case, and limitation.

## Finish line

Run `python -m course_days.day067`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Outbound fetching is a capability; the destination policy must be narrower than user input.

## Limitations

SSRF defenses are deployment-sensitive and need network-layer egress controls in addition to application checks.

[← Day 66](../066_day_csrf__cookies__and_cors/066_day_csrf__cookies__and_cors.md) · [Day index](../DAY_INDEX.md) · [Day 68 →](../068_day_misconfiguration_and_defaults/068_day_misconfiguration_and_defaults.md)
