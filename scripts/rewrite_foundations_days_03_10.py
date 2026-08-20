"""Author the remaining beginner-foundation chapters with real teaching prose."""

# ruff: noqa: E501
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DIRS = {
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
    11: "day_11_function_contracts",
}


@dataclass(frozen=True)
class Lesson:
    day: int
    title: str
    welcome: str
    problem: str
    vocabulary: str
    teaching: str
    trace: str
    mistakes: str
    guided: str
    security: str
    exercises: str
    finish: str
    references: str


def nav(day: int) -> str:
    previous = (
        f"[← Day {day - 1}](../{DIRS[day - 1]}/{DIRS[day - 1]}.md)"
        if day > 1
        else "[Day index](../DAY_INDEX.md)"
    )
    following = (
        f"[Day {day + 1} →](../{DIRS[day + 1]}/{DIRS[day + 1]}.md)" if day < 120 else ""
    )
    return f"{previous} · [Day index](../DAY_INDEX.md) · {following}".strip(" ·")


def render(lesson: Lesson) -> str:
    return f"""# Day {lesson.day}: {lesson.title}

{nav(lesson.day)}

## Welcome

{lesson.welcome}

This lesson is designed for a learner who may still need to look up how to create a file, run it, or read an error. Type the examples instead of reading them passively. Before running an experiment, write down what you expect. The difference between your prediction and Python's output is where learning happens.

## Prerequisites

Complete Day {lesson.day - 1}. Use the repository's local synthetic fixtures only. Keep a terminal open at the repository root and run each file with the Python command that worked on your computer.

## Outcomes

By the end of this lesson, you should be able to explain the new vocabulary in your own words, run and modify the examples, predict at least one boundary case, repair a deliberate mistake, and apply the idea to a bounded cybersecurity fixture.

## The problem

{lesson.problem}

## Security boundary

This lesson is educational and local. It does not authorize public scanning, credential use, data collection, exploitation, interception, or changes to systems you do not own. The cybersecurity examples use invented names, loopback targets, or repository fixtures.

## Vocabulary

{lesson.vocabulary}

## Lesson

{lesson.teaching}

## Worked examples

Run the examples in order. Each one changes only a small part of the previous idea.

## Execution trace

{lesson.trace}

## Common mistakes and repairs

{lesson.mistakes}

## Guided practice

{lesson.guided}

## Security application

{lesson.security}

## Independent exercises

{lesson.exercises}

## Finish line

{lesson.finish}

## References

{lesson.references}

{nav(lesson.day)}
"""


