# Day 86: Email and Phishing Fixtures

[← Day 85](../085_day_browser_and_document_artifacts/085_day_browser_and_document_artifacts.md) · [Day index](../DAY_INDEX.md) · [Day 87 →](../087_day_network_evidence/087_day_network_evidence.md)

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

Phishing analysis teaches headers, links, attachments, and social-engineering indicators without asking a learner to send, open, or interact with a real malicious message.

## Prerequisites

Complete Day 85. Use only the local fixtures and explicit loopback assessment scope supplied by the course.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using a tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Analyze a synthetic email fixture and report indicators, provenance, and uncertainty without visiting its links.

## Security boundary

This lesson is educational and authorized-lab-only. It does not authorize public scanning, credential guessing, exploitation, interception, persistence, or changes to systems you do not own.

## Lesson

### Vocabulary

An email header contains transport and message metadata. A URL is a destination string. An attachment is a referenced file. A lure is persuasive text designed to influence behavior.

## Worked examples

### Example 1: Parse headers

Header names and values are data to normalize.

```python
headers = {"From": "training@example.invalid", "Subject": "Review fixture"}
print(headers)
```

**What to observe:**

The headers are synthetic.

### Example 2: Extract a URL

Extraction does not mean navigation.

```python
body = "Please visit https://training.invalid/review"
print(body.split()[2])
```

**What to observe:**

The URL is printed as a string only.

### Example 3: Check domain policy

A training allowlist can reject unknown destinations.

```python
allowed = {"training.invalid"}
print("training.invalid" in allowed)
```

**What to observe:**

The destination is recognized as a fixture domain.

### Example 4: Model attachment metadata

Metadata can be reviewed without opening content.

```python
attachment = {"name": "invoice.pdf", "size": 1200, "opened": False}
print(attachment)
```

**What to observe:**

The attachment remains unopened.

### Example 5: Report uncertainty

A suspicious pattern is not proof of compromise.

```python
print({"signals": ["urgent language"], "clicked": False, "compromise": "not assessed"})
```

**What to observe:**

The report distinguishes observation.

## Execution trace

The parser reads a fixture, normalizes safe headers, extracts links without navigation, checks attachment metadata, and reports signals plus what was not observed.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| click link | analysis becomes execution | treat as text |
| open attachment | code or macros run | inspect metadata or sandbox under authority |
| sender equals identity | headers can be forged | state provenance limits |
| suspicious equals compromise | overclaiming | write neutral signals |
| publish raw email | personal data leaks | minimize and redact |

## Security application

Use synthetic email text and `.invalid` domains. Do not send messages, click links, open real attachments, or collect credentials.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the requested evidence, expected behavior, edge case, and limitation.

## Finish line

Run `python -m course_days.day086`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Phishing analysis is cautious interpretation of message features and provenance, not a test of a person’s intent.

## Limitations

Email headers and content can be forged, forwarded, truncated, or altered; attribution requires more evidence.

[← Day 85](../085_day_browser_and_document_artifacts/085_day_browser_and_document_artifacts.md) · [Day index](../DAY_INDEX.md) · [Day 87 →](../087_day_network_evidence/087_day_network_evidence.md)
