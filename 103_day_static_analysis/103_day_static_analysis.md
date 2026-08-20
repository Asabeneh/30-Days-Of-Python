# Day 103: Static Analysis and Code Review Signals

[← Day 102](../102_day_ci_quality_gates/102_day_ci_quality_gates.md) · [Day index](../DAY_INDEX.md) · [Day 104 →](../104_day_sbom_and_provenance/104_day_sbom_and_provenance.md)

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

Static tools find patterns without executing the program. They are valuable review assistants when their findings are understood, triaged, and combined with tests rather than treated as proof of security.

## Prerequisites

Complete Day 102. Work from a clean virtual environment and use only local synthetic fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using it
- run and modify all worked examples
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Run a local lint and type-check policy, classify findings, and record justified exceptions narrowly.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, destructive actions, persistence, or processing of private data.

## Lesson

### Vocabulary

Static analysis inspects source. A rule identifies a pattern. A suppression disables a finding. A false positive is a finding that does not represent a defect in context.

## Worked examples

### Example 1: Run a checker

A command returns findings for review.

```python
findings = [{"rule": "E501", "file": "module.py", "line": 10}]
print(findings)
```

**What to observe:**

The finding points to a location.

### Example 2: Classify severity

Not every warning has the same release impact.

```python
finding = {"rule": "unsafe-path", "severity": "high", "status": "open"}
print(finding)
```

**What to observe:**

The status drives action.

### Example 3: Justify an exception

A suppression should be narrow and documented.

```python
exception = {
    "rule": "line-length",
    "scope": "embedded fixture only",
    "reason": "generated teaching text",
}
print(exception)
```

**What to observe:**

The exception does not disable all checks.

### Example 4: Combine with tests

Static output and runtime behavior answer different questions.

```python
evidence = {"lint": "passed", "tests": "passed", "security_review": "pending"}
print(evidence)
```

**What to observe:**

The evidence remains multidimensional.

### Example 5: Review a diff

A clean tool result does not replace human review.

```python
review = {"diff_read": True, "assumptions_checked": True, "owner": "student"}
print(review)
```

**What to observe:**

The review record is explicit.

## Execution trace

Source is checked, findings are categorized, narrow exceptions are justified, tests add runtime evidence, and a human reviews assumptions before release.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| tool equals proof | behavior is untested | add tests and review |
| disable rule globally | signal disappears | narrow suppression |
| ignore all warnings | debt accumulates | triage and own findings |
| copy tool config blindly | checks mismatch code | understand rules |
| no version | result changes silently | record tool/version |

## Security application

Run only local tools on course code. Do not upload source containing private material to an external analyzer.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the evidence, output, edge case, and limitation requested by each question.

## Finish line

Run `python -m course_days.day103`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Static analysis is a signal generator; engineers interpret the signal and prove behavior with tests and review.

## Limitations

Static tools have blind spots, false positives, and configuration dependence.

[← Day 102](../102_day_ci_quality_gates/102_day_ci_quality_gates.md) · [Day index](../DAY_INDEX.md) · [Day 104 →](../104_day_sbom_and_provenance/104_day_sbom_and_provenance.md)
