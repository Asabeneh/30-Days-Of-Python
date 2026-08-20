# Day 1: How Programs Run and How to Practise Cybersecurity Safely

[Course home](../README.md) | [002 next](../002_day_values_names_and_input/002_day_values_names_and_input.md)

## Table of Contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Lesson](#lesson)
- [Common mistakes](#common-mistakes)
- [Practice](#practice)
- [Mental model](#mental-model)
- [Finish line](#finish-line)

## Why this lesson exists

This lesson is part of the first phase for a learner who may have never written code. It introduces one idea at a time and connects it to a small, safe cybersecurity problem.

## Prerequisites

- Day 0 or “none” if this is Day 1.
- A working setup from [SETUP.md](../SETUP.md).
- The safety rules in [SAFETY_AND_LAB_RULES.md](../SAFETY_AND_LAB_RULES.md).

## Outcomes

By the end, you can explain the day's mental model, run the starter, predict at least one result, correct one deliberate mistake, and apply the idea to a synthetic security fixture.

## The problem

Security engineering is programming applied to systems, data, and decisions. If the underlying programming idea is vague, the security label only makes the confusion harder to see. This day gives the idea a small problem before adding tools.

## Security boundary

This lesson uses only local text and synthetic examples. Do not replace the fixture path with a university, employer, public website, or another person's data. The objective is to learn a programming idea and a safe evidence habit, not to discover targets.

## Lesson
## Why this lesson exists

A beginner often sees a command print a result and concludes that the computer “just knows” what to do. That mental model makes every later tool feel magical. Security work becomes safer when you can name the program, file, input, output, and permission boundary involved in an action.

## The problem this solves

You need to answer four questions without guessing: where is the code, what reads it, what data enters it, and what evidence proves what happened? Python gives you an interpreter, a standard library, an error message, and a terminal. Today you will use all four.

## The runtime model

A `.py` file is text on disk. When you run `python path/to/file.py`, the Python interpreter reads that text, checks its syntax, executes statements in order, and writes output or an error. The operating system starts the interpreter as a process. The interpreter opens the file. The file may read input, but input does not become trustworthy merely because the interpreter accepted its type as a string.

```text
keyboard or fixture
        │
        ▼
Python program receives text
        │
        ▼
validation and transformation
        │
        ▼
output, evidence, or a clearly reported error
```

Run the starter from the repository root:

```text
python -m course_days.day001
```

Then change one printed name and predict the new output before running it again. That tiny experiment teaches the difference between source text and runtime behavior.

## Your first error is information

Create a temporary file with a missing closing parenthesis and run it. Python reports a `SyntaxError` before it can execute the file. Fix the parenthesis and run it again. Then create a `NameError` by using a name that was never assigned. The two errors answer different questions: the first says the program text is not shaped like Python; the second says the running program cannot find a name.

Read the first error line, the file path, and the line number. Do not start by searching the entire internet. First reduce the problem to the smallest example that still fails.

## Terminal and editor workflow

The terminal is not a black box. `pwd` or `Get-Location` tells you where you are. `ls` or `Get-ChildItem` lists files. `cd` changes the working directory. VS Code's integrated terminal is the same kind of terminal, placed beside your editor. Run the same course command in both places and compare the result.

## A first security distinction

A program can be technically capable of opening a file or connecting to a service without being authorized to do so. Python answers “can this process attempt the operation?” Professional security practice also asks “should it?” and “what evidence and cleanup are required?” Keep those questions separate from syntax.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| Running from the wrong folder | `No module named course_days` | Return to the repository root and verify the path |
| Using the wrong interpreter | A package appears missing | Select `.venv` and run `python -c "import sys; print(sys.executable)"` |
| Treating input as trusted | A classifier accepts malformed text | Parse, validate, and report rejected input |
| Ignoring the first error line | Repeated unrelated fixes | Read the file, line, and error type first |

## Finish line

You can run Day 1, explain the interpreter model, deliberately create and fix one syntax error, identify the current directory, and state why authorization is separate from technical capability.

## Prove it

Write five sentences: what is a runtime, what file did it read, what input did your starter receive, what output did it produce, and what would make a security action unauthorized?


## Common mistakes

The most useful debugging move is to reproduce the smallest failure, read the first error line, identify the value or assumption that differs from your expectation, and change one thing. Do not copy a large solution while the mental model is still unclear.

## Practice

1. **Level 1 — mechanical:** Run the starter, predict one output, change one input, and explain the difference.
2. **Level 2 — applied:** Complete the practice prompt using only concepts taught so far and the supplied synthetic fixture.
3. **Level 3 — synthesis:** Add one edge case, one negative test, and one short note explaining a security limitation.

Open [practice/prompts.md](practice/prompts.md) before [practice/hints.md](practice/hints.md). Review [practice/solutions.md](practice/solutions.md) only after a real attempt.

## Mental model

> Code is text; the Python interpreter turns it into behavior, and a security professional never separates capability from authorization.

## Finish line

Run `python -m course_days.day001`, pass the relevant tests, complete the Level 1 and Level 2 practice, and write one sentence about an edge case or security boundary.
