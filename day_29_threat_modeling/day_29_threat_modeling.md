# Day 29: Threat Modeling Before Automation

[← Day 28](../day_28_dependency_hygiene_and_sboms/day_28_dependency_hygiene_and_sboms.md) · [Day index](../DAY_INDEX.md) · [Day 30 →](../day_30_project__secure_evidence_journal/day_30_project__secure_evidence_journal.md)

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

Threat modeling turns “make it secure” into explicit assets, threats, controls, assumptions, and residual risk before code makes the decision harder to change.

## Prerequisites

Complete Day 28 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 29

## The problem

Threat-model the log triage tool and identify what can be harmed, how, and which control reduces the risk.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Lesson

### Vocabulary

An **asset** is something worth protecting. A **threat** is a potential harmful action or condition. A **control** reduces likelihood or impact. **Residual risk** remains after controls.

## Worked examples

### Example 1: Name an asset

Start with what the tool must protect.

```python
assets = ["synthetic evidence", "report integrity", "developer credentials"]
print(assets)
```

**What to observe:**

The list makes scope concrete.

### Example 2: Draw a trust boundary

Mark where data changes trust level.

```python
boundary = {
    "outside": "CLI path and fixture text",
    "inside": "validated event and report writer",
}
print(boundary)
```

**What to observe:**

The boundary identifies where validation belongs.

### Example 3: Describe a threat

A threat statement names actor, action, asset, and impact.

```python
threat = {
    "actor": "malformed fixture",
    "action": "exhausts line processing",
    "asset": "tool availability",
    "impact": "slow or incomplete report",
}
```

**What to observe:**

The threat is specific enough to select a control.

### Example 4: Choose a control

A control should connect directly to the threat.

```python
control = {"threat": threat, "measure": "line limit and truncation flag"}
print(control["measure"])
```

**What to observe:**

The control is bounded processing plus honest reporting.

### Example 5: Record residual risk

Controls change risk; they do not erase it.

```python
residual = "a maliciously shaped line may still be rejected and require review"
print(residual)
```

**What to observe:**

The remaining uncertainty is visible.

## Execution trace

The model starts at asset, crosses a trust boundary, names a threat, chooses a control, and records what remains. It is a reasoning process, not a decorative table.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| list tools instead of threats | controls have no rationale | describe harmful conditions |
| “secure” as a control | no testable behavior | name mechanism and evidence |
| ignore availability | only confidentiality is discussed | include resource abuse and failure |
| no owner | nobody maintains the control | identify responsibility |
| residual risk omitted | report implies certainty | state limits and follow-up |

## Security application

Create a threat model for local synthetic evidence. Do not model or test a public target. Every proposed control needs one local test or inspection method.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run every requested command, create the requested artifact, and record the limitation the exercise asks you to name.

## Finish line

Run `python -m course_days.day029`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Threat modeling is disciplined uncertainty reduction: identify what matters, what can go wrong, and what evidence supports the chosen control.

## Limitations

Threat models are hypotheses. They can miss threats, misunderstand assets, or become stale as the system changes.

[← Day 28](../day_28_dependency_hygiene_and_sboms/day_28_dependency_hygiene_and_sboms.md) · [Day index](../DAY_INDEX.md) · [Day 30 →](../day_30_project__secure_evidence_journal/day_30_project__secure_evidence_journal.md)
