# Day 94: CVE and Severity Reasoning

[← Day 93](../093_day_safe_service_discovery/093_day_safe_service_discovery.md) · [Day index](../DAY_INDEX.md) · [Day 95 →](../095_day_local_web_testing/095_day_local_web_testing.md)

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

A vulnerability identifier and a severity score are evidence inputs, not automatic remediation decisions. Engineers need affected version, exposure, exploitability, impact, and compensating controls.

## Prerequisites

Complete Day 93. Use only the local fixtures and explicit loopback assessment scope supplied by the course.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using a tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Evaluate a synthetic vulnerability record and produce a cautious local risk note.

## Security boundary

This lesson is educational and authorized-lab-only. It does not authorize public scanning, credential guessing, exploitation, interception, persistence, or changes to systems you do not own.

## Lesson

### Vocabulary

A vulnerability is a weakness. A CVE identifier names a published issue. Severity estimates impact and exploitability under a scoring model. Risk adds environment and business context.

## Worked examples

### Example 1: Model a record

A record needs affected component and version.

```python
vuln = {"id": "CVE-training", "component": "training-lib", "version": "1.0"}
print(vuln)
```

**What to observe:**

The issue is synthetic.

### Example 2: Separate severity and exposure

A high severity issue may not be reachable in this environment.

```python
vuln.update({"severity": "high", "exposed": False})
print(vuln)
```

**What to observe:**

The fields stay separate.

### Example 3: Check applicability

Affected version must be compared with the installed record.

```python
installed = "1.0"
print(installed == vuln["version"])
```

**What to observe:**

Applicability is a separate fact.

### Example 4: Record control

A compensating control changes local risk, not the published severity.

```python
vuln["control"] = "loopback-only service"
print(vuln)
```

**What to observe:**

The context is recorded.

### Example 5: Choose action

Action should include owner and deadline rather than panic.

```python
action = {
    "owner": "student",
    "next": "upgrade training dependency",
    "status": "planned",
}
print(action)
```

**What to observe:**

The response is actionable.

## Execution trace

The analyst verifies identity and version, assesses exposure and controls, separates published severity from local risk, and records an owned next action.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| score equals risk | environment is ignored | assess exposure and context |
| name equals affected | version is not checked | verify applicability |
| exploit immediately | testing exceeds authorization | remediate or use lab |
| no source/date | record is stale | preserve provenance |
| panic language | decision quality drops | write owner and next step |

## Security application

Use fictional vulnerability records and local dependencies. Do not download exploit code or test a public service.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the requested evidence, expected behavior, edge case, and limitation.

## Finish line

Run `python -m course_days.day094`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Vulnerability management connects published weakness, local applicability, exposure, controls, and ownership.

## Limitations

Severity models vary and can be incomplete; legal, business, and operational risk need domain owners.

[← Day 93](../093_day_safe_service_discovery/093_day_safe_service_discovery.md) · [Day index](../DAY_INDEX.md) · [Day 95 →](../095_day_local_web_testing/095_day_local_web_testing.md)
