# Day 1: Your First Python Program and Your First Safe Cybersecurity Habit

[Day index](../DAY_INDEX.md) · [Day 2 →](../day_2_values_names_and_input/day_2_values_names_and_input.md)








## Table of contents

- [Welcome to programming](#welcome-to-programming)
- [What you need before starting](#what-you-need-before-starting)
- [The problem: a computer does not understand an intention](#the-problem-a-computer-does-not-understand-an-intention)
- [Keywords and terms in ordinary language](#keywords-and-terms-in-ordinary-language)
  - [Program](#program)
  - [Source code](#source-code)
  - [Interpreter](#interpreter)
  - [Command](#command)
  - [Output](#output)
  - [Error](#error)
- [Topics](#topics)
- [Worked examples](#worked-examples)
  - [Example 1: reading the first line character by character](#example-1-reading-the-first-line-character-by-character)
  - [Example 2: sequence means top to bottom](#example-2-sequence-means-top-to-bottom)
  - [Example 3: comments are notes for humans](#example-3-comments-are-notes-for-humans)
  - [Example 4: a safe spelling error](#example-4-a-safe-spelling-error)
  - [Example 5: strings and quotation marks](#example-5-strings-and-quotation-marks)
  - [Example 6: calculations have visible intermediate steps](#example-6-calculations-have-visible-intermediate-steps)
- [Execution trace](#execution-trace)
- [Common mistakes and repairs](#common-mistakes-and-repairs)
- [Guided practice: build a safety notice](#guided-practice-build-a-safety-notice)
- [Security application: a safe local boundary](#security-application-a-safe-local-boundary)
- [Independent exercises](#independent-exercises)
- [Finish line](#finish-line)
- [References](#references)

## Welcome to programming

You are not expected to know what a variable, function, script, terminal, algorithm, or cybersecurity tool is yet. Today begins at the beginning.

Programming means writing instructions in a language that a computer can follow. Python is one language for writing those instructions. A Python program is usually a text file ending in `.py`. When you run that file, the Python interpreter reads the text, translates each instruction into an action, and reports what happened.

Cybersecurity adds an important responsibility: the same skills that help you inspect and protect a computer can also be misused. This course therefore starts with a habit before it starts with a tool:

> Only practise on systems, data, and accounts that you own or have explicit permission to use.

Today every example is local, synthetic, harmless, and resettable. You will not scan a network, guess a password, open a private log, or send traffic to a public target. You will learn how to create a file, run it, observe output, cause a safe error, repair it, and explain why the boundary matters.

Plan for 60–90 minutes. Type the examples yourself instead of copying them blindly. The goal is not to finish quickly; the goal is to know what your computer did and why.

## What you need before starting

Complete the repository’s [`SETUP.md`](../SETUP.md) and [`VS_CODE_SETUP.md`](../VS_CODE_SETUP.md). You need:

| Item | Why it matters |
| --- | --- |
| Python 3 | The interpreter that runs your `.py` files. |
| VS Code or another editor | The place where you write text that becomes code. |
| A terminal | The place where you ask the operating system to run commands. |
| The course repository | The controlled workspace for lessons and fixtures. |

Open a terminal. Move into the course repository. If you are unsure where you are, ask the terminal to print the current directory:

```text
pwd
```

On Windows PowerShell, `Get-Location` is the equivalent command. The exact command differs by operating system, but the idea is the same: confirm the folder before creating or running files.

Ask Python for its version:

```text
python --version
```

If that command is not found, try:

```text
python3 --version
```

Do not continue by guessing. Use the interpreter command that worked on your machine. Throughout this lesson, I will write `python`; replace it with `python3` when necessary.

## The problem: a computer does not understand an intention

Suppose you want the computer to greet you. You may think, “Tell the computer to say hello.” A computer cannot execute that sentence as ordinary English because it needs exact syntax: the spelling, punctuation, and structure that Python recognizes.

Create a file named `day_1_hello.py` and write:

```python
print("Hello, Python")
```

Save the file. In the terminal, run:

```text
python day_1_hello.py
```

Expected output:

```text
Hello, Python
```

You have just completed the smallest useful programming loop:

1. write text in a file;
2. save the file;
3. tell the interpreter to run it;
4. observe the output;
5. change the file and run it again.

If the terminal says it cannot find the file, the Python code may be perfectly correct. The terminal may simply be in a different folder. This is your first debugging distinction: **a program problem and a file-location problem are not the same problem**.

## Keywords and terms in ordinary language

### Program

A **program** is a set of instructions. `day_1_hello.py` is a program containing one instruction: call `print` with the text `Hello, Python`.

### Source code

**Source code** is the human-written text in the file. It is not the output. The line `print("Hello, Python")` is source code; `Hello, Python` is output.

### Interpreter

An **interpreter** is a program that reads Python source code and performs the instructions. When you type `python day_1_hello.py`, `python` is the interpreter command and the filename is the source file it should read.

### Command

A **command** is text you type into the terminal. `python day_1_hello.py` is a command. The terminal sends it to the operating system, which starts Python with that file as an input.

### Output

**Output** is what a program sends back for a human or another program to read. `print()` writes ordinary output to the terminal.

### Error

An **error** is information that the computer gives you when it cannot perform an instruction as written. An error is not a personal failure. It is evidence about what Python could not understand or do.

## Topics

This lesson moves through four topics: what a Python program is, how the interpreter runs it, how to read an error, and how to practise safely. Each topic introduces one idea before the next one depends on it.

## Worked examples

The examples in this section are deliberately small. Run each one before moving to the next. The explanation is part of the lesson, not optional commentary.

### Example 1: reading the first line character by character

Look again at:

```python
print("Hello, Python")
```

The word `print` is the name of a built-in Python function. A **function** is a named action that can receive information, perform work, and sometimes give a result back. You will learn functions deeply later; today you only need to recognize that `print` is an action provided by Python.

The opening parenthesis `(` begins the information given to the function. The quotation marks surround a string. A **string** is text. The closing parenthesis `)` tells Python that the call is finished.

Python reads the line approximately like this:

1. find the built-in action named `print`;
2. read the string value `Hello, Python` between the quotation marks;
3. give that string to `print`;
4. write the string to the terminal;
5. move to the next line, which does not exist.

The quotation marks tell Python where the text begins and ends. They are part of the source code, but `print` does not display them:

```text
source code: print("Hello, Python")
output:      Hello, Python
```

Change the text to your own name and run the program again:

```python
print("Hello, Ada")
```

Only the value inside the quotation marks changed. The instruction stayed the same.

### Example 2: sequence means top to bottom

Add a second instruction:

```python
print("Hello, Python")
print("I am learning one instruction at a time")
```

Expected output:

```text
Hello, Python
I am learning one instruction at a time
```

Python normally executes instructions from top to bottom. That order is called **sequence**. If you reverse the lines, the output reverses too.

Try this deliberate experiment:

```python
print("second")
print("first")
```

Predict the output before running it. The computer is not correcting your meaning; it is following the sequence you wrote. This idea will become important when a security tool must read data before analyzing it, or validate a value before trusting it.

### Example 3: comments are notes for humans

A comment is text in the source code that Python ignores when it runs. In Python, a comment begins with `#`:

```python
# This line explains the safety boundary to a human reader.
print("Only authorized practice is safe practice")
```

Expected output:

```text
Only authorized practice is safe practice
```

The comment does not appear because Python does not execute it. Comments are useful for explaining why a decision exists, but they cannot protect a system by themselves. A comment saying “this input is safe” does not validate the input. Code and tests must enforce important rules.

### Example 4: a safe spelling error

A beginner may type `Print` with a capital `P`:

```python
Print("Hello")
```

Run it. Python will report a `NameError` similar to:

```text
NameError: name 'Print' is not defined
```

Read the error in plain English: “I looked for a name called `Print`, but no such name has been defined.” Python is case-sensitive. `print` and `Print` are different names.

Repair the file:

```python
print("Hello")
```

Run it again. This is the beginner debugging loop:

1. reproduce the problem;
2. read the error type and line;
3. compare the code with the expected spelling or structure;
4. make one small repair;
5. run the program again.

Do not change five unrelated things at once. If the program works after five changes, you will not know which change fixed it.

### Example 5: strings and quotation marks

These are valid strings:

```python
print("double quotes")
print("single quotes")
```

Expected output:

```text
double quotes
single quotes
```

Use one style consistently inside a file. If the text itself contains the same quotation mark, you must either use the other kind or escape the character:

```python
print("The analyst said 'stop'.")
print('The analyst said "stop".')
```

A missing quotation mark creates a `SyntaxError`. Try this in a separate scratch file:

```python
print("missing the ending quote)
```

Python may report:

```text
SyntaxError: unterminated string literal
```

“Unterminated” means Python reached the end of the line while still waiting for the closing quotation mark. Add the missing quote, save, and run again.

### Example 6: calculations have visible intermediate steps

Do not hide every operation inside one large expression. Named intermediate steps make a program easier to inspect:

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

Python first stores `2` under `left`, then `3` under `right`, then adds those two values and stores the result under `answer`. Later, when a security tool makes a decision, being able to inspect intermediate values helps you detect wrong assumptions.

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

For this broken program:

```python
print("A")
Print("B")
print("C")
```

Python prints `A`, then stops at `Print("B")` because the name is unknown. It never reaches the third line. The output may be:

```text
A
```

followed by the error report. The line after an uncaught error is not executed. This is why a partially printed report does not necessarily mean the whole operation completed.

## Common mistakes and repairs

| Mistake | What you see | Smallest correction |
| --- | --- | --- |
| Running from the wrong directory | `can't open file` | print the current directory and use the lesson command |
| Using smart quotes | `SyntaxError` | replace them with ordinary Python quotes |
| Saving as `hello.py.txt` | the terminal cannot find the file | show file extensions and rename it |
| Ignoring the last traceback line | repeated failure | read the exception type and then the reported line |
| Calling an observation an attack | an unjustified conclusion | record the observation and confidence separately |
| Changing many lines during debugging | the repair is unclear | make one small change and rerun |

## Guided practice: build a safety notice

Create `guided_safety_notice.py`. Follow the steps; do not paste a finished solution.

**Step 1:** Write one `print` call that displays `Only authorized practice is safe practice.`

**Step 2:** Add a comment above it explaining that this course uses local, synthetic, bounded fixtures.

**Step 3:** Add a second `print` call that displays `Target: local training files only`.

**Step 4:** Run the file and copy the exact output.

**Step 5:** Break the program by changing `print` to `Print`. Run it and record the error type.

**Step 6:** Repair the capitalization and run again.

**Step 7:** Change only the target text to `Target: loopback service only`. Predict which output line changes before running it.

Your program should produce two lines similar to:

```text
Only authorized practice is safe practice.
Target: local training files only
```

The comment should not appear in the output. That is evidence that comments are for human readers while `print` is an executable instruction.

## Security application: a safe local boundary

Today’s cybersecurity application is intentionally small. Create a file that prints a clear boundary before later lessons begin handling synthetic events:

```python
print("Training mode: local and synthetic data only")
print("Authorization: practise only on owned or explicitly approved systems")
print("No credentials, private logs, or public targets")
```

Expected output:

```text
Training mode: local and synthetic data only
Authorization: practise only on owned or explicitly approved systems
No credentials, private logs, or public targets
```

This output does not magically enforce the boundary. It reminds the learner of the boundary. Enforcement will come from the repository’s fixtures, tests, safe lab scope, and your decisions. A sign on a door does not replace a lock; similarly, a printed warning does not replace authorization and technical controls.

## Independent exercises

Complete these in `practice/exercises.md` in order:

1. Create a file that prints your first name, your course goal, and the sentence `Only authorized practice is safe practice.` Run it and record the exact three-line output.
2. Add a comment above the program explaining why the course uses local, synthetic, bounded fixtures. Does the comment change the output? Prove your answer by running the file.
3. Write two `print` calls and predict the order of the two lines before running them. Swap the lines and explain the new output.
4. Deliberately write `Print("test")`. Record the error type and the line where it occurs. Repair it without changing any other line.
5. Deliberately remove a closing quotation mark in a scratch file. Record the useful part of the `SyntaxError`. Repair it and explain what “unterminated string” means.
6. Write a program that prints a three-line local lab boundary. Include the words `local`, `synthetic`, and `authorized`.
7. Add a comment containing a sentence that should not appear in output. Run the program and explain why it does not appear.
8. Create a program with three print calls where the second call has a deliberate name error. Predict which lines will appear before the error and which line will never run.
9. Repair Question 8 with one small change. Record the before and after output.
10. Run the course starter and write down the command you used, the output you received, and the folder from which you ran it.
11. Explain the difference between source code, a command, the interpreter, and output using this example: `python day_1_hello.py`.
12. Safety question: list three systems or data sources that are out of scope for this lesson and three safe substitutes inside the repository.
13. Write a short paragraph answering: why is reading an error message a programming skill rather than a sign that you failed?
14. Explain what the computer can and cannot infer from the printed sentence `Training mode: local and synthetic data only`.

## Finish line

Day 1 is complete when you can create and run a Python file without following a screenshot, explain what the interpreter is doing, intentionally create and repair a small error, distinguish source code from output, and state the authorization boundary in your own words.

Do not move forward because the program eventually ran once. Move forward when you can reproduce it, explain it, and repair a similar mistake in a fresh file.

## References

[1]: https://docs.python.org/3/tutorial/index.html "The official Python tutorial"
[2]: https://docs.python.org/3/tutorial/interpreter.html "Using the Python interpreter"
[3]: https://docs.python.org/3/tutorial/errors.html "Python errors and exceptions"
[4]: https://docs.python.org/3/tutorial/introduction.html "Python introduction and first steps"
[5]: https://www.nist.gov/cyberframework "NIST Cybersecurity Framework"
[6]: https://www.cisa.gov/topics/cyber-threats-and-advisories "CISA cyber threat guidance"
