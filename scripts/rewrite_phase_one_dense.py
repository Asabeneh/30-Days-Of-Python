"""Author dense beginner-first teaching chapters for Days 1–10."""

# ruff: noqa: E501
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DAY_DIRS = {
    1: "day_1_setup_and_safe_practice",
    2: "day_2_values_names_and_input",
    3: "day_3_types_and_parsing",
    4: "day_4_operators_and_decisions",
    5: "day_5_branching_and_triage",
    6: "day_6_loops_and_bounded_work",
    7: "day_7_collections_and_iocs",
    8: "day_8_strings_and_canonicalization",
    9: "day_9_functions_and_validation",
    10: "day_10_checkpoint_log_triage",
}

NAV = {
    1: (
        "Home",
        "../README.md",
        "Day 2",
        "../day_2_values_names_and_input/day_2_values_names_and_input.md",
    ),
    2: (
        "Day 1",
        "../day_1_setup_and_safe_practice/day_1_setup_and_safe_practice.md",
        "Day 3",
        "../day_3_types_and_parsing/day_3_types_and_parsing.md",
    ),
    3: (
        "Day 2",
        "../day_2_values_names_and_input/day_2_values_names_and_input.md",
        "Day 4",
        "../day_4_operators_and_decisions/day_4_operators_and_decisions.md",
    ),
    4: (
        "Day 3",
        "../day_3_types_and_parsing/day_3_types_and_parsing.md",
        "Day 5",
        "../day_5_branching_and_triage/day_5_branching_and_triage.md",
    ),
    5: (
        "Day 4",
        "../day_4_operators_and_decisions/day_4_operators_and_decisions.md",
        "Day 6",
        "../day_6_loops_and_bounded_work/day_6_loops_and_bounded_work.md",
    ),
    6: (
        "Day 5",
        "../day_5_branching_and_triage/day_5_branching_and_triage.md",
        "Day 7",
        "../day_7_collections_and_iocs/day_7_collections_and_iocs.md",
    ),
    7: (
        "Day 6",
        "../day_6_loops_and_bounded_work/day_6_loops_and_bounded_work.md",
        "Day 8",
        "../day_8_strings_and_canonicalization/day_8_strings_and_canonicalization.md",
    ),
    8: (
        "Day 7",
        "../day_7_collections_and_iocs/day_7_collections_and_iocs.md",
        "Day 9",
        "../day_9_functions_and_validation/day_9_functions_and_validation.md",
    ),
    9: (
        "Day 8",
        "../day_8_strings_and_canonicalization/day_8_strings_and_canonicalization.md",
        "Day 10",
        "../day_10_checkpoint_log_triage/day_10_checkpoint_log_triage.md",
    ),
    10: (
        "Day 9",
        "../day_9_functions_and_validation/day_9_functions_and_validation.md",
        "Day 11",
        "../day_11_function_contracts/day_11_function_contracts.md",
    ),
}


def top(
    day: int, title: str, why: str, prerequisites: str, outcomes: str, problem: str
) -> str:
    previous_name, previous_link, next_name, next_link = NAV[day]
    return f"""# Day {day}: {title}

[← {previous_name}]({previous_link}) · [Day index](../DAY_INDEX.md) · [{next_name} →]({next_link})

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

{why}

## Prerequisites

{prerequisites}

## Outcomes

By the end of this lesson, you can:

{outcomes}

## The problem

{problem}

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples may describe security signals, but they do not identify attackers, authorize testing, or justify touching public systems. Keep real credentials, private logs, and university or employer data out of the lesson.

## Lesson

"""


def tail(day: int, mental_model: str, limitations: str, video: str = "") -> str:
    video_block = (
        f"\n## Optional video support\n\n{video}\n\nUse the [timestamped video catalog](../VIDEO_RESOURCES.md) only after running the local examples. The written lesson and Python documentation remain authoritative.\n"
        if video
        else ""
    )
    return f"""## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples from this lesson as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run the starter, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> {mental_model}

## Limitations

{limitations}
{video_block}

[← {NAV[day][0]}]({NAV[day][1]}) · [Day index](../DAY_INDEX.md) · [{NAV[day][2]} →]({NAV[day][3]})
"""


LESSONS: dict[int, str] = {}

LESSONS[1] = (
    top(
        1,
        "How Programs Run and How to Practise Cybersecurity Safely",
        "A complete beginner needs a reliable first mental model before syntax becomes useful. You will see how a file becomes instructions, how the interpreter reports mistakes, and why safe security work begins with authorization and scope.",
        "Install Python and VS Code by following [SETUP.md](../SETUP.md). Run `python --version` and open the repository in VS Code.",
        "- run a Python file from the terminal\n- distinguish source code, interpreter, output, and error\n- read a traceback as a location and explanation\n- keep a security exercise local, synthetic, bounded, and resettable",
        "Suppose a teammate gives you a script and says it “checks suspicious activity.” Before changing it, you need to know how to run it, what it actually observes, and what it does when an input is wrong.",
    )
    + """### Source code is a set of instructions

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
"""
    + """## Worked examples

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
"""
    + tail(
        1,
        "A program is a sequence of instructions whose observable behavior depends on its source, inputs, and runtime state; safe security learning adds authorization and bounds before execution.",
        "This lesson does not teach debugging every Python error or establish a complete security methodology. It teaches the first runtime and authorization habits that later tools depend on.",
        "Watch [CS50P Lecture 0](https://www.youtube.com/watch?v=JP7ITIXGpHk&t=24s) from `00:24` for `hello.py`, then `09:54` for VS Code. Watch only after running the local examples.",
    )
)