LESSONS = [
    Lesson(
        3,
        "Types, Conversion, and Parsing Boundaries",
        "Yesterday you stored values under names and learned that keyboard input begins as text. Today you will learn how to distinguish kinds of values and how to convert text deliberately. A parser is a small translator: it takes an outside representation and turns it into an internal value the program can reason about.",
        "A log line may contain `severity=7`, but the characters `7` are not automatically the integer 7. If you add the wrong value, compare the wrong type, or silently treat malformed text as valid, a security tool can make a bad decision. The solution is to inspect, convert, validate, and reject clearly.",
        "A **type** describes what kind of value Python is holding. A `str` is text, an `int` is a whole number, a `float` is a decimal number, a `bool` is `True` or `False`, and `None` represents the deliberate absence of a value. **Conversion** asks Python to create a value of another type. **Parsing** is the wider job of interpreting a representation according to rules. **Validation** checks whether the interpreted value is allowed.",
        """Start with inspection:

```python
samples = ["7", 7, 7.5, True, None]

for sample in samples:
    print(repr(sample), type(sample).__name__)
```

Expected output:

```text
'7' str
7 int
7.5 float
True bool
None NoneType
```

The list is a container you will study later. For now, notice that the same-looking idea can have different representations. The quotation marks make `"7"` text. The absence of quotation marks makes `7` a number. `None` is not the same as the string `"None"`; one means no value, the other is text that spells a word.

Conversion is explicit:

```python
raw = " 7 "
clean = raw.strip()
severity = int(clean)
print(repr(raw))
print(repr(clean))
print(severity + 1)
```

Expected output:

```text
' 7 '
'7'
8
```

`strip()` removes whitespace at the edges. It does not turn text into a number. `int()` performs that conversion. Keeping the names `raw`, `clean`, and `severity` makes the boundary visible.

Now break the assumption:

```python
raw = "seven"
severity = int(raw)
```

Python raises `ValueError`. The error means the input was text, but it was not text that Python could interpret as an integer. The correct response is not to hide the exception. A real tool should report a safe validation error and decide whether to reject the record, ask again, or mark it unknown.

Conversion is not the same as policy:

```python
severity = int("99")
print(severity)
```

This succeeds because `99` is a valid integer. It may still violate the application's policy if the accepted range is 0 through 10. Validation comes after conversion:

```python
severity = int("99")
if not 0 <= severity <= 10:
    raise ValueError("severity must be between 0 and 10")
```

The condition is a question with a Boolean answer. Day 4 will teach comparisons and decisions more carefully; today notice the separation: first produce an integer, then decide whether it is allowed.

Boolean conversion deserves caution:

```python
print(bool("false"))
print(bool(""))
print(bool(0))
print(bool(1))
```

Expected output:

```text
True
False
False
True
```

`bool("false")` is `True` because the string is not empty. It does not understand the English word false. A parser for human text must define its own accepted words instead of trusting `bool` to translate them.

A small parser can make the policy visible:

```python
def parse_boolean(text):
    normalized = text.strip().casefold()
    if normalized in {"true", "yes", "1"}:
        return True
    if normalized in {"false", "no", "0"}:
        return False
    raise ValueError("expected yes/no, true/false, or 1/0")
```

Read the function from top to bottom. It receives text, removes edge whitespace, makes case comparisons predictable, accepts a small allowlist of words, and rejects everything else. The function does not guess what `"maybe"` means.

A parser should also decide what to do with missing input:

```python
def parse_optional_limit(text):
    cleaned = text.strip()
    if cleaned == "":
        return None
    limit = int(cleaned)
    if not 1 <= limit <= 100:
        raise ValueError("limit must be from 1 through 100")
    return limit
```

Here `None` means “the operator did not provide a limit.” It is different from `0`, which is a number and is rejected by policy. A program that confuses missing, empty, zero, and invalid values can process too much data or report a false result.

Try a prediction experiment. What will each line print?

```python
print(type("7").__name__)
print(type(int("7")).__name__)
print("7" + "0")
print(int("7") + 0)
```

Run it only after writing your prediction. The output demonstrates that conversion changes what operations mean.

The mental model is a boundary table:

| Stage | Example | Question |
| --- | --- | --- |
| Raw input | `" 7 "` | What characters arrived? |
| Cleaned text | `"7"` | What harmless formatting was removed? |
| Converted value | `7` | What type did the parser create? |
| Validated value | `7` within 0–10 | Is this value allowed here? |
| Application decision | review or accept | What should the program do next? |

Do not skip straight from raw text to a security decision. Each stage gives you evidence and a place to handle failure."""
        "",
        """Trace this program:

```python
raw = " 08 "
clean = raw.strip()
number = int(clean)
allowed = 0 <= number <= 10
print(allowed)
```

| Step | Name | Value | Type |
| ---: | --- | --- | --- |
| 1 | `raw` | `" 08 "` | `str` |
| 2 | `clean` | `"08"` | `str` |
| 3 | `number` | `8` | `int` |
| 4 | `allowed` | `True` | `bool` |
| 5 | output | `True` | terminal text |

Now replace `raw` with `"eleven"`. The program stops at `int(clean)`, so `allowed` is never created. If you replace it with `"99"`, conversion succeeds but `allowed` becomes `False`. Those are different failure categories: malformed representation versus a valid value outside the application's permitted range.""",
        """| Mistake | Why it happens | Repair |
| --- | --- | --- |
| Treating `"7"` as `7` | They look alike when printed. | Inspect the type and convert explicitly. |
| Using `bool("false")` as a parser | Truthiness is mistaken for language parsing. | Normalize and compare an allowlist. |
| Converting without a range check | A valid integer may still be unsafe for the application. | Validate the allowed interval. |
| Treating empty text as zero | Missing input and zero have different meanings. | Represent missing input explicitly with `None`. |
| Catching every exception | Programmer errors become invisible. | Catch only expected input errors at the boundary. |
| Printing raw input in a report | Diagnostic output may leak sensitive data. | Keep raw data local and report safe metadata. |""",
        """Build a parser in checkpoints.

1. Begin with `raw = " 7 "` and print it with `repr`.
2. Create `clean` using `strip()` and print both values.
3. Convert `clean` to an integer named `severity` and print its type.
4. Add a range check for 0 through 10.
5. Test the values `0`, `10`, `-1`, `11`, and `high` one at a time.
6. For `high`, produce a safe message such as `invalid integer` rather than printing a traceback in the report.
7. Add a second parser for yes/no text. Accept only the documented words.

At each checkpoint, run the file. Do not add the next layer until you can explain the current output. If a test fails, write down whether the failure happened during cleaning, conversion, or validation."""
        "",
        """A synthetic log record is an ideal boundary exercise:

```python
record = {"severity": " 7 ", "authenticated": "no"}
```

The values are text because they came from an outside representation. Parse them into an internal record:

```python
severity = int(record["severity"].strip())
authenticated = parse_boolean(record["authenticated"])
```

This does not prove that the record is authentic. It only prevents the rest of the program from pretending that unparsed text is already a trusted integer or Boolean. In a real security tool, the parser would also report which field failed, limit input size, preserve provenance, and avoid including secrets in the error message.

Use only synthetic records. Do not paste a real log line into this exercise because real logs may contain usernames, tokens, addresses, or personal data."""
        "",
        """1. Print the type name of `"7"`, `7`, `7.0`, `True`, and `None`.
2. Convert `"42"` to an integer and `"0.5"` to a float. Print both values and types.
3. Try to convert `"high"` to an integer. Record the exception type and explain the message.
4. Show why `bool("false")` is `True`. Write an explicit parser that treats `false`, `no`, and `0` as false.
5. Write a parser that accepts integer severities from 0 through 10 and rejects `-1`, `11`, empty text, and `high`.
6. Explain the difference between raw input, cleaned text, converted value, and validated value.
7. Write `parse_optional_limit` so empty text returns `None` and non-empty text must be an integer from 1 through 100.
8. Create a synthetic record containing string fields for severity and authentication. Parse both fields and print their resulting types.
9. Add a safe error report that names the invalid field but does not print the full raw record.
10. Write a table of five inputs and classify each as missing, malformed, valid-but-out-of-range, or accepted.
11. Explain why a valid integer can still be unsafe for a program.
12. Safety question: name three kinds of input that must remain outside today's files and explain why parsing does not create authorization.

Use [hints](practice/hints.md) only after attempting the question. Use [solutions](practice/solutions.md) to compare reasoning, not to replace it."""
        "",
        "Day 3 is complete when you can inspect a value's type, explain why conversion and validation are separate, write a bounded parser, distinguish missing from invalid, and describe the security limitation of parsing synthetic input. You should be able to trace a failure to the exact stage where it occurred.",
        '''[1]: https://docs.python.org/3/library/functions.html#type "Python type documentation"
[2]: https://docs.python.org/3/library/functions.html#int "Python int documentation"
[3]: https://docs.python.org/3/library/stdtypes.html#truth-value-testing "Python truth-value testing"
[4]: https://docs.python.org/3/tutorial/errors.html "Python errors and exceptions"
[5]: https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html "OWASP input validation guidance"''',
    ),
    Lesson(
        4,
        "Operators, Comparisons, and Decisions",
        "A program becomes useful when it can do more than print fixed text. It can calculate, compare, and choose. Today you will learn the symbols that express those actions and how Python turns a comparison into a Boolean decision.",
        "A triage tool might need to ask whether a severity is high enough for review, whether a record is empty, or whether two values are equal. If you confuse assignment with comparison or misunderstand `and` and `or`, the tool may take the wrong branch.",
        "An **operator** is a symbol or word that performs an operation. An **expression** is code that produces a value. A **comparison** produces `True` or `False`. A **condition** is an expression used to choose a path. **Precedence** is the order Python uses when several operators appear together.",
        """Begin with arithmetic:

```python
failed = 7
allowed = 3
remaining = failed - allowed
print(remaining)
```

Expected output is `4`. The expression `failed - allowed` is evaluated before assignment to `remaining`. Addition, subtraction, multiplication, division, floor division, remainder, and exponentiation have different meanings:

```python
print(7 + 2)
print(7 - 2)
print(7 * 2)
print(7 / 2)
print(7 // 2)
print(7 % 2)
print(7 ** 2)
```

Expected output:

```text
9
5
14
3.5
3
1
49
```

The remainder operator `%` is useful for asking whether a number divides evenly. It is not a security detector by itself; it is just arithmetic.

Comparisons answer questions:

```python
severity = 7
print(severity == 7)
print(severity != 4)
print(severity > 5)
print(severity <= 10)
```

The comparison operator is `==`; assignment is `=`. This distinction is one of the most common beginner errors. `severity = 7` changes the stored value. `severity == 7` asks whether the current value equals 7.

Combine questions with Boolean operators:

```python
severity = 7
is_known_source = True
needs_review = severity >= 7 and is_known_source
print(needs_review)
```

`and` requires both sides to be true. `or` requires at least one side to be true. `not` reverses a Boolean result. Read the condition in plain English before reading it as code.

Decisions use `if`:

```python
severity = 7

if severity >= 7:
    print("review")
else:
    print("record")
```

The colon begins the block controlled by the condition. Indentation shows which statements belong to the block. If severity is 7, Python runs the indented `print("review")`. Otherwise it runs the `else` block.

Add a third path with `elif`:

```python
if severity >= 9:
    label = "urgent"
elif severity >= 7:
    label = "review"
else:
    label = "routine"

print(label)
```

Python tests the branches from top to bottom and stops at the first true branch. The order matters. If you put `severity >= 7` first, a severity of 9 will be labelled review and never reach urgent. Conditions must be ordered from the more specific or urgent case to the broader case.

Precedence can surprise you:

```python
result = False or True and False
print(result)
```

Python evaluates `and` before `or`, so this behaves like `False or (True and False)`, which is `False`. When a condition matters, use parentheses even if you know the precedence:

```python
result = (False or True) and False
print(result)
```

This is now `False` for a different reason. Parentheses make the intended grouping visible to a future reader.

Truthiness is another decision rule. Empty strings, empty lists, zero, and `None` are commonly false in a Boolean context; non-empty values are commonly true. Do not use truthiness as a replacement for a precise policy when the difference between missing and zero matters.

```python
value = ""
if value:
    print("has text")
else:
    print("empty")
```

The output is `empty`. The condition did not compare `value` to a word; Python asked whether the value was considered true.""",
        """Trace:

```python
severity = 8
known = True

if severity >= 9:
    decision = "urgent"
elif severity >= 7 and known:
    decision = "review"
else:
    decision = "routine"
```

| Step | Question | Result |
| ---: | --- | --- |
| 1 | Is `8 >= 9`? | `False`, continue. |
| 2 | Is `8 >= 7`? | `True`. |
| 3 | Is `known` true? | `True`. |
| 4 | Is `True and True`? | `True`, choose review. |
| 5 | Run `else`? | No, the chain already chose a branch. |

Change `known` to `False`. Step 3 becomes false, so the combined condition becomes false and the decision becomes routine. The number did not change; the second piece of evidence changed the path.""",
        """| Mistake | Why it happens | Repair |
| --- | --- | --- |
| `if severity = 7` | Assignment and comparison look similar. | Use `==` for a question. |
| Broad condition first | A later urgent branch becomes unreachable. | Order branches deliberately. |
| Missing indentation | Python cannot identify the block. | Indent the controlled statements consistently. |
| Long condition without parentheses | Precedence is hidden. | Add parentheses and explain the grouping. |
| Treating `0` as missing | Truthiness is confused with meaning. | Compare explicitly when zero is valid. |
| Using `or` when both facts are required | One true side is enough. | Use `and` for “both must hold.” |""",
        """Build a triage decision in checkpoints. Start with a `severity` value and a Boolean `source_is_known` value. First print each input. Then write three branches: urgent for 9–10, review for 7–8 from a known source, and routine otherwise. Test 10 known, 8 known, 8 unknown, 4 known, and -1.

Before each run, write the expected label. When a result surprises you, inspect the comparison values separately:

```python
print(severity >= 9)
print(severity >= 7)
print(source_is_known)
```

This is often easier than staring at one long condition. A good debugger breaks a complicated question into smaller questions.""",
        """In defensive tooling, a condition should express a documented policy rather than a feeling. For a synthetic event, you might decide that a record needs review only when the severity is at least 7 **and** the record passed a source-quality check. That rule is not universal. It is a local training policy.

Write the policy in English first, then translate it:

> Review this synthetic record when its severity is 7 or higher and its source label is known.

```python
review = severity >= 7 and source_is_known
```

The code is easier to review because the variable names carry the policy. It still does not prove that a record is malicious, that a source is authentic, or that an alert deserves a real-world response.""",
        """1. Predict the output of each arithmetic operator in a small program.
2. Explain the difference between `=` and `==` using a sentence and code.
3. Write comparisons for severity equal to 7, greater than 7, and between 0 and 10.
4. Build an `if/elif/else` classifier for urgent, review, and routine.
5. Test the classifier at every boundary: 0, 6, 7, 8, 9, and 10.
6. Write one condition that requires two facts with `and` and one that accepts either fact with `or`.
7. Add parentheses to a mixed `and`/`or` expression and explain why.
8. Demonstrate the difference between an empty string, zero, and `None` in an `if` statement.
9. Write a safe decision for a synthetic event and explain what the decision cannot prove.
10. Create a deliberate branch-order bug, demonstrate it with severity 9, and repair it.
11. Write a short explanation of operator precedence for a beginner.
12. Safety question: explain why a decision rule should not be used to accuse a person automatically.""",
        "Day 4 is complete when you can predict a comparison, choose between `and` and `or`, explain the difference between assignment and equality, order branches correctly, and state the limits of a synthetic triage decision.",
        '''[1]: https://docs.python.org/3/reference/expressions.html#operator-precedence "Python operator precedence"
[2]: https://docs.python.org/3/tutorial/controlflow.html#if-statements "Python conditional statements"
[3]: https://docs.python.org/3/library/stdtypes.html#truth-value-testing "Python truth-value testing"
[4]: https://owasp.org/www-community/controls/Logging "OWASP logging guidance"''',
    ),
    Lesson(
        5,
        "Branching and a First Triage Classifier",
        "Yesterday you learned the symbols that produce decisions. Today you will slow down and design a branching program carefully. The goal is not to write clever conditions; it is to make the path a reader can predict, test, and explain.",
        "A classifier receives a synthetic record and must choose one label. If conditions overlap, if a field is missing, or if every unexpected value is treated as safe, the result becomes misleading. A branching design needs an order, a default, and a clear treatment of uncertainty.",
        "A **branch** is one possible path through a program. A **classifier** assigns a label according to rules. A **default** is what happens when no special case matches. **Unknown** means the program lacks enough information; it should not automatically mean safe.",
        """Start with one branch:

```python
severity = 8

if severity >= 7:
    print("review")
```

If the condition is false, Python prints nothing. That may be correct for a small experiment, but a reporting tool often needs an explicit default. Add `else`:

```python
if severity >= 7:
    print("review")
else:
    print("routine")
```

Now every numeric input receives a label, but the design still assumes the value is valid. Add validation before classification rather than hiding invalid data inside a normal label.

```python
severity = 12

if not 0 <= severity <= 10:
    label = "invalid"
elif severity >= 7:
    label = "review"
else:
    label = "routine"

print(label)
```

This ordering is important. The invalid check comes before the ordinary severity rules. Otherwise 12 would be classified as review even though it violates the documented range.

Add source quality:

```python
severity = 8
source = "unknown"

if source != "training-auth":
    label = "unknown-source"
elif severity >= 9:
    label = "urgent"
elif severity >= 7:
    label = "review"
else:
    label = "routine"

print(label)
```

This classifier chooses `unknown-source` before examining severity. That is a policy choice: an unknown source prevents this training classifier from making a severity decision. Another system might preserve both labels instead of choosing one. The important lesson is to document the choice.

Nested branches are sometimes readable, but they can become difficult to trace:

```python
if source == "training-auth":
    if severity >= 7:
        print("review")
    else:
        print("routine")
else:
    print("unknown-source")
```

The flat `if/elif/else` chain and the nested version can represent the same rule. Choose the form that makes the policy easiest to test. Do not nest conditions merely to look advanced.

You can also return a label from a function, but functions are tomorrow's main topic. For today, notice that storing the label in a name makes it available for a later report:

```python
label = "review"
print(f"classification={label}")
```

A branch can choose a value without immediately printing it. Separating decision from output makes later testing easier.""",
        """Trace the classifier:

```python
severity = 12
source = "training-auth"

if not 0 <= severity <= 10:
    label = "invalid"
elif source != "training-auth":
    label = "unknown-source"
elif severity >= 9:
    label = "urgent"
elif severity >= 7:
    label = "review"
else:
    label = "routine"
```

Python checks the first condition. `12` is not between 0 and 10, so `label` becomes `invalid`. Python skips every later branch. If you move the invalid check below `severity >= 9`, the same input becomes urgent. That is a bug in policy order, not in Python syntax.

Make a decision table before coding:

| Input | Expected label |
| --- | --- |
| severity 12 | invalid |
| severity 8, unknown source | unknown-source |
| severity 9, known source | urgent |
| severity 7, known source | review |
| severity 3, known source | routine |

The table is a small specification. The code is an implementation of that specification.""",
        """| Mistake | Symptom | Repair |
| --- | --- | --- |
| No invalid branch | Bad data receives a normal label. | Validate before classifying. |
| `else` means safe | Unknown conditions are treated as routine. | Use an explicit unknown label. |
| Overlapping conditions | The first matching rule wins unexpectedly. | Order and test the rules. |
| Printing inside every branch | The decision cannot be reused or tested easily. | Store a label, then report it. |
| Nested code too deeply | The path is hard to trace. | Use a table or flat chain where clearer. |""",
        """Create a decision table on paper for a fictional event. Include fields `severity`, `source`, and `authenticated`. Decide what should happen when each field is invalid or missing. Then implement only the first five rows.

Run one test per row. If a result is wrong, do not change the table to match the program. Treat the table as the intended behavior and repair the code. Add a print statement showing which input row you are testing so that a failure is easy to locate.

Finally, change the program so it returns or stores a label before printing. This small separation will prepare you for functions and tests on Day 9.""",
        """A defensive classifier should preserve uncertainty. For synthetic logs, an invalid severity should not become a low-priority event, and a missing source should not become a trusted source. A label such as `unknown` is not a weakness in the program; it is a truthful statement about incomplete information.

Never use this training classifier to make decisions about a real person. It has no trustworthy collection path, identity proof, context, or organizational policy. It demonstrates branching and safe uncertainty only.""",
        """1. Write a two-branch classifier for a number being inside or outside 0–10.
2. Add an explicit `unknown` path for missing source text.
3. Create a five-row decision table before writing code.
4. Implement urgent, review, routine, invalid, and unknown-source labels.
5. Test every boundary and copy the observed result.
6. Create an overlapping-rule bug and explain why the first matching branch wins.
7. Rewrite a nested classifier as a flat chain and compare readability.
8. Store a label before printing it.
9. Add a safe message that reports `classification=unknown` without making an accusation.
10. Explain why `else` should not automatically mean safe.
11. Add a test case for a missing field and describe the desired behavior.
12. Safety question: identify one way an automated classifier could cause harm if treated as a verdict.""",
        "Day 5 is complete when you can design a decision table, implement ordered branches, preserve unknown and invalid states, test every boundary, and explain why a classifier is not an accusation.",
        '''[1]: https://docs.python.org/3/tutorial/controlflow.html#if-statements "Python conditional statements"
[2]: https://docs.python.org/3/reference/compound_stmts.html "Python compound statements"
[3]: https://csrc.nist.gov/glossary/term/risk "NIST risk glossary"
[4]: https://www.cisa.gov/topics/cyber-threats-and-advisories "CISA cyber threat guidance"''',
    ),
    Lesson(
        6,
        "Loops, Bounds, and Resource Safety",
        "A loop repeats work. Repetition is powerful because security tools often process many records, but repetition is also a place where a beginner can accidentally create an infinite loop, read an unbounded file, or produce an enormous report. Today you will learn repetition with an explicit stopping rule.",
        "A program needs to inspect several synthetic events without copying the same line five times. It also needs to stop. A loop without a bound or a progress rule can consume time, memory, and attention indefinitely.",
        "A **loop** repeats a block. A `for` loop visits items in a sequence. A `while` loop continues while a condition is true. A **bound** is a deliberate maximum. `break` stops a loop; `continue` skips to the next iteration. An **iteration** is one pass through the body.",
        """Start with a `for` loop:

```python
for number in [1, 2, 3]:
    print(number)
```

Expected output is one number per line. Python takes the first item, assigns it to `number`, runs the indented body, then repeats for the next item. The name `number` changes during the loop, but the list is finite.

The `range` function creates a sequence of numbers for a loop:

```python
for index in range(3):
    print(f"index={index}")
```

The output is 0, 1, and 2. The stop value 3 is not included. This is a common source of off-by-one mistakes. Read `range(3)` as “produce three positions starting at zero,” not “count from one to three.”

Use a counter when you need a total:

```python
failed = ["a", "b", "c"]
count = 0

for event in failed:
    count += 1
    print(f"examining={event}")

print(f"total={count}")
```

The counter starts at zero and increases once per item. The list is already finite, so this loop has a natural bound.

A `while` loop needs a progress rule:

```python
attempt = 0
while attempt < 3:
    print(f"attempt={attempt}")
    attempt += 1
```

If you forget `attempt += 1`, the condition remains true forever. A safe `while` loop should make its changing state and maximum attempts visible.

You can add a second safety bound:

```python
items_seen = 0
for event in events:
    if items_seen >= 100:
        break
    print(event)
    items_seen += 1
```

This protects the consumer even if `events` is larger than expected. A bound is not an invitation to ignore the data source; it is a last line of resource control.

`continue` can skip an item, but use it carefully:

```python
for event in ["", "login_failed", "", "logout"]:
    if event == "":
        continue
    print(event)
```

The empty values are skipped. If you skip too much, your report may look clean because the program discarded the evidence. Record how many items were skipped when that matters.

Nested loops multiply work. A loop over 100 files containing a loop over 1,000 lines may inspect 100,000 combinations. Before adding nesting, estimate the work and set a bound.""",
        """Trace:

```python
items = ["a", "b", "c"]
count = 0
for item in items:
    count += 1
    print(item, count)
```

| Iteration | `item` | `count` before | `count` after |
| ---: | --- | ---: | ---: |
| 1 | `a` | 0 | 1 |
| 2 | `b` | 1 | 2 |
| 3 | `c` | 2 | 3 |

For a `while` loop, trace both the condition and the changing value. If the value never changes toward the stopping condition, the loop is unsafe. The fastest way to debug a loop is often to print a small state value and add a temporary maximum iteration count.""",
        """| Mistake | Symptom | Repair |
| --- | --- | --- |
| Forgetting progress in `while` | Infinite loop. | Update the state every iteration. |
| Assuming `range(3)` includes 3 | Missing or extra work. | Test the endpoints explicitly. |
| No maximum input count | Resource use depends on an untrusted source. | Set a finite bound. |
| `continue` hides evidence | The report silently loses records. | Count and explain skipped items. |
| Nested loops without estimating work | Slow or exhausting processing. | Bound each dimension or redesign. |""",
        """Write a loop in checkpoints. First loop over three literal event names and print them. Then count them. Then skip empty strings while incrementing a `skipped` counter. Finally, add a maximum of three processed items to a list containing five items.

For each change, write the expected processed count and skipped count before running. If your program produces a different answer, inspect the state at the start and end of each iteration. Do not begin with a file or network source; learn the loop with a small list first.""",
        """A log tool may need to process many records, but “many” must be turned into a documented resource policy. A training parser can accept at most 100 lines, 1 MB, or 10 seconds of work. These numbers are examples, not universal security thresholds.

When a bound is reached, report that processing was incomplete. Do not silently present the first 100 records as if they were the entire source. A bounded report is more honest when it says `complete=False` or `truncated=True`.""",
        """1. Loop over three event names and predict the output order.
2. Use `range(5)` and write down the exact values it produces.
3. Count a list without using `len`.
4. Write a `while` loop with a maximum of five attempts.
5. Deliberately remove the progress statement and explain why the loop would not end.
6. Skip empty events and count how many were skipped.
7. Stop after three processed events and report truncation.
8. Estimate the work in a nested loop of 10 files and 100 lines.
9. Build a synthetic bounded log summary.
10. Explain why a loop limit protects availability but can reduce completeness.
11. Write a test for an empty list and a list larger than the bound.
12. Safety question: explain why an unbounded loop over an untrusted file can become a security problem.""",
        "Day 6 is complete when you can explain one `for` loop and one `while` loop step by step, identify their stopping rule, add a finite work bound, account for skipped data, and report incomplete processing honestly.",
        '''[1]: https://docs.python.org/3/tutorial/controlflow.html#for-statements "Python for statements"
[2]: https://docs.python.org/3/reference/compound_stmts.html#while "Python while statements"
[3]: https://docs.python.org/3/library/functions.html#range "Python range documentation"
[4]: https://owasp.org/www-community/attacks/Denial_of_Service "OWASP denial of service overview"''',
    ),
    Lesson(
        7,
        "Collections and an Indicator Catalog",
        "One value is useful, but cybersecurity programs usually handle groups of values. Today you will learn lists, tuples, sets, and dictionaries by asking what each collection promises and when that promise matters.",
        "A small indicator catalog needs to preserve observations, remove duplicates when appropriate, and attach fields such as type and source. Choosing the wrong collection can lose order, overwrite values, or make a report hard to understand.",
        "A **list** is an ordered, changeable collection. A **tuple** is an ordered collection commonly used for fixed groups. A **set** stores unique values without promising list-style order. A **dictionary** maps keys to values. A **membership test** asks whether a value is present.",
        """A list preserves order:

```python
events = ["login_failed", "logout", "login_failed"]
print(events[0])
print(len(events))
```

The first item has index 0, not index 1. The list contains a duplicate because the same event occurred twice. Lists are appropriate when order and repeated observations matter.

A set removes duplicates:

```python
indicators = {"example.invalid", "example.invalid", "training.invalid"}
print(len(indicators))
print("training.invalid" in indicators)
```

The length is 2. A set is useful for asking whether a value has already been seen. Do not use it when the count or original order of observations is important.

A dictionary stores related fields:

```python
record = {
    "value": "example.invalid",
    "kind": "domain",
    "source": "training-fixture",
}
print(record["kind"])
```

The key `kind` retrieves the value `domain`. A missing key raises `KeyError` when accessed with brackets. You can use `.get` when missing data has a documented fallback:

```python
confidence = record.get("confidence")
print(confidence)
```

This prints `None` because the key is absent. Do not use a fallback simply to hide a required field; decide whether missing confidence should reject the record or mark it unknown.

Tuples are useful for fixed pairs:

```python
address = ("127.0.0.1", 8000)
host, port = address
print(host)
print(port)
```

The two assignments unpack the tuple. The address is not a real remote target; it is a local training value. The point is to learn how related values can travel together.

A catalog may combine collections:

```python
catalog = [
    {"value": "example.invalid", "kind": "domain"},
    {"value": "127.0.0.1", "kind": "address"},
]
for item in catalog:
    print(f"{item['kind']}={item['value']}")
```

Read the outer list as “many records” and each inner dictionary as “fields for one record.” This shape appears often in JSON and API responses.

Mutation changes a collection:

```python
items = ["a", "b"]
items.append("c")
print(items)
```

The list now contains three items. A name referring to a mutable list can observe changes made elsewhere. Later lessons will discuss copying and shared state; for now, remember that a collection can be changed after creation.""",
        """Trace a deduplication task:

```python
observed = ["a", "b", "a"]
unique = set(observed)
report = {"observed": len(observed), "unique": len(unique)}
print(report)
```

| Step | Name | Value |
| ---: | --- | --- |
| 1 | `observed` | three observations, including a duplicate |
| 2 | `unique` | two unique values |
| 3 | `report` | a dictionary containing both counts |

The set answers a uniqueness question but does not preserve the event sequence. Keep both collections when both facts matter.""",
        """| Mistake | Symptom | Repair |
| --- | --- | --- |
| Indexing at 1 | The first item is missed or an error occurs. | Remember that Python starts at 0. |
| Set for a timeline | Order and duplicate count disappear. | Keep a list for observations. |
| Dictionary key missing | `KeyError`. | Validate required keys or use a deliberate fallback. |
| Mutable list shared | One function changes another function's data. | Copy or document ownership. |
| Treating a value as trusted because it is in a set | Membership only answers presence. | Preserve source and confidence fields. |""",
        """Create a small indicator catalog in stages. Begin with a list of three synthetic strings. Add a duplicate and count observations. Convert to a set and count unique values. Then create dictionaries containing `value`, `kind`, and `source`.

Write a report that prints both `observed_count` and `unique_count`. Add one record with a missing `confidence` key and decide whether your program should print `unknown` or reject the record. Explain your choice before coding it.""",
        """Collections help organize evidence but do not make evidence true. A list preserves the observations your fixture contained. A set can help detect duplicates. A dictionary can label fields. None of them proves that an indicator is malicious, that a source is authentic, or that a real-world action is justified.

Use `.invalid` domains, loopback addresses, and invented hashes in exercises. Do not resolve, scan, or query these values against public services.""",
        """1. Create a list with three events and print the first and last item.
2. Explain why the first list index is 0.
3. Add a duplicate and calculate observed and unique counts.
4. Create a set and demonstrate membership.
5. Create a dictionary with `value`, `kind`, and `source`.
6. Access a missing dictionary key and record the exception.
7. Repair the missing-key behavior with a documented fallback.
8. Build a list of dictionaries representing synthetic indicators.
9. Add a tuple for a loopback host and port.
10. Explain which collection preserves order and which removes duplicates.
11. Write a report that includes source and confidence without claiming a verdict.
12. Safety question: explain why storing an indicator in a collection does not authorize acting on it.""",
        "Day 7 is complete when you can choose a collection based on order, uniqueness, mutability, and key-value structure, build a small catalog, handle missing fields, and preserve the difference between an observation and an interpretation.",
        '''[1]: https://docs.python.org/3/tutorial/datastructures.html "Python data structures"
[2]: https://docs.python.org/3/library/stdtypes.html#dict "Python dictionary documentation"
[3]: https://docs.python.org/3/library/stdtypes.html#set "Python set documentation"
[4]: https://www.cisa.gov/topics/cyber-threats-and-advisories "CISA cyber threat guidance"''',
    ),
    Lesson(
        8,
        "Strings, Encoding, and Canonicalization",
        "Security data often arrives as text, but text is not one simple thing. Case, whitespace, Unicode, separators, and encoding can make two strings look similar while comparing differently. Today you will learn to normalize text deliberately without destroying the original evidence.",
        "A tool wants to compare event labels consistently, but input may contain spaces, different capitalization, or different textual representations. If it silently changes the evidence, it may make a useful comparison while losing the original context.",
        "A **string** is a sequence of text characters. **Whitespace** includes spaces, tabs, and line breaks. **Encoding** maps characters to bytes. **Canonicalization** turns equivalent representations into one comparison form. **Normalization** should be recorded when the original matters.",
        """Start with string methods:

```python
raw = "  Login_Failed  "
print(raw.strip())
print(raw.lower())
print(raw.strip().casefold())
```

`strip()` removes edge whitespace. `lower()` changes letters to lowercase. `casefold()` is designed for more complete case-insensitive comparisons. Neither method changes `raw`; strings are immutable, so each method returns a new string.

Splitting turns one string into pieces:

```python
line = "level=7 source=training-auth"
parts = line.split()
print(parts)
```

Expected output is a list of two pieces. `split()` uses whitespace by default. You can specify a separator:

```python
pair = "severity:7"
key, value = pair.split(":", 1)
print(key)
print(value)
```

The second argument `1` limits the number of splits. Without a limit, a value containing a colon could produce more pieces than expected. Parsing rules should state what happens when the delimiter is missing.

Joining performs the opposite movement:

```python
fields = ["source=training-auth", "severity=7"]
line = " ".join(fields)
print(line)
```

Use `repr()` when debugging invisible characters:

```python
value = "login_failed\n"
print(value)
print(repr(value))
```

The first print creates a line break from the value. The second shows the escape sequence so you can see it.

Canonicalization should be narrow. If you want to compare event labels, define the comparison form:

```python
def canonical_label(text):
    return text.strip().casefold().replace("-", "_")

print(canonical_label(" Login-Failed "))
```

The result is `login_failed`. Keep the raw label if you need to report exactly what arrived. Canonicalization for comparison is not permission to overwrite evidence.

Encoding matters when text becomes bytes:

```python
text = "café"
encoded = text.encode("utf-8")
print(encoded)
print(encoded.decode("utf-8"))
```

UTF-8 is a common encoding, but a decoder must use the encoding that matches the data source. Decoding bytes with the wrong encoding can raise `UnicodeDecodeError` or produce the wrong characters.

Never normalize paths, URLs, identifiers, or security tokens with a generic string function without understanding the context. A comparison form for labels is not automatically safe for a filesystem path or a URL.""",
        """Trace:

```python
raw = "  Login-Failed \n"
comparison = raw.strip().casefold().replace("-", "_")
print(repr(raw))
print(comparison)
```

| Step | Value |
| ---: | --- |
| 1 | raw text includes spaces and a newline |
| 2 | `strip()` removes the edge whitespace |
| 3 | `casefold()` changes letter case |
| 4 | `replace()` changes the selected separator |
| 5 | `repr(raw)` still shows the original representation |

The comparison value is useful for matching. The raw value remains useful for provenance and debugging.""",
        """| Mistake | Symptom | Repair |
| --- | --- | --- |
| `lower()` used as universal security normalization | Context-specific rules are ignored. | Define the exact comparison policy. |
| Discarding raw input | The original evidence cannot be reviewed. | Preserve a safe reference or original fixture. |
| `split()` without a rule | Unexpected field counts. | Limit splits and handle missing separators. |
| Decoding with a guess | Errors or corrupted text. | Use documented source encoding. |
| Replacing every symbol | Meaning changes silently. | Canonicalize only the intended field. |""",
        """Take the string `"  Login-Failed "` through checkpoints: inspect it with `repr`, strip it, casefold it, replace the dash, and compare it with `"login_failed"`. Then add a second label that should not match and prove the result.

Create a small parser for `key=value` fields. Test a normal field, a field with extra `=`, a missing separator, and an empty value. Write down which cases your parser accepts and why.""",
        """In security tools, canonicalization can prevent duplicate labels or inconsistent comparisons, but it can also hide meaningful differences if applied too broadly. Keep raw synthetic text separate from its normalized comparison form. A report might contain `raw_label` as a redacted or fixture reference and `canonical_label` as the value used for a rule.

Do not normalize or inspect real personal identifiers, URLs, tokens, or private logs in this lesson.""",
        """1. Show the difference between `strip`, `lower`, and `casefold` on a sample.
2. Use `repr` to reveal a newline and a tab.
3. Split a key-value pair at the first colon only.
4. Join three fields with a separator.
5. Write `canonical_label` for a documented label policy.
6. Preserve both raw and canonical values in a synthetic record.
7. Encode and decode a non-ASCII string using UTF-8.
8. Trigger and explain a missing-separator case.
9. Explain why generic replacement is dangerous for a URL or path.
10. Build a small text normalizer and test empty, spaced, and mixed-case input.
11. Describe the difference between characters and bytes.
12. Safety question: explain why retaining raw text can be a privacy concern and how fixtures reduce that risk.""",
        "Day 8 is complete when you can inspect invisible text, choose a narrow canonicalization rule, preserve original context, explain encoding, and handle malformed text without silently changing its meaning.",
        '''[1]: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "Python string documentation"
[2]: https://docs.python.org/3/library/stdtypes.html#str.casefold "Python casefold documentation"
[3]: https://docs.python.org/3/library/stdtypes.html#str.encode "Python string encoding documentation"
[4]: https://owasp.org/www-community/attacks/Unicode_Encoding "OWASP Unicode encoding considerations"''',
    ),
    Lesson(
        9,
        "Functions, Contracts, and Validation",
        "Your programs are now long enough that copying blocks creates mistakes. A function gives a named job a boundary: it receives inputs, performs one responsibility, and returns a result. Today you will write small functions and state what each one promises.",
        "A parser, classifier, and report formatter should be testable separately. If one giant script reads input, validates it, decides a label, and prints output, it is difficult to locate a failure or reuse one piece safely.",
        "A **function** is a reusable named block. A **parameter** is a name in the function definition. An **argument** is the value supplied when calling it. `return` sends a result back. A **contract** describes accepted inputs, produced outputs, and failure behavior. **Scope** describes where a name exists.",
        """Define the smallest function:

```python
def add_one(number):
    return number + 1

result = add_one(4)
print(result)
```

The `def` line creates the function. `number` is a parameter. The indented body adds one. `return` sends 5 back to the caller. The function does not print by itself; the caller decides what to do with the result.

A parameter can have a default:

```python
def label_source(source="unknown"):
    return source.strip().casefold()

print(label_source())
print(label_source(" Training-Auth "))
```

The first call uses the default. The second supplies an argument. Defaults are useful only when “missing” really has a documented meaning.

Write a function that validates a range:

```python
def validate_severity(value):
    if not isinstance(value, int):
        raise TypeError("severity must be an integer")
    if not 0 <= value <= 10:
        raise ValueError("severity must be between 0 and 10")
    return value
```

This function has a contract. It accepts an integer in the range 0–10 and returns that integer. It raises `TypeError` when the type is wrong and `ValueError` when the type is right but the value is outside the allowed range.

Why distinguish those errors? Because they describe different repairs. A type error may mean the caller forgot to convert input. A value error may mean the caller supplied a number outside policy. A user-facing program may display the same safe message, but a developer needs the distinction while debugging.

A function can call another function:

```python
def parse_severity(text):
    value = int(text.strip())
    return validate_severity(value)
```

The parser converts representation. The validator checks the internal value. Keeping those jobs separate makes each one easier to test.

Scope surprises beginners:

```python
def create_label():
    label = "review"
    return label

result = create_label()
print(result)
```

The name `label` exists inside the function. The caller can use `result` because the function returned the value. A name created inside the function is not automatically available outside it.

Avoid hidden side effects when possible:

```python
def format_summary(source, severity):
    return f"source={source} severity={severity}"
```

This function returns text and does not write a file, contact a network, or modify a global list. Pure or mostly pure functions are easier to test because the same inputs produce the same result.

A function contract should state edge cases. For `parse_severity`, decide what empty text means, whether spaces are accepted, and whether a plus sign such as `+7` is allowed. Python will have behavior even when you have not written a policy; your job is to decide whether that behavior matches the program's purpose.""",
        """Trace:

```python
def parse_severity(text):
    cleaned = text.strip()
    value = int(cleaned)
    if not 0 <= value <= 10:
        raise ValueError("outside range")
    return value

answer = parse_severity(" 7 ")
print(answer)
```

| Step | Event | State |
| ---: | --- | --- |
| 1 | Define function | Python stores the function definition. |
| 2 | Call with `" 7 "` | `text` refers to the raw string. |
| 3 | `strip()` | `cleaned` becomes `"7"`. |
| 4 | `int()` | `value` becomes `7`. |
| 5 | Range check | `7` is accepted. |
| 6 | `return value` | caller receives `7` as `answer`. |

If the call is `parse_severity("high")`, the function stops at `int(cleaned)` and never reaches the range check. If the call is `parse_severity("99")`, conversion succeeds but the range check raises `ValueError`.""",
        """| Mistake | Symptom | Repair |
| --- | --- | --- |
| Function prints instead of returning | Caller cannot reuse the value. | Return the result and print at the boundary. |
| No contract | Different callers assume different behavior. | State types, ranges, and failures. |
| One giant function | Errors are hard to isolate. | Separate parsing, validation, decision, and output. |
| Hidden global state | Calls affect one another. | Pass inputs explicitly. |
| Catching errors inside the validator | The caller cannot distinguish failure. | Raise expected exceptions or return a documented result. |""",
        """Write three functions in order. First, `parse_severity(text)` converts text. Second, `validate_severity(value)` checks type and range. Third, `format_summary(source, severity)` returns a labelled string.

Test each function independently before composing them. Use one valid value, one malformed value, one out-of-range value, and one missing or empty value. For every failure, write which function should own the failure and why.""",
        """Functions are useful in security engineering because they let you place controls at explicit boundaries. A parser can refuse malformed text. A validator can enforce a finite range. A formatter can avoid printing secrets. A classifier can return `unknown` instead of making a verdict.

A function contract is not authorization. A perfectly tested function can still be used against a system without permission. Keep all examples local and synthetic.""",
        """1. Write `add_one` and explain parameter, argument, and return value.
2. Write a function with a default source label.
3. Implement and test `validate_severity`.
4. Separate parsing from validation.
5. Write a formatter that returns rather than prints.
6. Demonstrate a `TypeError` and a `ValueError` with different inputs.
7. Explain local scope using a small function.
8. Test empty, whitespace-only, valid, and out-of-range text.
9. Write a function contract in a comment or docstring.
10. Compose parser, validator, and formatter for a synthetic record.
11. Explain why pure functions are easier to test.
12. Safety question: explain why a safe function still needs a safe caller and authorized target.""",
        "Day 9 is complete when you can write a small function with a clear contract, explain the difference between parameters and arguments, return a result, separate conversion from validation, and test expected failures.",
        '''[1]: https://docs.python.org/3/tutorial/controlflow.html#defining-functions "Python function tutorial"
[2]: https://docs.python.org/3/library/exceptions.html "Python built-in exceptions"
[3]: https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces "Python scopes and namespaces"
[4]: https://owasp.org/www-community/attacks/Improper_Input_Validation "OWASP input validation overview"''',
    ),
    Lesson(
        10,
        "Checkpoint: Build a Safe Log-Triage Classifier",
        "Today you will combine the first nine days into one small program. This is not a leap into advanced security tooling. It is a controlled checkpoint that proves you can move from text to values, validate them, choose a label, count records, and report what happened without exposing sensitive-looking fields.",
        "A log-triage program must accept a small synthetic fixture, parse each line, classify it according to a documented rule, count outcomes, and tell the learner if processing stopped or completed. The program must be honest about malformed lines and bounded in its work.",
        "A **fixture** is a supplied test input. A **pipeline** is a sequence of transformations. **Triage** is prioritizing items for review, not declaring guilt. A **summary** is a compact report. **Completeness** says whether all permitted input was processed.",
        """Start with a fixture represented as a list of strings:

```python
lines = [
    "severity=8 source=training-auth event=login_failed",
    "severity=2 source=training-auth event=logout",
    "severity=high source=training-auth event=login_failed",
]
```

This is not a real log and it does not come from a network. It is a small, visible input. Begin with one line and split it:

```python
line = lines[0]
fields = {}
for part in line.split():
    key, value = part.split("=", 1)
    fields[key] = value

print(fields)
```

Expected output is a dictionary containing three text fields. Notice that the severity is still text. Pass it through the parser from Day 9:

```python
severity = parse_severity(fields["severity"])
```

The third line contains `severity=high`, so the parser will raise an expected conversion error. A checkpoint program should not crash the whole report because one synthetic line is malformed. Decide on a policy: count the line as `invalid`, record a safe reason, and continue.

A small classification function might look like this:

```python
def classify(severity_text, source):
    try:
        severity = parse_severity(severity_text)
    except (TypeError, ValueError):
        return "invalid"

    if source != "training-auth":
        return "unknown-source"
    if severity >= 7:
        return "review"
    return "routine"
```

This function does not print, access files, or contact a network. It receives values and returns one label. The caller can count the labels and decide how to report them.

Build a counter:

```python
counts = {"review": 0, "routine": 0, "invalid": 0, "unknown-source": 0}
label = classify("8", "training-auth")
counts[label] += 1
print(counts)
```

The dictionary contains every expected label before processing starts. That means a zero count is visible in the final report. A report that omits zero categories can be harder to compare across runs.

Add a bounded loop:

```python
limit = 100
processed = 0

for line in lines:
    if processed >= limit:
        break
    processed += 1
    print(f"processing line {processed}")
```

The limit is much larger than this fixture, but it demonstrates the policy. A real tool should also bound line length, total bytes, and output size.

A complete checkpoint design has stages:

| Stage | Question |
| --- | --- |
| Read | Which fixture is permitted? |
| Parse | Can this line become fields? |
| Convert | Can severity become an integer? |
| Validate | Is severity within 0–10? |
| Classify | Which documented label applies? |
| Count | How many labels occurred? |
| Report | What happened, and was processing complete? |

Do not hide all stages in one enormous function. Give each stage a small job and test it with a tiny input before composing the pipeline.

The final report might look like:

```text
source=synthetic-fixture
processed=3
complete=True
review=1
routine=1
invalid=1
unknown-source=0
```

The report says what the classifier did. It does not say that a real attack happened or that any person is dangerous.""",
        """Trace the three-line fixture:

| Line | Raw severity | Source | Result | Count change |
| ---: | --- | --- | --- | --- |
| 1 | `8` | `training-auth` | `review` | review +1 |
| 2 | `2` | `training-auth` | `routine` | routine +1 |
| 3 | `high` | `training-auth` | `invalid` | invalid +1 |

After the loop, `processed` is 3 and `complete` is true because the fixture ended before the limit. If the fixture contains 150 lines and the limit is 100, `complete` must be false. Do not report that the entire source was clean when only the first 100 permitted records were processed.""",
        """| Mistake | Symptom | Repair |
| --- | --- | --- |
| One malformed line crashes all processing | The report is incomplete without saying why. | Catch expected input errors per line. |
| Invalid becomes routine | Bad data receives a reassuring label. | Keep `invalid` separate. |
| No processing limit | Work grows with untrusted input. | Bound records and bytes. |
| Print raw lines | Sensitive fields may leak. | Report line number and safe reason. |
| Count only positive labels | Zero categories disappear. | Initialize every expected category. |
| Classifier claims an attack | A rule becomes an accusation. | Say `review` or `needs-review`. |""",
        """Build the project in seven checkpoints:

1. Create a three-line in-memory fixture.
2. Write a parser for space-separated `key=value` fields.
3. Test the parser with one missing equals sign and one extra equals sign.
4. Reuse a bounded severity parser.
5. Write a classifier with `review`, `routine`, `invalid`, and `unknown-source` outcomes.
6. Process the fixture with a finite record limit and count every outcome.
7. Print a safe summary containing source label, counts, processed count, and completeness.

At each checkpoint, run the smallest test possible. Keep raw lines out of the final report. If you need to debug a line, use a synthetic fixture and print only a redacted representation.""",
        """This checkpoint demonstrates defensive programming habits rather than offensive capability. The input is synthetic. The work is finite. The parser and validator are explicit. Invalid data is not silently treated as safe. The report distinguishes review from routine and does not identify a person or contact a target.

A real log-triage system would need authenticated collection, schema versioning, time handling, access control, retention, tests against realistic formats, and human review. This checkpoint teaches only the small programming foundation required before those topics.""",
        """1. Run the starter and explain each printed field.
2. Parse one valid fixture line into a dictionary.
3. Parse a line with an extra equals sign using `split("=", 1)`.
4. Handle a line without an equals sign as invalid.
5. Reuse `parse_severity` and classify valid and invalid severities.
6. Add a known-source and unknown-source fixture.
7. Count each result category, including categories with zero results.
8. Add a processing limit and a `complete` field.
9. Write a safe summary that never prints a raw line.
10. Add tests for empty input, malformed input, valid high severity, and a source mismatch.
11. Explain why a `review` label is not an attack verdict.
12. Explain how a bounded loop protects resources but may reduce completeness.
13. Write a short threat model listing asset, input, trust boundary, and residual risk.
14. Safety question: state exactly what this project is allowed to read and what it is forbidden to touch.

Use [hints](practice/hints.md) before [solutions](practice/solutions.md), and write a short explanation beside every code change.""",
        "Day 10 is complete when you can explain the pipeline from fixture to report, process valid and invalid lines without losing the distinction, enforce a finite limit, test edge cases, and state the safety boundary without being prompted.",
        '''[1]: https://docs.python.org/3/tutorial/datastructures.html "Python data structures"
[2]: https://docs.python.org/3/tutorial/controlflow.html "Python control flow"
[3]: https://docs.python.org/3/library/exceptions.html "Python exceptions"
[4]: https://csrc.nist.gov/glossary/term/log_analysis "NIST log analysis glossary"
[5]: https://owasp.org/www-community/attacks/Denial_of_Service "OWASP denial of service overview"''',
    ),
]


def main() -> int:
    for lesson in LESSONS:
        path = ROOT / DIRS[lesson.day] / f"{DIRS[lesson.day]}.md"
        path.write_text(render(lesson), encoding="utf-8")
    print("Authored beginner-first teaching chapters for Days 3–10.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
