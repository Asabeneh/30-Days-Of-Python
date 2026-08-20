# Day 5: Branching and a First Triage Classifier

[← Day 4](../004_day_operators_and_decisions/004_day_operators_and_decisions.md) · [Day index](../DAY_INDEX.md) · [Day 6 →](../006_day_loops_and_bounded_work/006_day_loops_and_bounded_work.md)

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

A classifier chooses among paths. In security work, a branch should make a limited, explainable recommendation—not claim that an incident is proven.

## Prerequisites

Complete Day 4 and be able to write and test a boolean expression.

## Outcomes

By the end of this lesson, you can:

- use `if`, `elif`, and `else`
- order conditions from specific to general
- return a label and reason
- test branch boundaries
- separate observations from conclusions

## The problem

A synthetic event can be normal, needs review, or invalid. The program needs a stable policy for each case and a reason that a human can inspect.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples may describe security signals, but they do not identify attackers, authorize testing, or justify touching public systems. Keep real credentials, private logs, and university or employer data out of the lesson.

## Lesson

### The shape of a branch

```python
severity = 8
if severity >= 7:
    label = "review"
elif severity >= 4:
    label = "watch"
else:
    label = "normal"
print(label)
```

Python checks conditions from top to bottom and executes the first true block. The order matters. If `severity >= 4` appeared first, a severity of `8` would be labeled `watch` and the later branch would never run.

### Add an invalid state

```python
if not 0 <= severity <= 10:
    label = "invalid"
elif severity >= 7:
    label = "review"
elif severity >= 4:
    label = "watch"
else:
    label = "normal"
```

Validate the domain before applying the policy. A severity of `99` should not become an urgent event merely because it is large.

### Return a decision and a reason

```python
def classify(severity, authenticated):
    if not 0 <= severity <= 10:
        return "invalid", "severity is outside 0..10"
    if severity >= 7 and not authenticated:
        return "review", "high severity and unauthenticated"
    if severity >= 7:
        return "watch", "high severity but authenticated"
    return "normal", "severity is below review threshold"
```

A tuple lets the caller keep the label and explanation together. The function does not print or assert that an attack happened.

### Branches are policies

A branch encodes a policy decision. Ask who chose the threshold, which data is trusted, how false positives are handled, and what happens when a field is missing. Code can execute correctly while the policy is still wrong for its context.
## Worked examples

### Example 1: exact boundaries

```python
for severity in [3, 4, 6, 7, 10]:
    print(severity, classify(severity, authenticated=True))
```

Predict the labels before running it. Boundaries `4` and `7` deserve explicit tests.

### Example 2: missing input

```python
def classify_record(record):
    if "severity" not in record:
        return "invalid", "severity is missing"
    if "authenticated" not in record:
        return "invalid", "authenticated is missing"
    return classify(record["severity"], record["authenticated"])
```

Missing is different from false. Do not silently replace a missing authentication field with `False` unless the policy explicitly says so.

### Example 3: a decision table

| Input | Expected label | Reason |
| --- | --- | --- |
| `severity=2, authenticated=True` | normal | below threshold |
| `severity=7, authenticated=True` | watch | high but authenticated |
| `severity=7, authenticated=False` | review | high and unauthenticated |
| `severity=11, authenticated=False` | invalid | outside domain |

### Example 4: do not bury output in policy

```python
def classify_for_cli(severity, authenticated):
    label, reason = classify(severity, authenticated)
    return {"label": label, "reason": reason}
```

A caller can print this dictionary, save it, or test it. Pure policy is easier to reuse.

### Example 5: an intentionally unresolved signal

```python
def classify_with_source(event):
    label, reason = classify_record(event)
    return {"label": label, "reason": reason, "source": event.get("source", "unknown")}
```

The source helps a reviewer understand provenance; it does not prove accuracy.

## Execution trace

For `classify(8, False)`:

| Step | Check | Result |
| ---: | --- | --- |
| 1 | `0 <= 8 <= 10` | true |
| 2 | `8 >= 7 and not False` | true |
| 3 | return | `("review", "high severity and unauthenticated")` |

For `classify(8, True)`, step 2 is false and the function returns `watch`.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| broad condition first | urgent events get a low label | order specific cases first |
| no invalid branch | malformed data enters policy | validate before classification |
| printing inside the classifier | tests must capture output | return structured data |
| using “attack” as a label | observation becomes conclusion | use neutral labels such as `review` |
| no reason field | reviewer cannot reproduce the decision | return label and reason |

## Security application

Run the classifier only against the supplied synthetic event fixture. Save the output as a review queue, not as an incident declaration. Add a note that a human must confirm context before escalation.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples from this lesson as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run the starter, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Branching turns explicit policy into paths; a good classifier validates its input, returns an explainable label, and stops short of claiming more than its evidence supports.

## Limitations

Thresholds are not universal truth. They can create false positives, false negatives, and unfair outcomes if the data or policy is poor.


[← Day 4](../004_day_operators_and_decisions/004_day_operators_and_decisions.md) · [Day index](../DAY_INDEX.md) · [Day 6 →](../006_day_loops_and_bounded_work/006_day_loops_and_bounded_work.md)