LESSONS[2] = (
    top(
        2,
        "Values, Names, Input, and Output",
        "Security tools constantly move data across boundaries: text from a file, numbers from a command line, and structured values inside a report. You need to know what a value is before deciding what it means.",
        "Complete Day 1. You should be able to create a file, run it, and read a traceback.",
        "- store values under meaningful names\n- distinguish strings, integers, floats, and booleans\n- explain why `input()` returns text\n- convert and format values deliberately\n- avoid printing sensitive values by accident",
        'A triage utility receives `"7"` from a terminal. Is that the number seven, the text seven, or an invalid value that only looks numeric? The program must decide explicitly.',
    )
    + """### Values and names

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
"""
    + """## Worked examples

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
"""
    + tail(
        2,
        "Values have types, names refer to current values, and input is untrusted text until a program converts and validates it.",
        "The examples do not define a universal severity scale or prove that a record is authentic. A real system needs a documented schema and trustworthy collection path.",
        "Watch [CS50P Lecture 0](https://www.youtube.com/watch?v=JP7ITIXGpHk&t=736s) from `12:16` for return values and variables, then compare with the local examples.",
    )
)

LESSONS[3] = (
    top(
        3,
        "Types, Conversion, and Boundary Validation",
        "Most security automation failures begin at a boundary: a command-line argument, JSON field, filename, or log line is not the shape the program expected. Python gives you conversion tools, but you must add policy.",
        "Complete Days 1–2. Be comfortable with `str`, `int`, `float`, `bool`, dictionaries, and f-strings.",
        "- inspect a value’s type\n- convert text deliberately\n- distinguish conversion errors from policy violations\n- write a bounded parser\n- test valid, boundary, and invalid inputs",
        'A port number arrives as text. `int("70000")` succeeds, but port 70000 is outside the valid range. A parser must separate “Python can read this” from “the application accepts this.”',
    )
    + """### Inspect before you interpret

```python
values = ["443", 443, 443.0, None]
for value in values:
    print(repr(value), type(value).__name__)
```

Inspection is not validation. It tells you what arrived, not whether the value is safe or meaningful.

### Conversion can fail

```python
for raw in ["443", " 443 ", "four-four-three"]:
    try:
        print(raw, "->", int(raw.strip()))
    except ValueError as error:
        print(raw, "rejected:", error)
```

The `try` block contains the operation that may fail. The `except ValueError` handles the expected conversion problem. A broad `except Exception` would also catch programming mistakes and make them look like ordinary bad input.

### Policy comes after conversion

```python
def parse_port(text):
    port = int(text.strip())
    if not 1 <= port <= 65535:
        raise ValueError("port must be between 1 and 65535")
    return port
```

`parse_port("70000")` converts successfully and then fails the application rule. `parse_port("abc")` fails during conversion. Both are rejected, but for different reasons.

### Optional values are not automatically safe

```python
def parse_limit(text, default=100):
    if text is None or text.strip() == "":
        return default
    limit = int(text)
    if not 1 <= limit <= 10_000:
        raise ValueError("limit is outside the allowed bound")
    return limit
```

Defaults should be explicit and bounded. A missing limit should not silently become “unlimited.”
"""
    + """## Worked examples

### Example 1: a boolean parser

```python
def parse_bool(text):
    normalized = text.strip().casefold()
    if normalized in {"true", "yes", "1"}:
        return True
    if normalized in {"false", "no", "0"}:
        return False
    raise ValueError("expected true or false")
```

This parser does not treat every non-empty string as true. It names the accepted vocabulary.

### Example 2: a severity parser

```python
def parse_severity(text):
    severity = int(text.strip())
    if severity < 0 or severity > 10:
        raise ValueError("severity must be from 0 to 10")
    return severity
```

Try `"0"`, `"10"`, `"11"`, `"-1"`, and `"high"`. The first two are accepted; the rest are rejected by either policy or conversion.

### Example 3: parse a record at the boundary

```python
def parse_event(record):
    source = record.get("source", "").strip()
    if not source:
        raise ValueError("source is required")
    return {"source": source, "severity": parse_severity(record["severity"])}
```

A missing or blank source is rejected before a downstream classifier can pretend the record is complete.

### Example 4: preserve the reason for rejection

```python
def describe_parse(record):
    try:
        return {"ok": True, "event": parse_event(record)}
    except (KeyError, TypeError, ValueError) as error:
        return {"ok": False, "reason": str(error)}
```

The caller receives an explicit failure result. It should not silently return an empty event.

### Example 5: negative tests

```python
assert parse_port("443") == 443
for bad in ["0", "65536", "abc"]:
    try:
        parse_port(bad)
    except ValueError:
        pass
    else:
        raise AssertionError(f"accepted invalid port: {bad}")
```

A negative test proves that the rejection path exists. It is not optional decoration in a security utility.

## Execution trace

For `parse_port(" 443 ")`:

| Step | Operation | Result |
| ---: | --- | --- |
| 1 | `text.strip()` | `"443"` |
| 2 | `int(...)` | `443` |
| 3 | range check | `True` |
| 4 | `return port` | caller receives integer `443` |

For `parse_port("70000")`, conversion succeeds but the range check is false. For `parse_port("https")`, conversion raises before the range check.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| Checking only `isdigit()` | negative or whitespace cases behave unexpectedly | convert and catch `ValueError`, then enforce policy |
| Using `int(text)` without a bound | huge values consume later resources | enforce a maximum immediately |
| Returning `None` for every error | callers cannot distinguish missing from malformed | raise or return a structured failure |
| Catching `Exception` | coding errors look like bad input | catch expected boundary exceptions |
| Trusting a type hint | runtime dictionaries still contain wrong types | validate actual values |

## Security application

Use a JSON-like fixture containing `source`, `severity`, `port`, and `limit`. Parse every field at the boundary, reject invalid records with a reason, and prove that no rejected record reaches the triage decision.
"""
    + tail(
        3,
        "Conversion answers whether Python can interpret a value; validation answers whether the application accepts it.",
        "A parser can enforce shape and policy, but it cannot prove who supplied the data or whether the surrounding record is authentic.",
        "Watch [CS50P Lecture 0](https://www.youtube.com/watch?v=JP7ITIXGpHk&t=240s) from `04:00` for the interpreter and `05:06` for functions and arguments.",
    )
)

