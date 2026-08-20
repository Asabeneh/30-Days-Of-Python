# Day 64: Injection and Parameterized Queries

[← Day 63](../day_63_authentication_and_authorization/day_63_authentication_and_authorization.md) · [Day index](../DAY_INDEX.md) · [Day 65 →](../day_65_xss_and_output_encoding/day_65_xss_and_output_encoding.md)









## Table of contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is Injection and Parameterized Queries?](#what-is-injection-and-parameterized-queries)
  - [Why is Injection and Parameterized Queries useful?](#why-is-injection-and-parameterized-queries-useful)
  - [How will Python use this idea?](#how-will-python-use-this-idea)
  - [What are the security limits?](#what-are-the-security-limits)
- [Worked examples](#worked-examples)
  - [Example 1: The unsafe shape](#example-1-the-unsafe-shape)
  - [Example 2: Use a placeholder](#example-2-use-a-placeholder)
  - [Example 3: Validate an identifier](#example-3-validate-an-identifier)
  - [Example 4: Bound a result](#example-4-bound-a-result)
  - [Example 5: Test a quote as data](#example-5-test-a-quote-as-data)
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

Injection occurs when data is interpreted as code or query syntax. The core defense is to keep data separate from the language being executed and to validate values at the boundary.

## Prerequisites

Complete Day 63. Use only the local course fixtures, loopback services, and synthetic records described by the lesson.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using the tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state the trust boundary and residual risk
- complete the numbered cybersecurity exercises

## The problem

Store and search synthetic cases in SQLite using parameters, then compare it with an intentionally unsafe string-building example without executing attacker input.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, interception, exploit delivery, real-user profiling, or changes to systems you do not own.

## Keywords and terms

Injection changes the meaning of an interpreter input. A parameterized query sends values separately from SQL syntax. Allowlisting constrains identifiers or operations.

## Topics

### What is Injection and Parameterized Queries?

Injection occurs when data is interpreted as code or query syntax. The core defense is to keep data separate from the language being executed and to validate values at the boundary.

### Why is Injection and Parameterized Queries useful?

Store and search synthetic cases in SQLite using parameters, then compare it with an intentionally unsafe string-building example without executing attacker input.

### How will Python use this idea?

Read the worked examples next. For each one, identify the input, the operation, the result, and the boundary that prevents the example from doing more than the lesson allows.

### What are the security limits?

The examples remain local, synthetic, bounded, and authorized. A successful program run demonstrates behavior on the fixture; it does not prove authenticity, compromise, or permission to act on a real target.

## Worked examples

### Example 1: The unsafe shape

String concatenation mixes data and SQL grammar; keep this as a non-executed illustration.

```python
username = "training-user"
unsafe_sql = "SELECT * FROM users WHERE name = '" + username + "'"
print(unsafe_sql)
```

**What to observe:**

The query text contains data inside its syntax.

### Example 2: Use a placeholder

The database receives SQL structure and value separately.

```python
query = "SELECT * FROM users WHERE name = ?"
params = (username,)
print(query, params)
```

**What to observe:**

The value is not assembled into the query string.

### Example 3: Validate an identifier

Parameters are for values, not table or column names.

```python
allowed_columns = {"name", "severity"}
column = "severity"
if column not in allowed_columns:
    raise ValueError("column not allowed")
```

**What to observe:**

Only known identifiers are accepted.

### Example 4: Bound a result

A query can still return too many rows.

```python
limit = 20
if not 1 <= limit <= 100:
    raise ValueError("limit outside policy")
```

**What to observe:**

The database operation has a finite result bound.

### Example 5: Test a quote as data

A quote in a username should remain a value.

```python
candidate = "O'Reilly"
print((candidate,))
```

**What to observe:**

The parameter tuple holds the literal text.

## Read the first example line by line

The first runnable example introduces **Injection and Parameterized Queries**. Copy it into a new file and run it before changing anything. Then use this table to read the same code slowly. A line-by-line explanation does not replace practice: it shows you what to look for when a program behaves differently from your prediction.

| Line | Code | What Python is doing |
| ---: | --- | --- |
| 1 | `username = "training-user"` | Assignment: Python evaluates the right side and stores the result under the name on the left. |
| 2 | `unsafe_sql = "SELECT * FROM users WHERE name = '" + username + "'"` | Assignment: Python evaluates the right side and stores the result under the name on the left. |
| 3 | `print(unsafe_sql)` | Output call: Python evaluates the argument and writes a representation to the terminal. |

After the run, write down the value created by each assignment, the condition tested by each branch, and the output that appeared. Change one input only. If the result changes, identify the line that used that input. If the result does not change, explain why the input was not part of the decision. This is the same tracing habit used later when reviewing security automation.
## Execution trace

The program validates the operation and bounds, sends a fixed query with parameters, receives rows, and serializes only selected fields. It never turns user text into SQL source.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| concatenate values | input changes query syntax | use parameters |
| parameterize identifiers | API does not treat table names as values | allowlist identifiers |
| trust ORM blindly | raw fragments still bypass safety | review generated SQL and APIs |
| no result bound | query exhausts resources | cap rows and time |
| demonstrate with live target | unsafe practice expands scope | use local SQLite |

## Security application

Use only in-memory or disposable SQLite with synthetic records. The lesson explains an unsafe pattern but must not execute exploit strings or target a public database.

## Line-by-line walkthrough

Read the first worked example from top to bottom rather than treating it as a magic recipe. The topic of this lesson is **Injection and Parameterized Queries**. First identify the input: what value, file, record, command, or configuration enters the example? Next identify the operation that changes or examines it. Finally identify the output and ask whether that output is merely an observation or a security conclusion. Python executes statements in order, so the name created on one line must exist before a later line can use it. When a line is a function call, identify the arguments, the function's promised return value, and any visible side effect. When a line is a condition, translate it into an ordinary question before deciding whether the branch is correct.

For each example, copy the code into a fresh file and run it unchanged. Then annotate it without editing the original: write one sentence beside each line describing its role. A useful annotation format is `input`, `transform`, `check`, `decision`, or `output`. After that, change only one value and rerun the program. If the output changes, explain which line observed the changed value. If it does not change, explain why the value was not used or why the rule filtered it. This habit is more valuable than memorizing a finished script because it teaches you to trace unfamiliar security code.

The expected output is evidence about the program, not proof about the outside world. A message such as `review` means that the local rule selected a review label. It does not prove that a person attacked a system. Keep these two statements separate in your notes. Also record failures. A `TypeError`, `ValueError`, timeout, missing-file error, or rejected configuration is often the program correctly refusing an unsafe or ambiguous input. The repair should make the policy clearer rather than hiding the error with a broad catch.

## Prediction experiments

Before each experiment, write a prediction in a comment or notebook. In Experiment A, run the smallest valid input from Example 1 and write the exact output. In Experiment B, replace one valid value with an empty, malformed, missing, or boundary value relevant to **Injection and Parameterized Queries**. Predict whether the program returns a result, raises an exception, rejects the record, or takes a different branch. In Experiment C, repeat the same input twice and inspect whether the program is deterministic. If a timestamp, random value, file order, or shared mutable state changes the result, identify that source of variation explicitly.

Do not use real addresses, credentials, private logs, public targets, or downloaded payloads for these experiments. Use the repository's synthetic fixtures, loopback values, `.invalid` names, and small in-memory inputs. Keep a table with four columns: input, prediction, observed output, and explanation. If the prediction is wrong, do not erase it. The mismatch is the part that teaches you how Python and the rule actually behave.

## Broken example and repair

Start with a deliberately broken version of the lesson's idea. A common beginner mistake is to combine parsing, policy, output, and side effects in one untested block. Another is to trust a value because it has the right shape, to use an unbounded loop, to print raw evidence, or to catch every exception. Break one rule at a time in a local copy. Run the program and capture the exception type or incorrect output. State the invariant that was violated: for example, "the input must be bounded," "the field must be validated before comparison," or "the report must not reveal raw fixture data."

Repair the example in small steps. First separate raw input from the internal value. Second add the narrowest check that expresses the intended policy. Third return or report a safe result. Fourth test one valid case, one invalid case, and one boundary case. Do not claim the repair is secure merely because it runs. Explain what remains outside the lesson's scope, such as authenticity, authorization, deployment configuration, or the correctness of the underlying policy. A good repair is easier for another beginner to inspect because each assumption is visible.

## Guided practice walkthrough

Use the following sequence before attempting the independent numbered questions. Choose one synthetic record related to **Injection and Parameterized Queries** and write down its allowed shape. For example, specify which fields are required, which values are bounded, and which fields must never be printed. Create the smallest input that satisfies the shape. Run the first example and compare the output with your prediction. Add one validation check, rerun the valid record, then test a malformed record. Keep the malformed record in the test set instead of deleting it.

Next, refactor one step into a small function or named stage. Give the stage one job and a name that describes the job. Add a print statement only while debugging, then remove it or replace it with a safe summary. Write one assertion about the result. Finally, explain the data flow in five sentences: where the fixture began, which transformation occurred, which check was applied, what label or value was produced, and what the program deliberately refused to do. Ask a peer to read the explanation without seeing the code and identify any assumption that was not documented.

## Bounded cybersecurity fixture walkthrough

The security application in this lesson uses a local, synthetic fixture. Treat the fixture as untrusted input even though it is stored in the repository. Set a maximum number of records, maximum field length, and maximum output size appropriate to the exercise. Preserve a safe source label such as `training-fixture`, but do not treat that label as proof that the data is authentic. If the fixture contains an indicator-like string, keep it inert and do not resolve, scan, connect to, upload, or enrich it from the network.

A defensible report should distinguish at least four things: what was observed, what rule matched, what uncertainty remains, and what action is permitted in this lab. For example, `observed=synthetic_event`, `rule=high_value`, `confidence=training-only`, and `action=write-local-report`. The last field is a laboratory boundary, not an operational recommendation. If your code cannot make that distinction, stop and improve the report before adding features. Security engineering is not only about detecting a pattern; it is also about limiting authority, preserving provenance, and communicating uncertainty.

At the end, perform a small review. Check that the program uses only local fixtures, has a finite workload, handles malformed input, avoids raw sensitive output, and leaves the fixture unchanged. Then write one residual-risk sentence. A useful form is: "This lesson demonstrates Injection and Parameterized Queries on synthetic data, but it does not establish authenticity, authorization, production readiness, or the presence of a real attack.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples as a starting point, then record the requested output, edge case, and limitation.

## Finish line

Run `python -m course_days.day64`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Injection is prevented when the interpreter’s language remains fixed and external data remains data.

## Limitations

Parameterized queries do not validate business logic, permissions, schema, or database availability.


## References

[1]: https://docs.python.org/3/ "Python documentation"
[2]: https://docs.python.org/3/tutorial/ "The Python tutorial"
[3]: https://owasp.org/www-project-top-ten/ "OWASP Top 10"
[4]: https://csrc.nist.gov/glossary "NIST cybersecurity glossary"

[← Day 63](../day_63_authentication_and_authorization/day_63_authentication_and_authorization.md) · [Day index](../DAY_INDEX.md) · [Day 65 →](../day_65_xss_and_output_encoding/day_65_xss_and_output_encoding.md)
