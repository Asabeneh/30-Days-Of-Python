# Day 104: SBOM and Provenance

[← Day 103](../day_103_static_analysis/day_103_static_analysis.md) · [Day index](../DAY_INDEX.md) · [Day 105 →](../day_105_secret_detection/day_105_secret_detection.md)









## Table of contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is SBOM and Provenance?](#what-is-sbom-and-provenance)
  - [Why is SBOM and Provenance useful?](#why-is-sbom-and-provenance-useful)
  - [How will Python use this idea?](#how-will-python-use-this-idea)
  - [What are the security limits?](#what-are-the-security-limits)
- [Worked examples](#worked-examples)
  - [Example 1: List components](#example-1-list-components)
  - [Example 2: Record source](#example-2-record-source)
  - [Example 3: Record builder](#example-3-record-builder)
  - [Example 4: Hash an artifact](#example-4-hash-an-artifact)
  - [Example 5: State unknowns](#example-5-state-unknowns)
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

Delivery teams need to know which components produced an artifact. An SBOM-like inventory and provenance record help answer what was built, from which source, with which tools, and under which review.

## Prerequisites

Complete Day 103. Work from a clean virtual environment and use only local synthetic fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using it
- run and modify all worked examples
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Create a small provenance record for a synthetic course artifact without claiming that metadata proves safety.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, destructive actions, persistence, or processing of private data.

## Keywords and terms

An SBOM inventories software components. Provenance records origin and build steps. An artifact is a produced file or image. Reproducibility means rebuilding from the same declared inputs.

## Topics

### What is SBOM and Provenance?

Delivery teams need to know which components produced an artifact. An SBOM-like inventory and provenance record help answer what was built, from which source, with which tools, and under which review.

### Why is SBOM and Provenance useful?

Create a small provenance record for a synthetic course artifact without claiming that metadata proves safety.

### How will Python use this idea?

Read the worked examples next. For each one, identify the input, the operation, the result, and the boundary that prevents the example from doing more than the lesson allows.

### What are the security limits?

The examples remain local, synthetic, bounded, and authorized. A successful program run demonstrates behavior on the fixture; it does not prove authenticity, compromise, or permission to act on a real target.

## Worked examples

### Example 1: List components

The inventory begins with names and versions.

```python
sbom = [{"name": "python", "version": "3.x"}, {"name": "course-tool", "version": "1.0"}]
print(sbom)
```

**What to observe:**

The components are named.

### Example 2: Record source

Source commit links output to a change.

```python
provenance = {"commit": "abc123", "branch": "course-redesign"}
print(provenance)
```

**What to observe:**

The source reference is explicit.

### Example 3: Record builder

The environment affects output.

```python
provenance.update({"builder": "local-ci", "python": "3.x"})
print(provenance)
```

**What to observe:**

The builder context is visible.

### Example 4: Hash an artifact

A digest identifies the bytes that were produced.

```python
import hashlib

print(hashlib.sha256(b"training-artifact").hexdigest()[:12])
```

**What to observe:**

A stable fingerprint is recorded.

### Example 5: State unknowns

Inventory is evidence, not a security guarantee.

```python
print({"unknown": ["transitive build behavior", "future vulnerability"]})
```

**What to observe:**

The report remains honest.

## Read the first example line by line

The first runnable example introduces **SBOM and Provenance**. Copy it into a new file and run it before changing anything. Then use this table to read the same code slowly. A line-by-line explanation does not replace practice: it shows you what to look for when a program behaves differently from your prediction.

| Line | Code | What Python is doing |
| ---: | --- | --- |
| 1 | `sbom = [{"name": "python", "version": "3.x"}, {"name": "course-tool", "version": "1.0"}]` | Assignment: Python evaluates the right side and stores the result under the name on the left. |
| 2 | `print(sbom)` | Output call: Python evaluates the argument and writes a representation to the terminal. |

After the run, write down the value created by each assignment, the condition tested by each branch, and the output that appeared. Change one input only. If the result changes, identify the line that used that input. If the result does not change, explain why the input was not part of the decision. This is the same tracing habit used later when reviewing security automation.
## Execution trace

The artifact is linked to source, builder, components, build steps, and digest; reviewers can compare records without treating the record as proof of a harmless supply chain.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| only direct dependencies | transitive code is missed | inventory full graph |
| no source commit | artifact cannot be traced | record provenance |
| hash equals trust | origin is overclaimed | protect source and process |
| stale SBOM | current artifact differs | generate per build |
| include secrets | metadata leaks | sanitize records |

## Security application

Use synthetic artifact names and local records. Do not publish private build metadata or install unreviewed packages.

## Line-by-line walkthrough

Read the first worked example from top to bottom rather than treating it as a magic recipe. The topic of this lesson is **SBOM and Provenance**. First identify the input: what value, file, record, command, or configuration enters the example? Next identify the operation that changes or examines it. Finally identify the output and ask whether that output is merely an observation or a security conclusion. Python executes statements in order, so the name created on one line must exist before a later line can use it. When a line is a function call, identify the arguments, the function's promised return value, and any visible side effect. When a line is a condition, translate it into an ordinary question before deciding whether the branch is correct.

For each example, copy the code into a fresh file and run it unchanged. Then annotate it without editing the original: write one sentence beside each line describing its role. A useful annotation format is `input`, `transform`, `check`, `decision`, or `output`. After that, change only one value and rerun the program. If the output changes, explain which line observed the changed value. If it does not change, explain why the value was not used or why the rule filtered it. This habit is more valuable than memorizing a finished script because it teaches you to trace unfamiliar security code.

The expected output is evidence about the program, not proof about the outside world. A message such as `review` means that the local rule selected a review label. It does not prove that a person attacked a system. Keep these two statements separate in your notes. Also record failures. A `TypeError`, `ValueError`, timeout, missing-file error, or rejected configuration is often the program correctly refusing an unsafe or ambiguous input. The repair should make the policy clearer rather than hiding the error with a broad catch.

## Prediction experiments

Before each experiment, write a prediction in a comment or notebook. In Experiment A, run the smallest valid input from Example 1 and write the exact output. In Experiment B, replace one valid value with an empty, malformed, missing, or boundary value relevant to **SBOM and Provenance**. Predict whether the program returns a result, raises an exception, rejects the record, or takes a different branch. In Experiment C, repeat the same input twice and inspect whether the program is deterministic. If a timestamp, random value, file order, or shared mutable state changes the result, identify that source of variation explicitly.

Do not use real addresses, credentials, private logs, public targets, or downloaded payloads for these experiments. Use the repository's synthetic fixtures, loopback values, `.invalid` names, and small in-memory inputs. Keep a table with four columns: input, prediction, observed output, and explanation. If the prediction is wrong, do not erase it. The mismatch is the part that teaches you how Python and the rule actually behave.

## Broken example and repair

Start with a deliberately broken version of the lesson's idea. A common beginner mistake is to combine parsing, policy, output, and side effects in one untested block. Another is to trust a value because it has the right shape, to use an unbounded loop, to print raw evidence, or to catch every exception. Break one rule at a time in a local copy. Run the program and capture the exception type or incorrect output. State the invariant that was violated: for example, "the input must be bounded," "the field must be validated before comparison," or "the report must not reveal raw fixture data."

Repair the example in small steps. First separate raw input from the internal value. Second add the narrowest check that expresses the intended policy. Third return or report a safe result. Fourth test one valid case, one invalid case, and one boundary case. Do not claim the repair is secure merely because it runs. Explain what remains outside the lesson's scope, such as authenticity, authorization, deployment configuration, or the correctness of the underlying policy. A good repair is easier for another beginner to inspect because each assumption is visible.

## Guided practice walkthrough

Use the following sequence before attempting the independent numbered questions. Choose one synthetic record related to **SBOM and Provenance** and write down its allowed shape. For example, specify which fields are required, which values are bounded, and which fields must never be printed. Create the smallest input that satisfies the shape. Run the first example and compare the output with your prediction. Add one validation check, rerun the valid record, then test a malformed record. Keep the malformed record in the test set instead of deleting it.

Next, refactor one step into a small function or named stage. Give the stage one job and a name that describes the job. Add a print statement only while debugging, then remove it or replace it with a safe summary. Write one assertion about the result. Finally, explain the data flow in five sentences: where the fixture began, which transformation occurred, which check was applied, what label or value was produced, and what the program deliberately refused to do. Ask a peer to read the explanation without seeing the code and identify any assumption that was not documented.

## Bounded cybersecurity fixture walkthrough

The security application in this lesson uses a local, synthetic fixture. Treat the fixture as untrusted input even though it is stored in the repository. Set a maximum number of records, maximum field length, and maximum output size appropriate to the exercise. Preserve a safe source label such as `training-fixture`, but do not treat that label as proof that the data is authentic. If the fixture contains an indicator-like string, keep it inert and do not resolve, scan, connect to, upload, or enrich it from the network.

A defensible report should distinguish at least four things: what was observed, what rule matched, what uncertainty remains, and what action is permitted in this lab. For example, `observed=synthetic_event`, `rule=high_value`, `confidence=training-only`, and `action=write-local-report`. The last field is a laboratory boundary, not an operational recommendation. If your code cannot make that distinction, stop and improve the report before adding features. Security engineering is not only about detecting a pattern; it is also about limiting authority, preserving provenance, and communicating uncertainty.

At the end, perform a small review. Check that the program uses only local fixtures, has a finite workload, handles malformed input, avoids raw sensitive output, and leaves the fixture unchanged. Then write one residual-risk sentence. A useful form is: "This lesson demonstrates SBOM and Provenance on synthetic data, but it does not establish authenticity, authorization, production readiness, or the presence of a real attack.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the evidence, output, edge case, and limitation requested by each question.

## Finish line

Run `python -m course_days.day104`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Provenance makes a build’s inputs and steps inspectable; it does not guarantee every component is secure.

## Limitations

SBOM formats, signing, and provenance standards need organizational tooling and verification.


## References

[1]: https://docs.python.org/3/ "Python documentation"
[2]: https://docs.python.org/3/tutorial/ "The Python tutorial"
[3]: https://owasp.org/www-project-top-ten/ "OWASP Top 10"
[4]: https://csrc.nist.gov/glossary "NIST cybersecurity glossary"

[← Day 103](../day_103_static_analysis/day_103_static_analysis.md) · [Day index](../DAY_INDEX.md) · [Day 105 →](../day_105_secret_detection/day_105_secret_detection.md)
