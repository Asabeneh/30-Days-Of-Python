# Day 29: Threat Models, Assets, and Abuse Cases

[Previous](../028_day_dependency_hygiene_and_sboms/028_day_dependency_hygiene_and_sboms.md) | [Next](../030_day_project__secure_evidence_journal/030_day_project__secure_evidence_journal.md)

## Table of Contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Core lesson](#core-lesson)
- [Common mistakes](#common-mistakes)
- [Practice](#practice)
- [Mental model](#mental-model)
- [Finish line](#finish-line)

## Why this lesson exists

Security engineering becomes dependable when its inputs, dependencies, failure behavior, and evidence are visible. This day builds one professional Python habit through a bounded local exercise.

## Prerequisites

Complete Day 28, keep [SETUP.md](../SETUP.md) available, and read [SAFETY_AND_LAB_RULES.md](../SAFETY_AND_LAB_RULES.md).

## Outcomes

You can explain the concept, trace the starter, make one controlled change, test a normal and negative case, and document one security limitation.

## The problem

A security utility often fails at a boundary: installation, command-line input, configuration, data serialization, logging, review, dependencies, or design assumptions. Today makes one such boundary explicit.

## Security boundary

Use only synthetic data and local files. Do not add real credentials, private evidence, public targets, or network access to the starter. Stop if the exercise leaves its documented scope.

## Core lesson

A threat model starts with assets and trust boundaries. Then describe plausible threats, controls, assumptions, and residual risk.

```text
asset: synthetic case record
trust boundary: CLI input → parser
threat: malformed field changes triage
control: schema validation + negative test
residual risk: parser does not prove source authenticity
```

Do not write “secure” as a control. Name the mechanism and the evidence that would show it works.

Security connection: threat modeling is a design activity, not a document added after the code is finished.

### Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| Treating tools as magic | The learner cannot reproduce the result | State the interpreter, input, command, and expected output |
| Trusting representation | Malformed data enters the decision layer | Validate fields and types at the boundary |
| Logging everything | Secrets or private data appear in output | Minimize, redact, and test logging behavior |
| Confusing a control with proof | A checklist is called “secure” | Name the test and the residual risk |

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested commands, produce the requested artifact, and record the edge case or limitation asked for by the exercise. Use [hints](practice/hints.md) only after a real attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Mental model

> A threat model turns vague concern into explicit assets, trust boundaries, threats, controls, assumptions, and residual risk.

## Finish line

Run the starter, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.
