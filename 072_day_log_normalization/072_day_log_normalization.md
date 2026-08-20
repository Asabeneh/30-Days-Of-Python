# Day 72: Log Normalization

[← Day 71](../071_day_telemetry_and_event_schemas/071_day_telemetry_and_event_schemas.md) · [Day index](../DAY_INDEX.md) · [Day 73 →](../073_day_ioc_enrichment/073_day_ioc_enrichment.md)

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

Real logs use inconsistent timestamps, separators, levels, and field names. Normalization is a documented transformation, not an excuse to erase raw evidence.

## Prerequisites

Complete Day 71. Use only the local course fixtures, loopback services, and synthetic records described by the lesson.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using the tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state the trust boundary and residual risk
- complete the numbered cybersecurity exercises

## The problem

Convert two synthetic log formats into one event schema and report rejected fields.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, interception, exploit delivery, real-user profiling, or changes to systems you do not own.

## Lesson

### Vocabulary

Normalization transforms equivalent source fields into canonical fields. A parser extracts. A mapper assigns. A rejected field is a data-quality result.

## Worked examples

### Example 1: Parse key-value text

Simple fixtures can be parsed with a bounded splitter.

```python
line = "level=warning user=student event=login_failed"
fields = dict(item.split("=", 1) for item in line.split())
print(fields)
```

**What to observe:**

The fields are strings.

### Example 2: Map names

Source keys can map to normalized names.

```python
normalized = {
    "severity": fields["level"],
    "actor": fields["user"],
    "event_type": fields["event"],
}
print(normalized)
```

**What to observe:**

The target schema is stable.

### Example 3: Handle malformed pairs

A bad token should be counted, not silently trusted.

```python
tokens = ["level=warning", "broken"]
rejected = [token for token in tokens if "=" not in token]
print(rejected)
```

**What to observe:**

`broken` is rejected.

### Example 4: Preserve raw id

The normalized record should point to its source line.

```python
normalized["provenance"] = {"line": 1, "source": "fixture-a"}
print(normalized)
```

**What to observe:**

The mapping can be reviewed.

### Example 5: Bound text

Line length and field count are resource controls.

```python
print({"max_line": 2000, "max_fields": 50})
```

**What to observe:**

The parser has finite limits.

## Execution trace

The normalizer bounds the line, extracts fields, maps names, converts types, records rejected tokens, and emits a versioned event with provenance.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| drop malformed tokens | quality problem disappears | count and report rejects |
| map by position | format variation breaks | map named fields |
| erase raw line | audit cannot reproduce | keep line reference |
| unlimited fields | parser abuse | cap count and lengths |
| call normalized event true | mapping is overtrusted | record quality and confidence |

## Security application

Use supplied synthetic log formats. Do not normalize real private logs without data-handling permission.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples as a starting point, then record the requested output, edge case, and limitation.

## Finish line

Run `python -m course_days.day072`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Normalization is a controlled translation with evidence of what changed and what failed.

## Limitations

A canonical schema can hide source-specific meaning if the mapping is too aggressive.

[← Day 71](../071_day_telemetry_and_event_schemas/071_day_telemetry_and_event_schemas.md) · [Day index](../DAY_INDEX.md) · [Day 73 →](../073_day_ioc_enrichment/073_day_ioc_enrichment.md)
