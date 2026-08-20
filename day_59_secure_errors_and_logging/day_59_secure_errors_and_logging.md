# Day 59: Secure Errors and Logging

[← Day 58](../day_58_safe_serialization/day_58_safe_serialization.md) · [Day index](../DAY_INDEX.md) · [Day 60 →](../day_60_project__tamper_evident_case_bundle/day_60_project__tamper_evident_case_bundle.md)

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

Crypto and network failures are sensitive. An error should help an operator recover without revealing keys, passwords, raw tokens, internal paths, or attacker-controlled formatting.

## Prerequisites

Complete Day 58. Run the repository checks and use only the local fixtures and explicitly authorized loopback services.

## Outcomes

By the end of this lesson, you can:

- explain the protocol or security property in plain language
- run and modify every worked example
- test a normal, boundary, and failure case
- identify the trust boundary and residual risk
- connect the concept to the numbered cybersecurity exercises

## The problem

Design error categories and structured logs for a local case bundle without exposing secret material.

## Security boundary

Use synthetic data, local fixtures, and loopback-only demonstrations. This lesson does not authorize scanning, interception, credential use, remote command execution, or changes to systems you do not own.

## Lesson

### Vocabulary

An error category groups a failure for a caller. A safe message is actionable but minimized. A correlation identifier links events without copying sensitive data.

## Worked examples

### Example 1: Define safe categories

Categories help callers choose behavior.

```python
categories = {
    "input": "reject",
    "timeout": "retry-or-stop",
    "integrity": "stop",
    "bug": "escalate",
}
print(categories)
```

**What to observe:**

The policy differs by failure.

### Example 2: Redact fields

Redaction happens on structured data before formatting.

```python
safe = {"event": "decrypt_failed", "case_id": "training", "key": "[REDACTED]"}
print(safe)
```

**What to observe:**

The key is not output.

### Example 3: Use correlation

A short case id helps search without exposing a raw payload.

```python
record = {"case_id": "training-059", "error": "integrity_check_failed"}
print(record)
```

**What to observe:**

The record is searchable and minimal.

### Example 4: Avoid exception echo

User-controlled text should not become an unescaped log record.

```python
message = "bad\nvalue".replace("\n", "\\n")
print(message)
```

**What to observe:**

The line break is visible as text.

### Example 5: Separate user message and debug detail

Different audiences need different fields and access.

```python
public = {"status": "rejected", "reason": "invalid record"}
debug = {"internal": "training-only detail"}
print(public)
```

**What to observe:**

The safe output is intentionally smaller.

## Execution trace

The boundary catches a known category, creates a minimal safe record, attaches a correlation id, and stores restricted detail separately or omits it.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| log key or plaintext | cryptographic material leaks | redact and minimize |
| echo attacker text | fake records or injection | encode control characters |
| same message for all | operators cannot act | categorize failures |
| detail in exception | traceback leaks paths and values | safe public error plus restricted detail |
| retry integrity failure | tampered data is processed | stop and review |

## Security application

Use synthetic errors and fake keys only. Tests must assert that key-like strings, passwords, and raw payloads cannot appear in safe logs.

## Line-by-line walkthrough

Read the first worked example from top to bottom rather than treating it as a magic recipe. The topic of this lesson is **Secure Errors and Logging**. First identify the input: what value, file, record, command, or configuration enters the example? Next identify the operation that changes or examines it. Finally identify the output and ask whether that output is merely an observation or a security conclusion. Python executes statements in order, so the name created on one line must exist before a later line can use it. When a line is a function call, identify the arguments, the function's promised return value, and any visible side effect. When a line is a condition, translate it into an ordinary question before deciding whether the branch is correct.

For each example, copy the code into a fresh file and run it unchanged. Then annotate it without editing the original: write one sentence beside each line describing its role. A useful annotation format is `input`, `transform`, `check`, `decision`, or `output`. After that, change only one value and rerun the program. If the output changes, explain which line observed the changed value. If it does not change, explain why the value was not used or why the rule filtered it. This habit is more valuable than memorizing a finished script because it teaches you to trace unfamiliar security code.

The expected output is evidence about the program, not proof about the outside world. A message such as `review` means that the local rule selected a review label. It does not prove that a person attacked a system. Keep these two statements separate in your notes. Also record failures. A `TypeError`, `ValueError`, timeout, missing-file error, or rejected configuration is often the program correctly refusing an unsafe or ambiguous input. The repair should make the policy clearer rather than hiding the error with a broad catch.

## Prediction experiments

