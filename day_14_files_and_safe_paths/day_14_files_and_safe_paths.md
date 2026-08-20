# Day 14: Files, Paths, and Safe Evidence Boundaries

[← Day 13](../day_13_exceptions_and_error_taxonomy/day_13_exceptions_and_error_taxonomy.md) · [Day index](../DAY_INDEX.md) · [Day 15 →](../day_15_iterators_and_generators/day_15_iterators_and_generators.md)






## Table of contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Lesson](#lesson)
  - [Vocabulary](#vocabulary)
- [Worked examples](#worked-examples)
  - [Example 1: Build a path](#example-1-build-a-path)
  - [Example 2: Resolve and constrain](#example-2-resolve-and-constrain)
  - [Example 3: Read with an encoding](#example-3-read-with-an-encoding)
  - [Example 4: Check size before reading](#example-4-check-size-before-reading)
  - [Example 5: Write a controlled report](#example-5-write-a-controlled-report)
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

Files are useful evidence sources and dangerous trust boundaries. A path supplied by a user can escape the intended directory, a large file can consume resources, and a report can overwrite something important.

## Prerequisites

Complete Days 1–13 and know how to catch a boundary exception.

## Outcomes

By the end of this lesson, you can:

- use `pathlib.Path` for readable path operations
- resolve and constrain a path to a base directory
- read text with an explicit encoding
- bound file size and line length
- write reports atomically in a fixture directory

## The problem

The checkpoint should read one supplied fixture and write one generated report without following `../` outside the training directory. The safety property must be testable.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples do not authorize access to public systems, university systems, employer systems, or accounts that you do not own.

## Lesson

### Vocabulary

A **path** is a description of a location. A **resolved path** is the normalized location after following relative components and links. A **trust boundary** is where data changes from an external or less-trusted source into a sensitive operation.

## Worked examples

### Example 1: Build a path

Joining path components is clearer with `Path` than string concatenation.

```python
from pathlib import Path

base = Path("training-fixtures")
path = base / "events.log"
print(path)
```

**What to observe:**

`training-fixtures/events.log` on POSIX-style output.

### Example 2: Resolve and constrain

Compare resolved paths rather than searching for a literal `..`.

```python
def safe_path(base, user_value):
    base = base.resolve()
    candidate = (base / user_value).resolve()
    if candidate != base and base not in candidate.parents:
        raise ValueError("path escapes fixture directory")
    return candidate
```

**What to observe:**

`../secret.txt` is rejected after resolution.

### Example 3: Read with an encoding

Text decoding is part of the file contract.

```python
text = path.read_text(encoding="utf-8")
print(text.splitlines()[:2])
```

**What to observe:**

The first two lines are read as Unicode text.

### Example 4: Check size before reading

A tool can refuse a fixture that exceeds its documented bound.

```python
maximum = 1_000_000
if path.stat().st_size > maximum:
    raise ValueError("fixture is too large")
```

**What to observe:**

The file is rejected before its full content enters memory.

### Example 5: Write a controlled report

Create output only beneath the chosen report directory.

```python
report_dir = Path("training-output")
report_dir.mkdir(exist_ok=True)
(report_dir / "summary.txt").write_text("complete\n", encoding="utf-8")
```

**What to observe:**

The output is local and resettable.

## Read the first example line by line

The first runnable example introduces **Files, Paths, and Safe Evidence Boundaries**. Copy it into a new file and run it before changing anything. Then use this table to read the same code slowly. A line-by-line explanation does not replace practice: it shows you what to look for when a program behaves differently from your prediction.

| Line | Code | What Python is doing |
| ---: | --- | --- |
| 1 | `from pathlib import Path` | Import statement: the program asks for code from a module. |
| 2 | `` | Blank line: it separates ideas for the human reader. |
| 3 | `base = Path("training-fixtures")` | Assignment: Python evaluates the right side and stores the result under the name on the left. |
| 4 | `path = base / "events.log"` | Assignment: Python evaluates the right side and stores the result under the name on the left. |
| 5 | `print(path)` | Output call: Python evaluates the argument and writes a representation to the terminal. |

After the run, write down the value created by each assignment, the condition tested by each branch, and the output that appeared. Change one input only. If the result changes, identify the line that used that input. If the result does not change, explain why the input was not part of the decision. This is the same tracing habit used later when reviewing security automation.
## Execution trace

For base `/course/training-fixtures` and user value `../secret.txt`, the candidate resolves to `/course/secret.txt`. The candidate is not inside the resolved base, so the function raises before opening it.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| string prefix check | `/base-other` looks like `/base` | compare resolved path parents |
| string concatenation | separators and `..` behave unexpectedly | use `Path` |
| no encoding | platform-dependent decoding | specify UTF-8 or the documented encoding |
| read before size check | memory spikes | inspect metadata first |
| overwrite source | evidence is destroyed | write to a dedicated output directory |

## Security application

Use only `shared/fixtures` or a temporary directory under the repository. Add tests for a normal relative path, `../` escape, absolute path, oversized fixture, and output cleanup.

## Line-by-line walkthrough

Read the first worked example from top to bottom rather than treating it as a magic recipe. The topic of this lesson is **Files, Paths, and Safe Evidence Boundaries**. First identify the input: what value, file, record, command, or configuration enters the example? Next identify the operation that changes or examines it. Finally identify the output and ask whether that output is merely an observation or a security conclusion. Python executes statements in order, so the name created on one line must exist before a later line can use it. When a line is a function call, identify the arguments, the function's promised return value, and any visible side effect. When a line is a condition, translate it into an ordinary question before deciding whether the branch is correct.

For each example, copy the code into a fresh file and run it unchanged. Then annotate it without editing the original: write one sentence beside each line describing its role. A useful annotation format is `input`, `transform`, `check`, `decision`, or `output`. After that, change only one value and rerun the program. If the output changes, explain which line observed the changed value. If it does not change, explain why the value was not used or why the rule filtered it. This habit is more valuable than memorizing a finished script because it teaches you to trace unfamiliar security code.

The expected output is evidence about the program, not proof about the outside world. A message such as `review` means that the local rule selected a review label. It does not prove that a person attacked a system. Keep these two statements separate in your notes. Also record failures. A `TypeError`, `ValueError`, timeout, missing-file error, or rejected configuration is often the program correctly refusing an unsafe or ambiguous input. The repair should make the policy clearer rather than hiding the error with a broad catch.

## Prediction experiments

Before each experiment, write a prediction in a comment or notebook. In Experiment A, run the smallest valid input from Example 1 and write the exact output. In Experiment B, replace one valid value with an empty, malformed, missing, or boundary value relevant to **Files, Paths, and Safe Evidence Boundaries**. Predict whether the program returns a result, raises an exception, rejects the record, or takes a different branch. In Experiment C, repeat the same input twice and inspect whether the program is deterministic. If a timestamp, random value, file order, or shared mutable state changes the result, identify that source of variation explicitly.

Do not use real addresses, credentials, private logs, public targets, or downloaded payloads for these experiments. Use the repository's synthetic fixtures, loopback values, `.invalid` names, and small in-memory inputs. Keep a table with four columns: input, prediction, observed output, and explanation. If the prediction is wrong, do not erase it. The mismatch is the part that teaches you how Python and the rule actually behave.

## Broken example and repair

Start with a deliberately broken version of the lesson's idea. A common beginner mistake is to combine parsing, policy, output, and side effects in one untested block. Another is to trust a value because it has the right shape, to use an unbounded loop, to print raw evidence, or to catch every exception. Break one rule at a time in a local copy. Run the program and capture the exception type or incorrect output. State the invariant that was violated: for example, "the input must be bounded," "the field must be validated before comparison," or "the report must not reveal raw fixture data."

Repair the example in small steps. First separate raw input from the internal value. Second add the narrowest check that expresses the intended policy. Third return or report a safe result. Fourth test one valid case, one invalid case, and one boundary case. Do not claim the repair is secure merely because it runs. Explain what remains outside the lesson's scope, such as authenticity, authorization, deployment configuration, or the correctness of the underlying policy. A good repair is easier for another beginner to inspect because each assumption is visible.

## Guided practice walkthrough

Use the following sequence before attempting the independent numbered questions. Choose one synthetic record related to **Files, Paths, and Safe Evidence Boundaries** and write down its allowed shape. For example, specify which fields are required, which values are bounded, and which fields must never be printed. Create the smallest input that satisfies the shape. Run the first example and compare the output with your prediction. Add one validation check, rerun the valid record, then test a malformed record. Keep the malformed record in the test set instead of deleting it.

Next, refactor one step into a small function or named stage. Give the stage one job and a name that describes the job. Add a print statement only while debugging, then remove it or replace it with a safe summary. Write one assertion about the result. Finally, explain the data flow in five sentences: where the fixture began, which transformation occurred, which check was applied, what label or value was produced, and what the program deliberately refused to do. Ask a peer to read the explanation without seeing the code and identify any assumption that was not documented.

## Bounded cybersecurity fixture walkthrough

The security application in this lesson uses a local, synthetic fixture. Treat the fixture as untrusted input even though it is stored in the repository. Set a maximum number of records, maximum field length, and maximum output size appropriate to the exercise. Preserve a safe source label such as `training-fixture`, but do not treat that label as proof that the data is authentic. If the fixture contains an indicator-like string, keep it inert and do not resolve, scan, connect to, upload, or enrich it from the network.

A defensible report should distinguish at least four things: what was observed, what rule matched, what uncertainty remains, and what action is permitted in this lab. For example, `observed=synthetic_event`, `rule=high_value`, `confidence=training-only`, and `action=write-local-report`. The last field is a laboratory boundary, not an operational recommendation. If your code cannot make that distinction, stop and improve the report before adding features. Security engineering is not only about detecting a pattern; it is also about limiting authority, preserving provenance, and communicating uncertainty.

At the end, perform a small review. Check that the program uses only local fixtures, has a finite workload, handles malformed input, avoids raw sensitive output, and leaves the fixture unchanged. Then write one residual-risk sentence. A useful form is: "This lesson demonstrates Files, Paths, and Safe Evidence Boundaries on synthetic data, but it does not establish authenticity, authorization, production readiness, or the presence of a real attack.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples above as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run `python -m course_days.day014`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A file operation is safe only when location, size, encoding, mode, and cleanup are explicit.

## Limitations

Path checks can be affected by symlinks, permissions, races, and platform differences. A local helper is not a replacement for a hardened production file service.


## References

[1]: https://docs.python.org/3/ "Python documentation"
[2]: https://docs.python.org/3/tutorial/ "The Python tutorial"
[3]: https://owasp.org/www-project-top-ten/ "OWASP Top 10"
[4]: https://csrc.nist.gov/glossary "NIST cybersecurity glossary"

[← Day 13](../day_13_exceptions_and_error_taxonomy/day_13_exceptions_and_error_taxonomy.md) · [Day index](../DAY_INDEX.md) · [Day 15 →](../day_15_iterators_and_generators/day_15_iterators_and_generators.md)
