# Day 2: Values, Names, Input, and Output

[← Day 1](../day_01_setup_and_safe_practice/day_01_setup_and_safe_practice.md) · [Day index](../DAY_INDEX.md) · [Day 3 →](../day_03_types_and_parsing/day_03_types_and_parsing.md)

## Welcome

Yesterday you learned how to open a terminal, create a Python file, run it, and read the difference between a successful program and a program that reports an error. Today you will learn how programs remember information while they are running.

A cybersecurity program constantly handles information. It may read the name of a log file, count failed logins, remember whether a check passed, or ask the operator for a limit. If the program cannot keep those pieces of information separate, its output becomes confusing and its decisions become unsafe.

This lesson is written for someone who has never programmed before. Do not rush through it. Type each example into a file, run it, compare your output with the expected output, and answer the prediction questions before looking at the explanation. A useful first session is approximately 60–90 minutes.

By the end, you should be able to explain what a **value**, **type**, **name**, **assignment**, **input**, and **output** are. You should also be able to convert text into a number deliberately, recognize a conversion error, format a useful message, and avoid printing sensitive-looking values.

## What you need before starting

You need the environment from Day 1 and a terminal opened at the repository root. Confirm that Python works:

```text
python --version
```

You should see Python 3.11 or a newer compatible Python 3 version. If your computer uses `python3` instead of `python`, use `python3` in every command below. The command name is not the important idea; running the correct Python interpreter is.

Create a scratch file named `day_02_notes.py` inside a temporary practice directory. You may write over this file while learning. Keep the lesson examples separate from your submitted exercise answers so you can compare them later.

## The problem: how can a program remember anything?

Imagine a person says, “The event came from the login system, its severity is 7, and it needs review.” A human listener can keep those three details in mind for a moment. A program cannot rely on human memory. It needs a way to store each detail and refer to it later.

A first attempt might be one long sentence:

```python
print("source=training-auth severity=7 review_required=True")
```

This prints a useful sentence, but Python does not know that `7` is a number or that `True` represents a yes/no condition. Everything inside the quotation marks is text. If you later want to add 1 to the severity, Python cannot do arithmetic with the entire sentence.

A better program stores the pieces separately:

```python
source = "training-auth"
severity = 7
review_required = True

print(source)
print(severity)
print(review_required)
```

The output is:

```text
training-auth
7
True
```

The important change is not the three `print` calls. The important change is that the program now has three named pieces of information that it can use independently.

## Vocabulary: six words you will use constantly

### Value

A **value** is one piece of data that a program can work with. In the example above, `"training-auth"`, `7`, and `True` are values. The quotation marks are part of Python’s way of writing a text value; they are not printed as part of the text when you use `print`.

### Type

A **type** tells Python what kind of value it is handling. A string is text. An integer is a whole number. A float is a number that may contain a decimal point. A Boolean is either `True` or `False`.

Types matter because different kinds of values support different operations. Adding two integers is arithmetic. Joining two strings is text construction. Python does not assume that values that look similar should behave the same way.

### Name

A **name** is the word a program uses to refer to a value later. In `severity = 7`, the name is `severity` and the value is `7`. A name is not the value itself. It is a label that lets the program find the value while the program is running.

### Assignment

**Assignment** means giving a name a value. The equals sign in Python, `=`, is the assignment operator. It does not mean that two mathematical quantities are being compared. Read this line as “store the value 7 under the name severity”:

```python
severity = 7
```

### Input

**Input** is information that enters a program. It can come from a keyboard, a file, a command-line argument, a network connection, or another program. Input is not automatically trustworthy. A later lesson will teach more validation, but today you will learn the first important boundary: keyboard input begins as text.

### Output

**Output** is information a program sends out. `print()` sends text to the terminal. A file write creates output in a file. A network response is output to another program. Output should be deliberate because a careless diagnostic print can reveal a password, token, private filename, or sensitive log line.

## Worked examples

### Example 1: Start with the smallest case

Run the first example exactly as written and explain the input, operation, and output.

### Example 2: Change one boundary

Change one value to an empty, malformed, or maximum-size case. Predict before running.

### Example 3: Repair a controlled mistake

Break one line deliberately, record the error, and repair only that line.

### Example 4: Apply the idea to a safe fixture

Use only the local synthetic fixture and explain what the result does and does not prove.

The examples in this section are deliberately small. Run each one before moving to the next. The explanations are part of the lesson, not optional commentary.

### First teaching example: giving values names

Create `day_02_notes.py` with this exact content:

```python
source = "training-auth"
severity = 7
review_required = True

print(source)
print(severity)
print(review_required)
```

Run it:

```text
python day_02_notes.py
```

Expected output:

```text
training-auth
7
True
```

