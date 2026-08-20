# Day 45: HTTP Requests, Responses, and Safe Parsing

[← Day 44](../044_day_dns_concepts/044_day_dns_concepts.md) · [Day index](../DAY_INDEX.md) · [Day 46 →](../046_day_tls_and_certificate_validation/046_day_tls_and_certificate_validation.md)

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

HTTP is a text-and-byte protocol used by security tools and applications. Understanding methods, status, headers, bodies, and limits helps a learner inspect a local service without treating requests as harmless by default.

## Prerequisites

Complete Day 44. Run the repository checks and use only the local fixtures and explicitly authorized loopback services.

## Outcomes

By the end of this lesson, you can:

- explain the protocol or security property in plain language
- run and modify every worked example
- test a normal, boundary, and failure case
- identify the trust boundary and residual risk
- connect the concept to the numbered cybersecurity exercises

## The problem

Parse a synthetic HTTP exchange and make a bounded request only to a supplied loopback service.

## Security boundary

Use synthetic data, local fixtures, and loopback-only demonstrations. This lesson does not authorize scanning, interception, credential use, remote command execution, or changes to systems you do not own.

## Lesson

### Vocabulary

A request has a method, target, headers, and body. A response has a status, headers, and body. Headers are metadata, not automatically safe input.

## Worked examples

### Example 1: Parse a request line

The method, target, and version are separate fields.

```python
line = "GET /health HTTP/1.1"
method, target, version = line.split()
print(method, target, version)
```

**What to observe:**

`GET /health HTTP/1.1` as three values.

### Example 2: Read a status

Status codes are categories, not complete explanations.

```python
status = 200
print(200 <= status < 300)
```

**What to observe:**

`True` for a successful class.

### Example 3: Build headers

Header names and values need validation and limits.

```python
headers = {"Accept": "application/json", "User-Agent": "training-client"}
print(headers)
```

**What to observe:**

The request identifies a bounded client.

### Example 4: Parse JSON deliberately

A content type does not guarantee valid JSON.

```python
import json

data = json.loads('{"status": "ok"}')
print(data["status"])
```

**What to observe:**

`ok`

### Example 5: Limit a body

Never read an unbounded response into memory.

```python
body = b"training response"
MAX = 4096
print(body[:MAX])
```

**What to observe:**

The preview is bounded.

## Execution trace

A parser reads the request line and headers, checks the declared limits, decodes the body according to a documented encoding, and returns a structured result or rejection.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| trust status only | error body is ignored | inspect status, headers, and body policy |
| follow redirects blindly | target changes | bound and review redirects |
| no body limit | memory abuse | cap bytes |
| log authorization header | credential leak | redact sensitive headers |
| request public targets | unauthorized traffic | use local fixtures or written permission |

## Security application

Use a loopback server or saved HTTP fixture. Document allowed method, host, path, body limit, timeout, and cleanup.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested local command, inspect its output, and record the limitation asked for by the exercise.

## Finish line

Run `python -m course_days.day045`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> HTTP is a structured exchange whose metadata and body cross a trust boundary; parse and bound both sides.

## Limitations

HTTP parsing and a successful local request do not prove application security or server identity.

[← Day 44](../044_day_dns_concepts/044_day_dns_concepts.md) · [Day index](../DAY_INDEX.md) · [Day 46 →](../046_day_tls_and_certificate_validation/046_day_tls_and_certificate_validation.md)
