# Day 11: Function Contracts and Explicit Security Decisions

[← Day 10](../day_10_checkpoint_log_triage/day_10_checkpoint_log_triage.md) · [Day index](../DAY_INDEX.md) · [Day 12 →](../day_12_modules_and_packages/day_12_modules_and_packages.md)

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

A function is where an idea becomes a reusable promise. Security utilities become trustworthy when their inputs, outputs, failures, and side effects are visible enough for another person to review.

## Prerequisites

Complete Days 1–10. You should be able to write a function, return a value, and test a boundary.

## Outcomes

By the end of this lesson, you can:

- write a precondition and postcondition
- distinguish a return value from a side effect
- use keyword-only arguments and immutable defaults
- preserve failure information
- test a contract rather than an implementation detail

## The problem

The phase-one classifier works, but its rules are hidden inside a script. A reviewer needs a small function whose contract says exactly which severity values are accepted, which label is returned, and what happens when the input is invalid.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples do not authorize access to public systems, university systems, employer systems, or accounts that you do not own.

## Lesson

### Vocabulary

A **precondition** describes what must be true before a call. A **postcondition** describes what the caller can rely on after a successful return. A **side effect** changes something outside the returned value, such as a file, log, database, or network service.

## Worked examples

### Example 1: The smallest contract

A function can make its accepted input and returned value obvious.

```python
def double(value):
    return value * 2


print(double(4))
```

**What to observe:**

8

### Example 2: A bounded contract

Validation belongs at the boundary so every caller receives the same rule.

```python
def severity_label(severity):
    if not isinstance(severity, int):
        raise TypeError("severity must be an integer")
    if not 0 <= severity <= 10:
        raise ValueError("severity must be between 0 and 10")
    return "high" if severity >= 7 else "normal"
```

**What to observe:**

`severity_label(7)` returns `high`; `severity_label(11)` raises `ValueError`.

### Example 3: Keyword-only safety options

Keyword-only parameters make an important option visible at the call site.

```python
def read_preview(path, *, max_bytes=4096):
    if max_bytes <= 0:
        raise ValueError("max_bytes must be positive")
    return path.read_bytes()[:max_bytes]
```

**What to observe:**

The caller must write `max_bytes=...`; an accidental positional limit is harder to review.

### Example 4: Return instead of print

Returning a structured value lets tests and callers inspect the decision without capturing terminal output.

```python
def finding(label, reason):
    return {"label": label, "reason": reason}


result = finding("review", "high severity")
print(result["label"])
```

**What to observe:**

`review`

### Example 5: Keep effects at the edge

File access is a side effect and should be separated from a pure parser.

```python
def format_report(event):
    return f"source={event['source']} severity={event['severity']}"
```

**What to observe:**

The function returns text and does not open a file or contact a service.

## Execution trace

For `severity_label(8)`, Python binds the argument, checks its type, checks the range, evaluates `8 >= 7`, and returns `high`. For `severity_label("8")`, the type precondition fails before policy logic runs.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| no return | caller receives `None` | return the promised value |
| broad `except` | programming errors become ordinary bad input | catch only expected boundary errors |
| mutable default | calls share hidden state | use `None` or an immutable default |
| hidden file write | a pure function changes evidence | keep effects in a small boundary function |
| undocumented range | callers guess the policy | state preconditions and test boundaries |

## Security application

Refactor one phase-one rule into a pure function and add a contract table. The exercise must use only synthetic events and must distinguish the observation `rule matched` from the conclusion `attack occurred`.

## Line-by-line walkthrough

Read the first worked example from top to bottom rather than treating it as a magic recipe. The topic of this lesson is **Function Contracts and Explicit Security Decisions**. First identify the input: what value, file, record, command, or configuration enters the example? Next identify the operation that changes or examines it. Finally identify the output and ask whether that output is merely an observation or a security conclusion. Python executes statements in order, so the name created on one line must exist before a later line can use it. When a line is a function call, identify the arguments, the function's promised return value, and any visible side effect. When a line is a condition, translate it into an ordinary question before deciding whether the branch is correct.

For each example, copy the code into a fresh file and run it unchanged. Then annotate it without editing the original: write one sentence beside each line describing its role. A useful annotation format is `input`, `transform`, `check`, `decision`, or `output`. After that, change only one value and rerun the program. If the output changes, explain which line observed the changed value. If it does not change, explain why the value was not used or why the rule filtered it. This habit is more valuable than memorizing a finished script because it teaches you to trace unfamiliar security code.

The expected output is evidence about the program, not proof about the outside world. A message such as `review` means that the local rule selected a review label. It does not prove that a person attacked a system. Keep these two statements separate in your notes. Also record failures. A `TypeError`, `ValueError`, timeout, missing-file error, or rejected configuration is often the program correctly refusing an unsafe or ambiguous input. The repair should make the policy clearer rather than hiding the error with a broad catch.

