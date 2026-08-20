# Day 28: Dependency Hygiene and SBOM Thinking

[← Day 27](../day_27_git_and_code_review/day_27_git_and_code_review.md) · [Day index](../DAY_INDEX.md) · [Day 29 →](../day_29_threat_modeling/day_29_threat_modeling.md)

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

Python packages expand what a tool can do and what it must trust. Dependency hygiene makes versions, origins, licenses, and update decisions visible.

## Prerequisites

Complete Day 27 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 28

## The problem

Produce a small inventory for the course tools without treating a package name as proof of safety.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Lesson

### Vocabulary

A **dependency** is code your project relies on. An **SBOM** is a machine-readable inventory of components. A **transitive dependency** is pulled in by another dependency.

## Worked examples

### Example 1: List dependencies

The project configuration is the starting point for an inventory.

```python
dependencies = ["pytest", "ruff", "mypy"]
for name in dependencies:
    print(name)
```

**What to observe:**

Each package is named explicitly.

### Example 2: Record a version

A version makes a test result more reproducible.

```python
package = {"name": "pytest", "version": "reviewed-version", "purpose": "tests"}
print(package)
```

**What to observe:**

The record has name, version, and purpose.

### Example 3: Separate runtime and development

A production tool should not ship every teaching utility.

```python
runtime = []
development = ["pytest", "ruff", "mypy"]
print(runtime, development)
```

**What to observe:**

The two sets have different deployment implications.

### Example 4: Check a lock-like record

A review can compare the declared record to the installed environment.

```python
declared = {"pytest"}
installed = {"pytest", "unexpected-package"}
print(installed - declared)
```

**What to observe:**

The unexpected package is visible for investigation.

### Example 5: State provenance questions

An inventory is a starting point for review.

```python
questions = [
    "Where was it obtained?",
    "Who maintains it?",
    "What license applies?",
    "When was it reviewed?",
]
print(questions)
```

**What to observe:**

The checklist prevents “it installed” from becoming “it is trusted.”

## Execution trace

The project declares components, the environment reports installed components, and a review compares the two while recording provenance and purpose.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| latest always | updates introduce surprises | review and test updates |
| package name only | typosquatting or confusion | verify source and provenance |
| ignore transitive packages | hidden code enters the build | inventory the full environment |
| no license record | distribution risk appears late | review license context |
| install into system | unrelated projects change | use the project environment |

## Security application

Create an SBOM-like table for the course environment only. Do not upload private dependency reports or install packages from unverified commands.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run every requested command, create the requested artifact, and record the limitation the exercise asks you to name.

## Finish line

Run `python -m course_days.day028`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A dependency is part of the system’s trust boundary even when your code did not write it.

## Limitations

An inventory does not prove a package is secure. Vulnerabilities, maintainer compromise, build tampering, and configuration risk remain possible.

[← Day 27](../day_27_git_and_code_review/day_27_git_and_code_review.md) · [Day index](../DAY_INDEX.md) · [Day 29 →](../day_29_threat_modeling/day_29_threat_modeling.md)