LESSONS[4] = (
    top(
        4,
        "Operators, Comparisons, Truthiness, and Precedence",
        "Security decisions are combinations of facts. Operators let a program calculate, compare, combine, and reject conditions, but a misplaced parenthesis or truthiness assumption can reverse a decision.",
        "Complete Days 1–3. Be able to parse integers and explain a boolean value.",
        "- calculate with arithmetic operators\n- compare values and combine conditions\n- predict precedence and use parentheses\n- distinguish false, missing, empty, and invalid data\n- review a security rule as a truth table",
        "You need a rule that reviews a high-severity event only when it has a source and is not explicitly marked trusted. The rule must be readable and testable at its boundaries.",
    )
    + """### Arithmetic is evaluation

```python
print(2 + 3 * 4)
print((2 + 3) * 4)
print(7 // 3)
print(7 % 3)
```

The output is `14`, `20`, `2`, and `1`. Multiplication happens before addition. Parentheses make the intended order visible. Floor division and remainder are useful when grouping records into batches, but do not confuse `//` with ordinary division.

### Comparisons produce booleans

```python
severity = 7
print(severity >= 7)
print(severity == "7")
print(severity != 3)
```

The output is `True`, `False`, and `True`. The integer `7` is not equal to the string `"7"`.

### Combine conditions deliberately

```python
severity = 8
source = "auth"
trusted = False
review = severity >= 7 and source != "" and not trusted
print(review)
```

The result is `True`. Read the expression as a sentence. If it becomes difficult to read, assign named boolean values and test them separately.

### Membership and identity are different

```python
status = "login_failed"
print("login" in status)
print(status is "login_failed")
```

The first expression asks whether text occurs inside another value. The second uses identity and should not be used for ordinary string equality. Use `==` for values. Python may warn about the `is` comparison.

### Truthiness is a conversion rule, not a security decision

```python
for value in ["", "false", [], [1], 0, 1, None]:
    print(repr(value), bool(value))
```

Empty strings, empty collections, zero, and `None` are falsey. The non-empty string `"false"` is truthy. A user-controlled word must be parsed explicitly.
"""
    + """## Worked examples

### Example 1: parentheses make policy visible

```python
review = (severity >= 7 and source != "") or force_review
```

This means either the event is high severity with a source, or a separate trusted workflow forces review. Without parentheses, a reviewer must remember precedence rules.

### Example 2: truth table for a triage rule

| Severity high? | Source present? | Trusted? | Review? |
| --- | --- | --- | --- |
| no | yes | no | no |
| yes | yes | no | yes |
| yes | no | no | no |
| yes | yes | yes | no |

Writing the table before coding exposes ambiguity. Should a trusted high-severity event be excluded or still reviewed? The owner must decide.

### Example 3: explicit text parsing

```python
def parse_trusted(text):
    value = text.strip().casefold()
    if value == "true":
        return True
    if value == "false":
        return False
    raise ValueError("trusted must be true or false")
```

Now `parse_trusted("false")` returns `False`, unlike `bool("false")`.

### Example 4: short-circuiting

```python
def has_source(event):
    return bool(event.get("source"))

review = event.get("severity", 0) >= 7 and has_source(event)
```

If the severity comparison is false, Python does not need to call `has_source`. Short-circuiting can avoid unsafe work, but do not hide required validation inside a condition that may never run.

### Example 5: range checks

```python
def valid_severity(value):
    return 0 <= value <= 10
```

Chained comparisons read like mathematics. Test `0`, `10`, `-1`, and `11`; the boundaries are where off-by-one mistakes appear.

## Execution trace

For `severity=8`, `source="auth"`, `trusted=False`:

| Step | Expression | Result |
| ---: | --- | --- |
| 1 | `severity >= 7` | `True` |
| 2 | `source != ""` | `True` |
| 3 | `not trusted` | `True` |
| 4 | combine with `and` | `True` |

Change `trusted` to `True`; step 3 becomes `False` and the final result becomes `False`.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| Missing parentheses | a rule passes the wrong combination | write a truth table and parenthesize |
| `is` for string equality | warnings or inconsistent behavior | use `==` |
| `bool("false")` | false text becomes true | parse allowed words |
| `x == 1 or 2` | condition is always truthy | write `x == 1 or x == 2` |
| treating empty as malicious | missing data becomes a conclusion | label missing data explicitly |

## Security application

Implement a pure `needs_review(event)` function for synthetic events. Return a boolean and write a separate explanation function. The decision must not print, open files, or contact services, so it can be tested exhaustively.
"""
    + tail(
        4,
        "A security decision is a boolean expression with assumptions; make the assumptions visible, test the truth table, and never confuse falsey data with a security conclusion.",
        "The rule is only a training policy. Real organizations need documented risk ownership, trusted data sources, escalation procedures, and review of false positives and negatives.",
        "Watch [CS50P Lecture 0](https://www.youtube.com/watch?v=JP7ITIXGpHk&t=306s) from `05:06` for function arguments and side effects.",
    )
)

