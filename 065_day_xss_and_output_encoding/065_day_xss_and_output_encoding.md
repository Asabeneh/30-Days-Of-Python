# Day 65: Cross-Site Scripting and Output Encoding

[← Day 64](../064_day_injection_and_parameterized_queries/064_day_injection_and_parameterized_queries.md) · [Day index](../DAY_INDEX.md) · [Day 66 →](../066_day_csrf__cookies__and_cors/066_day_csrf__cookies__and_cors.md)

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

A web application can turn stored or reflected text into browser-interpreted markup. The safe response is context-aware output encoding and a strict separation between data and HTML/JavaScript.

## Prerequisites

Complete Day 64. Use only the local course fixtures, loopback services, and synthetic records described by the lesson.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using the tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state the trust boundary and residual risk
- complete the numbered cybersecurity exercises

## The problem

Render a synthetic username as text and show why inserting it into an HTML string without escaping is unsafe.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, interception, exploit delivery, real-user profiling, or changes to systems you do not own.

## Lesson

### Vocabulary

XSS is unintended script execution in a browser context. Escaping encodes special characters. Context determines the correct encoding rule. Content Security Policy is a defense in depth control.

## Worked examples

### Example 1: Treat input as text

A username is data until a renderer chooses a context.

```python
username = "<training-user>"
print(username)
```

**What to observe:**

The characters remain literal text in the Python output.

### Example 2: Escape HTML

HTML escaping prevents `<` and `>` from becoming tags in a text context.

```python
import html

safe = html.escape(username, quote=True)
print(safe)
```

**What to observe:**

The angle brackets are encoded.

### Example 3: Use a template context

A template engine’s text interpolation is safer than string-built markup when configured correctly.

```python
context = {"username": safe}
print(context)
```

**What to observe:**

The model contains data, not executable markup.

### Example 4: Do not use raw HTML blindly

This illustrates the dangerous shape without a browser.

```python
unsafe_markup = "<p>" + username + "</p>"
print(unsafe_markup)
```

**What to observe:**

The output includes the original tag-like characters; a browser context could interpret them.

### Example 5: Set defense in depth

Encoding is primary; policy headers reduce impact if a bug remains.

```python
headers = {"Content-Security-Policy": "default-src 'self'"}
print(headers)
```

**What to observe:**

The header is a policy layer, not a replacement for encoding.

## Execution trace

The application stores raw data, selects the output context, applies the context’s encoding, and sends a response with defense-in-depth headers. It does not concatenate untrusted text into executable contexts.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| HTML escape everywhere | URL or JavaScript context remains unsafe | use context-aware encoding |
| mark untrusted HTML safe | browser interprets data | keep data and markup separate |
| strip `<script>` only | alternate syntax bypasses filter | encode and use safe sinks |
| rely on CSP only | policy gaps remain | fix output handling |
| test only plain names | special characters fail | include quotes, tags, and Unicode |

## Security application

Use synthetic values and a local rendered fixture. Do not publish a test payload or target a public site.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples as a starting point, then record the requested output, edge case, and limitation.

## Finish line

Run `python -m course_days.day065`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> XSS defense is a context decision: keep untrusted data as data and encode it for the exact output context.

## Limitations

Encoding cannot repair every DOM, URL, CSS, or browser integration mistake; review the whole rendering path.

[← Day 64](../064_day_injection_and_parameterized_queries/064_day_injection_and_parameterized_queries.md) · [Day index](../DAY_INDEX.md) · [Day 66 →](../066_day_csrf__cookies__and_cors/066_day_csrf__cookies__and_cors.md)
