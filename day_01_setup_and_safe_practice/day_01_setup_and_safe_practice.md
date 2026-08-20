# Day 1: How Programs Run and How to Practise Cybersecurity Safely

[← Home](../README.md) · [Day index](../DAY_INDEX.md) · [Day 2 →](../day_02_values_names_and_input/day_02_values_names_and_input.md)

## Table of Contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Lesson](#lesson)
- [Worked examples](#worked-examples)
- [Execution trace](#execution-trace)
- [Common mistakes](#common-mistakes)
- [Security application](#security-application)
- [Exercises](#exercises)
- [Finish line](#finish-line)

## Why this lesson exists

A complete beginner needs a reliable first mental model before syntax becomes useful. You will see how a file becomes instructions, how the interpreter reports mistakes, and why safe security work begins with authorization and scope.

## Prerequisites

Install Python and VS Code by following [SETUP.md](../SETUP.md). Run `python --version` and open the repository in VS Code.

## Outcomes

By the end of this lesson, you can:

- run a Python file from the terminal
- distinguish source code, interpreter, output, and error
- read a traceback as a location and explanation
- keep a security exercise local, synthetic, bounded, and resettable

## The problem

Suppose a teammate gives you a script and says it “checks suspicious activity.” Before changing it, you need to know how to run it, what it actually observes, and what it does when an input is wrong.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples may describe security signals, but they do not identify attackers, authorize testing, or justify touching public systems. Keep real credentials, private logs, and university or employer data out of the lesson.

## Lesson

### Source code is a set of instructions

A Python file is ordinary text. The interpreter reads that text and performs the instructions in order. The file is not magic, and the computer does not understand your intention; it follows the syntax and values that you provide.

Create `hello.py`:

```python
print("first line")
print("second line")
```

Run it from the repository root:

```text
$ python hello.py
first line
second line
```

The two calls run top to bottom. If you swap them, the output order swaps. This simple observation becomes important when a security tool records evidence: the order in which the tool reads, transforms, and reports data is part of its behavior.

### A program can calculate before it prints

```python
left = 2
right = 3
answer = left + right
print(answer)
```

Expected output:

```text
5
```

The names `left`, `right`, and `answer` make intermediate values visible. A beginner often writes one large expression, but named steps are easier to inspect and review.

### The interpreter reports syntax mistakes

```python
print("this line is valid")
print("this line is missing a quote)
```

Python stops before it can run the second line and reports a `SyntaxError`. The line number tells you where Python noticed the problem. It may not be the first character you should fix, because an unclosed quote or bracket can make the following line look wrong too.

Fix the quote, rerun the file, and observe that the first line now prints because the program can be parsed completely.

### Runtime errors are different

```python
number = int("not a number")
print(number)
```

This file is syntactically valid. Python begins executing it, then raises `ValueError` when `int` cannot interpret the text. The distinction matters:

| Error kind | When it happens | First question |
| --- | --- | --- |
| `SyntaxError` | before execution | Which punctuation or structure is incomplete? |
| `NameError` | during execution | Which name has not been defined? |
| `ValueError` | during a conversion or operation | Does the value fit the requested format? |

### Your first security distinction

A line that prints `"login_failed"` is an observation. It is not proof that a person attacked the system. A local fixture that contains a suspicious-looking line is safe to analyze; a real system requires authorization, scope, data-handling rules, and a plan to stop.

The course therefore uses four words repeatedly:

- **Authorized:** you have permission from the owner.
- **Local:** the program runs on your computer or a supplied fixture.
- **Synthetic:** the data is invented for practice.
- **Bounded:** the work has explicit limits on files, rows, time, and output.
## Worked examples

### Example 1: print a safe report header

```python
case_id = "training-001"
print(f"case={case_id} status=training-only")
```

Expected output:

```text
case=training-001 status=training-only
```

The `f` before the string lets Python replace `{case_id}` with the value. There is no real case data here.

### Example 2: trace a name change

```python
status = "new"
status = "review"
print(status)
```

The output is `review` because the second assignment replaces the value stored under `status`. The old value is not printed and is not automatically preserved as history. If you need history, store multiple records explicitly.

### Example 3: inspect the type

```python
value = "7"
print(type(value).__name__)
print(value)
```

Expected output is `str` followed by `7`. Text that looks like a number is still text until you convert and validate it.

### Example 4: make a deliberate failure

```python
print(10 / 0)
```

The interpreter raises `ZeroDivisionError`. Read the last traceback line first, then move upward to the file and line location. Do not delete the error without understanding what input made it possible.

### Example 5: a safe local boundary

```python
fixture_name = "sample_events.txt"
allowed_directory = "training-fixtures"
print(f"reading={fixture_name} from={allowed_directory}")
```

This reports an intended fixture without opening a path supplied by an unknown user. Later lessons will implement actual path validation.

## Execution trace

For this program:

```python
label = "warning"
level = 2
message = f"{label}:{level}"
print(message)
```

| Step | Statement | State or result |
| ---: | --- | --- |
| 1 | `label = "warning"` | `label` refers to a string |
| 2 | `level = 2` | `level` refers to an integer |
| 3 | `message = ...` | `message` becomes `"warning:2"` |
| 4 | `print(message)` | the string is displayed |

A trace is a small, human-readable record of the program’s state. It is more useful than saying “Python runs it somehow.”

## Common mistakes

| Mistake | What you see | Smallest correction |
| --- | --- | --- |
| Running the wrong directory | `can't open file` | print the current directory and use the lesson command |
| Using smart quotes | `SyntaxError` | replace them with ordinary Python quotes |
| Saving as `hello.py.txt` | the terminal cannot find the file | show file extensions and rename it |
| Ignoring the last traceback line | repeated failure | read the exception type and then the reported line |
| Calling an observation an attack | an unjustified conclusion | record the observation and confidence separately |

## Security application

Create a local note named `scope.md` containing the target, owner, allowed files, time window, stop condition, and cleanup command for a fictional fixture. This is not paperwork for its own sake. A written scope prevents a beginner from turning a learning command into an unauthorized action.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples from this lesson as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run the starter, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A program is a sequence of instructions whose observable behavior depends on its source, inputs, and runtime state; safe security learning adds authorization and bounds before execution.

## Limitations

This lesson does not teach debugging every Python error or establish a complete security methodology. It teaches the first runtime and authorization habits that later tools depend on.

## Optional video support

Watch [CS50P Lecture 0](https://www.youtube.com/watch?v=JP7ITIXGpHk&t=24s) from `00:24` for `hello.py`, then `09:54` for VS Code. Watch only after running the local examples.

Use the [timestamped video catalog](../VIDEO_RESOURCES.md) only after running the local examples. The written lesson and Python documentation remain authoritative.


[← Home](../README.md) · [Day index](../DAY_INDEX.md) · [Day 2 →](../day_02_values_names_and_input/day_02_values_names_and_input.md)