LESSONS[5] = (
    top(
        5,
        "Branching and a First Triage Classifier",
        "A classifier chooses among paths. In security work, a branch should make a limited, explainable recommendation—not claim that an incident is proven.",
        "Complete Day 4 and be able to write and test a boolean expression.",
        "- use `if`, `elif`, and `else`\n- order conditions from specific to general\n- return a label and reason\n- test branch boundaries\n- separate observations from conclusions",
        "A synthetic event can be normal, needs review, or invalid. The program needs a stable policy for each case and a reason that a human can inspect.",
    )
    + """### The shape of a branch

```python
severity = 8
if severity >= 7:
    label = "review"
elif severity >= 4:
    label = "watch"
else:
    label = "normal"
print(label)
```

Python checks conditions from top to bottom and executes the first true block. The order matters. If `severity >= 4` appeared first, a severity of `8` would be labeled `watch` and the later branch would never run.

### Add an invalid state

```python
if not 0 <= severity <= 10:
    label = "invalid"
elif severity >= 7:
    label = "review"
elif severity >= 4:
    label = "watch"
else:
    label = "normal"
```

Validate the domain before applying the policy. A severity of `99` should not become an urgent event merely because it is large.

### Return a decision and a reason

```python
def classify(severity, authenticated):
    if not 0 <= severity <= 10:
        return "invalid", "severity is outside 0..10"
    if severity >= 7 and not authenticated:
        return "review", "high severity and unauthenticated"
    if severity >= 7:
        return "watch", "high severity but authenticated"
    return "normal", "severity is below review threshold"
```

A tuple lets the caller keep the label and explanation together. The function does not print or assert that an attack happened.

### Branches are policies

A branch encodes a policy decision. Ask who chose the threshold, which data is trusted, how false positives are handled, and what happens when a field is missing. Code can execute correctly while the policy is still wrong for its context.
"""
    + """## Worked examples

### Example 1: exact boundaries

```python
for severity in [3, 4, 6, 7, 10]:
    print(severity, classify(severity, authenticated=True))
```

Predict the labels before running it. Boundaries `4` and `7` deserve explicit tests.

### Example 2: missing input

```python
def classify_record(record):
    if "severity" not in record:
        return "invalid", "severity is missing"
    if "authenticated" not in record:
        return "invalid", "authenticated is missing"
    return classify(record["severity"], record["authenticated"])
```

Missing is different from false. Do not silently replace a missing authentication field with `False` unless the policy explicitly says so.

### Example 3: a decision table

| Input | Expected label | Reason |
| --- | --- | --- |
| `severity=2, authenticated=True` | normal | below threshold |
| `severity=7, authenticated=True` | watch | high but authenticated |
| `severity=7, authenticated=False` | review | high and unauthenticated |
| `severity=11, authenticated=False` | invalid | outside domain |

### Example 4: do not bury output in policy

```python
def classify_for_cli(severity, authenticated):
    label, reason = classify(severity, authenticated)
    return {"label": label, "reason": reason}
```

A caller can print this dictionary, save it, or test it. Pure policy is easier to reuse.

### Example 5: an intentionally unresolved signal

```python
def classify_with_source(event):
    label, reason = classify_record(event)
    return {"label": label, "reason": reason, "source": event.get("source", "unknown")}
```

The source helps a reviewer understand provenance; it does not prove accuracy.

## Execution trace

For `classify(8, False)`:

| Step | Check | Result |
| ---: | --- | --- |
| 1 | `0 <= 8 <= 10` | true |
| 2 | `8 >= 7 and not False` | true |
| 3 | return | `("review", "high severity and unauthenticated")` |

For `classify(8, True)`, step 2 is false and the function returns `watch`.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| broad condition first | urgent events get a low label | order specific cases first |
| no invalid branch | malformed data enters policy | validate before classification |
| printing inside the classifier | tests must capture output | return structured data |
| using “attack” as a label | observation becomes conclusion | use neutral labels such as `review` |
| no reason field | reviewer cannot reproduce the decision | return label and reason |

## Security application

Run the classifier only against the supplied synthetic event fixture. Save the output as a review queue, not as an incident declaration. Add a note that a human must confirm context before escalation.
"""
    + tail(
        5,
        "Branching turns explicit policy into paths; a good classifier validates its input, returns an explainable label, and stops short of claiming more than its evidence supports.",
        "Thresholds are not universal truth. They can create false positives, false negatives, and unfair outcomes if the data or policy is poor.",
    )
)

