# Day 17: Timestamps, Timezones, and Incident Timelines

[← Previous lesson](../day_016_regular_expressions/day_016_regular_expressions.md) · [README](../README.md) · [Setup](../SETUP.md) · [VS Code](../VS_CODE_SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_018_classes_and_dataclasses/day_018_classes_and_dataclasses.md)









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
  - [What is Timestamps, Timezones, and Incident Timelines?](#what-is-timestamps-timezones-and-incident-timelines)
  - [Why is Timestamps, Timezones, and Incident Timelines useful?](#why-is-timestamps-timezones-and-incident-timelines-useful)
  - [How will Python use this idea?](#how-will-python-use-this-idea)
  - [What are the security limits?](#what-are-the-security-limits)
- [Worked examples](#worked-examples)
  - [Example 1: Parse UTC](#example-1-parse-utc)
  - [Example 2: Reject a naive value](#example-2-reject-a-naive-value)
  - [Example 3: Compare offsets](#example-3-compare-offsets)
  - [Example 4: Normalize to UTC](#example-4-normalize-to-utc)
  - [Example 5: Keep provenance](#example-5-keep-provenance)
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

Security evidence is often ordered by time, but timestamps arrive in different formats and offsets. A timeline is only as reliable as its parsing, timezone policy, and provenance.

## Prerequisites

Complete Days 1–16 and be able to parse strings at a boundary.

## Outcomes

By the end of this lesson, you can:

- parse ISO timestamps
- require timezone-aware values
- compare events in a common timezone
- preserve the raw timestamp
- identify clock and ordering limitations

## The problem

Two synthetic records show `10:00+00:00` and `11:00+01:00`. They represent the same instant. A naive string sort can suggest the wrong order.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples do not authorize access to public systems, university systems, employer systems, or accounts that you do not own.

## Keywords and terms

A **naive datetime** has no timezone. An **aware datetime** includes enough offset information to identify an instant. **Normalization** converts values into a common representation while **provenance** preserves how the value originally arrived.

## Topics

### What is Timestamps, Timezones, and Incident Timelines?

Security evidence is often ordered by time, but timestamps arrive in different formats and offsets. A timeline is only as reliable as its parsing, timezone policy, and provenance.

### Why is Timestamps, Timezones, and Incident Timelines useful?

Two synthetic records show `10:00+00:00` and `11:00+01:00`. They represent the same instant. A naive string sort can suggest the wrong order.

### How will Python use this idea?

Read the worked examples next. For each one, identify the input, the operation, the result, and the boundary that prevents the example from doing more than the lesson allows.

### What are the security limits?

The examples remain local, synthetic, bounded, and authorized. A successful program run demonstrates behavior on the fixture; it does not prove authenticity, compromise, or permission to act on a real target.

## Worked examples

### Example 1: Parse UTC

The `Z` suffix means UTC when converted to `+00:00`.

```python
from datetime import datetime

value = datetime.fromisoformat("2026-08-20T10:00:00+00:00")
print(value.tzinfo is not None)
```

**What to observe:**

`True`

### Example 2: Reject a naive value

A timestamp without an offset cannot be safely compared across sources.

```python
value = datetime.fromisoformat("2026-08-20T10:00:00")
if value.tzinfo is None:
    raise ValueError("timestamp needs a timezone")
```

**What to observe:**

The explicit error prevents an ambiguous timeline.

### Example 3: Compare offsets

Aware datetimes compare instants, not only displayed clock text.

```python
first = datetime.fromisoformat("2026-08-20T10:00:00+00:00")
second = datetime.fromisoformat("2026-08-20T11:00:00+01:00")
print(first == second)
```

**What to observe:**

`True`

### Example 4: Normalize to UTC

A common display timezone makes a report easier to read.

```python
from datetime import timezone

print(second.astimezone(timezone.utc))
```

**What to observe:**

The result displays the same instant in UTC.

### Example 5: Keep provenance

Store the original string beside the parsed value.

```python
record = {"raw_timestamp": "2026-08-20T11:00:00+01:00", "parsed": second}
```

**What to observe:**

The reviewer can check the transformation.

## Read the first example line by line

The first runnable example introduces **Timestamps, Timezones, and Incident Timelines**. Copy it into a new file and run it before changing anything. Then use this table to read the same code slowly. A line-by-line explanation does not replace practice: it shows you what to look for when a program behaves differently from your prediction.

| Line | Code | What Python is doing |
| ---: | --- | --- |
| 1 | `from datetime import datetime` | Import statement: the program asks for code from a module. |
| 2 | `` | Blank line: it separates ideas for the human reader. |
| 3 | `value = datetime.fromisoformat("2026-08-20T10:00:00+00:00")` | Assignment: Python evaluates the right side and stores the result under the name on the left. |
| 4 | `print(value.tzinfo is not None)` | Output call: Python evaluates the argument and writes a representation to the terminal. |

After the run, write down the value created by each assignment, the condition tested by each branch, and the output that appeared. Change one input only. If the result changes, identify the line that used that input. If the result does not change, explain why the input was not part of the decision. This is the same tracing habit used later when reviewing security automation.
## Execution trace

The two example timestamps compare equal because their offsets describe the same instant. If one value is naive, Python should reject it before sorting rather than inventing a timezone.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| sorting strings | offset events appear misordered | parse aware datetimes |
| assuming local time | results differ by machine | require or document timezone |
| dropping raw values | transformation cannot be audited | preserve provenance |
| treating order as causation | timeline overclaims | describe sequence and uncertainty |
| accepting future or impossible dates | fixture quality is hidden | document clock policy and test it |

## Security application

Build a synthetic timeline from fixture events, normalize to UTC, preserve raw timestamps, and report when two events have equal instants or when input lacks a timezone.

## Line-by-line walkthrough

Read the first worked example from top to bottom rather than treating it as a magic recipe. The topic of this lesson is **Timestamps, Timezones, and Incident Timelines**. First identify the input: what value, file, record, command, or configuration enters the example? Next identify the operation that changes or examines it. Finally identify the output and ask whether that output is merely an observation or a security conclusion. Python executes statements in order, so the name created on one line must exist before a later line can use it. When a line is a function call, identify the arguments, the function's promised return value, and any visible side effect. When a line is a condition, translate it into an ordinary question before deciding whether the branch is correct.

For each example, copy the code into a fresh file and run it unchanged. Then annotate it without editing the original: write one sentence beside each line describing its role. A useful annotation format is `input`, `transform`, `check`, `decision`, or `output`. After that, change only one value and rerun the program. If the output changes, explain which line observed the changed value. If it does not change, explain why the value was not used or why the rule filtered it. This habit is more valuable than memorizing a finished script because it teaches you to trace unfamiliar security code.

The expected output is evidence about the program, not proof about the outside world. A message such as `review` means that the local rule selected a review label. It does not prove that a person attacked a system. Keep these two statements separate in your notes. Also record failures. A `TypeError`, `ValueError`, timeout, missing-file error, or rejected configuration is often the program correctly refusing an unsafe or ambiguous input. The repair should make the policy clearer rather than hiding the error with a broad catch.

## Prediction experiments

Before each experiment, write a prediction in a comment or notebook. In Experiment A, run the smallest valid input from Example 1 and write the exact output. In Experiment B, replace one valid value with an empty, malformed, missing, or boundary value relevant to **Timestamps, Timezones, and Incident Timelines**. Predict whether the program returns a result, raises an exception, rejects the record, or takes a different branch. In Experiment C, repeat the same input twice and inspect whether the program is deterministic. If a timestamp, random value, file order, or shared mutable state changes the result, identify that source of variation explicitly.

Do not use real addresses, credentials, private logs, public targets, or downloaded payloads for these experiments. Use the repository's synthetic fixtures, loopback values, `.invalid` names, and small in-memory inputs. Keep a table with four columns: input, prediction, observed output, and explanation. If the prediction is wrong, do not erase it. The mismatch is the part that teaches you how Python and the rule actually behave.

## Broken example and repair

Start with a deliberately broken version of the lesson's idea. A common beginner mistake is to combine parsing, policy, output, and side effects in one untested block. Another is to trust a value because it has the right shape, to use an unbounded loop, to print raw evidence, or to catch every exception. Break one rule at a time in a local copy. Run the program and capture the exception type or incorrect output. State the invariant that was violated: for example, "the input must be bounded," "the field must be validated before comparison," or "the report must not reveal raw fixture data."

Repair the example in small steps. First separate raw input from the internal value. Second add the narrowest check that expresses the intended policy. Third return or report a safe result. Fourth test one valid case, one invalid case, and one boundary case. Do not claim the repair is secure merely because it runs. Explain what remains outside the lesson's scope, such as authenticity, authorization, deployment configuration, or the correctness of the underlying policy. A good repair is easier for another beginner to inspect because each assumption is visible.

## Guided practice walkthrough

Use the following sequence before attempting the independent numbered questions. Choose one synthetic record related to **Timestamps, Timezones, and Incident Timelines** and write down its allowed shape. For example, specify which fields are required, which values are bounded, and which fields must never be printed. Create the smallest input that satisfies the shape. Run the first example and compare the output with your prediction. Add one validation check, rerun the valid record, then test a malformed record. Keep the malformed record in the test set instead of deleting it.

Next, refactor one step into a small function or named stage. Give the stage one job and a name that describes the job. Add a print statement only while debugging, then remove it or replace it with a safe summary. Write one assertion about the result. Finally, explain the data flow in five sentences: where the fixture began, which transformation occurred, which check was applied, what label or value was produced, and what the program deliberately refused to do. Ask a peer to read the explanation without seeing the code and identify any assumption that was not documented.

## Bounded cybersecurity fixture walkthrough

The security application in this lesson uses a local, synthetic fixture. Treat the fixture as untrusted input even though it is stored in the repository. Set a maximum number of records, maximum field length, and maximum output size appropriate to the exercise. Preserve a safe source label such as `training-fixture`, but do not treat that label as proof that the data is authentic. If the fixture contains an indicator-like string, keep it inert and do not resolve, scan, connect to, upload, or enrich it from the network.

A defensible report should distinguish at least four things: what was observed, what rule matched, what uncertainty remains, and what action is permitted in this lab. For example, `observed=synthetic_event`, `rule=high_value`, `confidence=training-only`, and `action=write-local-report`. The last field is a laboratory boundary, not an operational recommendation. If your code cannot make that distinction, stop and improve the report before adding features. Security engineering is not only about detecting a pattern; it is also about limiting authority, preserving provenance, and communicating uncertainty.

At the end, perform a small review. Check that the program uses only local fixtures, has a finite workload, handles malformed input, avoids raw sensitive output, and leaves the fixture unchanged. Then write one residual-risk sentence. A useful form is: "This lesson demonstrates Timestamps, Timezones, and Incident Timelines on synthetic data, but it does not establish authenticity, authorization, production readiness, or the presence of a real attack.
## Exercises


The following numbered exercises are the canonical practice for this lesson. Attempt them here in order; use the separate hints and solutions only after a genuine attempt.

1. Parse `2026-08-20T12:00:00Z`. What timezone does the returned value use?
2. What should happen when a timestamp has no timezone offset? Test the rejection.
3. Parse two timestamps with different offsets and sort them in UTC. Which event occurred first?
4. Preserve the original timestamp string beside the normalized datetime. Why is provenance useful?
5. List two reasons a sorted timeline might still be an incomplete incident explanation.

6. Apply the lesson to the supplied local synthetic fixture and state the expected artifact before running it.
7. Add a normal case and predict the result before executing the code.
8. Add a boundary case and explain the chosen behavior.
9. Add an invalid case and keep the failure visible and understandable.
10. Reproduce the deliberate mistake from the lesson and record the smallest repair.
11. Add a focused test or evidence note for the most important behavior.
12. Write one limitation and one review question for a teammate.

Use only the supplied local, synthetic, bounded fixtures. Do not use real credentials, private data, public targets, or systems outside explicit authorization.

## Finish line

Run `python -m course_days.day017`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A timeline is an ordered interpretation of timestamped observations, not a complete story of causation.

## Limitations

Clock skew, delayed collection, missing events, and forged timestamps can make a correct sort misleading. Production investigations need corroboration and chain-of-custody procedures.


## References

[1]: https://docs.python.org/3/ "Python documentation"
[2]: https://docs.python.org/3/tutorial/ "The Python tutorial"
[3]: https://owasp.org/www-project-top-ten/ "OWASP Top 10"
[4]: https://csrc.nist.gov/glossary "NIST cybersecurity glossary"

[← Day 16](../day_016_regular_expressions/day_016_regular_expressions.md) · [Day index](../DAY_INDEX.md) · [Day 18 →](../day_018_classes_and_dataclasses/day_018_classes_and_dataclasses.md)
