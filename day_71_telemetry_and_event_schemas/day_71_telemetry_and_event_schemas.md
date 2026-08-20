# Day 71: Telemetry and Event Schemas

[← Day 70](../day_70_project__secure_case_api/day_70_project__secure_case_api.md) · [Day index](../DAY_INDEX.md) · [Day 72 →](../day_72_log_normalization/day_72_log_normalization.md)






## Table of contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Lesson](#lesson)
  - [Vocabulary](#vocabulary)
- [Worked examples](#worked-examples)
  - [Example 1: Define an event](#example-1-define-an-event)
  - [Example 2: Map source fields](#example-2-map-source-fields)
  - [Example 3: Validate time](#example-3-validate-time)
  - [Example 4: Preserve source](#example-4-preserve-source)
  - [Example 5: Version a schema](#example-5-version-a-schema)
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

Detection depends on events that different systems represent differently. A schema gives analysts stable fields while preserving source, time, and uncertainty.

## Prerequisites

Complete Day 70. Use only the local course fixtures, loopback services, and synthetic records described by the lesson.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using the tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state the trust boundary and residual risk
- complete the numbered cybersecurity exercises

## The problem

Define a normalized event schema for synthetic authentication activity and reject records that cannot support the required fields.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, interception, exploit delivery, real-user profiling, or changes to systems you do not own.

## Lesson

### Vocabulary

Telemetry is collected operational data. A schema defines fields and types. Normalization maps source-specific fields into common fields. Provenance identifies the source.

## Worked examples

### Example 1: Define an event

Start with fields needed for a decision.

```python
event = {
    "event_type": "auth_failure",
    "source": "training-auth",
    "actor": "student",
    "observed_at": "now",
}
print(event)
```

**What to observe:**

The event has stable names.

### Example 2: Map source fields

Normalization makes source differences explicit.

```python
source_record = {"user": "student", "action": "login_failed"}
normalized = {"actor": source_record["user"], "event_type": "auth_failure"}
print(normalized)
```

**What to observe:**

The mapping is visible.

### Example 3: Validate time

A detection without time cannot be placed in a sequence.

```python
if not event.get("observed_at"):
    raise ValueError("timestamp required")
```

**What to observe:**

The event is rejected when time is missing.

### Example 4: Preserve source

Normalized data must retain where it came from.

```python
normalized["provenance"] = {"source": "training-auth", "raw_id": "fixture-1"}
print(normalized)
```

**What to observe:**

The mapping is auditable.

### Example 5: Version a schema

Fields evolve; a version tells readers how to interpret them.

```python
normalized["schema_version"] = 1
print(normalized["schema_version"])
```

**What to observe:**

The version is explicit.

## Read the first example line by line

The first runnable example introduces **Telemetry and Event Schemas**. Copy it into a new file and run it before changing anything. Then use this table to read the same code slowly. A line-by-line explanation does not replace practice: it shows you what to look for when a program behaves differently from your prediction.

| Line | Code | What Python is doing |
| ---: | --- | --- |
| 1 | `event = {` | Assignment: Python evaluates the right side and stores the result under the name on the left. |
| 2 | `"event_type": "auth_failure",` | Expression or data declaration: read the names, values, and operators and predict the result. |
| 3 | `"source": "training-auth",` | Expression or data declaration: read the names, values, and operators and predict the result. |
| 4 | `"actor": "student",` | Expression or data declaration: read the names, values, and operators and predict the result. |
| 5 | `"observed_at": "now",` | Expression or data declaration: read the names, values, and operators and predict the result. |
| 6 | `}` | Expression or data declaration: read the names, values, and operators and predict the result. |
| 7 | `print(event)` | Output call: Python evaluates the argument and writes a representation to the terminal. |

After the run, write down the value created by each assignment, the condition tested by each branch, and the output that appeared. Change one input only. If the result changes, identify the line that used that input. If the result does not change, explain why the input was not part of the decision. This is the same tracing habit used later when reviewing security automation.
## Execution trace

The source record is mapped, required fields are checked, raw provenance is retained, and the versioned normalized event enters detection logic.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| drop source | analyst cannot trace mapping | preserve provenance |
| no schema version | fields drift silently | version and document |
| missing time accepted | sequence rules fail | reject or mark unknown |
| normalize away raw | audit loses context | retain safe references |
| event equals truth | collection errors become facts | record confidence |

## Security application

Use synthetic authentication events and local JSON fixtures only. Do not ingest real user telemetry.

## Line-by-line walkthrough

Read the first worked example from top to bottom rather than treating it as a magic recipe. The topic of this lesson is **Telemetry and Event Schemas**. First identify the input: what value, file, record, command, or configuration enters the example? Next identify the operation that changes or examines it. Finally identify the output and ask whether that output is merely an observation or a security conclusion. Python executes statements in order, so the name created on one line must exist before a later line can use it. When a line is a function call, identify the arguments, the function's promised return value, and any visible side effect. When a line is a condition, translate it into an ordinary question before deciding whether the branch is correct.

For each example, copy the code into a fresh file and run it unchanged. Then annotate it without editing the original: write one sentence beside each line describing its role. A useful annotation format is `input`, `transform`, `check`, `decision`, or `output`. After that, change only one value and rerun the program. If the output changes, explain which line observed the changed value. If it does not change, explain why the value was not used or why the rule filtered it. This habit is more valuable than memorizing a finished script because it teaches you to trace unfamiliar security code.

The expected output is evidence about the program, not proof about the outside world. A message such as `review` means that the local rule selected a review label. It does not prove that a person attacked a system. Keep these two statements separate in your notes. Also record failures. A `TypeError`, `ValueError`, timeout, missing-file error, or rejected configuration is often the program correctly refusing an unsafe or ambiguous input. The repair should make the policy clearer rather than hiding the error with a broad catch.

## Prediction experiments

Before each experiment, write a prediction in a comment or notebook. In Experiment A, run the smallest valid input from Example 1 and write the exact output. In Experiment B, replace one valid value with an empty, malformed, missing, or boundary value relevant to **Telemetry and Event Schemas**. Predict whether the program returns a result, raises an exception, rejects the record, or takes a different branch. In Experiment C, repeat the same input twice and inspect whether the program is deterministic. If a timestamp, random value, file order, or shared mutable state changes the result, identify that source of variation explicitly.

Do not use real addresses, credentials, private logs, public targets, or downloaded payloads for these experiments. Use the repository's synthetic fixtures, loopback values, `.invalid` names, and small in-memory inputs. Keep a table with four columns: input, prediction, observed output, and explanation. If the prediction is wrong, do not erase it. The mismatch is the part that teaches you how Python and the rule actually behave.

## Broken example and repair

Start with a deliberately broken version of the lesson's idea. A common beginner mistake is to combine parsing, policy, output, and side effects in one untested block. Another is to trust a value because it has the right shape, to use an unbounded loop, to print raw evidence, or to catch every exception. Break one rule at a time in a local copy. Run the program and capture the exception type or incorrect output. State the invariant that was violated: for example, "the input must be bounded," "the field must be validated before comparison," or "the report must not reveal raw fixture data."

Repair the example in small steps. First separate raw input from the internal value. Second add the narrowest check that expresses the intended policy. Third return or report a safe result. Fourth test one valid case, one invalid case, and one boundary case. Do not claim the repair is secure merely because it runs. Explain what remains outside the lesson's scope, such as authenticity, authorization, deployment configuration, or the correctness of the underlying policy. A good repair is easier for another beginner to inspect because each assumption is visible.

## Guided practice walkthrough

Use the following sequence before attempting the independent numbered questions. Choose one synthetic record related to **Telemetry and Event Schemas** and write down its allowed shape. For example, specify which fields are required, which values are bounded, and which fields must never be printed. Create the smallest input that satisfies the shape. Run the first example and compare the output with your prediction. Add one validation check, rerun the valid record, then test a malformed record. Keep the malformed record in the test set instead of deleting it.

Next, refactor one step into a small function or named stage. Give the stage one job and a name that describes the job. Add a print statement only while debugging, then remove it or replace it with a safe summary. Write one assertion about the result. Finally, explain the data flow in five sentences: where the fixture began, which transformation occurred, which check was applied, what label or value was produced, and what the program deliberately refused to do. Ask a peer to read the explanation without seeing the code and identify any assumption that was not documented.

## Bounded cybersecurity fixture walkthrough

The security application in this lesson uses a local, synthetic fixture. Treat the fixture as untrusted input even though it is stored in the repository. Set a maximum number of records, maximum field length, and maximum output size appropriate to the exercise. Preserve a safe source label such as `training-fixture`, but do not treat that label as proof that the data is authentic. If the fixture contains an indicator-like string, keep it inert and do not resolve, scan, connect to, upload, or enrich it from the network.

A defensible report should distinguish at least four things: what was observed, what rule matched, what uncertainty remains, and what action is permitted in this lab. For example, `observed=synthetic_event`, `rule=high_value`, `confidence=training-only`, and `action=write-local-report`. The last field is a laboratory boundary, not an operational recommendation. If your code cannot make that distinction, stop and improve the report before adding features. Security engineering is not only about detecting a pattern; it is also about limiting authority, preserving provenance, and communicating uncertainty.

At the end, perform a small review. Check that the program uses only local fixtures, has a finite workload, handles malformed input, avoids raw sensitive output, and leaves the fixture unchanged. Then write one residual-risk sentence. A useful form is: "This lesson demonstrates Telemetry and Event Schemas on synthetic data, but it does not establish authenticity, authorization, production readiness, or the presence of a real attack.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples as a starting point, then record the requested output, edge case, and limitation.

## Finish line

Run `python -m course_days.day071`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A schema creates stable analytical fields without erasing source or uncertainty.

## Limitations

A normalized event can still be incomplete, delayed, duplicated, or wrong.


## References

[1]: https://docs.python.org/3/ "Python documentation"
[2]: https://docs.python.org/3/tutorial/ "The Python tutorial"
[3]: https://owasp.org/www-project-top-ten/ "OWASP Top 10"
[4]: https://csrc.nist.gov/glossary "NIST cybersecurity glossary"

[← Day 70](../day_70_project__secure_case_api/day_70_project__secure_case_api.md) · [Day index](../DAY_INDEX.md) · [Day 72 →](../day_72_log_normalization/day_72_log_normalization.md)