LESSONS[6] = (
    top(
        6,
        "Loops, Bounds, and Resource Safety",
        "Automation often processes many records. A loop gives you repetition, but an unbounded loop or unbounded input can exhaust time and memory. Security engineering requires limits.",
        "Complete Day 5 and understand lists, conditions, and a returned classification.",
        "- iterate through a collection\n- use `range`, `break`, and `continue` deliberately\n- count and collect results\n- enforce record, line, and output limits\n- explain the trade-off between completeness and resource safety",
        "A log file may contain millions of lines. A beginner’s first loop reads everything and prints everything. A safer utility processes a documented maximum and reports what it skipped.",
    )
    + """### A `for` loop repeats a known sequence

```python
statuses = ["ok", "failed", "ok"]
for status in statuses:
    print(status)
```

Python assigns each item to `status` in order. The loop ends after the list is exhausted. The variable name is not special; choose one that describes each item.

### `range` produces a sequence of integers

```python
for number in range(3):
    print(number)
```

The output is `0`, `1`, `2`. The stop value is excluded. `range(1, 4)` produces `1`, `2`, `3`.

### Accumulate without losing the count

```python
failed = 0
for status in statuses:
    if status == "failed":
        failed += 1
print(failed)
```

The variable `failed` is state carried from one iteration to the next. Initialize it before the loop, and update it only when the condition is true.

### `continue` and `break`

```python
for line in ["", "login_failed", "malformed", "login_ok"]:
    if not line:
        continue
    if line == "malformed":
        break
    print(line)
```

The blank line is skipped. The malformed line stops the loop, so `login_ok` is never printed. Use these statements only when their effect is obvious; hidden early exits make evidence incomplete.

### Bounds are part of the function contract

```python
def first_matches(lines, needle, limit=100):
    if limit < 0:
        raise ValueError("limit must not be negative")
    matches = []
    for line in lines:
        if needle in line:
            matches.append(line)
            if len(matches) == limit:
                break
    return matches
```

This function has a maximum result count. If `limit` is `0`, the current implementation returns an empty list only after the first match; refine it as an exercise and test your chosen behavior.
"""
    + """## Worked examples

### Example 1: count by category

```python
counts = {"ok": 0, "failed": 0}
for status in ["ok", "failed", "failed"]:
    if status in counts:
        counts[status] += 1
print(counts)
```

The output is `{'ok': 1, 'failed': 2}`. The membership check prevents an unexpected status from creating a new category silently.

### Example 2: line limit

```python
lines = [f"event-{number}" for number in range(5)]
for index, line in enumerate(lines):
    if index >= 3:
        break
    print(line)
```

Only three lines print. `enumerate` provides both the position and the value.

### Example 3: maximum line length

```python
def accept_line(line, max_length=2000):
    if len(line) > max_length:
        return False
    return True
```

A line-length limit prevents one malformed record from consuming excessive processing time. A real parser should record that the line was rejected without storing the entire oversized content.

### Example 4: bounded generator input

```python
def take_first(items, limit):
    for index, item in enumerate(items):
        if index == limit:
            return
        yield item
```

A generator yields one item at a time. It can reduce memory use, but it still needs a limit.

### Example 5: progress evidence

```python
processed = 0
matched = 0
for line in lines:
    processed += 1
    if "failed" in line:
        matched += 1
print(f"processed={processed} matched={matched}")
```

A report should say how many records were considered and how many matched. That makes a bounded result interpretable.

## Execution trace

For `first_matches(["a", "login_failed", "b", "login_failed"], "login", 1)`:

| Iteration | Line | Match? | State |
| ---: | --- | --- | --- |
| 1 | `a` | no | `matches=[]` |
| 2 | `login_failed` | yes | append; length becomes 1 |
| 2 | limit check | stop | return one match |

The function intentionally does not inspect the remaining line. Its result is bounded, not complete.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| forgetting the stop value | one extra item is processed | test the exact limit |
| printing every record | huge or sensitive output | collect bounded evidence and summarize |
| no progress counters | result lacks context | report processed and matched counts |
| `while True` without a stop | the process never finishes | define a counter, timeout, or input end |
| loading a whole file first | memory grows with input | stream or cap the read |

## Security application

Process the supplied synthetic log fixture with a maximum of 100 lines and 2,000 characters per line. Report `processed`, `matched`, `rejected`, and `truncated`. A truncated report must say it is incomplete.
"""
    + tail(
        6,
        "A loop is a repeated state transition; a security loop must define how much input, time, memory, and output it is allowed to consume.",
        "A bound improves safety but can hide an event outside the inspected window. Always report truncation and choose limits from an explicit operational requirement.",
    )
)

LESSONS[7] = (
    top(
        7,
        "Collections and an Indicator Catalog",
        "Indicators arrive as repeated values with different roles: a list preserves events, a set removes duplicates, and a dictionary associates an indicator with metadata. Choosing the wrong collection can lose evidence or create ambiguity.",
        "Complete Day 6 and understand iteration and bounded processing.",
        "- choose between list, tuple, set, and dictionary\n- preserve order when evidence needs chronology\n- remove duplicates without losing first-seen order\n- associate indicator values with metadata\n- state what a collection can and cannot prove",
        "A synthetic fixture contains repeated domain-like strings and IP-like addresses. You need a catalog for quick membership checks while preserving the original event order for review.",
    )
    + """### Lists preserve order

```python
observations = ["dns", "auth", "dns"]
print(observations[0])
print(observations[-1])
observations.append("process")
print(observations)
```

Lists are mutable and ordered. The duplicate `dns` may be meaningful because it occurred twice.

### Sets support membership and uniqueness

```python
unique = set(observations)
print("dns" in unique)
print(unique)
```

A set removes duplicates and does not promise the chronological order of a list. Use it when uniqueness or membership is the purpose.

### Dictionaries map keys to values

```python
finding = {
    "indicator": "example.invalid",
    "kind": "domain",
    "confidence": "low",
}
print(finding["kind"])
print(finding.get("owner", "unknown"))
```

`finding["owner"]` would raise `KeyError` if missing; `.get` lets you choose a default. Do not let a default hide a required field.

### Tuples communicate fixed structure

```python
coordinate = ("example.invalid", "domain")
name, kind = coordinate
print(name, kind)
```

A tuple can signal that the pair should not be changed. It does not enforce security or validate either string.
"""
    + """## Worked examples

### Example 1: unique values in first-seen order

```python
def unique_in_order(values):
    seen = set()
    result = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result
```

This keeps the order of first appearance while using a set for quick membership checks.

### Example 2: catalog metadata

```python
catalog = {}
for value in ["example.invalid", "203.0.113.8", "example.invalid"]:
    kind = "domain" if "." in value and not value.replace(".", "").isdigit() else "ip-like"
    catalog.setdefault(value, {"kind": kind, "count": 0})
    catalog[value]["count"] += 1
print(catalog)
```

The heuristic is intentionally simple and not a real indicator validator. It illustrates how metadata can be attached without changing the raw value.

### Example 3: list of records

```python
events = [
    {"line": 1, "indicator": "example.invalid"},
    {"line": 2, "indicator": "example.invalid"},
]
for event in events:
    print(event["line"], event["indicator"])
```

A list of dictionaries preserves event order and supports later reporting.

### Example 4: defensive copy

```python
original = ["alpha", "beta"]
copy = original.copy()
copy.append("gamma")
print(original)
print(copy)
```

The original list is unchanged. Accidental aliasing can make a parser modify evidence that another part of the program expects to remain raw.

### Example 5: explicit missing data

```python
record = {"indicator": "example.invalid"}
owner = record.get("owner")
print(owner is None)
```

Missing ownership is a data-quality gap, not proof of maliciousness.

## Execution trace

For `unique_in_order(["a", "b", "a"])`:

| Value | `seen` before | Action | `result` after |
| --- | --- | --- | --- |
| `a` | `{}` | add and append | `["a"]` |
| `b` | `{a}` | add and append | `["a", "b"]` |
| `a` | `{a, b}` | skip | `["a", "b"]` |

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| converting every list to a set | chronology disappears | preserve the list and derive a set |
| using a list for repeated membership checks | code becomes slow on large input | use a set for membership |
| indexing a missing dictionary key | `KeyError` | decide whether missing is an error or default |
| mutating shared lists | raw evidence changes unexpectedly | copy before transforming |
| calling an indicator malicious | the value is treated as a conclusion | label it as observed and record confidence |

## Security application

Create a catalog from synthetic indicators in `shared/fixtures`. Keep the original observations, store a normalized key separately, count repeats, and record the source line. Do not resolve, scan, or contact the indicators.
"""
    + tail(
        7,
        "Choose a collection based on what must be preserved: lists for order, sets for uniqueness, dictionaries for relationships, and tuples for fixed groupings.",
        "A catalog is only as reliable as its input and labeling rules. Duplicate removal can hide frequency, and an indicator string alone does not establish threat intent.",
    )
)

