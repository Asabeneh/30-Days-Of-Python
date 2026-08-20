# Day 2: Variables, Names, Values, Input, and Output

[← Day 1](../day_01_setup_and_safe_practice/day_01_setup_and_safe_practice.md) · [Day index](../DAY_INDEX.md) · [Day 3 →](../day_03_types_and_parsing/day_03_types_and_parsing.md)





## Table of contents

- [Welcome](#welcome)
- [Before you begin](#before-you-begin)
- [What you will learn](#what-you-will-learn)
- [The problem: how does a program remember information?](#the-problem-how-does-a-program-remember-information)
- [Vocabulary](#vocabulary)
  - [Value](#value)
  - [Variable and name](#variable-and-name)
  - [Type](#type)
  - [Assignment](#assignment)
  - [Input and output](#input-and-output)
- [1. Creating variables with assignment](#1-creating-variables-with-assignment)
- [2. Naming variables correctly](#2-naming-variables-correctly)
  - [Naming rules](#naming-rules)
  - [Snake case and descriptive names](#snake-case-and-descriptive-names)
  - [Case sensitivity](#case-sensitivity)
  - [Reserved keywords](#reserved-keywords)
- [3. Python's basic data types](#3-pythons-basic-data-types)
- [4. Comments and readable code](#4-comments-and-readable-code)
- [5. Updating a variable](#5-updating-a-variable)
- [6. Reading keyboard input](#6-reading-keyboard-input)
- [7. Converting text deliberately](#7-converting-text-deliberately)
- [8. Printing useful output](#8-printing-useful-output)
- [Worked examples](#worked-examples)
  - [Example 1: A small value inventory](#example-1-a-small-value-inventory)
  - [Example 2: A naming boundary](#example-2-a-naming-boundary)
  - [Example 3: A conversion repair](#example-3-a-conversion-repair)
  - [Example 4: A safe local fixture](#example-4-a-safe-local-fixture)
  - [Example 5: Name, value, and type can disagree with your assumption](#example-5-name-value-and-type-can-disagree-with-your-assumption)
- [Execution trace](#execution-trace)
- [Common mistakes and repairs](#common-mistakes-and-repairs)
- [Guided practice](#guided-practice)
- [Security application: a safe event summary](#security-application-a-safe-event-summary)
- [Independent exercises](#independent-exercises)
- [Finish line](#finish-line)
- [References](#references)

## Welcome

A program becomes useful when it can remember information for a short time. It may remember a case identifier, a count of failed events, the name of a local fixture, or whether a check passed. Python remembers these values through **variables**.

A variable is not a mysterious box inside your computer. For now, use this simple mental model:

> A variable is a descriptive name connected to a value while the program is running.

If you write `severity = 7`, the name is `severity` and the value is `7`. Later, `print(severity)` asks Python to find the current value associated with that name.

The referenced variables tutorial uses a helpful beginner sequence: assignment first, then strings and numbers, naming rules, case sensitivity, reserved words, snake case, descriptive names, and comments.[1] This lesson follows that sequence and adds a cybersecurity habit: input is not automatically trustworthy, and output should not leak secrets.

Do not read the code passively. Type it, run it, change one value, and predict before you run again. If an error appears, copy the useful part into your notes and explain which assumption was wrong.

## Before you begin

Complete Day 1. Open a terminal at the repository root and confirm Python works:

```text
python --version
```

If your computer uses `python3`, use that command instead. Create a scratch file named `day02_notes.py`. You may rewrite this file while learning. Keep your numbered answers in `practice` so you can compare them with the lesson later.

## What you will learn

By the end of this lesson, you will be able to create variables, choose names that follow Python's rules, explain why names should be descriptive, distinguish strings, integers, floats, Booleans, and `None`, use comments without depending on them to rescue unclear code, update a stored value, read keyboard input, convert text to a number deliberately, format output with an f-string, and produce a safe summary that does not print a token-like value.

You will also understand an important boundary: assigning a value to a variable does not validate it. A variable called `trusted_source` can still contain untrusted text. A name is a label, not a guarantee.

## The problem: how does a program remember information?

Suppose a local training event has three facts:

```python
source = "training-auth"
severity = 7
review_required = True
```

The first value is text. The second is a whole number. The third is a Boolean. Python can now use each fact separately:

```python
print(source)
print(severity)
print(review_required)
```

Output:

```text
training-auth
7
True
```

Compare that with one large string:

```python
print("source=training-auth severity=7 review_required=True")
```

The large string may look informative, but Python sees one piece of text. It cannot automatically treat the `7` inside that text as a number. Separate variables make a program easier to calculate, validate, test, and explain.

## Vocabulary

### Value

A **value** is one piece of data. Examples include the text `"training-auth"`, the integer `7`, and the Boolean `True`.

### Variable and name

A **variable** is a name that refers to a value while the program is running. A **name** is the identifier you type in the code. In `severity = 7`, `severity` is the name and `7` is the value.

### Type

A **type** tells Python what kind of value it is handling. A string is text, an integer is a whole number, a float may contain a decimal point, a Boolean is `True` or `False`, and `None` represents an intentional absence of a value.

### Assignment

**Assignment** gives a name a value. Python uses the single equals sign `=` for assignment. Read `severity = 7` as “store 7 under the name severity,” not as a mathematical equality question.

### Input and output

**Input** is information entering a program. It may come from a keyboard, file, command-line argument, or network. **Output** is information the program sends to the terminal, a file, or another program. Input is not automatically trustworthy, and output should be deliberate.

## 1. Creating variables with assignment

Start with the smallest example:

```python
case_id = "training-001"
print(case_id)
```

Output:

```text
training-001
```

Python evaluates the value on the right, stores it under the name on the left, and then `print` retrieves the current value. The quotation marks tell Python that `training-001` is text.

Now store several values:

```python
case_id = "training-001"
severity = 7
review_required = True

print(case_id)
print(severity)
print(review_required)
```

Output:

```text
training-001
7
True
```

Change only `severity` to `4` and run the file again. The case identifier and Boolean stay the same, while the second output line changes. This is the first important mental model: a name gives you a way to refer to the current value again.

## 2. Naming variables correctly

### Naming rules

Python names may begin with a letter or an underscore. They may contain letters, numbers, and underscores after the first character. They cannot contain spaces or begin with a number. Python names are case-sensitive, so `severity`, `Severity`, and `SEVERITY` are three different names.[1]

Valid examples:

```python
case_id = "training-001"
record2 = "second"
_private_note = "local only"
```

Invalid examples:

```python
# 2records = 2       # cannot begin with a number
# case id = "x"      # spaces are not allowed
# case-id = "x"      # hyphen is interpreted as subtraction
```

Try one invalid example in a scratch file, not in your main exercise. Python will report a `SyntaxError`. That means Python could not understand the structure of the source code before it began running it.

### Snake case and descriptive names

Python code commonly uses **snake_case**: lowercase words joined by underscores. Prefer `failed_login_count` over `flc` or `x`:

```python
failed_login_count = 3
print(failed_login_count)
```

A descriptive name communicates purpose to your future self, your classmates, and a reviewer. Good names do not make a value trustworthy, but they make incorrect assumptions easier to notice.

Avoid single-letter names except for very small, conventional cases. `source` tells you much more than `s`. `maximum_records` tells you more than `m`.

### Case sensitivity

Run this:

```python
age = 18
Age = 21
print(age)
print(Age)
```

Output:

```text
18
21
```

Changing capitalization changes the name. This is useful when it is intentional and confusing when it is accidental. Choose one spelling and keep it consistent.

### Reserved keywords

Python reserves words such as `if`, `else`, `for`, `class`, and `def` for the language. Do not use them as variable names:

```python
# class = "training"  # SyntaxError
```

When you need a related name, choose something descriptive such as `class_name` or `if_result`.

## 3. Python's basic data types

Run this inspection program:

```python
text_seven = "7"
number_seven = 7
float_seven = 7.0
truth_value = True
missing_value = None

values = [text_seven, number_seven, float_seven, truth_value, missing_value]
for value in values:
    print(repr(value), type(value).__name__)
```

Output:

```text
'7' str
7 int
7.0 float
True bool
None NoneType
```

The quotation marks are visible around `'7'` because `repr` displays a debugging representation. The string `"7"` and integer `7` look similar to a human but behave differently:

```python
print("7" + "1")
print(7 + 1)
```

Output:

```text
71
8
```

The first line joins two pieces of text. The second performs arithmetic. If you try `print("7" + 1)`, Python raises a `TypeError` because it refuses to guess whether you wanted text or arithmetic.

Repair according to your intention:

```python
print("7" + str(1))
print(int("7") + 1)
```

The first output is `71`; the second is `8`. The correct conversion depends on the meaning of the data.

## 4. Comments and readable code

A comment begins with `#`. Python ignores the comment while running the program:

```python
# This is a local synthetic training value.
case_id = "training-001"
print(case_id)
```

Comments can explain why a choice exists, record a lab boundary, or leave a learning note. They should not be used to explain a name that could have been clearer. Prefer `maximum_records` over `m  # maximum records`.

A comment cannot change authorization. Writing `# safe to scan` does not make a real target safe or authorized. Keep the boundary in the code's input fixtures, permissions, and documented scope.

## 5. Updating a variable

The right side is evaluated before the assignment is stored:

```python
count = 0
print(count)
count = count + 1
print(count)
count += 1
print(count)
```

Output:

```text
0
1
2
```

Read `count = count + 1` as four steps: find the current value, add one, create the new value, and store it under the same name. The shorter `count += 1` means the same thing.

This pattern is common for a bounded processor, but a counter alone does not create a bound. A safe program also checks the counter against a maximum and stops when the maximum is reached.

## 6. Reading keyboard input

Create `ask_severity.py`:

```python
raw = input("Severity from 0 to 10: ")
print(repr(raw), type(raw).__name__)
```

When you type `7`, the output resembles:

```text
Severity from 0 to 10: 7
'7' str
```

`input()` returns text. Even if the user types digits, the result starts as a string. This is a boundary between the outside world and your program.

## 7. Converting text deliberately

Convert the text only when the program's meaning requires a number:

```python
raw = "7"
severity = int(raw)
print(severity + 1)
```

Output:

```text
8
```

If `raw` is `"high"`, `int(raw)` raises `ValueError`. That error says the representation cannot be interpreted as an integer. If `raw` is `"99"`, conversion succeeds, but a severity policy of 0 through 10 should still reject it. Conversion and validation are separate steps.

A bounded version is:

```python
raw = "7"
severity = int(raw)

if 0 <= severity <= 10:
    print(f"accepted severity={severity}")
else:
    print("rejected: outside the allowed range")
```

Day 3 will study conversion and validation more deeply. Today remember: a type tells Python what a value is, while a validation rule tells your program whether that value is allowed here.

## 8. Printing useful output

An f-string places current values inside readable text:

```python
case_id = "training-001"
severity = 7
review_required = True
print(f"case={case_id} severity={severity} review_required={review_required}")
```

Output:

```text
case=training-001 severity=7 review_required=True
```

Compare it with:

```python
print("case_id=case_id")
```

The second line prints the literal words because there is no `f` and no expression inside braces.

For a token-like value, report presence without printing the value:

```python
training_token = "synthetic-do-not-use"
print(f"token_present={bool(training_token)}")
```

Output:

```text
token_present=True
```

This is a safer display choice, not a complete secret-management system.

## Worked examples

### Example 1: A small value inventory

```python
source = "training-auth"
severity = 7
active = True
print(source, type(source).__name__)
print(severity, type(severity).__name__)
print(active, type(active).__name__)
```

The output identifies both the value and its type. Run it unchanged before editing it.

### Example 2: A naming boundary

Change `severity` to `Severity`. Predict what happens when the original `severity` is printed. Python treats the names as different, so the original name may produce `NameError` if it was never assigned.

### Example 3: A conversion repair

Broken code:

```python
raw_limit = "10"
print(raw_limit + 1)
```

Repair it as arithmetic:

```python
limit = int(raw_limit)
print(limit + 1)
```

Or repair it as text construction:

```python
print(raw_limit + " records")
```

### Example 4: A safe local fixture

```python
record = {
    "source": "training-auth",
    "severity": 7,
    "authenticated": False,
    "token": "synthetic-do-not-use",
}

print(
    f"source={record['source']} "
    f"severity={record['severity']} "
    f"authenticated={record['authenticated']} "
    f"token_present={bool(record['token'])}"
)
```

The output contains labels and safe values but not the token-like string.

### Example 5: Name, value, and type can disagree with your assumption

```python
severity = "7"
print(repr(severity), type(severity).__name__)
severity = int(severity)
print(repr(severity), type(severity).__name__)
```

The first output describes text. The second describes an integer. The name stayed the same, but the value and type changed. A name does not guarantee what it contains; inspect and validate at the boundary.

## Execution trace

Trace this program:

```python
raw = " 7 "
clean = raw.strip()
severity = int(clean)
report = f"severity={severity}"
print(report)
```

| Step | Instruction | Current result |
| ---: | --- | --- |
| 1 | assign `raw` | string containing spaces and `7` |
| 2 | call `raw.strip()` | string `"7"` |
| 3 | call `int(clean)` | integer `7` |
| 4 | build the f-string | `"severity=7"` |
| 5 | print the report | one safe output line |

If `raw` becomes `"high"`, Step 3 raises `ValueError`; Steps 4 and 5 never run. If `raw` becomes `"99"`, Step 3 succeeds, so the program still needs a range check before calling the value acceptable.

## Common mistakes and repairs

| Mistake | What Python sees | Repair |
| --- | --- | --- |
| `2case = "x"` | A name cannot begin with a number | Use `case2` or `case_number_two` |
| `case id = "x"` | Spaces split the statement | Use `case_id` |
| `severity = "7"` followed by `severity + 1` | Text is being used as a number | Convert with `int` if arithmetic is intended |
| `bool("false")` | A non-empty string is truthy | Parse accepted words explicitly later |
| `print("severity=severity")` | All characters are literal text | Use `print(f"severity={severity}")` |
| `count += 1` before initialization | The name does not exist yet | Start with `count = 0` |
| Printing `token` in a debug line | A sensitive-looking value may leak | Print a presence flag or redacted value |
| Calling a variable `class` or `for` | The name is reserved by Python | Choose a related descriptive name |

## Guided practice

Create `guided_event.py` and complete these checkpoints in order.

1. Store `source = "training-auth"`, `severity = 7`, and `authenticated = False`.
2. Print each value with `repr` and its type name.
3. Create `case_id = "training-002"` and print one f-string containing all four safe fields.
4. Create `token = "synthetic-do-not-use"`, but print only `token_present`.
5. Change `severity` to the string `"7"`. Run the program and explain whether the output changed or an error occurred.
6. Decide whether severity is text or a number. If arithmetic is intended, convert it with `int` before adding or comparing.
7. Ask for a maximum number of records with `input`, convert it, and reject numbers below 1 or above 100.

Before every run, predict the output. Keep the original token-like text out of the final report.

## Security application: a safe event summary

Use only this synthetic record:

```python
record = {
    "source": "training-auth",
    "severity": 7,
    "authenticated": False,
    "token": "synthetic-do-not-use",
}
```

The asset is the local fixture. The input is the dictionary supplied by the exercise. The trust boundary is the Python program reading that input. Authorization is limited to working inside this repository. Expected evidence is one local summary line. Cleanup means removing temporary output when the exercise ends. Residual risk remains because the record is invented and the program does not prove authenticity, maliciousness, or compromise.

Build this safe summary:

```python
summary = (
    f"source={record['source']} "
    f"severity={record['severity']} "
    f"authenticated={record['authenticated']} "
    f"token_present={bool(record['token'])}"
)
print(summary)
```

The program demonstrates organization and safe display. It does not authorize connecting to a real host, collecting a real log, or storing a real credential. A variable named `source` is not proof that the source is genuine.

## Independent exercises

Complete the numbered questions in [`practice/exercises.md`](practice/exercises.md) in order. Use hints only after a genuine attempt and solutions only to compare your reasoning.

1. Create a value inventory containing a string, integer, float, Boolean, and `None`. Print each value and its type name.
2. Assign `count = 0`, update it twice, and explain why `count = count + 1` is valid Python.
3. Print a case identifier as plain text and inside an f-string. Explain the difference.
4. Repair a program that tries to add the string `"7"` to the integer `1` in two different ways.
5. Use `input()` to read a severity and prove that the result begins as a string.
6. Convert the input to an integer and record the useful error line produced by `high`.
7. Add a range check for 0 through 10 and test the two boundaries plus one invalid value on each side.
8. Demonstrate case sensitivity with `severity` and `Severity`.
9. Write a safe summary for a synthetic record that reports `token_present` without printing the token.
10. Ask for a maximum record count and accept only integers from 1 through 100.
11. Create a deliberate `NameError` by printing a name before assigning it, then repair it.
12. Define value, variable, type, assignment, input, and output in your own words.
13. Explain why a value that looks like a number is not automatically safe or valid.
14. Safety question: list three kinds of information that must not be entered into today's files and explain why local synthetic fixtures are used.

## Finish line

Day 2 is complete when you can explain a value, variable, type, name, assignment, input, and output; follow Python naming rules; predict the behavior of string and integer values; convert keyboard text deliberately; bound a numeric input; and produce a summary that does not reveal a token-like value.

## References

[1]: https://www.freecodecamp.org/learn/python-v9/lecture-understanding-variables-and-data-types/how-do-you-declare-variables-and-what-are-naming-conventions-to-name-variables "Python variables and naming conventions"
[2]: https://docs.python.org/3/tutorial/introduction.html "Python tutorial introduction"
[3]: https://docs.python.org/3/library/functions.html#input "Python input documentation"
[4]: https://docs.python.org/3/library/functions.html#type "Python type documentation"
[5]: https://docs.python.org/3/library/functions.html#int "Python int documentation"
[6]: https://owasp.org/www-community/attacks/Improper_Error_Handling "OWASP error handling guidance"

[← Day 1](../day_01_setup_and_safe_practice/day_01_setup_and_safe_practice.md) · [Day index](../DAY_INDEX.md) · [Day 3 →](../day_03_types_and_parsing/day_03_types_and_parsing.md)
