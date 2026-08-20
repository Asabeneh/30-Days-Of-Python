# Day 20: Project: Build a Safe Log-Triage CLI

[Previous](../019_day_testing_with_pytest/019_day_testing_with_pytest.md) | [Next](../021_day_virtual_environments/021_day_virtual_environments.md)

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

Python becomes useful in cybersecurity when its behavior is predictable, testable, and explainable. This day introduces a professional engineering idea through a small local problem before asking you to combine it with other tools.

## Prerequisites

You should be able to run the previous day, write a small function, and use the setup in [SETUP.md](../SETUP.md). If a term is unfamiliar, return to the previous lesson rather than copying a later pattern.

## Outcomes

By the end, you can explain the core concept, trace the starter, predict a changed result, write a normal and negative test, and state what the exercise does not prove about a real system.

## The problem

Security data is untrusted, incomplete, and easy to misinterpret. The problem today is to make one transformation or decision explicit enough that another learner can run it, test it, and review its assumptions.

## Security boundary

Use only the synthetic fixtures supplied by the course or a local file you created. Do not substitute public targets, university systems, employer systems, real credentials, or private evidence. Read `lab/scope.md` before changing the exercise.

## Core lesson

The first project combines the phase: read a bounded synthetic log, parse a small grammar, classify events, preserve raw evidence, and print an explainable report.

### Requirements

The CLI accepts a fixture path and a maximum number of lines. It must reject paths outside the supplied fixture directory, report malformed lines without crashing the complete run, preserve raw text in findings, and distinguish observations from analyst conclusions.

### Suggested design

Separate the program into input validation, line parsing, policy classification, and output formatting. Test each layer independently. Use a `main()` function that translates exceptions into a short user-facing error and a non-zero exit status.

### Security connection

This is a triage helper, not an incident verdict. Its README must state its scope, data format, limitations, and how to reset the fixture.


### Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| Using a broad catch-all | A real failure looks like an empty success | Catch expected boundary errors and preserve unexpected failures |
| Skipping the raw value | A reviewer cannot reproduce the decision | Keep raw input next to normalized or parsed fields |
| Assuming a type hint is validation | Malformed runtime data still enters the function | Validate at the boundary and test rejection |
| Optimizing before measuring | The code becomes harder to explain | Build the simplest correct version, then measure |

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested commands, produce the requested artifact, and record the edge case or limitation asked for by the exercise. Use [hints](practice/hints.md) only after a real attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Mental model

> Project: Build a Safe Log-Triage CLI is valuable when the boundary, assumptions, failure behavior, and evidence are visible.

## Finish line

Run the starter, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.