Before each experiment, write a prediction in a comment or notebook. In Experiment A, run the smallest valid input from Example 1 and write the exact output. In Experiment B, replace one valid value with an empty, malformed, missing, or boundary value relevant to **Secure Errors and Logging**. Predict whether the program returns a result, raises an exception, rejects the record, or takes a different branch. In Experiment C, repeat the same input twice and inspect whether the program is deterministic. If a timestamp, random value, file order, or shared mutable state changes the result, identify that source of variation explicitly.

Do not use real addresses, credentials, private logs, public targets, or downloaded payloads for these experiments. Use the repository's synthetic fixtures, loopback values, `.invalid` names, and small in-memory inputs. Keep a table with four columns: input, prediction, observed output, and explanation. If the prediction is wrong, do not erase it. The mismatch is the part that teaches you how Python and the rule actually behave.

## Broken example and repair

Start with a deliberately broken version of the lesson's idea. A common beginner mistake is to combine parsing, policy, output, and side effects in one untested block. Another is to trust a value because it has the right shape, to use an unbounded loop, to print raw evidence, or to catch every exception. Break one rule at a time in a local copy. Run the program and capture the exception type or incorrect output. State the invariant that was violated: for example, "the input must be bounded," "the field must be validated before comparison," or "the report must not reveal raw fixture data."

Repair the example in small steps. First separate raw input from the internal value. Second add the narrowest check that expresses the intended policy. Third return or report a safe result. Fourth test one valid case, one invalid case, and one boundary case. Do not claim the repair is secure merely because it runs. Explain what remains outside the lesson's scope, such as authenticity, authorization, deployment configuration, or the correctness of the underlying policy. A good repair is easier for another beginner to inspect because each assumption is visible.

## Guided practice walkthrough

Use the following sequence before attempting the independent numbered questions. Choose one synthetic record related to **Secure Errors and Logging** and write down its allowed shape. For example, specify which fields are required, which values are bounded, and which fields must never be printed. Create the smallest input that satisfies the shape. Run the first example and compare the output with your prediction. Add one validation check, rerun the valid record, then test a malformed record. Keep the malformed record in the test set instead of deleting it.

Next, refactor one step into a small function or named stage. Give the stage one job and a name that describes the job. Add a print statement only while debugging, then remove it or replace it with a safe summary. Write one assertion about the result. Finally, explain the data flow in five sentences: where the fixture began, which transformation occurred, which check was applied, what label or value was produced, and what the program deliberately refused to do. Ask a peer to read the explanation without seeing the code and identify any assumption that was not documented.

## Bounded cybersecurity fixture walkthrough

The security application in this lesson uses a local, synthetic fixture. Treat the fixture as untrusted input even though it is stored in the repository. Set a maximum number of records, maximum field length, and maximum output size appropriate to the exercise. Preserve a safe source label such as `training-fixture`, but do not treat that label as proof that the data is authentic. If the fixture contains an indicator-like string, keep it inert and do not resolve, scan, connect to, upload, or enrich it from the network.

A defensible report should distinguish at least four things: what was observed, what rule matched, what uncertainty remains, and what action is permitted in this lab. For example, `observed=synthetic_event`, `rule=high_value`, `confidence=training-only`, and `action=write-local-report`. The last field is a laboratory boundary, not an operational recommendation. If your code cannot make that distinction, stop and improve the report before adding features. Security engineering is not only about detecting a pattern; it is also about limiting authority, preserving provenance, and communicating uncertainty.

At the end, perform a small review. Check that the program uses only local fixtures, has a finite workload, handles malformed input, avoids raw sensitive output, and leaves the fixture unchanged. Then write one residual-risk sentence. A useful form is: "This lesson demonstrates Secure Errors and Logging on synthetic data, but it does not establish authenticity, authorization, production readiness, or the presence of a real attack.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested local command, inspect its output, and record the limitation asked for by the exercise.

## Finish line

Run `python -m course_days.day059`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Secure error handling preserves enough information to act while withholding material that increases harm.

## Limitations

Logging policy depends on retention, access, correlation, and incident procedures outside the Python function.


## References

[1]: https://docs.python.org/3/ "Python documentation"
[2]: https://docs.python.org/3/tutorial/ "The Python tutorial"
[3]: https://owasp.org/www-project-top-ten/ "OWASP Top 10"
[4]: https://csrc.nist.gov/glossary "NIST cybersecurity glossary"

[← Day 58](../day_58_safe_serialization/day_58_safe_serialization.md) · [Day index](../DAY_INDEX.md) · [Day 60 →](../day_60_project__tamper_evident_case_bundle/day_60_project__tamper_evident_case_bundle.md)