LESSONS[8] = (
    top(
        8,
        "Strings, Encoding, and Canonicalization",
        "Text is where logs, usernames, URLs, commands, and evidence meet the program. Small differences in whitespace, case, Unicode, or encoding can cause duplicate records or incorrect comparisons.",
        "Complete Day 7. Be able to iterate through a list and preserve raw values.",
        "- inspect and transform strings\n- distinguish raw text from normalized keys\n- explain Unicode text and UTF-8 bytes\n- canonicalize without destroying evidence\n- avoid unsafe assumptions about text",
        "Two records contain `Admin`, ` admin `, and `Ａｄｍｉｎ`. A comparison policy may treat them as the same key, but an investigator may still need the original spellings.",
    )
    + """### Strings are sequences of text

```python
message = "login_failed"
print(len(message))
print(message[0])
print(message[-1])
print(message[0:5])
```

Indexes begin at zero. Slicing creates a new string and excludes the stop index. Do not assume that one visible character always equals one byte.

### Whitespace and case

```python
raw = "  Admin  "
print(raw.strip())
print(raw.strip().casefold())
```

`strip` removes surrounding whitespace. `casefold` is designed for case-insensitive comparison. Keep `raw` if the original representation is evidence.

### Replace is not validation

```python
value = "example.invalid/path"
print(value.replace("/", "_"))
```

Replacement creates a transformed value. It does not prove that the original path or domain is valid, safe, or authorized.

### Text and bytes

```python
text = "café"
data = text.encode("utf-8")
print(data)
print(data.decode("utf-8"))
```

The string is Unicode text. UTF-8 encodes it as bytes for storage or transport. Decode with the encoding you expect; arbitrary decoding can corrupt or reject data.

### Raw and canonical forms

```python
def canonical_key(text):
    return " ".join(text.strip().casefold().split())

raw = "  ADMIN   user "
print(raw)
print(canonical_key(raw))
```

The canonical key is useful for comparison, but it must not replace the raw observation in an evidence record.
"""
    + """## Worked examples

### Example 1: empty versus whitespace

```python
for value in ["", " ", "\n", "admin"]:
    print(repr(value), bool(value), bool(value.strip()))
```

A whitespace string is non-empty but has no visible content after stripping. Test the rule you actually intend.

### Example 2: Unicode normalization

```python
import unicodedata

value = "Ａｄｍｉｎ"
normalized = unicodedata.normalize("NFKC", value)
print(normalized)
```

Unicode normalization can make visually equivalent forms comparable. It can also change representation, so retain the raw input.

### Example 3: safe display

```python
line = "user=alice token=training-secret"
print(line.replace("training-secret", "[REDACTED]"))
```

This is a demonstration only. Real redaction should identify fields structurally and test that secrets cannot appear through alternate formatting.

### Example 4: bounded string input

```python
def accept_message(text, maximum=2000):
    if len(text) > maximum:
        raise ValueError("message is too long")
    return text
```

Length limits protect later processing. They do not guarantee that the content is harmless.

### Example 5: canonicalization with provenance

```python
record = {
    "raw_username": "  Admin ",
    "canonical_username": canonical_key("  Admin "),
}
print(record)
```

A reviewer can see both the original and the comparison key.

## Execution trace

For `canonical_key("  ADMIN   user ")`:

| Step | Operation | Result |
| ---: | --- | --- |
| 1 | `strip()` | `"ADMIN   user"` |
| 2 | `casefold()` | `"admin   user"` |
| 3 | `split()` | `["admin", "user"]` |
| 4 | `" ".join(...)` | `"admin user"` |

The transformation is deterministic and explainable.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| normalizing in place | original evidence is lost | store raw and canonical values separately |
| assuming ASCII | names or paths fail for Unicode | define encoding and test representative text |
| using `lower` everywhere | some Unicode cases compare poorly | use `casefold` for comparison when appropriate |
| stripping internal spaces | distinct values collapse | define whether internal whitespace is meaningful |
| redacting only one spelling | a secret leaks in another form | model fields and test variants |

## Security application

Build a local normalizer for synthetic usernames or indicator keys. Produce a table with raw value, canonical key, and reason for normalization. Never resolve or contact a normalized indicator.
"""
    + tail(
        8,
        "Canonicalization creates a comparison representation; evidence handling requires preserving the original text and documenting every transformation.",
        "No text normalization can determine intent or prove identity. Encoding errors, confusable characters, and lossy transformations require careful policy and review.",
        "Watch [CS50P Lecture 0](https://www.youtube.com/watch?v=JP7ITIXGpHk&t=24s) from `00:24` for the first program, then return to the local string examples.",
    )
)