Read the program from top to bottom. The first line creates the text value `"training-auth"` and assigns it to `source`. The second line creates the whole-number value `7` and assigns it to `severity`. The third line creates the Boolean value `True` and assigns it to `review_required`.

The blank line has no effect on the values. It is there for a human reader. The first `print(source)` asks Python to find the current value attached to `source` and display it. The next two lines do the same for the other names.

Now change only the severity:

```python
severity = 4
```

Run the file again. The first and third lines should stay the same, while the second printed line should become `4`. This is the first useful mental model:

> A name is a label whose current value can be used again later.

### Assignment is not a mathematical equation

Beginners often read this line as if it were algebra:

```python
count = count + 1
```

In mathematics, that would look impossible because no number is equal to itself plus one. In Python, the right side is evaluated first. Python reads the current value of `count`, adds 1, and stores the new result back under the same name.

Type this:

```python
count = 0
print(count)

count = count + 1
print(count)

count = count + 1
print(count)
```

Expected output:

```text
0
1
2
```

Trace the values:

| Line | Instruction | Value of `count` after the line |
| ---: | --- | ---: |
| 1 | Store `0` in `count` | 0 |
| 2 | Print the current value | 0 |
| 4 | Read 0, add 1, store 1 | 1 |
| 5 | Print the current value | 1 |
| 7 | Read 1, add 1, store 2 | 2 |
| 8 | Print the current value | 2 |

The name `count` did not create three different counters. It referred to one changing value. This pattern appears in event counters, retry counters, processed-record counters, and loop counters.

Python also provides the shorter form `count += 1`. It means the same thing as `count = count + 1`:

```python
count = 0
count += 1
print(count)
```

Expected output:

```text
1
```

Learn the longer form first. Once it makes sense, the shorter form becomes a convenience rather than a mysterious symbol.

### Types: values that look alike may behave differently

Run this program:

```python
text_seven = "7"
number_seven = 7
float_seven = 7.0
truth_value = True

print(repr(text_seven), type(text_seven).__name__)
print(repr(number_seven), type(number_seven).__name__)
print(repr(float_seven), type(float_seven).__name__)
print(repr(truth_value), type(truth_value).__name__)
```

Expected output:

```text
'7' str
7 int
7.0 float
True bool
```

Two built-in tools appear here. `type(value)` asks Python what type a value has. The `__name__` part extracts the readable name of that type. `repr(value)` shows a debugging representation, so the quotation marks around the string become visible.

The four values are different:

| Written value | Type | Meaning |
| --- | --- | --- |
| `"7"` | `str` | Two text characters: a 7. |
| `7` | `int` | The whole number seven. |
| `7.0` | `float` | A decimal-number representation of seven. |
| `True` | `bool` | A yes/no truth value. |

Try these expressions one at a time:

```python
print("7" + "1")
print(7 + 1)
print(7.0 + 1.0)
```

Expected output:

```text
71
8
8.0
```

The first line joins text. It does not perform arithmetic. The second and third lines perform numeric addition. If you try this, Python will stop with an error:

```python
print("7" + 1)
```

The useful part of the error will look like:

```text
TypeError: can only concatenate str (not "int") to str
```

Translate that message into ordinary language: “You asked me to join a string and an integer, but I do not know how to do that automatically.” The error is not Python being difficult. It is Python refusing to guess whether you wanted `"71"` or `8`.

Two safe repairs are possible, depending on your intention:

```python
# If you meant text construction:
print("7" + str(1))

# If you meant arithmetic:
print(int("7") + 1)
```

The first repair converts the integer to text and produces `71`. The second converts text to an integer and produces `8`. The correct repair comes from the meaning you want, not from a rule that says “always use `str`” or “always use `int`.”

### Input: the keyboard gives you text

Create a new file named `ask_severity.py`:

```python
raw = input("Severity from 0 to 10: ")
print(repr(raw), type(raw).__name__)
```

Run it:

```text
python ask_severity.py
```

When the prompt appears, type `7` and press Enter. The output should resemble:

```text
Severity from 0 to 10: 7
'7' str
```

The `7` you typed looks like a number to a human, but the keyboard supplied characters. The `input()` function returns a string. That is why `type(raw).__name__` reports `str`.

To perform arithmetic, convert the text:

```python
raw = input("Severity from 0 to 10: ")
severity = int(raw)
print(severity + 1)
```

If you type `7`, the output is `8`. If you type `high`, Python raises `ValueError` because the text cannot be interpreted as an integer:

```text
ValueError: invalid literal for int() with base 10: 'high'
```

The phrase “invalid literal” means that the text is not a valid written form for the conversion you requested. The conversion step is useful, but it is not a complete input policy. A value such as `99` can be a valid integer and still be outside a severity range of 0 through 10. Later lessons will separate conversion, validation, and error handling more carefully.

