# Day 30: Project: Build a Secure Evidence Journal

[Previous](../029_day_threat_modeling/029_day_threat_modeling.md) | [Next](../031_day_processes_and_system_calls/031_day_processes_and_system_calls.md)

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

Complete Day 29, keep [SETUP.md](../SETUP.md) available, and read [SAFETY_AND_LAB_RULES.md](../SAFETY_AND_LAB_RULES.md).

## Outcomes

You can explain the concept, trace the starter, make one controlled change, test a normal and negative case, and document one security limitation.

## The problem

A security utility often fails at a boundary: installation, command-line input, configuration, data serialization, logging, review, dependencies, or design assumptions. Today makes one such boundary explicit.

## Security boundary

Use only synthetic data and local files. Do not add real credentials, private evidence, public targets, or network access to the starter. Stop if the exercise leaves its documented scope.

## Core lesson

The evidence journal combines the phase. Each entry stores a timestamp, source, raw observation, normalized fields, and provenance. It should reject malformed records, redact named sensitive fields, and make edits visible rather than silently rewriting history.

Suggested design: a small dataclass for entries, a JSON Lines storage format, a validator, a redactor, and a CLI that accepts a bounded input path.

Project evidence: README, setup instructions, tests for invalid data and redaction, a threat model, a sample synthetic journal, and a retrospective.

Security connection: the journal is a learning project, not a chain-of-custody system for real investigations. Its limitations must be explicit.

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

> A secure evidence journal preserves raw observations, records provenance, redacts sensitive fields, and makes its limitations visible.

## Finish line

Run the starter, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.
