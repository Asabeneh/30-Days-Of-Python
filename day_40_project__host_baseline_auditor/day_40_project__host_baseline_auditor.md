# Day 40: Project: Host Baseline Auditor

[← Day 39](../day_39_host_inventories/day_39_host_inventories.md) · [Day index](../DAY_INDEX.md) · [Day 41 →](../day_41_addresses__ports__and_sockets/day_41_addresses__ports__and_sockets.md)

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

The project combines operating-system concepts into a local, bounded auditor. It should collect a small approved inventory, compare it to a synthetic baseline, and produce explainable drift without destructive action.

## Prerequisites

Complete Day 39 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 40

## The problem

Build a host baseline auditor for a fixture representation, with explicit scope, deterministic output, tests, and a resettable report.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Lesson

### Vocabulary

An **auditor** compares observed state with an expected baseline. A **control** defines what is allowed. A **finding** describes a difference and its evidence.

## Worked examples

### Example 1: Define the baseline

The baseline is data with scope and version, not a hidden assumption.

```python
baseline = {
    "version": 1,
    "scope": ["python_version", "fixture_files"],
    "python_version": "3.x",
}
print(baseline)
```

**What to observe:**

The expected state is visible.

### Example 2: Collect bounded state

The auditor should collect only the properties it has permission to inspect.

```python
observed = {"python_version": "3.x", "fixture_files": ["events.log"]}
print(observed)
```

**What to observe:**

The observed state matches the declared scope.

### Example 3: Compare fields

Each comparison should name its field and evidence.

```python
findings = []
if observed["python_version"] != baseline["python_version"]:
    findings.append({"field": "python_version", "status": "changed"})
print(findings)
```

**What to observe:**

No finding when the values match.

### Example 4: Handle missing state

Missing data is not the same as compliant state.

```python
if "fixture_files" not in observed:
    findings.append({"field": "fixture_files", "status": "not_observed"})
```

**What to observe:**

The report preserves uncertainty.

### Example 5: Write the project report

A report needs scope, timestamp, findings, limitations, and reset instructions.

```python
report = {"scope": baseline["scope"], "findings": findings, "complete": True}
print(report)
```

**What to observe:**

The artifact is reviewable and bounded.

## Execution trace

The auditor loads the versioned baseline, collects only approved local fixture state, normalizes it, compares field by field, reports changed/missing/not-observed states, and writes a safe report.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| audit everything | scope and privacy fail | define an allowlist of properties |
| missing equals compliant | blind spots look safe | report not observed |
| destructive remediation | audit changes the system | report first; remediate separately |
| nondeterministic output | diffs are noisy | sort and normalize |
| no reset | generated reports accumulate | document cleanup |

## Security application

The project is fixture-only and read-only. It must not alter permissions, services, processes, accounts, or network settings. Its README must include scope, baseline version, sample output, tests, limitations, and reset.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run every requested command, create the requested artifact, and record the limitation the exercise asks you to name.

## Finish line

Run `python -m course_days.day040`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> An auditor produces a bounded comparison between an approved baseline and an observed snapshot; it does not own the system or decide intent.

## Limitations

A baseline auditor cannot prove continuous compliance, detect every change, or safely remediate production systems without additional controls and authorization.

[← Day 39](../day_39_host_inventories/day_39_host_inventories.md) · [Day index](../DAY_INDEX.md) · [Day 41 →](../day_41_addresses__ports__and_sockets/day_41_addresses__ports__and_sockets.md)