A first bounded version looks like this:

```python
raw = input("Severity from 0 to 10: ")
severity = int(raw)

if 0 <= severity <= 10:
    print(f"accepted severity={severity}")
else:
    print("rejected: severity is outside 0 through 10")
```

The new word `if` introduces a decision, which Day 5 will teach properly. For now, read it as “run the indented block only when this condition is true.” The expression `0 <= severity <= 10` asks whether severity is at least 0 and at most 10.

### Formatting output so a human can read it

Printing separate values is useful while learning, but a tool usually needs a labeled line. Python’s f-string syntax lets you place values inside text:

```python
case_id = "training-002"
severity = 7
review_required = True

print(f"case={case_id} severity={severity} review_required={review_required}")
```

Expected output:

```text
case=training-002 severity=7 review_required=True
```

The letter `f` before the opening quotation mark tells Python that expressions inside braces should be replaced with their current values. The text outside braces is printed literally.

Compare these two lines:

```python
print("case_id=case_id")
print(f"case_id={case_id}")
```

The first prints the word `case_id` twice because it is all ordinary text. The second prints the value stored in the name `case_id`.

For safe diagnostics, report whether a sensitive-looking value exists without printing the value itself:

```python
api_key = "training-placeholder"

print(f"api_key_present={bool(api_key)}")
```

Expected output:

```text
api_key_present=True
```

Do not treat this as a complete secret-management solution. It is only a safer display choice for a learning exercise. A real program must also control where secrets come from, who can read them, how they are rotated, and whether logs retain them.

## Guided practice: build an event summary

Now build a small program with guidance instead of copying a finished answer. Create `guided_event.py` and complete these steps in order.

**Step 1: store three values.** Use the text value `training-auth`, the integer value `7`, and the Boolean value `False`.

**Step 2: inspect the types.** Print each value with `repr()` and `type(...).__name__` so you can see what Python believes each value is.

**Step 3: make one labeled line.** Use an f-string with the labels `source`, `severity`, and `authenticated`.

**Step 4: add a safe presence field.** Create a placeholder variable named `token` but print only `token_present`, not the token itself.

**Step 5: break one thing deliberately.** Change the severity from the integer `7` to the string `"7"`. Run the program. Does the output change? Does it fail? Explain why.

**Step 6: repair the meaning.** Decide whether the field should be text or a number. If it is a number, convert it before doing arithmetic. If it is only a label, keep it as text and do not add to it.

A possible checkpoint output is:

```text
source=training-auth severity=7 authenticated=False token_present=True
```

Your spacing may differ, but the labels and values should be understandable. If your output contains a token-like value, stop and remove it before continuing.

## Execution trace

The tables below show how Python moves from input text to a final value. Read them slowly; tracing is a skill you will use when debugging security tools.

### Two complete execution traces

### Trace A: successful conversion

Code:

```python
raw = " 7 "
clean = raw.strip()
severity = int(clean)
print(severity + 1)
```

| Step | Expression | Result | Type |
| ---: | --- | --- | --- |
| 1 | `raw = " 7 "` | three visible characters plus spaces | `str` |
| 2 | `raw.strip()` | `"7"` | `str` |
| 3 | `int("7")` | `7` | `int` |
| 4 | `severity + 1` | `8` | `int` |
| 5 | `print(...)` | writes `8` to the terminal | output |

### Trace B: failed conversion

If `raw` is `"high"`, stripping does not change it. `int("high")` cannot produce an integer, so Python raises `ValueError` at that line. The `print` call is never reached. This is an important control-flow fact: when an uncaught error occurs, Python stops executing the remaining lines in that run.

## Common mistakes and repairs

| Mistake | What Python sees | What you should do |
| --- | --- | --- |
| `severity = "7"` followed by `severity + 1` | Text is being used as a number. | Convert to `int` if arithmetic is intended. |
| `bool("false")` | A non-empty string, which is truthy. | Normalize and compare the text explicitly in a later parsing function. |
| `print("severity=severity")` | All characters are ordinary text. | Use `print(f"severity={severity}")`. |
| `print(token)` in a diagnostic | The sensitive-looking value may enter terminal history or logs. | Print only a safe presence flag or redacted form. |
| `int("7.5")` | The text is not an integer literal. | Decide whether a float is appropriate and validate the accepted format. |
| `count = count + 1` before defining `count` | Python cannot find the name. | Assign an initial value such as `count = 0` first. |
| Copying a dictionary and assuming it validates values | A dictionary stores whatever you put into it. | Validate at the input boundary. |

## Security application: safe event summaries

A log-triage tool may receive records containing fields such as `source`, `severity`, `authenticated`, and `token`. Today you are not building a parser or deciding whether a person is malicious. You are learning to keep values separate, identify their types, and produce a report that does not expose a sensitive field.

