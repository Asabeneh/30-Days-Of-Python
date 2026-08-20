# Day 117: Capstone Planning

[← Day 116](../116_day_research_and_source_evaluation/116_day_research_and_source_evaluation.md) · [Day index](../DAY_INDEX.md) · [Day 118 →](../118_day_capstone_implementation/118_day_capstone_implementation.md)

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

A capstone should demonstrate judgment, not become an unbounded collection of tools. Planning turns a broad security goal into a scoped problem, architecture, milestones, tests, and demonstration evidence.

## Prerequisites

Complete Day 116. Work from a clean virtual environment and use only local synthetic fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using it
- run and modify all worked examples
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Plan a defensive Python capstone that combines local telemetry, safe validation, reporting, tests, and one specialization track.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, destructive actions, persistence, or processing of private data.

## Lesson

### Vocabulary

A capstone is an integrated project. A milestone is a bounded increment. A decision log records important trade-offs. A definition of done states evidence.

## Worked examples

### Example 1: Choose a problem

A good problem has a user, asset, and safe boundary.

```python
problem = {
    "user": "student analyst",
    "asset": "synthetic events",
    "boundary": "local fixtures",
}
print(problem)
```

**What to observe:**

The project is bounded.

### Example 2: Define milestones

Milestones reduce a large project into demonstrable steps.

```python
milestones = ["schema", "parser", "policy", "tests", "report", "review"]
print(milestones)
```

**What to observe:**

The order is visible.

### Example 3: Choose architecture

Reuse tested modules rather than copy code.

```python
architecture = {"input": "fixture", "core": "pure policy", "output": "redacted report"}
print(architecture)
```

**What to observe:**

The design has boundaries.

### Example 4: Define done

Completion needs artifacts and explanation.

```python
done = ["tests pass", "README", "threat model", "sample output", "limitations"]
print(done)
```

**What to observe:**

The evidence is concrete.

### Example 5: Record a trade-off

A decision log explains why the project is shaped this way.

```python
decision = {
    "choice": "fixture-only",
    "benefit": "safe reproducibility",
    "cost": "not production telemetry",
}
print(decision)
```

**What to observe:**

The trade-off is honest.

## Execution trace

The capstone moves from user/asset/boundary to milestones, architecture, evidence, and trade-offs. Scope is reduced until the learner can finish and explain it.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| build every tool | project never finishes | choose one outcome |
| no threat model | features create risk | model before code |
| demo only | no tests or evidence | define done |
| copy libraries blindly | understanding is missing | explain decisions |
| production claims | local project is overclaimed | state limits |

## Security application

Choose a local defensive capstone. No public data collection, exploit capability, or real credential integration.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the evidence, output, edge case, and limitation requested by each question.

## Finish line

Run `python -m course_days.day117`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A capstone is a bounded argument that the learner can design, build, test, review, and explain a security tool.

## Limitations

A plan cannot predict every implementation problem; revise scope when evidence shows it is too large.

[← Day 116](../116_day_research_and_source_evaluation/116_day_research_and_source_evaluation.md) · [Day index](../DAY_INDEX.md) · [Day 118 →](../118_day_capstone_implementation/118_day_capstone_implementation.md)
