# Day 22: Command-Line Interfaces and Explicit Input

[← Day 21](../day_21_virtual_environments/day_21_virtual_environments.md) · [Day index](../DAY_INDEX.md) · [Day 23 →](../day_23_configuration_and_secrets/day_23_configuration_and_secrets.md)






## Table of contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Lesson](#lesson)
  - [Vocabulary](#vocabulary)
- [Worked examples](#worked-examples)
  - [Example 1: Parse a flag](#example-1-parse-a-flag)
  - [Example 2: Show help](#example-2-show-help)
  - [Example 3: Reject a bound](#example-3-reject-a-bound)
  - [Example 4: Return a status](#example-4-return-a-status)
  - [Example 5: Keep paths as data](#example-5-keep-paths-as-data)
- [Read the first example line by line](#read-the-first-example-line-by-line)
- [Execution trace](#execution-trace)
- [Common mistakes](#common-mistakes)
- [Security application](#security-application)
- [Line-by-line walkthrough](#line-by-line-walkthrough)
- [Prediction experiments](#prediction-experiments)
- [Broken example and repair](#broken-example-and-repair)
- [Guided practice walkthrough](#guided-practice-walkthrough)
- [Bounded cybersecurity fixture walkthrough](#bounded-cybersecurity-fixture-walkthrough)
- [Exercises](#exercises)
- [Finish line](#finish-line)
- [Mental model](#mental-model)
- [Limitations](#limitations)
- [References](#references)

## Why this lesson exists

A CLI is the first trust boundary for many security utilities. Clear options, help text, validation, and exit statuses make a tool safer to automate and easier to review.

## Prerequisites

Complete Day 21 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 22

## The problem

Turn the log triage function into a command that accepts a fixture path, a finite limit, and an output mode without relying on ambiguous positional input.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Lesson

### Vocabulary

An **argument parser** turns shell text into values. An **exit status** communicates success or failure. A **flag** is an explicit named option.

## Worked examples

### Example 1: Parse a flag

`argparse` converts a command into a namespace.

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--limit", type=int, default=100)
args = parser.parse_args(["--limit", "5"])
print(args.limit)
```

**What to observe:**

`5` as an integer.

### Example 2: Show help

Help is part of the public contract.

```python
parser = argparse.ArgumentParser(description="Review a local training fixture")
parser.add_argument("--input", required=True)
print(parser.format_help())
```

**What to observe:**

The help names the required input and its purpose.

### Example 3: Reject a bound

Type conversion is not enough; enforce a safe domain.

```python
def positive_limit(value):
    number = int(value)
    if not 1 <= number <= 10_000:
        raise argparse.ArgumentTypeError("limit must be 1..10000")
    return number
```

**What to observe:**

Bad limits are rejected before processing begins.

### Example 4: Return a status

Shell automation needs a stable result.

```python
def main():
    return 0


raise SystemExit(main())
```

**What to observe:**

Zero conventionally means success; document non-zero meanings.

### Example 5: Keep paths as data

An input path is not a shell command.

```python
parser.add_argument("--input", type=Path)
print(args.input)
```

**What to observe:**

The value remains a path object until a bounded file function accepts it.

## Read the first example line by line

The first runnable example introduces **Command-Line Interfaces and Explicit Input**. Copy it into a new file and run it before changing anything. Then use this table to read the same code slowly. A line-by-line explanation does not replace practice: it shows you what to look for when a program behaves differently from your prediction.

| Line | Code | What Python is doing |
| ---: | --- | --- |
| 1 | `import argparse` | Import statement: the program asks for code from a module. |
| 2 | `` | Blank line: it separates ideas for the human reader. |
| 3 | `parser = argparse.ArgumentParser()` | Assignment: Python evaluates the right side and stores the result under the name on the left. |
| 4 | `parser.add_argument("--limit", type=int, default=100)` | Assignment: Python evaluates the right side and stores the result under the name on the left. |
| 5 | `args = parser.parse_args(["--limit", "5"])` | Assignment: Python evaluates the right side and stores the result under the name on the left. |
| 6 | `print(args.limit)` | Output call: Python evaluates the argument and writes a representation to the terminal. |

After the run, write down the value created by each assignment, the condition tested by each branch, and the output that appeared. Change one input only. If the result changes, identify the line that used that input. If the result does not change, explain why the input was not part of the decision. This is the same tracing habit used later when reviewing security automation.
## Execution trace

The shell provides tokens, argparse converts them, the custom validator checks policy, and only then does the tool resolve a path or process a fixture.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| `shell=True` for convenience | input becomes command syntax | pass data as arguments |
| no help | users guess the interface | describe every option |
| unlimited default | automation consumes too much | choose a finite bound |
| print errors and return 0 | scripts treat failure as success | use documented exit statuses |
| positional secrets | shell history stores them | use safer secret mechanisms and never echo values |

## Security application

Build a local CLI that accepts only the course fixture root, a finite line limit, and a report path beneath a dedicated output directory. Test invalid paths and limits.

## Line-by-line walkthrough

Read the first worked example from top to bottom rather than treating it as a magic recipe. The topic of this lesson is **Command-Line Interfaces and Explicit Input**. First identify the input: what value, file, record, command, or configuration enters the example? Next identify the operation that changes or examines it. Finally identify the output and ask whether that output is merely an observation or a security conclusion. Python executes statements in order, so the name created on one line must exist before a later line can use it. When a line is a function call, identify the arguments, the function's promised return value, and any visible side effect. When a line is a condition, translate it into an ordinary question before deciding whether the branch is correct.

For each example, copy the code into a fresh file and run it unchanged. Then annotate it without editing the original: write one sentence beside each line describing its role. A useful annotation format is `input`, `transform`, `check`, `decision`, or `output`. After that, change only one value and rerun the program. If the output changes, explain which line observed the changed value. If it does not change, explain why the value was not used or why the rule filtered it. This habit is more valuable than memorizing a finished script because it teaches you to trace unfamiliar security code.

The expected output is evidence about the program, not proof about the outside world. A message such as `review` means that the local rule selected a review label. It does not prove that a person attacked a system. Keep these two statements separate in your notes. Also record failures. A `TypeError`, `ValueError`, timeout, missing-file error, or rejected configuration is often the program correctly refusing an unsafe or ambiguous input. The repair should make the policy clearer rather than hiding the error with a broad catch.

## Prediction experiments

Before each experiment, write a prediction in a comment or notebook. In Experiment A, run the smallest valid input from Example 1 and write the exact output. In Experiment B, replace one valid value with an empty, malformed, missing, or boundary value relevant to **Command-Line Interfaces and Explicit Input**. Predict whether the program returns a result, raises an exception, rejects the record, or takes a different branch. In Experiment C, repeat the same input twice and inspect whether the program is deterministic. If a timestamp, random value, file order, or shared mutable state changes the result, identify that source of variation explicitly.

Do not use real addresses, credentials, private logs, public targets, or downloaded payloads for these experiments. Use the repository's synthetic fixtures, loopback values, `.invalid` names, and small in-memory inputs. Keep a table with four columns: input, prediction, observed output, and explanation. If the prediction is wrong, do not erase it. The mismatch is the part that teaches you how Python and the rule actually behave.

## Broken example and repair

Start with a deliberately broken version of the lesson's idea. A common beginner mistake is to combine parsing, policy, output, and side effects in one untested block. Another is to trust a value because it has the right shape, to use an unbounded loop, to print raw evidence, or to catch every exception. Break one rule at a time in a local copy. Run the program and capture the exception type or incorrect output. State the invariant that was violated: for example, "the input must be bounded," "the field must be validated before comparison," or "the report must not reveal raw fixture data."

Repair the example in small steps. First separate raw input from the internal value. Second add the narrowest check that expresses the intended policy. Third return or report a safe result. Fourth test one valid case, one invalid case, and one boundary case. Do not claim the repair is secure merely because it runs. Explain what remains outside the lesson's scope, such as authenticity, authorization, deployment configuration, or the correctness of the underlying policy. A good repair is easier for another beginner to inspect because each assumption is visible.

## Guided practice walkthrough

Use the following sequence before attempting the independent numbered questions. Choose one synthetic record related to **Command-Line Interfaces and Explicit Input** and write down its allowed shape. For example, specify which fields are required, which values are bounded, and which fields must never be printed. Create the smallest input that satisfies the shape. Run the first example and compare the output with your prediction. Add one validation check, rerun the valid record, then test a malformed record. Keep the malformed record in the test set instead of deleting it.

Next, refactor one step into a small function or named stage. Give the stage one job and a name that describes the job. Add a print statement only while debugging, then remove it or replace it with a safe summary. Write one assertion about the result. Finally, explain the data flow in five sentences: where the fixture began, which transformation occurred, which check was applied, what label or value was produced, and what the program deliberately refused to do. Ask a peer to read the explanation without seeing the code and identify any assumption that was not documented.

## Bounded cybersecurity fixture walkthrough

The security application in this lesson uses a local, synthetic fixture. Treat the fixture as untrusted input even though it is stored in the repository. Set a maximum number of records, maximum field length, and maximum output size appropriate to the exercise. Preserve a safe source label such as `training-fixture`, but do not treat that label as proof that the data is authentic. If the fixture contains an indicator-like string, keep it inert and do not resolve, scan, connect to, upload, or enrich it from the network.

A defensible report should distinguish at least four things: what was observed, what rule matched, what uncertainty remains, and what action is permitted in this lab. For example, `observed=synthetic_event`, `rule=high_value`, `confidence=training-only`, and `action=write-local-report`. The last field is a laboratory boundary, not an operational recommendation. If your code cannot make that distinction, stop and improve the report before adding features. Security engineering is not only about detecting a pattern; it is also about limiting authority, preserving provenance, and communicating uncertainty.

At the end, perform a small review. Check that the program uses only local fixtures, has a finite workload, handles malformed input, avoids raw sensitive output, and leaves the fixture unchanged. Then write one residual-risk sentence. A useful form is: "This lesson demonstrates Command-Line Interfaces and Explicit Input on synthetic data, but it does not establish authenticity, authorization, production readiness, or the presence of a real attack.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run every requested command, create the requested artifact, and record the limitation the exercise asks you to name.

## Finish line

Run `python -m course_days.day022`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A CLI makes program assumptions visible at the point where human or automation input enters.

## Limitations

A well-designed CLI cannot authorize the target. Its caller still needs permission, and its path and output policy need defense in depth.


## References

[1]: https://docs.python.org/3/ "Python documentation"
[2]: https://docs.python.org/3/tutorial/ "The Python tutorial"
[3]: https://owasp.org/www-project-top-ten/ "OWASP Top 10"
[4]: https://csrc.nist.gov/glossary "NIST cybersecurity glossary"

[← Day 21](../day_21_virtual_environments/day_21_virtual_environments.md) · [Day index](../DAY_INDEX.md) · [Day 23 →](../day_23_configuration_and_secrets/day_23_configuration_and_secrets.md)
