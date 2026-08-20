# Day 66: CSRF, Cookies, and CORS

[← Day 65](../day_65_xss_and_output_encoding/day_65_xss_and_output_encoding.md) · [Day index](../DAY_INDEX.md) · [Day 67 →](../day_67_ssrf_and_outbound_controls/day_67_ssrf_and_outbound_controls.md)

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

Browser state creates security behavior that is not visible in a single Python function. Cookies carry session context, CSRF defenses bind state-changing requests to intent, and CORS controls which browser origins may read responses.

## Prerequisites

Complete Day 65. Use only the local course fixtures, loopback services, and synthetic records described by the lesson.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using the tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state the trust boundary and residual risk
- complete the numbered cybersecurity exercises

## The problem

Model a local state-changing request and decide which cookie, CSRF, and origin checks belong to it.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, interception, exploit delivery, real-user profiling, or changes to systems you do not own.

## Lesson

### Vocabulary

A cookie is browser-managed state. CSRF tricks a browser into sending ambient credentials. CORS is a browser read-access policy, not an authentication mechanism.

## Worked examples

### Example 1: Describe a session cookie

Cookie properties affect exposure and browser behavior.

```python
cookie = {"name": "session", "secure": True, "httponly": True, "samesite": "Lax"}
print(cookie)
```

**What to observe:**

The flags are explicit.

### Example 2: Separate read and write

State-changing methods deserve stronger protection.

```python
method = "POST"
changes_state = method in {"POST", "PUT", "PATCH", "DELETE"}
print(changes_state)
```

**What to observe:**

`True` for `POST`.

### Example 3: Check a CSRF token

A server compares a token bound to the session and request context.

```python
session_token = "training-csrf"
provided = "training-csrf"
print(session_token == provided)
```

**What to observe:**

The example is a fictional equality check; real comparison and lifecycle belong in the framework.

### Example 4: Allow a known origin

CORS should name allowed origins rather than mirror arbitrary input.

```python
allowed = {"https://training.local"}
origin = "https://training.local"
print(origin in allowed)
```

**What to observe:**

The origin is explicitly allowed.

### Example 5: Do not confuse CORS with auth

A server still checks identity and permission.

```python
controls = ["authentication", "authorization", "CSRF", "CORS"]
print(controls)
```

**What to observe:**

The controls solve different problems.

## Execution trace

The browser sends cookies according to cookie policy; the server authenticates and authorizes, checks CSRF for state-changing requests, and emits an explicit CORS policy for browser reads.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| CORS as auth | non-browser caller bypasses it | enforce auth server-side |
| wildcard origin with credentials | origin trust is too broad | allowlist origins |
| no CSRF for cookie auth | cross-site state change | use framework defense and tokens |
| insecure cookie flags | session exposure | use Secure/HttpOnly/SameSite policy |
| token in URL | leaks through history and referrers | use appropriate request channels |

## Security application

Use a local conceptual service and synthetic cookie names. Do not collect real sessions or demonstrate attacks against a public browser application.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples as a starting point, then record the requested output, edge case, and limitation.

## Finish line

Run `python -m course_days.day066`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Cookies, CSRF, CORS, authentication, and authorization are separate browser and server controls.

## Limitations

Exact behavior depends on browser, framework, deployment, and same-site topology; a checklist is not a complete review.

[← Day 65](../day_65_xss_and_output_encoding/day_65_xss_and_output_encoding.md) · [Day index](../DAY_INDEX.md) · [Day 67 →](../day_67_ssrf_and_outbound_controls/day_67_ssrf_and_outbound_controls.md)
