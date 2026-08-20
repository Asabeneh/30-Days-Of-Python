# Day 98: Bounded Fuzzing

[← Day 97](../day_97_input_validation_testing/day_97_input_validation_testing.md) · [Day index](../DAY_INDEX.md) · [Day 99 →](../day_99_findings_and_retesting/day_99_findings_and_retesting.md)

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

Fuzzing generates varied inputs to find crashes and contract violations. Without bounds and a resettable target, it can become an availability problem instead of a learning exercise.

## Prerequisites

Complete Day 97. Use only the local fixtures and explicit loopback assessment scope supplied by the course.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using a tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Generate small synthetic inputs, run them against a pure validator, and record crashes without unbounded loops or network traffic.

## Security boundary

This lesson is educational and authorized-lab-only. It does not authorize public scanning, credential guessing, exploitation, interception, persistence, or changes to systems you do not own.

## Lesson

### Vocabulary

Fuzzing varies input automatically. A seed makes a run reproducible. A corpus is a collection of inputs. A crash is an unexpected failure requiring minimization.

## Worked examples

### Example 1: Create a seed

Reproducibility begins with a fixed seed.

```python
import random

rng = random.Random(98)
print([rng.randint(0, 9) for _ in range(5)])
```

**What to observe:**

The sequence repeats for the same seed.

### Example 2: Generate a bounded string

Limit length and alphabet.

```python
alphabet = "abc012"
value = "".join(rng.choice(alphabet) for _ in range(8))
print(value)
```

**What to observe:**

The input is small and printable.

### Example 3: Run a pure validator

A pure function avoids external side effects.

```python
def accepts(text):
    return len(text) <= 10 and text.isalnum()


print(accepts(value))
```

**What to observe:**

The result is deterministic for the input.

### Example 4: Record a failure

A crash record needs the seed and input, not a secret dump.

```python
failure = {"seed": 98, "input": value, "error": "training failure"}
print(failure)
```

**What to observe:**

The case is reproducible.

### Example 5: Stop at a budget

Runs need a finite case and time budget.

```python
budget = {"cases": 100, "seconds": 5}
print(budget)
```

**What to observe:**

The fuzzer cannot run forever.

## Execution trace

The runner seeds the generator, creates bounded inputs, invokes a pure local validator, records exceptions with the seed, and stops at case/time limits.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| random unseeded | failure cannot reproduce | record seed |
| unlimited cases | resource exhaustion | finite budget |
| network target | accidental load | pure function or local fixture |
| store all inputs | output grows | retain failing/minimized cases |
| call crash vulnerability | finding is overclaimed | report reproducible behavior |

## Security application

Fuzz only pure course validators or a disposable local service with explicit approval and tiny budgets. Do not fuzz public services.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the requested evidence, expected behavior, edge case, and limitation.

## Finish line

Run `python -m course_days.day098`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Bounded fuzzing is reproducible variation under a finite resource and scope contract.

## Limitations

Finding a crash does not automatically establish exploitability, impact, or root cause.

[← Day 97](../day_97_input_validation_testing/day_97_input_validation_testing.md) · [Day index](../DAY_INDEX.md) · [Day 99 →](../day_99_findings_and_retesting/day_99_findings_and_retesting.md)
