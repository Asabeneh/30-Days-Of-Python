# Day 32: Linux Command-Line Concepts

[← Day 31](../031_day_processes_and_system_calls/031_day_processes_and_system_calls.md) · [Day index](../DAY_INDEX.md) · [Day 33 →](../033_day_paths_and_file_metadata/033_day_paths_and_file_metadata.md)

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

Security engineers need a shell mental model before automating it. Understanding paths, streams, exit statuses, and pipes helps a learner inspect a local system without treating commands as magic incantations.

## Prerequisites

Complete Day 31 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 32

## The problem

Use harmless commands to inspect the repository and connect their outputs to Python’s process model.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Lesson

### Vocabulary

A **shell** starts programs and connects streams. `stdout` is normal output. `stderr` is diagnostic output. A **pipe** sends one process’s output to another.

## Worked examples

### Example 1: Print the current directory

A relative path has meaning only relative to the current working directory.

```python
pwd
```

**What to observe:**

The shell prints the absolute working directory.

### Example 2: List deliberately

Start with visible, bounded directory contents.

```python
ls -la shared/fixtures
```

**What to observe:**

The command lists the fixture directory; inspect before acting.

### Example 3: Search text

`grep` filters text but should be used on authorized local fixtures.

```python
grep -n "severity" shared/fixtures/events.log
```

**What to observe:**

Matching lines appear with line numbers.

### Example 4: Inspect exit status

A command can fail even when the shell displays output.

```python
grep -q "missing" shared/fixtures/events.log
echo $?
```

**What to observe:**

A non-zero status means the pattern was not found.

### Example 5: Connect streams conceptually

Pipelines transform output, but each stage needs bounded inputs.

```python
printf "ok\nfailed\n" | grep failed
```

**What to observe:**

`failed` is selected from synthetic text.

## Execution trace

The shell resolves a command, opens streams, runs it in the current directory, and stores an exit status. Python can reproduce the process while making argv and cwd more explicit.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| wrong directory | command sees wrong files | run `pwd` first |
| `rm` while learning | data is destroyed | inspect with `ls` and use resettable fixtures |
| pipe hides failure | final output looks fine | inspect each status or use Python stages |
| quote confusion | arguments split unexpectedly | understand shell quoting and prefer argv lists in Python |
| public target | unauthorized activity | restrict to local fixtures |

## Security application

Use only repository fixtures. Do not run enumeration, scanning, or destructive commands; the goal is streams and process reasoning.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run every requested command, create the requested artifact, and record the limitation the exercise asks you to name.

## Finish line

Run `python -m course_days.day032`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> The shell is a language that creates processes and connects streams; Python automation should make that implicit behavior visible.

## Limitations

Shell behavior differs by platform and shell implementation. Production automation needs a supported command set and explicit error handling.

[← Day 31](../031_day_processes_and_system_calls/031_day_processes_and_system_calls.md) · [Day index](../DAY_INDEX.md) · [Day 33 →](../033_day_paths_and_file_metadata/033_day_paths_and_file_metadata.md)