LESSONS[9] = (
    top(
        9,
        "Functions, Contracts, and Validation",
        "Functions let you name a decision, reuse it, and test it without repeating setup. In security engineering, a function contract makes assumptions visible at the boundary.",
        "Complete Days 1–8. You should be comfortable with types, conditions, loops, collections, and strings.",
        "- define and call functions\n- pass arguments and return values\n- keep side effects at the boundary\n- express preconditions and postconditions\n- test normal, boundary, and invalid cases",
        "A log-triage program becomes difficult to review when parsing, classification, printing, and file access are mixed together. Separate functions make each claim smaller and testable.",
    )
    + """### Defining a function

```python
def add(left, right):
    return left + right

print(add(2, 3))
```

`def` creates a function. `left` and `right` are parameters. `return` sends a value back to the caller. Calling `add(2, 3)` binds the arguments and runs the body.

### A function can be pure

```python
def severity_label(severity):
    if not 0 <= severity <= 10:
        raise ValueError("severity must be between 0 and 10")
    return "high" if severity >= 7 else "normal"
```

This function does not print, open files, or use the network. For the same valid input, it returns the same result. Pure functions are easier to test and reason about.

### Contracts describe behavior

A useful contract answers:

- What inputs are accepted?
- What does the function return?
- What happens when input is invalid?
- Does it change files, global state, or external systems?

Write the contract before the implementation. It gives a reviewer something precise to check.

### Arguments and defaults

```python
def summarize(events, limit=100):
    if limit < 0:
        raise ValueError("limit must not be negative")
    selected = events[:limit]
    return {"processed": len(selected), "truncated": len(events) > limit}
```

Defaults are part of the policy. A default limit of `100` is safer than an accidental unbounded read.

### Keep effects at the edge

```python
def format_finding(label, reason):
    return f"label={label} reason={reason}"

message = format_finding("review", "high severity")
print(message)
```

Formatting is separate from printing. A caller can save, test, or display the returned message.
"""
    + """## Worked examples

### Example 1: keyword arguments

```python
def connect_summary(host, port, *, timeout=3):
    return {"host": host, "port": port, "timeout": timeout}

print(connect_summary("127.0.0.1", 8000, timeout=1))
```

The `*` makes `timeout` keyword-only, which can make security-sensitive options harder to pass accidentally.

### Example 2: validation at the function boundary

```python
def require_source(value):
    if not isinstance(value, str):
        raise TypeError("source must be text")
    value = value.strip()
    if not value:
        raise ValueError("source must not be blank")
    return value
```

The function checks both type and policy. The caller receives a clear failure instead of a later obscure error.

### Example 3: returning structured evidence

```python
def inspect_event(event):
    source = require_source(event.get("source"))
    severity = int(event["severity"])
    return {"source": source, "severity": severity, "observed": True}
```

This still needs a severity range check. A function can be useful while remaining incomplete; document the contract rather than pretending it is finished.

### Example 4: a testable caller

```python
def classify_and_format(event):
    label = severity_label(event["severity"])
    return format_finding(label, event["reason"])
```

Because the helper functions return values, tests can exercise them without capturing terminal output.

### Example 5: one side effect at the edge

```python
def write_report(path, text):
    path.write_text(text + "\n", encoding="utf-8")
```

File writing is a side effect. It belongs in a small function with an explicit path policy and test fixture, not inside a pure classifier.

## Execution trace

For `severity_label(8)`:

| Step | Operation | Result |
| ---: | --- | --- |
| 1 | bind `severity` | `8` |
| 2 | validate range | true |
| 3 | evaluate `severity >= 7` | true |
| 4 | return | `"high"` |

The caller receives a value. The function does not decide that a real incident occurred.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| forgetting `return` | caller receives `None` | return the intended value |
| mutable default argument | calls share unexpected state | use `None` or an immutable default |
| hidden print or file write | unit tests become awkward | keep effects at the boundary |
| vague contract | callers guess allowed input | state preconditions and failures |
| validating only in the caller | another caller bypasses checks | validate at the function boundary |

## Security application

Refactor the Day 5 classifier into pure functions for parsing, policy, explanation, and output formatting. Add tests that prove each function’s contract. Keep file access and terminal output in the CLI boundary.
"""
    + tail(
        9,
        "A function is a named contract: explicit inputs enter, a defined result leaves, and side effects are visible at the boundary.",
        "A pure function can still implement a bad policy, receive unauthenticated data, or be called unsafely. Contracts improve review; they do not replace threat modeling.",
        "Watch [CS50P Lecture 0](https://www.youtube.com/watch?v=JP7ITIXGpHk&t=306s) from `05:06` for functions, arguments, and side effects.",
    )
)

