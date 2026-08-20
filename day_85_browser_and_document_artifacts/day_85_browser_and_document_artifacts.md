# Day 85: Browser and Document Artifacts

[← Day 84](../day_84_sqlite_artifacts/day_84_sqlite_artifacts.md) · [Day index](../DAY_INDEX.md) · [Day 86 →](../day_86_email_and_phishing_fixtures/day_86_email_and_phishing_fixtures.md)

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

Browser history, downloaded files, and office documents may contain useful context and sensitive personal data. Analysis should use supplied fixtures and minimize what is copied into reports.

## Prerequisites

Complete Day 84. Use only the local fixtures and explicit loopback assessment scope supplied by the course.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using a tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Extract a few fields from synthetic browser and document fixtures without interpreting them as proof of a person’s intent.

## Security boundary

This lesson is educational and authorized-lab-only. It does not authorize public scanning, credential guessing, exploitation, interception, persistence, or changes to systems you do not own.

## Lesson

### Vocabulary

An artifact is a recorded object. Metadata describes creation or modification. Content is the body. Provenance records source and handling.

## Worked examples

### Example 1: Model a history row

A history record needs URL-like text, time, and source.

```python
row = {
    "url": "https://training.local/docs",
    "visited_at": "2026-08-20T10:00:00Z",
    "source": "fixture",
}
print(row)
```

**What to observe:**

The source and time are present.

### Example 2: Redact a query

URLs may include tokens or personal identifiers.

```python
from urllib.parse import urlsplit, urlunsplit

parts = urlsplit(row["url"])
print(urlunsplit((parts.scheme, parts.netloc, parts.path, "", "")))
```

**What to observe:**

The query and fragment are omitted.

### Example 3: Model document metadata

Metadata and content should be separated.

```python
document = {"name": "training.doc", "author": "synthetic", "content_hash": "digest"}
print(document)
```

**What to observe:**

The report can minimize content.

### Example 4: Check fixture type

A parser should not assume every file is the expected format.

```python
allowed = {".json", ".txt"}
print(".json" in allowed)
```

**What to observe:**

The allowed formats are explicit.

### Example 5: State interpretation

A visit or metadata field is an observation, not intent.

```python
print({"observation": "fixture URL recorded", "intent": "not assessed"})
```

**What to observe:**

The report avoids attribution.

## Execution trace

The analyst reads only a supplied fixture, extracts selected fields, removes unnecessary query data, records hashes and provenance, and writes a neutral interpretation.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| copy full URLs | tokens or personal data leak | redact query/fragment |
| browsing equals intent | evidence becomes accusation | state intent unassessed |
| open real profile | privacy violation | use fixtures |
| trust extension | parser confusion | validate format and size |
| publish document content | unnecessary exposure | minimize fields |

## Security application

Use synthetic browser rows and documents created for the course. Do not inspect a real browser profile or personal document.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the requested evidence, expected behavior, edge case, and limitation.

## Finish line

Run `python -m course_days.day085`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Artifacts preserve traces of activity and metadata; interpretation must remain cautious and privacy-aware.

## Limitations

Artifacts can be shared, manipulated, stale, or incomplete, and lawful access requirements vary.

[← Day 84](../day_84_sqlite_artifacts/day_84_sqlite_artifacts.md) · [Day index](../DAY_INDEX.md) · [Day 86 →](../day_86_email_and_phishing_fixtures/day_86_email_and_phishing_fixtures.md)
