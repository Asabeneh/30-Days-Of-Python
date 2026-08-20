# Day 116: Research and Source Evaluation

[← Day 115](../day_115_privacy_and_retention/day_115_privacy_and_retention.md) · [Day index](../DAY_INDEX.md) · [Day 117 →](../day_117_capstone_planning/day_117_capstone_planning.md)

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

Security learners meet conflicting tutorials, outdated commands, and impressive but unsafe demonstrations. Research skill means checking primary sources, version, scope, evidence, and reproducibility.

## Prerequisites

Complete Day 115. Work from a clean virtual environment and use only local synthetic fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using it
- run and modify all worked examples
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Evaluate three synthetic source records and choose which one can support a course claim.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, destructive actions, persistence, or processing of private data.

## Lesson

### Vocabulary

A primary source is closest to the authority or specification. A secondary source explains or summarizes. Currency is how up to date a source is. Reproducibility means another learner can verify the claim.

## Worked examples

### Example 1: Record a source

A source record needs title, publisher, date, and URL.

```python
source = {
    "title": "Python docs",
    "publisher": "Python",
    "date": "current",
    "url": "https://docs.python.org/3/",
}
print(source)
```

**What to observe:**

The provenance is visible.

### Example 2: Check claim fit

A good source supports the exact claim, not just the topic.

```python
claim = "input returns text"
source["supports"] = claim
print(source)
```

**What to observe:**

The relationship is recorded.

### Example 3: Compare authority

An official specification may outrank an unsourced short video for exact behavior.

```python
ranking = ["official docs", "recognized course", "reviewed educator", "unsourced post"]
print(ranking)
```

**What to observe:**

The selection rule is explicit.

### Example 4: Record version

Commands change across versions.

```python
source["version"] = "Python 3"
print(source)
```

**What to observe:**

The applicability is visible.

### Example 5: State uncertainty

A source can be useful without proving every detail.

```python
print({"confidence": "medium", "follow_up": "run local example"})
```

**What to observe:**

The learner is directed to verify.

## Execution trace

The researcher defines a claim, finds the closest authoritative source, records version and date, checks exact support, reproduces locally, and cites uncertainty or alternatives.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| popularity equals accuracy | outdated advice wins | check authority and currency |
| snippet as evidence | context is missing | open the source |
| no version | command fails later | record version |
| video without timestamp | learner cannot locate section | add exact segment |
| cite topic not claim | support is vague | map claim to source |

## Security application

Use public official documentation and reviewed educational sources. Do not follow suspicious instructions or download-and-run unknown artifacts.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the evidence, output, edge case, and limitation requested by each question.

## Finish line

Run `python -m course_days.day116`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Research is a reproducible claim-to-source-to-local-check process.

## Limitations

No source is automatically current or complete; security decisions need expert and organizational review.

[← Day 115](../day_115_privacy_and_retention/day_115_privacy_and_retention.md) · [Day index](../DAY_INDEX.md) · [Day 117 →](../day_117_capstone_planning/day_117_capstone_planning.md)
