# Day 72: Log Normalization

[← Previous lesson](../day_071_telemetry_and_event_schemas/day_071_telemetry_and_event_schemas.md) · [README](../README.md) · [Setup](../SETUP.md) · [VS Code](../VS_CODE_SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_073_ioc_enrichment/day_073_ioc_enrichment.md)









## Start here

Read the [course README](../README.md), complete the [setup guide](../SETUP.md) and [VS Code setup](../VS_CODE_SETUP.md), then use the [day index](../DAY_INDEX.md) to confirm where this lesson fits. Run the linked local starter before attempting the numbered exercises in this lesson, then use [hints](practice/hints.md) and [solutions](practice/solutions.md) only after an honest attempt.

## Table of contents

- [Start here](#start-here)

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is Log Normalization?](#what-is-log-normalization)
  - [Why is Log Normalization useful?](#why-is-log-normalization-useful)
  - [How will Python use this idea?](#how-will-python-use-this-idea)
  - [What are the security limits?](#what-are-the-security-limits)
- [Worked examples](#worked-examples)
  - [Example 1: Parse key-value text](#example-1-parse-key-value-text)
  - [Example 2: Map names](#example-2-map-names)
  - [Example 3: Handle malformed pairs](#example-3-handle-malformed-pairs)
  - [Example 4: Preserve raw id](#example-4-preserve-raw-id)
  - [Example 5: Bound text](#example-5-bound-text)
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

Real logs use inconsistent timestamps, separators, levels, and field names. Normalization is a documented transformation, not an excuse to erase raw evidence.

## Prerequisites

Complete Day 71. Use only the local course fixtures, loopback services, and synthetic records described by the lesson.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using the tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state the trust boundary and residual risk
- complete the numbered cybersecurity exercises

## The problem

Convert two synthetic log formats into one event schema and report rejected fields.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, interception, exploit delivery, real-user profiling, or changes to systems you do not own.

## Keywords and terms

Normalization transforms equivalent source fields into canonical fields. A parser extracts. A mapper assigns. A rejected field is a data-quality result.

## Topics

### What is Log Normalization?

Real logs use inconsistent timestamps, separators, levels, and field names. Normalization is a documented transformation, not an excuse to erase raw evidence.

### Why is Log Normalization useful?

Convert two synthetic log formats into one event schema and report rejected fields.

### How will Python use this idea?

Read the worked examples next. For each one, identify the input, the operation, the result, and the boundary that prevents the example from doing more than the lesson allows.

### What are the security limits?

The examples remain local, synthetic, bounded, and authorized. A successful program run demonstrates behavior on the fixture; it does not prove authenticity, compromise, or permission to act on a real target.

## Worked examples

### Example 1: Parse key-value text

Simple fixtures can be parsed with a bounded splitter.

```python
line = "level=warning user=student event=login_failed"
fields = dict(item.split("=", 1) for item in line.split())
print(fields)
```

**What to observe:**

The fields are strings.

### Example 2: Map names

Source keys can map to normalized names.

```python
normalized = {
    "severity": fields["level"],
    "actor": fields["user"],
    "event_type": fields["event"],
}
print(normalized)
```

**What to observe:**

The target schema is stable.

### Example 3: Handle malformed pairs

A bad token should be counted, not silently trusted.

```python
tokens = ["level=warning", "broken"]
rejected = [token for token in tokens if "=" not in token]
print(rejected)
```

**What to observe:**

`broken` is rejected.

### Example 4: Preserve raw id

The normalized record should point to its source line.

```python
normalized["provenance"] = {"line": 1, "source": "fixture-a"}
print(normalized)
```

**What to observe:**

The mapping can be reviewed.

### Example 5: Bound text

Line length and field count are resource controls.

```python
print({"max_line": 2000, "max_fields": 50})
```

**What to observe:**

The parser has finite limits.

## Read the first example line by line

The first runnable example introduces **Log Normalization**. Copy it into a new file and run it before changing anything. Then use this table to read the same code slowly. A line-by-line explanation does not replace practice: it shows you what to look for when a program behaves differently from your prediction.

| Line | Code | What Python is doing |
| ---: | --- | --- |
| 1 | `line = "level=warning user=student event=login_failed"` | Assignment: Python evaluates the right side and stores the result under the name on the left. |
| 2 | `fields = dict(item.split("=", 1) for item in line.split())` | Assignment: Python evaluates the right side and stores the result under the name on the left. |
| 3 | `print(fields)` | Output call: Python evaluates the argument and writes a representation to the terminal. |

After the run, write down the value created by each assignment, the condition tested by each branch, and the output that appeared. Change one input only. If the result changes, identify the line that used that input. If the result does not change, explain why the input was not part of the decision. This is the same tracing habit used later when reviewing security automation.
## Execution trace

The normalizer bounds the line, extracts fields, maps names, converts types, records rejected tokens, and emits a versioned event with provenance.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| drop malformed tokens | quality problem disappears | count and report rejects |
| map by position | format variation breaks | map named fields |
| erase raw line | audit cannot reproduce | keep line reference |
| unlimited fields | parser abuse | cap count and lengths |
| call normalized event true | mapping is overtrusted | record quality and confidence |

## Security application

Use supplied synthetic log formats. Do not normalize real private logs without data-handling permission.

## Line-by-line walkthrough

Read the first worked example from top to bottom rather than treating it as a magic recipe. The topic of this lesson is **Log Normalization**. First identify the input: what value, file, record, command, or configuration enters the example? Next identify the operation that changes or examines it. Finally identify the output and ask whether that output is merely an observation or a security conclusion. Python executes statements in order, so the name created on one line must exist before a later line can use it. When a line is a function call, identify the arguments, the function's promised return value, and any visible side effect. When a line is a condition, translate it into an ordinary question before deciding whether the branch is correct.

For each example, copy the code into a fresh file and run it unchanged. Then annotate it without editing the original: write one sentence beside each line describing its role. A useful annotation format is `input`, `transform`, `check`, `decision`, or `output`. After that, change only one value and rerun the program. If the output changes, explain which line observed the changed value. If it does not change, explain why the value was not used or why the rule filtered it. This habit is more valuable than memorizing a finished script because it teaches you to trace unfamiliar security code.

The expected output is evidence about the program, not proof about the outside world. A message such as `review` means that the local rule selected a review label. It does not prove that a person attacked a system. Keep these two statements separate in your notes. Also record failures. A `TypeError`, `ValueError`, timeout, missing-file error, or rejected configuration is often the program correctly refusing an unsafe or ambiguous input. The repair should make the policy clearer rather than hiding the error with a broad catch.

## Prediction experiments

Before each experiment, write a prediction in a comment or notebook. In Experiment A, run the smallest valid input from Example 1 and write the exact output. In Experiment B, replace one valid value with an empty, malformed, missing, or boundary value relevant to **Log Normalization**. Predict whether the program returns a result, raises an exception, rejects the record, or takes a different branch. In Experiment C, repeat the same input twice and inspect whether the program is deterministic. If a timestamp, random value, file order, or shared mutable state changes the result, identify that source of variation explicitly.

Do not use real addresses, credentials, private logs, public targets, or downloaded payloads for these experiments. Use the repository's synthetic fixtures, loopback values, `.invalid` names, and small in-memory inputs. Keep a table with four columns: input, prediction, observed output, and explanation. If the prediction is wrong, do not erase it. The mismatch is the part that teaches you how Python and the rule actually behave.

## Broken example and repair

Start with a deliberately broken version of the lesson's idea. A common beginner mistake is to combine parsing, policy, output, and side effects in one untested block. Another is to trust a value because it has the right shape, to use an unbounded loop, to print raw evidence, or to catch every exception. Break one rule at a time in a local copy. Run the program and capture the exception type or incorrect output. State the invariant that was violated: for example, "the input must be bounded," "the field must be validated before comparison," or "the report must not reveal raw fixture data."

Repair the example in small steps. First separate raw input from the internal value. Second add the narrowest check that expresses the intended policy. Third return or report a safe result. Fourth test one valid case, one invalid case, and one boundary case. Do not claim the repair is secure merely because it runs. Explain what remains outside the lesson's scope, such as authenticity, authorization, deployment configuration, or the correctness of the underlying policy. A good repair is easier for another beginner to inspect because each assumption is visible.

## Guided practice walkthrough

Use the following sequence before attempting the independent numbered questions. Choose one synthetic record related to **Log Normalization** and write down its allowed shape. For example, specify which fields are required, which values are bounded, and which fields must never be printed. Create the smallest input that satisfies the shape. Run the first example and compare the output with your prediction. Add one validation check, rerun the valid record, then test a malformed record. Keep the malformed record in the test set instead of deleting it.

Next, refactor one step into a small function or named stage. Give the stage one job and a name that describes the job. Add a print statement only while debugging, then remove it or replace it with a safe summary. Write one assertion about the result. Finally, explain the data flow in five sentences: where the fixture began, which transformation occurred, which check was applied, what label or value was produced, and what the program deliberately refused to do. Ask a peer to read the explanation without seeing the code and identify any assumption that was not documented.

## Bounded cybersecurity fixture walkthrough

The security application in this lesson uses a local, synthetic fixture. Treat the fixture as untrusted input even though it is stored in the repository. Set a maximum number of records, maximum field length, and maximum output size appropriate to the exercise. Preserve a safe source label such as `training-fixture`, but do not treat that label as proof that the data is authentic. If the fixture contains an indicator-like string, keep it inert and do not resolve, scan, connect to, upload, or enrich it from the network.

A defensible report should distinguish at least four things: what was observed, what rule matched, what uncertainty remains, and what action is permitted in this lab. For example, `observed=synthetic_event`, `rule=high_value`, `confidence=training-only`, and `action=write-local-report`. The last field is a laboratory boundary, not an operational recommendation. If your code cannot make that distinction, stop and improve the report before adding features. Security engineering is not only about detecting a pattern; it is also about limiting authority, preserving provenance, and communicating uncertainty.

At the end, perform a small review. Check that the program uses only local fixtures, has a finite workload, handles malformed input, avoids raw sensitive output, and leaves the fixture unchanged. Then write one residual-risk sentence. A useful form is: "This lesson demonstrates Log Normalization on synthetic data, but it does not establish authenticity, authorization, production readiness, or the presence of a real attack.
## Exercises


The following numbered exercises are the canonical practice for this lesson. Attempt them here in order; use the separate hints and solutions only after a genuine attempt.

1. Run the starter for **Day 72: Log Normalization** unchanged. What does it print, return, or create? Record the command and observed result.
2. Define the main keyword from this lesson in plain language and point to the first line where the idea appears.
3. Write down the input, operation, output, and owner of the important value before changing any code.
4. Use the supplied local example. Say which file you will change.
5. Add one normal case and predict its result before running it.
6. Add one boundary case and decide whether it should return a value, reject input, or show a safe empty/failure state.
7. Add one invalid or malformed case. Capture the visible error or rejection without hiding it with a broad catch.
8. Reproduce the deliberate mistake from the lesson, record the error, and repair the smallest possible line.
9. Write one test that fails when the important result is removed.
10. Answer: Which function or file makes the important decision? Point to its name.
11. Write one limitation: what does your successful run not prove about a real system or production readiness?
12. Prepare a short review note naming the changed files, commands, evidence, remaining risk, and next step.

Use only the supplied fixtures or a local resettable example. Do not use real credentials, private data, public targets, or systems outside explicit authorization.

## Finish line

Run `python -m course_days.day072`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Normalization is a controlled translation with evidence of what changed and what failed.

## Limitations

A canonical schema can hide source-specific meaning if the mapping is too aggressive.


## References

[1]: https://docs.python.org/3/ "Python documentation"
[2]: https://docs.python.org/3/tutorial/ "The Python tutorial"
[3]: https://owasp.org/www-project-top-ten/ "OWASP Top 10"
[4]: https://csrc.nist.gov/glossary "NIST cybersecurity glossary"

[← Day 71](../day_071_telemetry_and_event_schemas/day_071_telemetry_and_event_schemas.md) · [Day index](../DAY_INDEX.md) · [Day 73 →](../day_073_ioc_enrichment/day_073_ioc_enrichment.md)
