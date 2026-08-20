# Day 12: Modules, Packages, and Import Boundaries

[← Day 11](../011_day_function_contracts/011_day_function_contracts.md) · [Day index](../DAY_INDEX.md) · [Day 13 →](../013_day_exceptions_and_error_taxonomy/013_day_exceptions_and_error_taxonomy.md)

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

A security tool that grows in one file becomes difficult to test, review, and reuse. Modules let you separate parsing, policy, formatting, and command-line orchestration while keeping import behavior predictable.

## Prerequisites

Complete Day 11 and know how a function contract is written.

## Outcomes

By the end of this lesson, you can:

- create a module with a focused public function
- import a name without running unrelated work
- distinguish a module from a package
- use `__name__ == "__main__"` correctly
- avoid circular and wildcard imports

## The problem

A log utility should be importable by tests without printing a banner, reading a file, or starting a server. The command-line entry point should run only when the module is executed directly.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples do not authorize access to public systems, university systems, employer systems, or accounts that you do not own.

## Lesson

### Vocabulary

A **module** is usually one `.py` file. A **package** is a directory of modules with an importable structure. An **import side effect** is work performed merely because another file imported a name.

## Worked examples

### Example 1: A focused module

Keep one concept in one file and import the function elsewhere.

```python
# parsers.py
def parse_pair(text):
    left, right = text.split(":", 1)
    return left, right


# main.py
from parsers import parse_pair

print(parse_pair("auth:failed"))
```

**What to observe:**

`('auth', 'failed')`

### Example 2: The main guard

The guard prevents CLI-only behavior during tests and imports.

```python
def main():
    print("running as a program")


if __name__ == "__main__":
    main()
```

**What to observe:**

Importing the module defines `main` without printing; executing the file prints the message.

### Example 3: A package path

A package gives related modules a stable namespace.

```python
from course_days.day012 import parse_pair

print(parse_pair("source:message"))
```

**What to observe:**

The import name documents where the behavior lives.

### Example 4: Explicit exports

An explicit `__all__` or documented public function helps reviewers distinguish supported API from helpers.

```python
__all__ = ["parse_pair"]


def parse_pair(text):
    return tuple(text.split(":", 1))
```

**What to observe:**

The public surface is intentionally small.

### Example 5: Avoid import-time file access

Opening a file while importing makes tests depend on the current directory and hidden state.

```python
def load_fixture(path):
    return path.read_text(encoding="utf-8")


# no call occurs during import
```

**What to observe:**

The caller chooses when and which authorized fixture to read.

## Execution trace

When `main.py` imports `parse_pair`, Python loads the module, creates the function, and skips the guarded `main()` call. When the same file is executed directly, `__name__` is `"__main__"` and the entry point runs.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| import-time work | tests print or read unexpected files | move work into functions |
| wildcard imports | origin of a name is unclear | use explicit imports |
| circular imports | partially initialized module error | invert the dependency or extract a third module |
| running from the wrong directory | package cannot be found | use the project command and environment |
| huge public surface | every helper becomes an accidental API | expose a small documented interface |

## Security application

Split the checkpoint into parser, policy, report, and CLI modules. The only target is the local repository fixture; importing any module must not contact the network or read outside the fixture.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples above as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run `python -m course_days.day012`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A module is a boundary for responsibility; importing it should define reusable behavior without surprising side effects.

## Limitations

Module organization does not make unsafe behavior safe. A well-organized tool can still have a flawed parser or an unauthorized target.

[← Day 11](../011_day_function_contracts/011_day_function_contracts.md) · [Day index](../DAY_INDEX.md) · [Day 13 →](../013_day_exceptions_and_error_taxonomy/013_day_exceptions_and_error_taxonomy.md)
