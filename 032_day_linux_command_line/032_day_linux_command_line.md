# Day 32: Linux Command Line and Permission Thinking

[Previous](../031_day_processes_and_system_calls/031_day_processes_and_system_calls.md) | [Next](../033_day_paths_and_file_metadata/033_day_paths_and_file_metadata.md)

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

A Python security tool interacts with a host that has processes, permissions, paths, resource limits, and concurrent work. This lesson makes one host-level boundary visible and testable.

## Prerequisites

Complete Day 31, keep [SETUP.md](../SETUP.md) available, and read [SAFETY_AND_LAB_RULES.md](../SAFETY_AND_LAB_RULES.md).

## Outcomes

You can explain the concept, trace the starter, make one controlled change, test a normal and negative case, and state what the local fixture does not represent.

## The problem

Host automation can collect useful evidence or cause unexpected load and data exposure. The problem today is to make the target, permission, resource, and cleanup assumptions explicit before writing a broader tool.

## Security boundary

Use only the repository and supplied synthetic fixtures. Do not inspect other users, services, university systems, employer systems, or public targets. Keep collection bounded and stop if scope changes.

<!-- video-resources:start -->
## Video support

**Inline recommendation:** [Introduction to Linux & Terminal Commands - Full Course for Beginners](https://www.youtube.com/watch?v=iwolPf6kN-k).

- Watch [00:00–01:37: Intro](https://www.youtube.com/watch?v=iwolPf6kN-k&t=0s) for **course orientation**. Then return to this lesson and run the local starter.
- Watch [01:37–03:57: About the lecture](https://www.youtube.com/watch?v=iwolPf6kN-k&t=97s) for **why the terminal matters**. Then return to this lesson and run the local starter.
- Watch [03:57–06:24: Terminal Emulator](https://www.youtube.com/watch?v=iwolPf6kN-k&t=237s) for **terminal window**. Then return to this lesson and run the local starter.
- Watch [06:24–08:58: What is Shell](https://www.youtube.com/watch?v=iwolPf6kN-k&t=384s) for **shell versus terminal**. Then return to this lesson and run the local starter.
- Watch [08:58–11:04: List commands](https://www.youtube.com/watch?v=iwolPf6kN-k&t=538s) for **listing and inspection**. Then return to this lesson and run the local starter.
- Watch [11:04–12:24: ls](https://www.youtube.com/watch?v=iwolPf6kN-k&t=664s) for **list directory contents**. Then return to this lesson and run the local starter.
- Watch [12:24–12:54: mkdir](https://www.youtube.com/watch?v=iwolPf6kN-k&t=744s) for **create a directory**. Then return to this lesson and run the local starter.
- Watch [12:54–15:00: cd](https://www.youtube.com/watch?v=iwolPf6kN-k&t=774s) for **change directory**. Then return to this lesson and run the local starter.

Written alternative: [https://ubuntu.com/tutorials/command-line-for-beginners](https://ubuntu.com/tutorials/command-line-for-beginners).
<!-- video-resources:end -->

## Core lesson

The shell is both a user interface and a language with quoting, expansion, pipes, and redirection rules. Learn the command first, then automate it only when the boundary is clear.

```text
python -c "from pathlib import Path; print(Path.cwd())"
```

Prefer Python APIs for file operations you can express directly. If you use a shell command in a lab, record the exact command, target directory, expected output, and cleanup.

Security connection: a command that is harmless in one directory can be dangerous in another. Current directory and privileges are part of the risk model.

### Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| Assuming a name proves identity | A process or file is attributed without evidence | Record the exact observation and its limits |
| Using free-form commands | Shell metacharacters change behavior | Pass argument lists and allowlist programs |
| Ignoring limits | A collector can run forever or consume memory | Add bounds, timeouts, and cancellation |
| Treating differences as verdicts | A baseline change is called compromise | Report the difference and seek context |

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested commands, produce the requested artifact, and record the edge case or limitation asked for by the exercise. Use [hints](practice/hints.md) only after a real attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Mental model

> The command line is a programmable interface to the host, so every command should have a clear target and bounded effect.

## Finish line

Run the starter, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.
