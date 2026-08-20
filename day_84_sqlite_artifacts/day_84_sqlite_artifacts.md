# Day 84: SQLite Artifacts

[← Day 83](../day_83_filesystem_timelines/day_83_filesystem_timelines.md) · [Day index](../DAY_INDEX.md) · [Day 85 →](../day_85_browser_and_document_artifacts/day_85_browser_and_document_artifacts.md)

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

Applications often store useful evidence in local databases. Safe analysis requires read-only copies, schema discovery, parameterized queries, bounded rows, and careful handling of deleted or stale records.

## Prerequisites

Complete Day 83. Use only the local fixtures and explicit loopback assessment scope supplied by the course.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using a tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Inspect a disposable SQLite fixture and produce a query result without modifying the source database.

## Security boundary

This lesson is educational and authorized-lab-only. It does not authorize public scanning, credential guessing, exploitation, interception, persistence, or changes to systems you do not own.

## Lesson

### Vocabulary

A SQLite artifact is a database file. A schema describes tables and columns. Read-only analysis avoids altering the source. A query plan affects resource behavior.

## Worked examples

### Example 1: Connect to memory

Use an in-memory database while learning SQL shape.

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE events (id INTEGER, kind TEXT)")
print(db.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall())
```

**What to observe:**

The table is visible.

### Example 2: Insert fixture rows

Synthetic data makes the query repeatable.

```python
db.executemany("INSERT INTO events VALUES (?, ?)", [(1, "login"), (2, "process")])
print(db.execute("SELECT COUNT(*) FROM events").fetchone())
```

**What to observe:**

`(2,)`

### Example 3: Use parameters

Values remain separate from SQL syntax.

```python
kind = "login"
print(db.execute("SELECT id FROM events WHERE kind = ?", (kind,)).fetchall())
```

**What to observe:**

`[(1,)]`

### Example 4: Bound rows

A forensic query should not accidentally return millions of rows.

```python
print(db.execute("SELECT id, kind FROM events LIMIT ?", (10,)).fetchall())
```

**What to observe:**

The result is finite.

### Example 5: Copy before work

A source artifact should be preserved before analysis.

```python
paths = {"source": "evidence/app.db", "working_copy": "analysis/app.db"}
print(paths)
```

**What to observe:**

The source and copy are distinct.

## Execution trace

The analyst preserves a source copy, discovers schema, uses parameters and read-only operations, caps results, and records query purpose and limitations.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| query original writable | evidence changes | work on a copy or read-only connection |
| string SQL | injection and quoting errors | parameterize |
| assume table names | query fails or misreads | inspect schema |
| no limit | analysis exhausts resources | bound result |
| missing timezone | timeline is wrong | normalize and preserve raw |

## Security application

Use only a disposable fixture. Do not open private browser, application, or workplace databases.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the requested evidence, expected behavior, edge case, and limitation.

## Finish line

Run `python -m course_days.day084`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Database analysis is a bounded, read-only interpretation of a preserved artifact.

## Limitations

SQLite internals, deleted records, journaling, and application semantics require specialized tools and careful authorization.

[← Day 83](../day_83_filesystem_timelines/day_83_filesystem_timelines.md) · [Day index](../DAY_INDEX.md) · [Day 85 →](../day_85_browser_and_document_artifacts/day_85_browser_and_document_artifacts.md)