LESSONS[10] = (
    top(
        10,
        "Checkpoint: Build a Safe Log-Triage Classifier",
        "A checkpoint turns isolated syntax into a small engineering artifact. You will combine input validation, bounded reading, parsing, classification, and reporting without claiming more than synthetic evidence supports.",
        "Complete Days 1–9. Run the phase tests and make sure your environment is active.",
        "- describe a small security tool’s data flow\n- process a bounded synthetic log fixture\n- preserve observations while adding derived labels\n- test normal, malformed, and out-of-scope inputs\n- write a README that states scope and limitations",
        "A teammate asks for a command that reads a local training log and prints events that deserve review. The tool must not read arbitrary paths, print secrets, run indefinitely, or describe a matched rule as proof of compromise.",
    )
    + """## Project requirements

Build or complete the `log-triage` checkpoint using a local fixture.

### Required data flow

```text
fixture path
   ↓
safe path and size checks
   ↓
bounded line reader
   ↓
record parser
   ↓
validated event
   ↓
triage policy
   ↓
explainable report
```

Keep each stage small. If a test fails, the data flow should help you locate the failing boundary.

### Suggested fixture

```text
2026-08-20T10:00:00Z source=auth severity=2 authenticated=true message=login_ok
2026-08-20T10:01:00Z source=auth severity=8 authenticated=false message=login_failed
malformed line without fields
```

This fixture is invented for the course. It is not evidence of a real event.

### Parse only what you need

```python
def parse_line(line):
    fields = {}
    for item in line.split():
        if "=" not in item:
            continue
        key, value = item.split("=", 1)
        fields[key] = value
    return fields
```

This starter is intentionally incomplete. It does not validate required fields, timestamps, severity, or message length. Your job is to add those boundaries in the exercises.

### Classify with an explicit policy

```python
def classify_event(event):
    severity = event["severity"]
    authenticated = event["authenticated"]
    if severity >= 7 and not authenticated:
        return "review", "high severity and unauthenticated"
    return "normal", "no training rule matched"
```

This says exactly what the training policy does. It does not search the internet, identify a person, or prove an attack.

### Report derived data separately

```python
def report(event, label, reason):
    return {
        "timestamp": event["timestamp"],
        "source": event["source"],
        "severity": event["severity"],
        "label": label,
        "reason": reason,
    }
```

The report contains selected evidence and derived fields. Decide whether the raw message is necessary; if it can contain secrets, redact or omit it.

## Worked examples

### Example 1: a bounded reader

```python
def read_lines(lines, max_lines=100):
    for index, line in enumerate(lines):
        if index == max_lines:
            return
        yield line.rstrip("\n")
```

The function stops at the documented bound. A real file wrapper should also enforce a path and line-length policy.

### Example 2: boolean parsing

```python
def parse_authenticated(value):
    normalized = value.casefold()
    if normalized == "true":
        return True
    if normalized == "false":
        return False
    raise ValueError("authenticated must be true or false")
```

Do not use `bool(value)` for this field.

### Example 3: timestamp parsing

```python
from datetime import datetime

def parse_timestamp(value):
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("timestamp must include a timezone")
    return parsed
```

A timezone-aware timestamp can be compared consistently. The function still needs policy around future dates or clock skew in a real system.

### Example 4: handling one malformed line

```python
for line in fixture:
    try:
        event = parse_event(line)
    except ValueError as error:
        print({"status": "rejected", "reason": str(error)})
        continue
    print({"status": "accepted", "source": event["source"]})
```

The tool preserves the fact of rejection without printing the entire malformed line.

### Example 5: project evidence

A finished checkpoint should include:

| Artifact | What it proves |
| --- | --- |
| `README.md` | setup, scope, data format, limitations |
| source module | the implementation is reproducible |
| tests | normal and negative behavior |
| synthetic fixture | the example is resettable |
| sample report | the output is explainable |
| threat model | assumptions and residual risks |

## Execution trace

For the second fixture line:

| Stage | Value |
| --- | --- |
| raw line | timestamp, source, severity, auth, message text |
| parsed fields | dictionary of strings |
| validated event | timestamp, source, integer severity, boolean auth |
| policy | `severity >= 7 and not authenticated` → true |
| derived result | `label=review` with a reason |
| report | selected evidence plus derived decision |

If parsing fails, the line must not reach the policy stage.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| accepting arbitrary paths | tool can read outside the fixture | resolve and enforce a base directory |
| no line limit | large input consumes resources | stop at a documented maximum |
| trusting every key | malformed data becomes a decision | validate required fields and types |
| printing raw lines | private values leak into reports | redact or summarize |
| calling `review` an attack | evidence becomes an accusation | use neutral labels and confidence |
| no truncation notice | report looks complete | include `truncated=true` when bounded |

## Security application

Run only against the supplied fixture. The project’s scope is local training data, the cleanup is deleting generated reports, and the residual risk is that synthetic rules can produce false positives or miss patterns not represented in the fixture. Document these limits in the project README.
"""
    + tail(
        10,
        "A small security tool is a chain of bounded, testable transformations; every derived conclusion must remain visibly separate from the observations that produced it.",
        "This checkpoint is not a SIEM, an incident-response system, or a detector for real compromise. It teaches engineering boundaries and evidence discipline; real production work requires authorized data, operational ownership, monitoring, and review.",
    )
)


def main() -> int:
    for day, body in LESSONS.items():
        directory = ROOT / DAY_DIRS[day]
        path = directory / f"{directory.name}.md"
        path.write_text(body, encoding="utf-8")
    print("Authored dense teaching chapters for Days 1–10.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
