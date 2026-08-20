# Day 64: Injection and Parameterized Queries

[← Day 63](../day_63_authentication_and_authorization/day_63_authentication_and_authorization.md) · [Day index](../DAY_INDEX.md) · [Day 65 →](../day_65_xss_and_output_encoding/day_65_xss_and_output_encoding.md)

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

Injection occurs when data is interpreted as code or query syntax. The core defense is to keep data separate from the language being executed and to validate values at the boundary.

## Prerequisites

Complete Day 63. Use only the local course fixtures, loopback services, and synthetic records described by the lesson.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using the tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state the trust boundary and residual risk
- complete the numbered cybersecurity exercises

## The problem

Store and search synthetic cases in SQLite using parameters, then compare it with an intentionally unsafe string-building example without executing attacker input.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, interception, exploit delivery, real-user profiling, or changes to systems you do not own.

## Lesson

### Vocabulary

Injection changes the meaning of an interpreter input. A parameterized query sends values separately from SQL syntax. Allowlisting constrains identifiers or operations.

## Worked examples

### Example 1: The unsafe shape

String concatenation mixes data and SQL grammar; keep this as a non-executed illustration.

```python
username = "training-user"
unsafe_sql = "SELECT * FROM users WHERE name = '" + username + "'"
print(unsafe_sql)
```

**What to observe:**

The query text contains data inside its syntax.

### Example 2: Use a placeholder

The database receives SQL structure and value separately.

```python
query = "SELECT * FROM users WHERE name = ?"
params = (username,)
print(query, params)
```

**What to observe:**

The value is not assembled into the query string.

### Example 3: Validate an identifier

Parameters are for values, not table or column names.

```python
allowed_columns = {"name", "severity"}
column = "severity"
if column not in allowed_columns:
    raise ValueError("column not allowed")
```

**What to observe:**

Only known identifiers are accepted.

### Example 4: Bound a result

A query can still return too many rows.

```python
limit = 20
if not 1 <= limit <= 100:
    raise ValueError("limit outside policy")
```

**What to observe:**

The database operation has a finite result bound.

### Example 5: Test a quote as data

A quote in a username should remain a value.

```python
candidate = "O'Reilly"
print((candidate,))
```

**What to observe:**

The parameter tuple holds the literal text.

## Execution trace

The program validates the operation and bounds, sends a fixed query with parameters, receives rows, and serializes only selected fields. It never turns user text into SQL source.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| concatenate values | input changes query syntax | use parameters |
| parameterize identifiers | API does not treat table names as values | allowlist identifiers |
| trust ORM blindly | raw fragments still bypass safety | review generated SQL and APIs |
| no result bound | query exhausts resources | cap rows and time |
| demonstrate with live target | unsafe practice expands scope | use local SQLite |

## Security application

Use only in-memory or disposable SQLite with synthetic records. The lesson explains an unsafe pattern but must not execute exploit strings or target a public database.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples as a starting point, then record the requested output, edge case, and limitation.

## Finish line

Run `python -m course_days.day064`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Injection is prevented when the interpreter’s language remains fixed and external data remains data.

## Limitations

Parameterized queries do not validate business logic, permissions, schema, or database availability.

[← Day 63](../day_63_authentication_and_authorization/day_63_authentication_and_authorization.md) · [Day index](../DAY_INDEX.md) · [Day 65 →](../day_65_xss_and_output_encoding/day_65_xss_and_output_encoding.md)
