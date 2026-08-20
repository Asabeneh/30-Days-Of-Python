# Day 4: Operators, Comparisons, Truthiness, and Precedence

[← Day 3](../003_day_types_and_parsing/003_day_types_and_parsing.md) · [Day index](../DAY_INDEX.md) · [Day 5 →](../005_day_branching_and_triage/005_day_branching_and_triage.md)

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

Security decisions are combinations of facts. Operators let a program calculate, compare, combine, and reject conditions, but a misplaced parenthesis or truthiness assumption can reverse a decision.

## Prerequisites

Complete Days 1–3. Be able to parse integers and explain a boolean value.

## Outcomes

By the end of this lesson, you can:

- calculate with arithmetic operators
- compare values and combine conditions
- predict precedence and use parentheses
- distinguish false, missing, empty, and invalid data
- review a security rule as a truth table

## The problem

You need a rule that reviews a high-severity event only when it has a source and is not explicitly marked trusted. The rule must be readable and testable at its boundaries.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples may describe security signals, but they do not identify attackers, authorize testing, or justify touching public systems. Keep real credentials, private logs, and university or employer data out of the lesson.

## Lesson

### Arithmetic is evaluation

```python
print(2 + 3 * 4)
print((2 + 3) * 4)
print(7 // 3)
print(7 % 3)
```

The output is `14`, `20`, `2`, and `1`. Multiplication happens before addition. Parentheses make the intended order visible. Floor division and remainder are useful when grouping records into batches, but do not confuse `//` with ordinary division.

### Comparisons produce booleans

```python
severity = 7
print(severity >= 7)
print(severity == "7")
print(severity != 3)
```

The output is `True`, `False`, and `True`. The integer `7` is not equal to the string `"7"`.

### Combine conditions deliberately

```python
severity = 8
source = "auth"
trusted = False
review = severity >= 7 and source != "" and not trusted
print(review)
```

The result is `True`. Read the expression as a sentence. If it becomes difficult to read, assign named boolean values and test them separately.

### Membership and identity are different

```python
status = "login_failed"
print("login" in status)
print(status is "login_failed")
```

The first expression asks whether text occurs inside another value. The second uses identity and should not be used for ordinary string equality. Use `==` for values. Python may warn about the `is` comparison.

### Truthiness is a conversion rule, not a security decision

```python
for value in ["", "false", [], [1], 0, 1, None]:
    print(repr(value), bool(value))
```

Empty strings, empty collections, zero, and `None` are falsey. The non-empty string `"false"` is truthy. A user-controlled word must be parsed explicitly.
## Worked examples

### Example 1: parentheses make policy visible

```python
review = (severity >= 7 and source != "") or force_review
```

This means either the event is high severity with a source, or a separate trusted workflow forces review. Without parentheses, a reviewer must remember precedence rules.

### Example 2: truth table for a triage rule

| Severity high? | Source present? | Trusted? | Review? |
| --- | --- | --- | --- |
| no | yes | no | no |
| yes | yes | no | yes |
| yes | no | no | no |
| yes | yes | yes | no |

Writing the table before coding exposes ambiguity. Should a trusted high-severity event be excluded or still reviewed? The owner must decide.

### Example 3: explicit text parsing

```python
def parse_trusted(text):
    value = text.strip().casefold()
    if value == "true":
        return True
    if value == "false":
        return False
    raise ValueError("trusted must be true or false")
```

Now `parse_trusted("false")` returns `False`, unlike `bool("false")`.

### Example 4: short-circuiting

```python
def has_source(event):
    return bool(event.get("source"))


review = event.get("severity", 0) >= 7 and has_source(event)
```

If the severity comparison is false, Python does not need to call `has_source`. Short-circuiting can avoid unsafe work, but do not hide required validation inside a condition that may never run.

### Example 5: range checks

```python
def valid_severity(value):
    return 0 <= value <= 10
```

Chained comparisons read like mathematics. Test `0`, `10`, `-1`, and `11`; the boundaries are where off-by-one mistakes appear.

## Execution trace

For `severity=8`, `source="auth"`, `trusted=False`:

| Step | Expression | Result |
| ---: | --- | --- |
| 1 | `severity >= 7` | `True` |
| 2 | `source != ""` | `True` |
| 3 | `not trusted` | `True` |
| 4 | combine with `and` | `True` |

Change `trusted` to `True`; step 3 becomes `False` and the final result becomes `False`.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| Missing parentheses | a rule passes the wrong combination | write a truth table and parenthesize |
| `is` for string equality | warnings or inconsistent behavior | use `==` |
| `bool("false")` | false text becomes true | parse allowed words |
| `x == 1 or 2` | condition is always truthy | write `x == 1 or x == 2` |
| treating empty as malicious | missing data becomes a conclusion | label missing data explicitly |

## Security application

Implement a pure `needs_review(event)` function for synthetic events. Return a boolean and write a separate explanation function. The decision must not print, open files, or contact services, so it can be tested exhaustively.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples from this lesson as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run the starter, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A security decision is a boolean expression with assumptions; make the assumptions visible, test the truth table, and never confuse falsey data with a security conclusion.

## Limitations

The rule is only a training policy. Real organizations need documented risk ownership, trusted data sources, escalation procedures, and review of false positives and negatives.

## Optional video support

Watch [CS50P Lecture 0](https://www.youtube.com/watch?v=JP7ITIXGpHk&t=306s) from `05:06` for function arguments and side effects.

Use the [timestamped video catalog](../VIDEO_RESOURCES.md) only after running the local examples. The written lesson and Python documentation remain authoritative.


[← Day 3](../003_day_types_and_parsing/003_day_types_and_parsing.md) · [Day index](../DAY_INDEX.md) · [Day 5 →](../005_day_branching_and_triage/005_day_branching_and_triage.md)
