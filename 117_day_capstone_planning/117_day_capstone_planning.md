# Day 117: Capstone planning

[Previous](../116_day_research_and_source_evaluation/116_day_research_and_source_evaluation.md) | [Next](../118_day_capstone_implementation/118_day_capstone_implementation.md)

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

This lesson belongs to **Advanced Integration and Capstone**. It turns one engineering concept into a runnable, testable, and explainable security practice. The final lesson will be expanded with execution traces, diagrams, common-mistake tables, and worked examples before that phase is marked complete.

## Prerequisites

Complete the previous lesson and keep the repository setup from [SETUP.md](../SETUP.md) available. Revisit the linked previous lesson if any term is unfamiliar.

## Outcomes

By the end, you can explain the concept, run the starter, predict a result, write a small test, identify one failure mode, and state the security boundary of the exercise.

## The problem

Security engineering requires reliable decisions under imperfect input and failure. This day introduces **Capstone planning** through a bounded local fixture before asking you to generalize the pattern.

## Security boundary

Use only the supplied synthetic data or a local fixture. Do not substitute public targets, university systems, employer systems, real credentials, or private evidence. Stop if the scope changes.

## Concept map

Start with the smallest runnable example in `starter/main.py`. Trace the input, transformation, decision, and output. Then deliberately change one input and predict the result before running again. The full lesson expansion will add a visual data-flow diagram, a common-mistakes table, and an explanation of what the tool cannot conclude.

## Practice

Complete [practice/prompts.md](practice/prompts.md) before opening [hints](practice/hints.md) or [solutions](practice/solutions.md). Level 1 builds mechanical fluency. Level 2 applies the idea to a security utility. Level 3 asks for an edge case, negative test, or design trade-off.

## Mental model

> A security tool is a small program whose assumptions, inputs, outputs, and limits must be made visible.

## Finish line

Run the starter, pass the day tests when present, complete the core practice, and write one sentence naming an edge case and one sentence naming the lab boundary.
