# Day 7: Collections and an Indicator Catalog

[← Day 6](../day_06_loops_and_bounded_work/day_06_loops_and_bounded_work.md) · [Day index](../DAY_INDEX.md) · [Day 8 →](../day_08_strings_and_canonicalization/day_08_strings_and_canonicalization.md)

## Table of Contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Lesson](#lesson)
- [Worked examples](#worked-examples)
- [Execution trace](#execution-trace)
- [Common mistakes](#common-mistakes)
- [Security application](#security-application)
- [Exercises](#exercises)
- [Finish line](#finish-line)

## Why this lesson exists

Indicators arrive as repeated values with different roles: a list preserves events, a set removes duplicates, and a dictionary associates an indicator with metadata. Choosing the wrong collection can lose evidence or create ambiguity.

## Prerequisites

Complete Day 6 and understand iteration and bounded processing.

## Outcomes

By the end of this lesson, you can:

- choose between list, tuple, set, and dictionary
- preserve order when evidence needs chronology
- remove duplicates without losing first-seen order
- associate indicator values with metadata
- state what a collection can and cannot prove

## The problem

A synthetic fixture contains repeated domain-like strings and IP-like addresses. You need a catalog for quick membership checks while preserving the original event order for review.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples may describe security signals, but they do not identify attackers, authorize testing, or justify touching public systems. Keep real credentials, private logs, and university or employer data out of the lesson.

## Lesson

### Lists preserve order

```python
observations = ["dns", "auth", "dns"]
print(observations[0])
print(observations[-1])
observations.append("process")
print(observations)
```

Lists are mutable and ordered. The duplicate `dns` may be meaningful because it occurred twice.

### Sets support membership and uniqueness

```python
unique = set(observations)
print("dns" in unique)
print(unique)
```

A set removes duplicates and does not promise the chronological order of a list. Use it when uniqueness or membership is the purpose.

### Dictionaries map keys to values

```python
finding = {
    "indicator": "example.invalid",
    "kind": "domain",
    "confidence": "low",
}
print(finding["kind"])
print(finding.get("owner", "unknown"))
```

`finding["owner"]` would raise `KeyError` if missing; `.get` lets you choose a default. Do not let a default hide a required field.

### Tuples communicate fixed structure

```python
coordinate = ("example.invalid", "domain")
name, kind = coordinate
print(name, kind)
```

A tuple can signal that the pair should not be changed. It does not enforce security or validate either string.
## Worked examples

### Example 1: unique values in first-seen order

```python
def unique_in_order(values):
    seen = set()
    result = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result
```

This keeps the order of first appearance while using a set for quick membership checks.

### Example 2: catalog metadata

```python
catalog = {}
for value in ["example.invalid", "203.0.113.8", "example.invalid"]:
    kind = (
        "domain" if "." in value and not value.replace(".", "").isdigit() else "ip-like"
    )
    catalog.setdefault(value, {"kind": kind, "count": 0})
    catalog[value]["count"] += 1
print(catalog)
```

The heuristic is intentionally simple and not a real indicator validator. It illustrates how metadata can be attached without changing the raw value.

### Example 3: list of records

```python
events = [
    {"line": 1, "indicator": "example.invalid"},
    {"line": 2, "indicator": "example.invalid"},
]
for event in events:
    print(event["line"], event["indicator"])
```

A list of dictionaries preserves event order and supports later reporting.

### Example 4: defensive copy

```python
original = ["alpha", "beta"]
copy = original.copy()
copy.append("gamma")
print(original)
print(copy)
```

The original list is unchanged. Accidental aliasing can make a parser modify evidence that another part of the program expects to remain raw.

### Example 5: explicit missing data

```python
record = {"indicator": "example.invalid"}
owner = record.get("owner")
print(owner is None)
```

Missing ownership is a data-quality gap, not proof of maliciousness.

## Execution trace

For `unique_in_order(["a", "b", "a"])`:

| Value | `seen` before | Action | `result` after |
| --- | --- | --- | --- |
| `a` | `{}` | add and append | `["a"]` |
| `b` | `{a}` | add and append | `["a", "b"]` |
| `a` | `{a, b}` | skip | `["a", "b"]` |

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| converting every list to a set | chronology disappears | preserve the list and derive a set |
| using a list for repeated membership checks | code becomes slow on large input | use a set for membership |
| indexing a missing dictionary key | `KeyError` | decide whether missing is an error or default |
| mutating shared lists | raw evidence changes unexpectedly | copy before transforming |
| calling an indicator malicious | the value is treated as a conclusion | label it as observed and record confidence |

## Security application

Create a catalog from synthetic indicators in `shared/fixtures`. Keep the original observations, store a normalized key separately, count repeats, and record the source line. Do not resolve, scan, or contact the indicators.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples from this lesson as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run the starter, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Choose a collection based on what must be preserved: lists for order, sets for uniqueness, dictionaries for relationships, and tuples for fixed groupings.

## Limitations

A catalog is only as reliable as its input and labeling rules. Duplicate removal can hide frequency, and an indicator string alone does not establish threat intent.


[← Day 6](../day_06_loops_and_bounded_work/day_06_loops_and_bounded_work.md) · [Day index](../DAY_INDEX.md) · [Day 8 →](../day_08_strings_and_canonicalization/day_08_strings_and_canonicalization.md)
