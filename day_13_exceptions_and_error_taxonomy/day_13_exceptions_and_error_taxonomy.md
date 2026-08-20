# Day 13: Exceptions and Error Taxonomy

[← Day 12](../day_12_modules_and_packages/day_12_modules_and_packages.md) · [Day index](../DAY_INDEX.md) · [Day 14 →](../day_14_files_and_safe_paths/day_14_files_and_safe_paths.md)

## Table of Contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Lesson](#lesson)
- [Vocabulary](#vocabulary)
- [Worked examples](#worked-examples)
- [Execution trace](#execution-trace)
- [Common mistakes](#common-mistakes)
- [Security application](#security-application)
- [Exercises](#exercises)
- [Finish line](#finish-line)

## Why this lesson exists

Errors are part of a security tool’s output. If a program hides a malformed record, a permission failure, and a programming bug under one `except`, operators cannot know what happened or what to do next.

## Prerequisites

Complete Days 1–12 and be comfortable with modules, functions, and conversion errors.

## Outcomes

By the end of this lesson, you can:

- read a traceback from the bottom up
- raise a precise exception at a boundary
- catch only what the caller can handle
- preserve context with exception chaining
- separate rejected input from unavailable resources

## The problem

The log parser sees a missing field, the fixture path is outside the allowed directory, and the report file cannot be written. These are different failures and require different messages and tests.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples do not authorize access to public systems, university systems, employer systems, or accounts that you do not own.

## Lesson

### Vocabulary

An **exception** is an object describing an abnormal condition. **Raising** transfers control to a handler. **Catching** says the current layer knows how to recover or report. An exception chain preserves the original cause.

## Worked examples

### Example 1: Catch the expected conversion error

Handle malformed user input at the CLI boundary.

```python
try:
    severity = int(raw)
except ValueError:
    print("severity must be an integer")
```

**What to observe:**

The user sees a useful message instead of a traceback.

### Example 2: Raise a policy error

A successful conversion can still violate a domain rule.

```python
def require_limit(value):
    if not 1 <= value <= 1000:
        raise ValueError("limit must be 1..1000")
    return value
```

**What to observe:**

`require_limit(1001)` raises a precise policy error.

### Example 3: Use separate exception types

A caller can react differently to invalid data and a missing file.

```python
class InvalidRecord(ValueError):
    pass


class FixtureNotFound(FileNotFoundError):
    pass
```

**What to observe:**

The type communicates the recovery path.

### Example 4: Chain a cause

Translate a low-level exception while preserving why it happened.

```python
try:
    value = int(raw)
except ValueError as error:
    raise InvalidRecord("severity is malformed") from error
```

**What to observe:**

The message is domain-specific and the original `ValueError` remains available.

### Example 5: Do not hide failures

A catch-all returning an empty list looks like a successful scan with no findings.

```python
try:
    records = load_fixture(path)
except FixtureNotFound:
    return {"status": "unavailable"}
```

**What to observe:**

The caller can distinguish unavailable input from an empty result.

## Execution trace

For `int("high")`, Python raises `ValueError`; the boundary catches it and raises `InvalidRecord` with the original error chained. A programming error such as a misspelled variable should remain visible instead of being converted into `invalid input`.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| `except Exception` everywhere | real bugs disappear | catch only recoverable types |
| `except: pass` | evidence silently vanishes | report or re-raise with context |
| one error for all cases | operators cannot choose a response | define a small error taxonomy |
| leaking raw input | secrets appear in messages | use safe field names and redaction |
| retrying every error | malformed data is processed repeatedly | retry only transient resource failures |

## Security application

Add a rejection report for malformed synthetic records and a separate unavailable-fixture result. Never include the full raw line or a secret in the exception message.

## Line-by-line walkthrough

Read the first worked example from top to bottom rather than treating it as a magic recipe. The topic of this lesson is **Exceptions and Error Taxonomy**. First identify the input: what value, file, record, command, or configuration enters the example? Next identify the operation that changes or examines it. Finally identify the output and ask whether that output is merely an observation or a security conclusion. Python executes statements in order, so the name created on one line must exist before a later line can use it. When a line is a function call, identify the arguments, the function's promised return value, and any visible side effect. When a line is a condition, translate it into an ordinary question before deciding whether the branch is correct.

For each example, copy the code into a fresh file and run it unchanged. Then annotate it without editing the original: write one sentence beside each line describing its role. A useful annotation format is `input`, `transform`, `check`, `decision`, or `output`. After that, change only one value and rerun the program. If the output changes, explain which line observed the changed value. If it does not change, explain why the value was not used or why the rule filtered it. This habit is more valuable than memorizing a finished script because it teaches you to trace unfamiliar security code.

The expected output is evidence about the program, not proof about the outside world. A message such as `review` means that the local rule selected a review label. It does not prove that a person attacked a system. Keep these two statements separate in your notes. Also record failures. A `TypeError`, `ValueError`, timeout, missing-file error, or rejected configuration is often the program correctly refusing an unsafe or ambiguous input. The repair should make the policy clearer rather than hiding the error with a broad catch.

## Prediction experiments

Before each experiment, write a prediction in a comment or notebook. In Experiment A, run the smallest valid input from Example 1 and write the exact output. In Experiment B, replace one valid value with an empty, malformed, missing, or boundary value relevant to **Exceptions and Error Taxonomy**. Predict whether the program returns a result, raises an exception, rejects the record, or takes a different branch. In Experiment C, repeat the same input twice and inspect whether the program is deterministic. If a timestamp, random value, file order, or shared mutable state changes the result, identify that source of variation explicitly.

Do not use real addresses, credentials, private logs, public targets, or downloaded payloads for these experiments. Use the repository's synthetic fixtures, loopback values, `.invalid` names, and small in-memory inputs. Keep a table with four columns: input, prediction, observed output, and explanation. If the prediction is wrong, do not erase it. The mismatch is the part that teaches you how Python and the rule actually behave.

## Broken example and repair

Start with a deliberately broken version of the lesson's idea. A common beginner mistake is to combine parsing, policy, output, and side effects in one untested block. Another is to trust a value because it has the right shape, to use an unbounded loop, to print raw evidence, or to catch every exception. Break one rule at a time in a local copy. Run the program and capture the exception type or incorrect output. State the invariant that was violated: for example, "the input must be bounded," "the field must be validated before comparison," or "the report must not reveal raw fixture data."

Repair the example in small steps. First separate raw input from the internal value. Second add the narrowest check that expresses the intended policy. Third return or report a safe result. Fourth test one valid case, one invalid case, and one boundary case. Do not claim the repair is secure merely because it runs. Explain what remains outside the lesson's scope, such as authenticity, authorization, deployment configuration, or the correctness of the underlying policy. A good repair is easier for another beginner to inspect because each assumption is visible.

## Guided practice walkthrough

Use the following sequence before attempting the independent numbered questions. Choose one synthetic record related to **Exceptions and Error Taxonomy** and write down its allowed shape. For example, specify which fields are required, which values are bounded, and which fields must never be printed. Create the smallest input that satisfies the shape. Run the first example and compare the output with your prediction. Add one validation check, rerun the valid record, then test a malformed record. Keep the malformed record in the test set instead of deleting it.

Next, refactor one step into a small function or named stage. Give the stage one job and a name that describes the job. Add a print statement only while debugging, then remove it or replace it with a safe summary. Write one assertion about the result. Finally, explain the data flow in five sentences: where the fixture began, which transformation occurred, which check was applied, what label or value was produced, and what the program deliberately refused to do. Ask a peer to read the explanation without seeing the code and identify any assumption that was not documented.

## Bounded cybersecurity fixture walkthrough

The security application in this lesson uses a local, synthetic fixture. Treat the fixture as untrusted input even though it is stored in the repository. Set a maximum number of records, maximum field length, and maximum output size appropriate to the exercise. Preserve a safe source label such as `training-fixture`, but do not treat that label as proof that the data is authentic. If the fixture contains an indicator-like string, keep it inert and do not resolve, scan, connect to, upload, or enrich it from the network.

A defensible report should distinguish at least four things: what was observed, what rule matched, what uncertainty remains, and what action is permitted in this lab. For example, `observed=synthetic_event`, `rule=high_value`, `confidence=training-only`, and `action=write-local-report`. The last field is a laboratory boundary, not an operational recommendation. If your code cannot make that distinction, stop and improve the report before adding features. Security engineering is not only about detecting a pattern; it is also about limiting authority, preserving provenance, and communicating uncertainty.

At the end, perform a small review. Check that the program uses only local fixtures, has a finite workload, handles malformed input, avoids raw sensitive output, and leaves the fixture unchanged. Then write one residual-risk sentence. A useful form is: "This lesson demonstrates Exceptions and Error Taxonomy on synthetic data, but it does not establish authenticity, authorization, production readiness, or the presence of a real attack.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples above as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run `python -m course_days.day013`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> An exception is information about a failed assumption; classify it so the correct layer can recover, report, or stop.

## Limitations

Exception messages can be sensitive and exception types are not a complete observability strategy. Production systems also need structured logs, metrics, and ownership.


## References

[1]: https://docs.python.org/3/ "Python documentation"
[2]: https://docs.python.org/3/tutorial/ "The Python tutorial"
[3]: https://owasp.org/www-project-top-ten/ "OWASP Top 10"
[4]: https://csrc.nist.gov/glossary "NIST cybersecurity glossary"

[← Day 12](../day_12_modules_and_packages/day_12_modules_and_packages.md) · [Day index](../DAY_INDEX.md) · [Day 14 →](../day_14_files_and_safe_paths/day_14_files_and_safe_paths.md)