## Prediction experiments

Before each experiment, write a prediction in a comment or notebook. In Experiment A, run the smallest valid input from Example 1 and write the exact output. In Experiment B, replace one valid value with an empty, malformed, missing, or boundary value relevant to **Function Contracts and Explicit Security Decisions**. Predict whether the program returns a result, raises an exception, rejects the record, or takes a different branch. In Experiment C, repeat the same input twice and inspect whether the program is deterministic. If a timestamp, random value, file order, or shared mutable state changes the result, identify that source of variation explicitly.

Do not use real addresses, credentials, private logs, public targets, or downloaded payloads for these experiments. Use the repository's synthetic fixtures, loopback values, `.invalid` names, and small in-memory inputs. Keep a table with four columns: input, prediction, observed output, and explanation. If the prediction is wrong, do not erase it. The mismatch is the part that teaches you how Python and the rule actually behave.

## Broken example and repair

Start with a deliberately broken version of the lesson's idea. A common beginner mistake is to combine parsing, policy, output, and side effects in one untested block. Another is to trust a value because it has the right shape, to use an unbounded loop, to print raw evidence, or to catch every exception. Break one rule at a time in a local copy. Run the program and capture the exception type or incorrect output. State the invariant that was violated: for example, "the input must be bounded," "the field must be validated before comparison," or "the report must not reveal raw fixture data."

Repair the example in small steps. First separate raw input from the internal value. Second add the narrowest check that expresses the intended policy. Third return or report a safe result. Fourth test one valid case, one invalid case, and one boundary case. Do not claim the repair is secure merely because it runs. Explain what remains outside the lesson's scope, such as authenticity, authorization, deployment configuration, or the correctness of the underlying policy. A good repair is easier for another beginner to inspect because each assumption is visible.

## Guided practice walkthrough

Use the following sequence before attempting the independent numbered questions. Choose one synthetic record related to **Function Contracts and Explicit Security Decisions** and write down its allowed shape. For example, specify which fields are required, which values are bounded, and which fields must never be printed. Create the smallest input that satisfies the shape. Run the first example and compare the output with your prediction. Add one validation check, rerun the valid record, then test a malformed record. Keep the malformed record in the test set instead of deleting it.

Next, refactor one step into a small function or named stage. Give the stage one job and a name that describes the job. Add a print statement only while debugging, then remove it or replace it with a safe summary. Write one assertion about the result. Finally, explain the data flow in five sentences: where the fixture began, which transformation occurred, which check was applied, what label or value was produced, and what the program deliberately refused to do. Ask a peer to read the explanation without seeing the code and identify any assumption that was not documented.

## Bounded cybersecurity fixture walkthrough

The security application in this lesson uses a local, synthetic fixture. Treat the fixture as untrusted input even though it is stored in the repository. Set a maximum number of records, maximum field length, and maximum output size appropriate to the exercise. Preserve a safe source label such as `training-fixture`, but do not treat that label as proof that the data is authentic. If the fixture contains an indicator-like string, keep it inert and do not resolve, scan, connect to, upload, or enrich it from the network.

A defensible report should distinguish at least four things: what was observed, what rule matched, what uncertainty remains, and what action is permitted in this lab. For example, `observed=synthetic_event`, `rule=high_value`, `confidence=training-only`, and `action=write-local-report`. The last field is a laboratory boundary, not an operational recommendation. If your code cannot make that distinction, stop and improve the report before adding features. Security engineering is not only about detecting a pattern; it is also about limiting authority, preserving provenance, and communicating uncertainty.

At the end, perform a small review. Check that the program uses only local fixtures, has a finite workload, handles malformed input, avoids raw sensitive output, and leaves the fixture unchanged. Then write one residual-risk sentence. A useful form is: "This lesson demonstrates Function Contracts and Explicit Security Decisions on synthetic data, but it does not establish authenticity, authorization, production readiness, or the presence of a real attack.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples above as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run `python -m course_days.day011`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A function contract is a small trust boundary: explicit input enters, a defined result leaves, and side effects are visible.

## Limitations

A contract improves review but cannot prove that the caller supplied authentic data or that the policy is correct for a production environment.


## References

[1]: https://docs.python.org/3/ "Python documentation"
[2]: https://docs.python.org/3/tutorial/ "The Python tutorial"
[3]: https://owasp.org/www-project-top-ten/ "OWASP Top 10"
[4]: https://csrc.nist.gov/glossary "NIST cybersecurity glossary"

[← Day 10](../day_10_checkpoint_log_triage/day_10_checkpoint_log_triage.md) · [Day index](../DAY_INDEX.md) · [Day 12 →](../day_12_modules_and_packages/day_12_modules_and_packages.md)
