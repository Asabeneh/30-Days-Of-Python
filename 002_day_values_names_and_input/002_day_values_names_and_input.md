# Day 2: Values, Names, Input, and Output

[← Day 1](../001_day_setup_and_safe_practice/001_day_setup_and_safe_practice.md) · [Day index](../DAY_INDEX.md) · [Day 3 →](../003_day_types_and_parsing/003_day_types_and_parsing.md)

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

Security tools constantly move data across boundaries: text from a file, numbers from a command line, and structured values inside a report. You need to know what a value is before deciding what it means.

## Prerequisites

Complete Day 1. You should be able to create a file, run it, and read a traceback.

## Outcomes

By the end of this lesson, you can:

- store values under meaningful names
- distinguish strings, integers, floats, and booleans
- explain why `input()` returns text
- convert and format values deliberately
- avoid printing sensitive values by accident

## The problem

A triage utility receives `"7"` from a terminal. Is that the number seven, the text seven, or an invalid value that only looks numeric? The program must decide explicitly.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples may describe security signals, but they do not identify attackers, authorize testing, or justify touching public systems. Keep real credentials, private logs, and university or employer data out of the lesson.

## Lesson

### Values and names

A value is data such as the string `"login_failed"`, the integer `7`, or the boolean `True`. A variable is a name that refers to a value. Assignment binds the name; it does not permanently label the value.

```python
severity = 7
message = "login_failed"
review_required = True

print(severity)
print(message)
print(review_required)
```

Expected output is one value per line. The names make the program readable. `severity = 7` does not mean that every future severity is seven; it means that this name currently refers to that integer.

### Types answer “what kind of value is this?”

```python
samples = ["7", 7, 7.0, True]
for sample in samples:
    print(repr(sample), type(sample).__name__)
```

Expected output:

```text
'7' str
7 int
7.0 float
True bool
```

The string and integer may look similar when printed, but they support different operations. `"7" + "1"` produces `"71"`, while `7 + 1` produces `8`.

### `input()` always begins as text

```python
raw = input("Severity: ")
print(repr(raw), type(raw).__name__)
```

If you type `7`, the output still identifies a string. The keyboard produces characters. The program must convert them and validate the result before using them as a number.

```python
raw = input("Severity: ")
severity = int(raw)
print(severity + 1)
```

This works for `7` but raises `ValueError` for `high`. A conversion is not the same as validation; it only checks whether Python can interpret the text as an integer.

### Formatting output

```python
case_id = "training-002"
severity = 7
print(f"case={case_id} severity={severity}")
```

An f-string makes the relationship between the labels and values obvious. Avoid printing raw tokens, passwords, or full private records while experimenting.

### Conversions are decisions

```python
text = " 42 "
number = int(text.strip())
ratio = float("0.5")
flag = bool("false")
print(number, ratio, flag)
```

The last line prints `42 0.5 True`. This surprises beginners: `bool("false")` is `True` because every non-empty string is truthy. It does not parse the word false. Later, you will write an explicit parser.
## Worked examples

### Example 1: a typed event record

```python
event = {
    "source": "training-auth",
    "severity": 7,
    "authenticated": False,
}
print(event["source"])
print(type(event["severity"]).__name__)
```

The dictionary groups related values. The source is text, severity is an integer, and authenticated is a boolean. A dictionary does not magically guarantee that future values have the same types.

### Example 2: input conversion with a visible boundary

```python
raw = " 7 "
clean = raw.strip()
severity = int(clean)
print(f"raw={raw!r} clean={clean!r} severity={severity}")
```

The `!r` representation makes surrounding spaces visible. Keep raw and cleaned values during debugging; discard or redact them according to the data policy in a real tool.

### Example 3: why strings concatenate

```python
left = "failed"
right = "login"
print(left + ":" + right)
```

The result is `failed:login`. For a larger report, f-strings are usually easier to read than many `+` operators.

### Example 4: a safe conversion function

```python
def parse_severity(text):
    value = int(text.strip())
    if not 0 <= value <= 10:
        raise ValueError("severity must be between 0 and 10")
    return value
```

This is an early example of a boundary: convert, check the allowed range, then return. The full function-contract lesson comes later.

### Example 5: output without secrets

```python
case_id = "training-002"
api_key_present = True
print(f"case={case_id} api_key_present={api_key_present}")
```

The program records whether a key exists without printing the key. “Present” is often enough for a diagnostic report.

## Execution trace

For `raw = " 7 "`, `severity = int(raw.strip())`:

| Step | Value | Type |
| ---: | --- | --- |
| 1 | `" 7 "` | `str` |
| 2 | `raw.strip()` → `"7"` | `str` |
| 3 | `int("7")` → `7` | `int` |
| 4 | `severity + 1` → `8` | `int` |

If `raw = "high"`, step 3 raises `ValueError`; no severity integer is produced.

## Common mistakes

| Mistake | Why it happens | Correction |
| --- | --- | --- |
| Adding `"7" + 1` | visual similarity hides type difference | convert after validation |
| Using `bool("false")` | truthiness is confused with parsing | compare normalized text explicitly |
| Printing `raw` in a report | debugging output becomes data leakage | redact or print only safe metadata |
| Reusing `value` for different types | the name hides the change | use clear names such as `raw`, `clean`, and `severity` |
| Assuming a dictionary validates data | containers store values without policy | validate at the boundary |

## Security application

Build a synthetic event summary that prints `source`, `severity`, and `authenticated`, but never prints a field named `token`, `password`, or `secret`. Add one test that proves the forbidden field value does not appear in the output.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples from this lesson as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run the starter, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Values have types, names refer to current values, and input is untrusted text until a program converts and validates it.

## Limitations

The examples do not define a universal severity scale or prove that a record is authentic. A real system needs a documented schema and trustworthy collection path.

## Optional video support

Watch [CS50P Lecture 0](https://www.youtube.com/watch?v=JP7ITIXGpHk&t=736s) from `12:16` for return values and variables, then compare with the local examples.

Use the [timestamped video catalog](../VIDEO_RESOURCES.md) only after running the local examples. The written lesson and Python documentation remain authoritative.


[← Day 1](../001_day_setup_and_safe_practice/001_day_setup_and_safe_practice.md) · [Day index](../DAY_INDEX.md) · [Day 3 →](../003_day_types_and_parsing/003_day_types_and_parsing.md)
