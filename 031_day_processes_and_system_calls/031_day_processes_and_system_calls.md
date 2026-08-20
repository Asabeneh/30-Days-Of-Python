# Day 31: Processes and Safe System Calls

[← Day 30](../030_day_project__secure_evidence_journal/030_day_project__secure_evidence_journal.md) · [Day index](../DAY_INDEX.md) · [Day 32 →](../032_day_linux_command_line/032_day_linux_command_line.md)

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

Operating-system automation is powerful because it crosses from Python into another process. It is dangerous when arguments, environment, working directory, output, and lifetime are implicit.

## Prerequisites

Complete Day 30 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 31

## The problem

Run a harmless local command and capture its result without turning user input into shell syntax.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Lesson

### Vocabulary

A **process** is a running program. `subprocess.run` starts and waits for one. `argv` is the list of arguments. A **return code** reports process completion.

## Worked examples

### Example 1: Run an argument list

Pass the program and each argument as separate data values.

```python
import subprocess

result = subprocess.run(
    ["python", "--version"], capture_output=True, text=True, check=False
)
print(result.returncode)
```

**What to observe:**

Usually `0` for a successful local interpreter call.

### Example 2: Capture output

Captured output can be tested instead of printed blindly.

```python
result = subprocess.run(
    ["python", "-c", "print('training')"], capture_output=True, text=True
)
print(result.stdout.strip())
```

**What to observe:**

`training`

### Example 3: Check failure explicitly

A non-zero return code is data the caller must handle.

```python
result = subprocess.run(
    ["python", "-c", "raise SystemExit(2)"], capture_output=True, text=True
)
print(result.returncode)
```

**What to observe:**

`2`

### Example 4: Set a working directory

The current directory affects relative paths and should be explicit.

```python
result = subprocess.run(
    ["python", "-c", "import pathlib; print(pathlib.Path.cwd())"],
    cwd="shared/fixtures",
    capture_output=True,
    text=True,
)
```

**What to observe:**

The child prints the approved fixture directory.

### Example 5: Use a timeout

A child process must not run forever.

```python
subprocess.run(["python", "-c", "import time; time.sleep(1)"], timeout=2)
```

**What to observe:**

The process finishes within the bound.

## Execution trace

Python creates the child with the chosen argv, cwd, environment, capture settings, and timeout; it returns a result or raises a timeout/OS error. Each option changes the trust boundary.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| `shell=True` with input | input becomes shell syntax | use argv lists |
| inherit current directory | relative path escapes scope | set `cwd` |
| ignore return code | failure looks successful | inspect or use `check=True` deliberately |
| capture unlimited output | memory grows | cap or stream output |
| no timeout | process hangs | set a finite timeout |

## Security application

Run only interpreters or harmless commands against the course fixture. Never turn this lesson into a scanner or remote command runner.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run every requested command, create the requested artifact, and record the limitation the exercise asks you to name.

## Finish line

Run `python -m course_days.day031`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A subprocess call is an operating-system trust boundary whose command, arguments, directory, environment, output, and lifetime must be explicit.

## Limitations

Even `shell=False` does not make a command safe if the executable, arguments, privileges, or working directory are unsafe.

[← Day 30](../030_day_project__secure_evidence_journal/030_day_project__secure_evidence_journal.md) · [Day index](../DAY_INDEX.md) · [Day 32 →](../032_day_linux_command_line/032_day_linux_command_line.md)