Use this synthetic record:

```python
record = {
    "source": "training-auth",
    "severity": 7,
    "authenticated": False,
    "token": "synthetic-do-not-use",
}

safe_summary = (
    f"source={record['source']} "
    f"severity={record['severity']} "
    f"authenticated={record['authenticated']} "
    f"token_present={bool(record['token'])}"
)

print(safe_summary)
```

Expected output:

```text
source=training-auth severity=7 authenticated=False token_present=True
```

Notice what this example does **not** prove. It does not prove that the record came from a trusted source. It does not prove that severity 7 has a universal meaning. It does not prove that the token is safe to possess. It only demonstrates a safer output choice: report that a value is present without printing the value.

The security boundary is deliberate: use synthetic records, keep the exercise local, and never paste a real password, API key, private log, or university system output into this file.

## Independent exercises

Complete these in order in `practice/exercises.md`. Write your prediction before running each relevant program. Use the hints only after you have made a genuine attempt.

1. Create `practice/value_inventory.py` with one string, one integer, one float, and one Boolean. Print each value and its type name. Copy the exact output into your answer.
2. Write three assignment statements for `count`: first assign `0`, then add `1`, then add `1` again. Predict the final output before running the program. Explain why `count = count + 1` is valid Python.
3. Create a variable named `event_name` containing `"login_failed"`. Print it once by itself and once inside an f-string labelled `event=`. Explain the difference between the two lines.
4. Write a program containing `left = "7"` and `right = 1`. First try `left + right` and record the exception type. Then repair the program in two ways: one that produces the text `71`, and one that produces the number `8`.
5. Ask the user for a severity with `input()`. Print the value using `repr()` and its type name. Type `7`. Is the result an `int` or a `str`? Explain why.
6. Convert the input from Question 5 to an integer. Try the input `high`. Copy the useful error line and explain what “invalid literal” means in this situation.
7. Add a range check for 0 through 10. Test `0`, `10`, `-1`, and `11`. Record which inputs are accepted and which are rejected.
8. Write a one-line f-string containing `case_id`, `severity`, and `review_required`. Change only the values, run the file again, and explain which parts of the output changed.
9. Create a synthetic record with `source`, `severity`, `authenticated`, and `token`. Print a safe summary that includes `token_present=True` or `False` but never prints the token value. Use a test or a captured output check to prove that the token value is absent.
10. Write a program that asks for a maximum number of records. Convert the input to an integer and reject values less than 1 or greater than 100. Explain why a bound is safer than accepting any integer.
11. Make a deliberate mistake by printing a name before assigning it. Copy the exception type. Then assign the name before printing it and explain the repair.
12. In your own words, define value, type, name, assignment, input, and output. Give one Python example for each word and one cybersecurity example where confusing the word could cause a problem.
13. Write a short paragraph answering this question: why is “the input looks like a number” not enough reason to trust it?
14. Safety question: list three kinds of information that must not be entered into today’s files and explain why local synthetic fixtures are used instead.

## Hints

For Question 4, `str(1)` creates text while `int("7")` creates a number. For Question 6, look at the line that calls `int`. For Question 7, compare the number with both bounds using `0 <= value <= 10`. For Question 9, use `bool(record["token"])` only to report presence. For Question 10, convert first, then compare the resulting integer with the allowed range.

## Finish line

Day 2 is complete when you can do all of the following without copying the lesson code:

1. Explain the difference between a value, a type, and a name.
2. Read `count = count + 1` as a sequence of operations rather than as an algebra equation.
3. Predict why `"7" + 1` raises an error and repair it according to the intended meaning.
4. Explain why `input()` returns a string even when the user types digits.
5. Convert and bound a numeric input.
6. Produce a labelled summary without printing a token-like value.
7. Explain one limitation of today’s synthetic security application.

If one of these is still a guess, return to the matching section, type the smallest example again, and change one value. Understanding is built by observing the program, not by memorizing a sentence.

## References

[1]: https://docs.python.org/3/library/functions.html#input "Python built-in input documentation"
[2]: https://docs.python.org/3/library/functions.html#print "Python built-in print documentation"
[3]: https://docs.python.org/3/library/functions.html#type "Python built-in type documentation"
[4]: https://docs.python.org/3/library/functions.html#int "Python built-in int documentation"
[5]: https://docs.python.org/3/tutorial/introduction.html "Python tutorial introduction"
[6]: https://owasp.org/www-community/attacks/Improper_Error_Handling "OWASP improper error handling guidance"

[← Day 1](../day_01_setup_and_safe_practice/day_01_setup_and_safe_practice.md) · [Day index](../DAY_INDEX.md) · [Day 3 →](../day_03_types_and_parsing/day_03_types_and_parsing.md)
