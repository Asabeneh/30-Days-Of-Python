# Day 101: Secure SDLC and Security Requirements

[← Day 100](../100_day_project__authorized_local_assessment/100_day_project__authorized_local_assessment.md) · [Day index](../DAY_INDEX.md) · [Day 102 →](../102_day_ci_quality_gates/102_day_ci_quality_gates.md)

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

Security is cheaper to reason about before code and deployment decisions harden. A secure software-development lifecycle turns assets, abuse cases, controls, tests, and ownership into ordinary engineering work.

## Prerequisites

Complete Day 100. Work from a clean virtual environment and use only local synthetic fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using it
- run and modify all worked examples
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Translate a synthetic case API requirement into security acceptance criteria that can be tested before release.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, destructive actions, persistence, or processing of private data.

## Lesson

### Vocabulary

An abuse case describes harmful use. A security requirement states a control. Acceptance criteria define observable evidence. A threat model records assumptions and residual risk.

## Worked examples

### Example 1: Name an asset

Begin with what the feature must protect.

```python
asset = {"name": "synthetic case records", "owner": "course", "impact": "privacy"}
print(asset)
```

**What to observe:**

The asset and owner are explicit.

### Example 2: Write an abuse case

Describe a harmful condition without writing an exploit.

```python
abuse = "A caller reads a case outside its assigned scope."
print(abuse)
```

**What to observe:**

The misuse is testable as an authorization case.

### Example 3: Write a requirement

Turn the abuse case into a control.

```python
requirement = "The service must check object scope before returning a case."
print(requirement)
```

**What to observe:**

The requirement states behavior.

### Example 4: Define acceptance evidence

A requirement needs a proof method.

```python
acceptance = {
    "case": "cross-object read",
    "expected": 403,
    "test": "test_authorization_matrix",
}
print(acceptance)
```

**What to observe:**

The control has observable evidence.

### Example 5: Assign ownership

Unowned requirements become forgotten requirements.

```python
print({"owner": "service-team", "review": "before release"})
```

**What to observe:**

The lifecycle includes responsibility.

## Execution trace

The requirement begins with an asset and abuse case, becomes a control, receives a testable acceptance criterion, and is assigned to an owner before implementation.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| security at the end | architecture is expensive to change | write requirements early |
| vague secure language | no test can prove it | name observable behavior |
| no owner | control is forgotten | assign responsibility |
| exploit-first | scope and safety drift | use abuse cases and fixtures |
| no residual risk | release claim is overconfident | record limits |

## Security application

Use the local synthetic case API only. Turn its security requirements into tests and review items; do not build new attack capability.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the evidence, output, edge case, and limitation requested by each question.

## Finish line

Run `python -m course_days.day101`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Secure SDLC is a repeatable path from asset and abuse case to owned, testable control.

## Limitations

No lifecycle prevents all defects; security requirements need domain, privacy, and operational review.

[← Day 100](../100_day_project__authorized_local_assessment/100_day_project__authorized_local_assessment.md) · [Day index](../DAY_INDEX.md) · [Day 102 →](../102_day_ci_quality_gates/102_day_ci_quality_gates.md)
