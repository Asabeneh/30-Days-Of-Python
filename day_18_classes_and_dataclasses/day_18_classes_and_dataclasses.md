# Day 18: Dataclasses and Evidence Models

[← Day 17](../day_17_dates_and_timelines/day_17_dates_and_timelines.md) · [Day index](../DAY_INDEX.md) · [Day 19 →](../day_19_testing_with_pytest/day_19_testing_with_pytest.md)






## Table of contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Lesson](#lesson)
  - [Vocabulary](#vocabulary)
- [Worked examples](#worked-examples)
  - [Example 1: The smallest dataclass](#example-1-the-smallest-dataclass)
  - [Example 2: Validate on construction](#example-2-validate-on-construction)
  - [Example 3: Freeze a finding](#example-3-freeze-a-finding)
  - [Example 4: Convert deliberately](#example-4-convert-deliberately)
  - [Example 5: Keep evidence references narrow](#example-5-keep-evidence-references-narrow)
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

A dictionary is flexible but lets field names and types drift. A dataclass gives a security tool a visible model for a finding, its evidence reference, and its confidence without pretending that the model authenticates the data.

## Prerequisites

Complete Days 1–17 and understand functions, validation, collections, and timestamps.

## Outcomes

By the end of this lesson, you can:

- define a dataclass with typed fields
- validate values in `__post_init__`
- use frozen objects for immutable findings
- serialize safely without leaking raw evidence
- distinguish a model from proof

## The problem

A report needs a stable finding shape. Reviewers should know which fields are required, which are derived, and which identifier points back to a local fixture.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples do not authorize access to public systems, university systems, employer systems, or accounts that you do not own.

## Lesson

### Vocabulary

A **dataclass** generates useful representation and comparison methods for a class. A **frozen** dataclass prevents reassignment after construction. A field type documents intent but does not validate arbitrary runtime input.

## Worked examples

### Example 1: The smallest dataclass

Fields describe the model in one place.

```python
from dataclasses import dataclass


@dataclass
class Finding:
    title: str
    severity: int
```

**What to observe:**

`Finding(title='...', severity=...)` is readable when printed.

### Example 2: Validate on construction

Reject invalid severity before the object enters the report pipeline.

```python
@dataclass
class Finding:
    title: str
    severity: int

    def __post_init__(self):
        if not self.title.strip():
            raise ValueError("title is required")
        if not 0 <= self.severity <= 10:
            raise ValueError("severity is outside 0..10")
```

**What to observe:**

An invalid object cannot be constructed.

### Example 3: Freeze a finding

An immutable result prevents accidental mutation after review.

```python
@dataclass(frozen=True)
class EvidenceRef:
    case_id: str
    line: int
```

**What to observe:**

Assigning `ref.line = 3` raises `FrozenInstanceError`.

### Example 4: Convert deliberately

`asdict` produces data for a report, but the model should not contain secrets.

```python
from dataclasses import asdict

finding = Finding("training rule matched", 7)
print(asdict(finding))
```

**What to observe:**

A dictionary with only the declared safe fields is produced.

### Example 5: Keep evidence references narrow

Use a case and line identifier rather than embedding a whole raw record.

```python
ref = EvidenceRef("training-018", 2)
print(ref)
```

**What to observe:**

The report points to local evidence without copying it everywhere.

## Read the first example line by line

The first runnable example introduces **Dataclasses and Evidence Models**. Copy it into a new file and run it before changing anything. Then use this table to read the same code slowly. A line-by-line explanation does not replace practice: it shows you what to look for when a program behaves differently from your prediction.

| Line | Code | What Python is doing |
| ---: | --- | --- |
| 1 | `from dataclasses import dataclass` | Import statement: the program asks for code from a module. |
| 2 | `` | Blank line: it separates ideas for the human reader. |
| 3 | `` | Blank line: it separates ideas for the human reader. |
| 4 | `@dataclass` | Expression or data declaration: read the names, values, and operators and predict the result. |
| 5 | `class Finding:` | Expression or data declaration: read the names, values, and operators and predict the result. |
| 6 | `title: str` | Expression or data declaration: read the names, values, and operators and predict the result. |
| 7 | `severity: int` | Expression or data declaration: read the names, values, and operators and predict the result. |

After the run, write down the value created by each assignment, the condition tested by each branch, and the output that appeared. Change one input only. If the result changes, identify the line that used that input. If the result does not change, explain why the input was not part of the decision. This is the same tracing habit used later when reviewing security automation.
## Execution trace

Construction calls the generated initializer, then `__post_init__` validates the fields. A frozen object can be read and serialized, but its attributes cannot be reassigned.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| trusting type hints | runtime strings enter integer fields | validate in construction or boundary parser |
| storing raw secrets | reports leak sensitive data | store redacted references |
| mutable finding | later code changes reviewed evidence | freeze when immutability is intended |
| no equality tests | duplicate findings are unclear | define identity and compare deliberately |
| model as proof | a clean object is mistaken for true evidence | state provenance and confidence |

## Security application

Model synthetic findings with title, severity, confidence, and an evidence reference. Do not embed private or real raw evidence. Add tests for invalid severity, blank title, and immutable references.

## Line-by-line walkthrough

Read the first worked example from top to bottom rather than treating it as a magic recipe. The topic of this lesson is **Dataclasses and Evidence Models**. First identify the input: what value, file, record, command, or configuration enters the example? Next identify the operation that changes or examines it. Finally identify the output and ask whether that output is merely an observation or a security conclusion. Python executes statements in order, so the name created on one line must exist before a later line can use it. When a line is a function call, identify the arguments, the function's promised return value, and any visible side effect. When a line is a condition, translate it into an ordinary question before deciding whether the branch is correct.

For each example, copy the code into a fresh file and run it unchanged. Then annotate it without editing the original: write one sentence beside each line describing its role. A useful annotation format is `input`, `transform`, `check`, `decision`, or `output`. After that, change only one value and rerun the program. If the output changes, explain which line observed the changed value. If it does not change, explain why the value was not used or why the rule filtered it. This habit is more valuable than memorizing a finished script because it teaches you to trace unfamiliar security code.

The expected output is evidence about the program, not proof about the outside world. A message such as `review` means that the local rule selected a review label. It does not prove that a person attacked a system. Keep these two statements separate in your notes. Also record failures. A `TypeError`, `ValueError`, timeout, missing-file error, or rejected configuration is often the program correctly refusing an unsafe or ambiguous input. The repair should make the policy clearer rather than hiding the error with a broad catch.

## Prediction experiments

Before each experiment, write a prediction in a comment or notebook. In Experiment A, run the smallest valid input from Example 1 and write the exact output. In Experiment B, replace one valid value with an empty, malformed, missing, or boundary value relevant to **Dataclasses and Evidence Models**. Predict whether the program returns a result, raises an exception, rejects the record, or takes a different branch. In Experiment C, repeat the same input twice and inspect whether the program is deterministic. If a timestamp, random value, file order, or shared mutable state changes the result, identify that source of variation explicitly.

Do not use real addresses, credentials, private logs, public targets, or downloaded payloads for these experiments. Use the repository's synthetic fixtures, loopback values, `.invalid` names, and small in-memory inputs. Keep a table with four columns: input, prediction, observed output, and explanation. If the prediction is wrong, do not erase it. The mismatch is the part that teaches you how Python and the rule actually behave.

## Broken example and repair

Start with a deliberately broken version of the lesson's idea. A common beginner mistake is to combine parsing, policy, output, and side effects in one untested block. Another is to trust a value because it has the right shape, to use an unbounded loop, to print raw evidence, or to catch every exception. Break one rule at a time in a local copy. Run the program and capture the exception type or incorrect output. State the invariant that was violated: for example, "the input must be bounded," "the field must be validated before comparison," or "the report must not reveal raw fixture data."

Repair the example in small steps. First separate raw input from the internal value. Second add the narrowest check that expresses the intended policy. Third return or report a safe result. Fourth test one valid case, one invalid case, and one boundary case. Do not claim the repair is secure merely because it runs. Explain what remains outside the lesson's scope, such as authenticity, authorization, deployment configuration, or the correctness of the underlying policy. A good repair is easier for another beginner to inspect because each assumption is visible.

## Guided practice walkthrough

Use the following sequence before attempting the independent numbered questions. Choose one synthetic record related to **Dataclasses and Evidence Models** and write down its allowed shape. For example, specify which fields are required, which values are bounded, and which fields must never be printed. Create the smallest input that satisfies the shape. Run the first example and compare the output with your prediction. Add one validation check, rerun the valid record, then test a malformed record. Keep the malformed record in the test set instead of deleting it.

Next, refactor one step into a small function or named stage. Give the stage one job and a name that describes the job. Add a print statement only while debugging, then remove it or replace it with a safe summary. Write one assertion about the result. Finally, explain the data flow in five sentences: where the fixture began, which transformation occurred, which check was applied, what label or value was produced, and what the program deliberately refused to do. Ask a peer to read the explanation without seeing the code and identify any assumption that was not documented.

## Bounded cybersecurity fixture walkthrough

The security application in this lesson uses a local, synthetic fixture. Treat the fixture as untrusted input even though it is stored in the repository. Set a maximum number of records, maximum field length, and maximum output size appropriate to the exercise. Preserve a safe source label such as `training-fixture`, but do not treat that label as proof that the data is authentic. If the fixture contains an indicator-like string, keep it inert and do not resolve, scan, connect to, upload, or enrich it from the network.

A defensible report should distinguish at least four things: what was observed, what rule matched, what uncertainty remains, and what action is permitted in this lab. For example, `observed=synthetic_event`, `rule=high_value`, `confidence=training-only`, and `action=write-local-report`. The last field is a laboratory boundary, not an operational recommendation. If your code cannot make that distinction, stop and improve the report before adding features. Security engineering is not only about detecting a pattern; it is also about limiting authority, preserving provenance, and communicating uncertainty.

At the end, perform a small review. Check that the program uses only local fixtures, has a finite workload, handles malformed input, avoids raw sensitive output, and leaves the fixture unchanged. Then write one residual-risk sentence. A useful form is: "This lesson demonstrates Dataclasses and Evidence Models on synthetic data, but it does not establish authenticity, authorization, production readiness, or the presence of a real attack.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples above as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run `python -m course_days.day018`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A dataclass is a readable model for a decision or observation; it is not an authenticity guarantee.

## Limitations

Dataclasses do not enforce trust, authorization, provenance, or serialization safety by themselves. A model can faithfully represent bad input.


## References

[1]: https://docs.python.org/3/ "Python documentation"
[2]: https://docs.python.org/3/tutorial/ "The Python tutorial"
[3]: https://owasp.org/www-project-top-ten/ "OWASP Top 10"
[4]: https://csrc.nist.gov/glossary "NIST cybersecurity glossary"

[← Day 17](../day_17_dates_and_timelines/day_17_dates_and_timelines.md) · [Day index](../DAY_INDEX.md) · [Day 19 →](../day_19_testing_with_pytest/day_19_testing_with_pytest.md)
