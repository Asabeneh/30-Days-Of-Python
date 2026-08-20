# Day 3: Types, Conversion, and Parsing Boundaries

[← Day 2](../day_02_values_names_and_input/day_02_values_names_and_input.md) · [Day index](../DAY_INDEX.md) · [Day 4 →](../day_04_operators_and_decisions/day_04_operators_and_decisions.md)





## Table of contents

- [Welcome](#welcome)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Vocabulary](#vocabulary)
- [Lesson](#lesson)
- [1. Read a value's type before choosing an operation](#1-read-a-values-type-before-choosing-an-operation)
- [2. Convert first, validate second](#2-convert-first-validate-second)
- [3. Boolean conversion is not language understanding](#3-boolean-conversion-is-not-language-understanding)
- [4. Missing, malformed, and out-of-range are different](#4-missing-malformed-and-out-of-range-are-different)
- [Worked examples](#worked-examples)
  - [Example 1: A first runnable case](#example-1-a-first-runnable-case)
  - [Example 2: A boundary case](#example-2-a-boundary-case)
  - [Example 3: A deliberate experiment](#example-3-a-deliberate-experiment)
  - [Example 4: A bounded security fixture](#example-4-a-bounded-security-fixture)
  - [Example 5: A valid conversion can still fail policy](#example-5-a-valid-conversion-can-still-fail-policy)
- [Execution trace](#execution-trace)
- [Common mistakes and repairs](#common-mistakes-and-repairs)
- [Guided practice](#guided-practice)
- [Security application](#security-application)
- [Independent exercises](#independent-exercises)
- [Finish line](#finish-line)
- [References](#references)

## Welcome

Yesterday you stored values under names and learned that keyboard input begins as text. Today you will learn how to distinguish kinds of values and how to convert text deliberately. A parser is a small translator: it takes an outside representation and turns it into an internal value the program can reason about.

This lesson is designed for a learner who may still need to look up how to create a file, run it, or read an error. Type the examples instead of reading them passively. Before running an experiment, write down what you expect. The difference between your prediction and Python's output is where learning happens.

## Prerequisites

Complete Day 2. Use the repository's local synthetic fixtures only. Keep a terminal open at the repository root and run each file with the Python command that worked on your computer.

## Outcomes

By the end of this lesson, you should be able to explain the new vocabulary in your own words, run and modify the examples, predict at least one boundary case, repair a deliberate mistake, and apply the idea to a bounded cybersecurity fixture.

## The problem

A log line may contain `severity=7`, but the characters `7` are not automatically the integer 7. If you add the wrong value, compare the wrong type, or silently treat malformed text as valid, a security tool can make a bad decision. The solution is to inspect, convert, validate, and reject clearly.

## Security boundary

This lesson is educational and local. It does not authorize public scanning, credential use, data collection, exploitation, interception, or changes to systems you do not own. The cybersecurity examples use invented names, loopback targets, or repository fixtures.

## Vocabulary

A **type** describes what kind of value Python is holding. A `str` is text, an `int` is a whole number, a `float` is a decimal number, a `bool` is `True` or `False`, and `None` represents the deliberate absence of a value. **Conversion** asks Python to create a value of another type. **Parsing** is the wider job of interpreting a representation according to rules. **Validation** checks whether the interpreted value is allowed.

## Lesson

Start with inspection:

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

Do not skip straight from raw text to a security decision. Each stage gives you evidence and a place to handle failure.

## 1. Read a value's type before choosing an operation

Start with five values that look different when Python displays them:

```python
samples = ["7", 7, 7.0, True, None]
for sample in samples:
    print(repr(sample), type(sample).__name__)
```

Expected output:

```text
'7' str
7 int
7.0 float
True bool
None NoneType
```

The quotation marks around `"7"` make it text. The absence of quotation marks around `7` makes it an integer. `None` is a special value meaning that a value is deliberately absent. It is not the same as the text `"None"`.

Before you call a function such as `int`, `float`, or `str`, ask what meaning the result should have. `int("7")` creates the number seven. `str(7)` creates text containing the character seven. Conversion changes the type but does not prove that the input is honest or allowed.

## 2. Convert first, validate second

Conversion answers “Can Python interpret these characters as this type?” Validation answers “Is the resulting value allowed by this program?” Keep the questions separate:

```python
raw = "99"
severity = int(raw)
print(severity)
print(0 <= severity <= 10)
```

Output:

```text
99
False
```

The conversion succeeded. The policy check failed. If `raw` were `"high"`, conversion itself would fail with `ValueError`. These are different problems and should receive different explanations.

A safe boundary function can make the policy visible:

```python
def parse_severity(raw):
    cleaned = raw.strip()
    value = int(cleaned)
    if not 0 <= value <= 10:
        raise ValueError("severity must be between 0 and 10")
    return value
```

Do not catch an error merely to make the program look successful. Decide whether the caller should reject the record, ask again, or label the value unknown.

## 3. Boolean conversion is not language understanding

This surprising example is worth running:

```python
print(bool("false"))
print(bool(""))
print(bool(0))
print(bool(1))
```

Output:

```text
True
False
False
True
```

`bool` asks whether a value is truthy. It does not translate English words. The non-empty string `"false"` is truthy. If a program receives words, define the accepted words explicitly:

```python
def parse_yes_no(raw):
    word = raw.strip().casefold()
    if word in {"yes", "true", "1"}:
        return True
    if word in {"no", "false", "0"}:
        return False
    raise ValueError("expected an accepted yes/no value")
```

An allowlist is easier to review than a guess. It also gives malformed input a clear outcome.

## 4. Missing, malformed, and out-of-range are different

Use a small table to reason about inputs:

| Input | Conversion | Policy result |
| --- | --- | --- |
| `""` | empty text | missing or rejected, by policy |
| `"high"` | conversion fails | malformed |
| `"99"` | produces integer 99 | out of range |
| `"7"` | produces integer 7 | accepted for a 0–10 rule |

Write a prediction for each before testing. In a security tool, these distinctions help a reviewer understand whether the source was incomplete, incorrectly formatted, or simply outside the documented range. None of the categories proves malicious intent.

## Worked examples

Run the examples in order. Each one changes only a small part of the previous idea.

### Example 1: A first runnable case

Run the smallest version first and explain what each line contributes.

### Example 2: A boundary case

Change exactly one input to an empty, malformed, or out-of-range value. Predict the result before running it.

### Example 3: A deliberate experiment

Make one controlled change, record the output, and compare it with your prediction. Do not change several lines at once.

### Example 4: A bounded security fixture

Apply the idea to the synthetic fixture in this lesson. The fixture is local, finite, and invented; it is not permission to inspect real systems.

### Example 5: A valid conversion can still fail policy

```python
raw = "99"
value = int(raw)
print(value)
print(0 <= value <= 10)
```

Conversion succeeds, but the range check is false. Keep conversion errors and policy errors separate so the final report explains what happened.

## Execution trace

Trace this program:

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

Now replace `raw` with `"eleven"`. The program stops at `int(clean)`, so `allowed` is never created. If you replace it with `"99"`, conversion succeeds but `allowed` becomes `False`. Those are different failure categories: malformed representation versus a valid value outside the application's permitted range.

## Common mistakes and repairs

| Mistake | Why it happens | Repair |
| --- | --- | --- |
| Treating `"7"` as `7` | They look alike when printed. | Inspect the type and convert explicitly. |
| Using `bool("false")` as a parser | Truthiness is mistaken for language parsing. | Normalize and compare an allowlist. |
| Converting without a range check | A valid integer may still be unsafe for the application. | Validate the allowed interval. |
| Treating empty text as zero | Missing input and zero have different meanings. | Represent missing input explicitly with `None`. |
| Catching every exception | Programmer errors become invisible. | Catch only expected input errors at the boundary. |
| Printing raw input in a report | Diagnostic output may leak sensitive data. | Keep raw data local and report safe metadata. |

## Guided practice

Build a parser in checkpoints.

1. Begin with `raw = " 7 "` and print it with `repr`.
2. Create `clean` using `strip()` and print both values.
3. Convert `clean` to an integer named `severity` and print its type.
4. Add a range check for 0 through 10.
5. Test the values `0`, `10`, `-1`, `11`, and `high` one at a time.
6. For `high`, produce a safe message such as `invalid integer` rather than printing a traceback in the report.
7. Add a second parser for yes/no text. Accept only the documented words.

At each checkpoint, run the file. Do not add the next layer until you can explain the current output. If a test fails, write down whether the failure happened during cleaning, conversion, or validation.

## Security application

A synthetic log record is an ideal boundary exercise:

```python
record = {"severity": " 7 ", "authenticated": "no"}
```

The values are text because they came from an outside representation. Parse them into an internal record:

```python
severity = int(record["severity"].strip())
authenticated = parse_boolean(record["authenticated"])
```

This does not prove that the record is authentic. It only prevents the rest of the program from pretending that unparsed text is already a trusted integer or Boolean. In a real security tool, the parser would also report which field failed, limit input size, preserve provenance, and avoid including secrets in the error message.

Use only synthetic records. Do not paste a real log line into this exercise because real logs may contain usernames, tokens, addresses, or personal data.

## Independent exercises

Complete these in [`practice/exercises.md`](practice/exercises.md) in order:

1. Print the type name of `"7"`, `7`, `7.0`, `True`, and `None`.
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

Use [hints](practice/hints.md) only after attempting the question. Use [solutions](practice/solutions.md) to compare reasoning, not to replace it.

## Finish line

Day 3 is complete when you can inspect a value's type, explain why conversion and validation are separate, write a bounded parser, distinguish missing from invalid, and describe the security limitation of parsing synthetic input. You should be able to trace a failure to the exact stage where it occurred.

## References

[1]: https://docs.python.org/3/library/functions.html#type "Python type documentation"
[2]: https://docs.python.org/3/library/functions.html#int "Python int documentation"
[3]: https://docs.python.org/3/library/stdtypes.html#truth-value-testing "Python truth-value testing"
[4]: https://docs.python.org/3/tutorial/errors.html "Python errors and exceptions"
[5]: https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html "OWASP input validation guidance"

[← Day 2](../day_02_values_names_and_input/day_02_values_names_and_input.md) · [Day index](../DAY_INDEX.md) · [Day 4 →](../day_04_operators_and_decisions/day_04_operators_and_decisions.md)
