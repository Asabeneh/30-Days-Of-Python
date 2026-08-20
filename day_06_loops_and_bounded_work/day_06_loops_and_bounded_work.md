# Day 6: Loops, Bounds, and Resource Safety

[← Day 5](../day_05_branching_and_triage/day_05_branching_and_triage.md) · [Day index](../DAY_INDEX.md) · [Day 7 →](../day_07_collections_and_iocs/day_07_collections_and_iocs.md)

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

Automation often processes many records. A loop gives you repetition, but an unbounded loop or unbounded input can exhaust time and memory. Security engineering requires limits.

## Prerequisites

Complete Day 5 and understand lists, conditions, and a returned classification.

## Outcomes

By the end of this lesson, you can:

- iterate through a collection
- use `range`, `break`, and `continue` deliberately
- count and collect results
- enforce record, line, and output limits
- explain the trade-off between completeness and resource safety

## The problem

A log file may contain millions of lines. A beginner’s first loop reads everything and prints everything. A safer utility processes a documented maximum and reports what it skipped.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples may describe security signals, but they do not identify attackers, authorize testing, or justify touching public systems. Keep real credentials, private logs, and university or employer data out of the lesson.

## Lesson

### A `for` loop repeats a known sequence

```python
statuses = ["ok", "failed", "ok"]
for status in statuses:
    print(status)
```

Python assigns each item to `status` in order. The loop ends after the list is exhausted. The variable name is not special; choose one that describes each item.

### `range` produces a sequence of integers

```python
for number in range(3):
    print(number)
```

The output is `0`, `1`, `2`. The stop value is excluded. `range(1, 4)` produces `1`, `2`, `3`.

### Accumulate without losing the count

```python
failed = 0
for status in statuses:
    if status == "failed":
        failed += 1
print(failed)
```

The variable `failed` is state carried from one iteration to the next. Initialize it before the loop, and update it only when the condition is true.

### `continue` and `break`

```python
for line in ["", "login_failed", "malformed", "login_ok"]:
    if not line:
        continue
    if line == "malformed":
        break
    print(line)
```

The blank line is skipped. The malformed line stops the loop, so `login_ok` is never printed. Use these statements only when their effect is obvious; hidden early exits make evidence incomplete.

### Bounds are part of the function contract

```python
def first_matches(lines, needle, limit=100):
    if limit < 0:
        raise ValueError("limit must not be negative")
    matches = []
    for line in lines:
        if needle in line:
            matches.append(line)
            if len(matches) == limit:
                break
    return matches
```

This function has a maximum result count. If `limit` is `0`, the current implementation returns an empty list only after the first match; refine it as an exercise and test your chosen behavior.
## Worked examples

### Example 1: count by category

```python
counts = {"ok": 0, "failed": 0}
for status in ["ok", "failed", "failed"]:
    if status in counts:
        counts[status] += 1
print(counts)
```

The output is `{'ok': 1, 'failed': 2}`. The membership check prevents an unexpected status from creating a new category silently.

### Example 2: line limit

```python
lines = [f"event-{number}" for number in range(5)]
for index, line in enumerate(lines):
    if index >= 3:
        break
    print(line)
```

Only three lines print. `enumerate` provides both the position and the value.

### Example 3: maximum line length

```python
def accept_line(line, max_length=2000):
    if len(line) > max_length:
        return False
    return True
```

A line-length limit prevents one malformed record from consuming excessive processing time. A real parser should record that the line was rejected without storing the entire oversized content.

### Example 4: bounded generator input

```python
def take_first(items, limit):
    for index, item in enumerate(items):
        if index == limit:
            return
        yield item
```

A generator yields one item at a time. It can reduce memory use, but it still needs a limit.

### Example 5: progress evidence

```python
processed = 0
matched = 0
for line in lines:
    processed += 1
    if "failed" in line:
        matched += 1
print(f"processed={processed} matched={matched}")
```

A report should say how many records were considered and how many matched. That makes a bounded result interpretable.

## Execution trace

For `first_matches(["a", "login_failed", "b", "login_failed"], "login", 1)`:

| Iteration | Line | Match? | State |
| ---: | --- | --- | --- |
| 1 | `a` | no | `matches=[]` |
| 2 | `login_failed` | yes | append; length becomes 1 |
| 2 | limit check | stop | return one match |

The function intentionally does not inspect the remaining line. Its result is bounded, not complete.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| forgetting the stop value | one extra item is processed | test the exact limit |
| printing every record | huge or sensitive output | collect bounded evidence and summarize |
| no progress counters | result lacks context | report processed and matched counts |
| `while True` without a stop | the process never finishes | define a counter, timeout, or input end |
| loading a whole file first | memory grows with input | stream or cap the read |

## Security application

Process the supplied synthetic log fixture with a maximum of 100 lines and 2,000 characters per line. Report `processed`, `matched`, `rejected`, and `truncated`. A truncated report must say it is incomplete.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples from this lesson as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run the starter, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A loop is a repeated state transition; a security loop must define how much input, time, memory, and output it is allowed to consume.

## Limitations

A bound improves safety but can hide an event outside the inspected window. Always report truncation and choose limits from an explicit operational requirement.


[← Day 5](../day_05_branching_and_triage/day_05_branching_and_triage.md) · [Day index](../DAY_INDEX.md) · [Day 7 →](../day_07_collections_and_iocs/day_07_collections_and_iocs.md)
