# Day 21: Virtual Environments and Reproducible Setup

[← Day 20](../day_20_project__log_triage_cli/day_20_project__log_triage_cli.md) · [Day index](../DAY_INDEX.md) · [Day 22 →](../day_22_cli_design/day_22_cli_design.md)

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

A script that works only on its author’s machine is not a reliable security tool. Virtual environments give a project an isolated interpreter and make its dependency assumptions visible.

## Prerequisites

Complete Day 20 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 21

## The problem

A new learner must install the course without confusing the system Python, a global package, and the repository environment.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Lesson

### Vocabulary

A **virtual environment** is an isolated Python installation for one project. The **interpreter** is the executable that runs code. A **dependency** is a package or tool the project needs.

## Worked examples

### Example 1: Create an environment

Use Python’s built-in module to create a `.venv` directory.

```python
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

**What to observe:**

The prompt usually shows `(.venv)` after activation.

### Example 2: Prove the interpreter

Do not trust the prompt alone; ask the selected interpreter where it lives.

```python
python -c "import sys; print(sys.executable)"
```

**What to observe:**

The printed path should point inside the repository’s `.venv`.

### Example 3: Install through the interpreter

`python -m pip` makes it less likely that pip belongs to another Python.

```python
python -m pip install -r requirements-dev.txt
python -m pip list
```

**What to observe:**

The installed tools are associated with the active interpreter.

### Example 4: Freeze a small environment

A project record makes a setup reviewable.

```python
python -m pip freeze > local-environment.txt
```

**What to observe:**

The file records versions; do not commit private paths or unrelated global packages.

### Example 5: Deactivate and compare

Seeing the interpreter change makes environment isolation concrete.

```python
deactivate
python -c "import sys; print(sys.executable)"
```

**What to observe:**

The executable path changes away from `.venv`.

## Execution trace

Activation changes the shell’s command lookup; it does not change Python itself. `python -m pip` uses the interpreter selected by `python`, so the package and runtime stay aligned.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| global install | one project breaks another | activate `.venv` |
| wrong interpreter in VS Code | imports appear missing | select the repository interpreter |
| commit `.venv` | huge machine-specific diff | ignore it and recreate it |
| trust activation blindly | shell and editor disagree | print `sys.executable` |
| install without a record | setup cannot be reproduced | document dependencies and versions |

## Security application

Create and remove a disposable environment for the course only. Never install unknown packages into the system interpreter, and never place credentials in environment snapshots.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run every requested command, create the requested artifact, and record the limitation the exercise asks you to name.

## Finish line

Run `python -m course_days.day021`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> An environment is a reproducible boundary around the interpreter and its dependencies.

## Limitations

Virtual environments do not sandbox malicious code, prove package provenance, or protect a host from a dangerous dependency. Use trusted sources and review the dependency list.

[← Day 20](../day_20_project__log_triage_cli/day_20_project__log_triage_cli.md) · [Day index](../DAY_INDEX.md) · [Day 22 →](../day_22_cli_design/day_22_cli_design.md)
