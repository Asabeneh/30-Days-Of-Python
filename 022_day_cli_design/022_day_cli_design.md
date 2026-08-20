# Day 22: Command-Line Interfaces as Explicit Contracts

[Previous](../021_day_virtual_environments/021_day_virtual_environments.md) | [Next](../023_day_configuration_and_secrets/023_day_configuration_and_secrets.md)

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

Complete Day 21, keep [SETUP.md](../SETUP.md) available, and read [SAFETY_AND_LAB_RULES.md](../SAFETY_AND_LAB_RULES.md).

## Outcomes

You can explain the concept, trace the starter, make one controlled change, test a normal and negative case, and document one security limitation.

## The problem

A security utility often fails at a boundary: installation, command-line input, configuration, data serialization, logging, review, dependencies, or design assumptions. Today makes one such boundary explicit.

## Security boundary

Use only synthetic data and local files. Do not add real credentials, private evidence, public targets, or network access to the starter. Stop if the exercise leaves its documented scope.

## Core lesson

`argparse` turns a command line into named values and documented errors. Design the interface before writing its implementation: what is required, what is optional, what is the default, and what exit status means failure?

```python
parser.add_argument("--limit", type=int, default=100)
```

The parser rejects values that cannot be converted to integers, but it cannot decide whether 100 is an appropriate resource bound. That is application logic.

Security connection: explicit flags reduce hidden behavior. Never place passwords directly in command history, and do not let a path argument escape the documented fixture directory.

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

> A CLI is an interface contract: arguments, defaults, errors, and exit codes should be visible rather than hidden in global state.

## Finish line

Run the starter, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.
