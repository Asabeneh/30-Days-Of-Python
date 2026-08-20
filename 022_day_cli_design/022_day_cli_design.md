# Day 22: Command-Line Interfaces and Explicit Input

[← Day 21](../021_day_virtual_environments/021_day_virtual_environments.md) · [Day index](../DAY_INDEX.md) · [Day 23 →](../023_day_configuration_and_secrets/023_day_configuration_and_secrets.md)

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

A CLI is the first trust boundary for many security utilities. Clear options, help text, validation, and exit statuses make a tool safer to automate and easier to review.

## Prerequisites

Complete Day 21 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 22

## The problem

Turn the log triage function into a command that accepts a fixture path, a finite limit, and an output mode without relying on ambiguous positional input.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Lesson

### Vocabulary

An **argument parser** turns shell text into values. An **exit status** communicates success or failure. A **flag** is an explicit named option.

## Worked examples

### Example 1: Parse a flag

`argparse` converts a command into a namespace.

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--limit", type=int, default=100)
args = parser.parse_args(["--limit", "5"])
print(args.limit)
```

**What to observe:**

`5` as an integer.

### Example 2: Show help

Help is part of the public contract.

```python
parser = argparse.ArgumentParser(description="Review a local training fixture")
parser.add_argument("--input", required=True)
print(parser.format_help())
```

**What to observe:**

The help names the required input and its purpose.

### Example 3: Reject a bound

Type conversion is not enough; enforce a safe domain.

```python
def positive_limit(value):
    number = int(value)
    if not 1 <= number <= 10_000:
        raise argparse.ArgumentTypeError("limit must be 1..10000")
    return number
```

**What to observe:**

Bad limits are rejected before processing begins.

### Example 4: Return a status

Shell automation needs a stable result.

```python
def main():
    return 0


raise SystemExit(main())
```

**What to observe:**

Zero conventionally means success; document non-zero meanings.

### Example 5: Keep paths as data

An input path is not a shell command.

```python
parser.add_argument("--input", type=Path)
print(args.input)
```

**What to observe:**

The value remains a path object until a bounded file function accepts it.

## Execution trace

The shell provides tokens, argparse converts them, the custom validator checks policy, and only then does the tool resolve a path or process a fixture.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| `shell=True` for convenience | input becomes command syntax | pass data as arguments |
| no help | users guess the interface | describe every option |
| unlimited default | automation consumes too much | choose a finite bound |
| print errors and return 0 | scripts treat failure as success | use documented exit statuses |
| positional secrets | shell history stores them | use safer secret mechanisms and never echo values |

## Security application

Build a local CLI that accepts only the course fixture root, a finite line limit, and a report path beneath a dedicated output directory. Test invalid paths and limits.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run every requested command, create the requested artifact, and record the limitation the exercise asks you to name.

## Finish line

Run `python -m course_days.day022`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A CLI makes program assumptions visible at the point where human or automation input enters.

## Limitations

A well-designed CLI cannot authorize the target. Its caller still needs permission, and its path and output policy need defense in depth.

[← Day 21](../021_day_virtual_environments/021_day_virtual_environments.md) · [Day index](../DAY_INDEX.md) · [Day 23 →](../023_day_configuration_and_secrets/023_day_configuration_and_secrets.md)
