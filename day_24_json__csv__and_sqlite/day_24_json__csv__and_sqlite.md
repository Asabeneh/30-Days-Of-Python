# Day 24: JSON, CSV, and SQLite Data Boundaries

[← Day 23](../day_23_configuration_and_secrets/day_23_configuration_and_secrets.md) · [Day index](../DAY_INDEX.md) · [Day 25 →](../day_25_type_hints_and_static_checks/day_25_type_hints_and_static_checks.md)

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

Security engineering moves between text formats and databases. Each boundary needs a schema, encoding decision, and safe query or serialization method.

## Prerequisites

Complete Day 23 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 24

## The problem

Load synthetic event records, validate them, store them locally, and retrieve a summary without concatenating user input into SQL.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Lesson

### Vocabulary

JSON represents structured values. CSV represents rows and columns. SQLite is a local relational database. A **parameterized query** keeps data separate from SQL syntax.

## Worked examples

### Example 1: Round-trip JSON

JSON maps common Python values to a text representation.

```python
import json

record = {"source": "auth", "severity": 7}
text = json.dumps(record)
print(json.loads(text)["severity"])
```

**What to observe:**

`7` after serialization and parsing.

### Example 2: Read CSV rows

`csv.DictReader` maps column names to row values, which still arrive as strings.

```python
import csv
from io import StringIO

rows = csv.DictReader(StringIO("source,severity\nauth,7\n"))
print(next(rows))
```

**What to observe:**

`{'source': 'auth', 'severity': '7'}`; validate and convert severity.

### Example 3: Create a table

A schema makes stored fields visible.

```python
import sqlite3

connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE events (source TEXT, severity INTEGER)")
```

**What to observe:**

The database now has a table with two columns.

### Example 4: Parameterize data

Never build SQL by concatenating input.

```python
connection.execute("INSERT INTO events VALUES (?, ?)", ("auth", 7))
row = connection.execute(
    "SELECT source, severity FROM events WHERE severity >= ?", (7,)
).fetchone()
print(row)
```

**What to observe:**

`('auth', 7)`

### Example 5: Close the boundary

A context manager commits or closes a short-lived database session.

```python
with sqlite3.connect("training.db") as db:
    db.execute("CREATE TABLE IF NOT EXISTS notes (text TEXT)")
```

**What to observe:**

The connection is cleaned up when the block exits.

## Execution trace

CSV values arrive as strings; validation converts them into an internal record; the parameterized query receives values separately from the SQL statement.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| trust JSON shape | missing or wrong fields reach policy | validate schema |
| assume CSV types | severity compares as text | convert explicitly |
| SQL concatenation | input becomes query syntax | use placeholders |
| store raw secrets | local database becomes a leak | minimize and redact |
| no migration note | schema changes silently break tools | document schema and version |

## Security application

Use a temporary SQLite file under training output, parameterized statements, synthetic rows, and cleanup after tests. Never import a private CSV.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run every requested command, create the requested artifact, and record the limitation the exercise asks you to name.

## Finish line

Run `python -m course_days.day024`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Serialization is a boundary transformation; a safe database call keeps data values separate from executable syntax.

## Limitations

Parameterized SQL prevents one class of injection but does not authorize data access, validate business logic, or protect a database file’s permissions.

[← Day 23](../day_23_configuration_and_secrets/day_23_configuration_and_secrets.md) · [Day index](../DAY_INDEX.md) · [Day 25 →](../day_25_type_hints_and_static_checks/day_25_type_hints_and_static_checks.md)
