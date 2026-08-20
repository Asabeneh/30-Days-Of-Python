# Day 10: Checkpoint: Build a Safe Log-Triage Classifier

[← Day 9](../day_09_functions_and_validation/day_09_functions_and_validation.md) · [Day index](../DAY_INDEX.md) · [Day 11 →](../day_11_function_contracts/day_11_function_contracts.md)

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

A checkpoint turns isolated syntax into a small engineering artifact. You will combine input validation, bounded reading, parsing, classification, and reporting without claiming more than synthetic evidence supports.

## Prerequisites

Complete Days 1–9. Run the phase tests and make sure your environment is active.

## Outcomes

By the end of this lesson, you can:

- describe a small security tool’s data flow
- process a bounded synthetic log fixture
- preserve observations while adding derived labels
- test normal, malformed, and out-of-scope inputs
- write a README that states scope and limitations

## The problem

A teammate asks for a command that reads a local training log and prints events that deserve review. The tool must not read arbitrary paths, print secrets, run indefinitely, or describe a matched rule as proof of compromise.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples may describe security signals, but they do not identify attackers, authorize testing, or justify touching public systems. Keep real credentials, private logs, and university or employer data out of the lesson.

## Lesson

## Project requirements

Build or complete the `log-triage` checkpoint using a local fixture.

### Required data flow

```text
fixture path
   ↓
safe path and size checks
   ↓
bounded line reader
   ↓
record parser
   ↓
validated event
   ↓
triage policy
   ↓
explainable report
```

Keep each stage small. If a test fails, the data flow should help you locate the failing boundary.

### Suggested fixture

```text
2026-08-20T10:00:00Z source=auth severity=2 authenticated=true message=login_ok
2026-08-20T10:01:00Z source=auth severity=8 authenticated=false message=login_failed
malformed line without fields
```

This fixture is invented for the course. It is not evidence of a real event.

### Parse only what you need

```python
def parse_line(line):
    fields = {}
    for item in line.split():
        if "=" not in item:
            continue
        key, value = item.split("=", 1)
        fields[key] = value
    return fields
```

This starter is intentionally incomplete. It does not validate required fields, timestamps, severity, or message length. Your job is to add those boundaries in the exercises.

### Classify with an explicit policy

```python
def classify_event(event):
    severity = event["severity"]
    authenticated = event["authenticated"]
    if severity >= 7 and not authenticated:
        return "review", "high severity and unauthenticated"
    return "normal", "no training rule matched"
```

This says exactly what the training policy does. It does not search the internet, identify a person, or prove an attack.

### Report derived data separately

```python
def report(event, label, reason):
    return {
        "timestamp": event["timestamp"],
        "source": event["source"],
        "severity": event["severity"],
        "label": label,
        "reason": reason,
    }
```

The report contains selected evidence and derived fields. Decide whether the raw message is necessary; if it can contain secrets, redact or omit it.

## Worked examples

### Example 1: a bounded reader

```python
def read_lines(lines, max_lines=100):
    for index, line in enumerate(lines):
        if index == max_lines:
            return
        yield line.rstrip("
")
```

The function stops at the documented bound. A real file wrapper should also enforce a path and line-length policy.

### Example 2: boolean parsing

```python
def parse_authenticated(value):
    normalized = value.casefold()
    if normalized == "true":
        return True
    if normalized == "false":
        return False
    raise ValueError("authenticated must be true or false")
```

Do not use `bool(value)` for this field.

### Example 3: timestamp parsing

```python
from datetime import datetime


def parse_timestamp(value):
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("timestamp must include a timezone")
    return parsed
```

A timezone-aware timestamp can be compared consistently. The function still needs policy around future dates or clock skew in a real system.

### Example 4: handling one malformed line

```python
for line in fixture:
    try:
        event = parse_event(line)
    except ValueError as error:
        print({"status": "rejected", "reason": str(error)})
        continue
    print({"status": "accepted", "source": event["source"]})
```

The tool preserves the fact of rejection without printing the entire malformed line.

### Example 5: project evidence

A finished checkpoint should include:

| Artifact | What it proves |
| --- | --- |
| `README.md` | setup, scope, data format, limitations |
| source module | the implementation is reproducible |
| tests | normal and negative behavior |
| synthetic fixture | the example is resettable |
| sample report | the output is explainable |
| threat model | assumptions and residual risks |

## Execution trace

For the second fixture line:

| Stage | Value |
| --- | --- |
| raw line | timestamp, source, severity, auth, message text |
| parsed fields | dictionary of strings |
| validated event | timestamp, source, integer severity, boolean auth |
| policy | `severity >= 7 and not authenticated` → true |
| derived result | `label=review` with a reason |
| report | selected evidence plus derived decision |

If parsing fails, the line must not reach the policy stage.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| accepting arbitrary paths | tool can read outside the fixture | resolve and enforce a base directory |
| no line limit | large input consumes resources | stop at a documented maximum |
| trusting every key | malformed data becomes a decision | validate required fields and types |
| printing raw lines | private values leak into reports | redact or summarize |
| calling `review` an attack | evidence becomes an accusation | use neutral labels and confidence |
| no truncation notice | report looks complete | include `truncated=true` when bounded |

## Security application

Run only against the supplied fixture. The project’s scope is local training data, the cleanup is deleting generated reports, and the residual risk is that synthetic rules can produce false positives or miss patterns not represented in the fixture. Document these limits in the project README.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples from this lesson as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run the starter, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A small security tool is a chain of bounded, testable transformations; every derived conclusion must remain visibly separate from the observations that produced it.

## Limitations

This checkpoint is not a SIEM, an incident-response system, or a detector for real compromise. It teaches engineering boundaries and evidence discipline; real production work requires authorized data, operational ownership, monitoring, and review.


[← Day 9](../day_09_functions_and_validation/day_09_functions_and_validation.md) · [Day index](../DAY_INDEX.md) · [Day 11 →](../day_11_function_contracts/day_11_function_contracts.md)
