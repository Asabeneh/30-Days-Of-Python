# Day 61: Local service architecture

[Previous](../060_day_project__tamper_evident_case_bundle/060_day_project__tamper_evident_case_bundle.md) | [Next](../062_day_request_parsing_and_validation/062_day_request_parsing_and_validation.md)

## Table of Contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Concept map](#concept-map)
- [Practice](#practice)
- [Mental model](#mental-model)
- [Finish line](#finish-line)

## Why this lesson exists

This lesson belongs to **Web Services and Application Security**. It turns one engineering concept into a runnable, testable, and explainable security practice. The final lesson will be expanded with execution traces, diagrams, common-mistake tables, and worked examples before that phase is marked complete.

## Prerequisites

Complete the previous lesson and keep the repository setup from [SETUP.md](../SETUP.md) available. Revisit the linked previous lesson if any term is unfamiliar.

## Outcomes

By the end, you can explain the concept, run the starter, predict a result, write a small test, identify one failure mode, and state the security boundary of the exercise.

## The problem

Security engineering requires reliable decisions under imperfect input and failure. This day introduces **Local service architecture** through a bounded local fixture before asking you to generalize the pattern.

## Security boundary

Use only the supplied synthetic data or a local fixture. Do not substitute public targets, university systems, employer systems, real credentials, or private evidence. Stop if the scope changes.

## Concept map

Start with the smallest runnable example in `starter/main.py`. Trace the input, transformation, decision, and output. Then deliberately change one input and predict the result before running again. The full lesson expansion will add a visual data-flow diagram, a common-mistakes table, and an explanation of what the tool cannot conclude.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested commands, produce the requested artifact, and record the edge case or limitation asked for by the exercise. Use [hints](practice/hints.md) only after a real attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Mental model

> A security tool is a small program whose assumptions, inputs, outputs, and limits must be made visible.

## Finish line

Run the starter, pass the day tests when present, complete the core practice, and write one sentence naming an edge case and one sentence naming the lab boundary.


<!-- video-resources:start -->
## Video support

**Optional recommendation:** [Security Concepts - CompTIA Network+ N10-009 - 4.1](https://www.youtube.com/watch?v=51W4Fhds7DQ).

- Watch [00:00–13:06: Complete focused lesson](https://www.youtube.com/watch?v=51W4Fhds7DQ&t=0s) for **security concepts**. Then return to this lesson and run the local starter.

Written alternative: [https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf).
<!-- video-resources:end -->
