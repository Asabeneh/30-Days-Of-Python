# Day 19: Testing Security Utilities

[← Day 18](../day_18_classes_and_dataclasses/day_18_classes_and_dataclasses.md) · [Day index](../DAY_INDEX.md) · [Day 20 →](../day_20_project__log_triage_cli/day_20_project__log_triage_cli.md)

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

Tests turn a claim about code into a repeatable check. Security tests should cover ordinary behavior, boundaries, malformed inputs, and the absence of dangerous side effects.

## Prerequisites

Complete Days 1–18 and run the existing pytest suite once.

## Outcomes

By the end of this lesson, you can:

- write a focused test
- use arrange, act, assert
- test boundaries and rejection paths
- isolate filesystem work with temporary paths
- distinguish unit evidence from system confidence

## The problem

A parser that passes one happy-path test may still accept an invalid port, leak a token, or read outside its fixture. The test suite must make those failures visible.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples do not authorize access to public systems, university systems, employer systems, or accounts that you do not own.

## Lesson

### Vocabulary

A **unit test** checks one small behavior. A **fixture** prepares repeatable input. A **negative test** proves that an invalid or unsafe case is rejected. A **regression test** preserves a behavior after a bug is fixed.

## Worked examples

### Example 1: Arrange, act, assert

Keep the test readable by separating setup, call, and expectation.

```python
def test_severity_label_high():
    result = severity_label(8)
    assert result == "high"
```

**What to observe:**

A failure points to the contract.

### Example 2: Parametrize boundaries

Multiple boundary cases should share the same claim.

```python
import pytest


@pytest.mark.parametrize("value", [0, 10])
def test_severity_boundaries(value):
    assert severity_label(value) in {"normal", "high"}
```

**What to observe:**

Both accepted endpoints are checked.

### Example 3: Assert rejection

A test should prove an invalid value fails for the intended reason.

```python
def test_bad_port_rejected():
    with pytest.raises(ValueError, match="1..65535"):
        parse_port("70000")
```

**What to observe:**

The test fails if the value is silently accepted.

### Example 4: Use a temporary path

Filesystem tests should not write into the repository or a real home directory.

```python
def test_report(tmp_path):
    path = tmp_path / "report.txt"
    write_report(path, "training")
    assert path.read_text(encoding="utf-8") == "training\n"
```

**What to observe:**

pytest cleans the temporary directory.

### Example 5: Test no secret leakage

A report contract can assert that a token is absent.

```python
def test_report_redacts_token():
    output = render({"token": "training-secret"})
    assert "training-secret" not in output
```

**What to observe:**

The negative property is explicit.

## Execution trace

A test first creates the fixture, calls one behavior, and then asserts the contract. A failure should tell you which claim broke; a test that only checks `result is not None` is weak evidence.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| testing implementation details | harmless refactor breaks tests | assert observable contracts |
| only happy paths | malformed input is untested | add rejection and boundary cases |
| shared real files | tests interfere or leak data | use `tmp_path` and fixtures |
| giant integration test | failure location is unclear | keep units small and add focused integration tests |
| trusting coverage alone | lines run without meaningful assertions | review the claims each test makes |

## Security application

Write tests for the phase-two tools: safe path rejection, bounded line handling, severity validation, timestamp timezone requirements, dataclass immutability, and redaction. Use only synthetic fixtures.

## Line-by-line walkthrough

Read the first worked example from top to bottom rather than treating it as a magic recipe. The topic of this lesson is **Testing Security Utilities**. First identify the input: what value, file, record, command, or configuration enters the example? Next identify the operation that changes or examines it. Finally identify the output and ask whether that output is merely an observation or a security conclusion. Python executes statements in order, so the name created on one line must exist before a later line can use it. When a line is a function call, identify the arguments, the function's promised return value, and any visible side effect. When a line is a condition, translate it into an ordinary question before deciding whether the branch is correct.

For each example, copy the code into a fresh file and run it unchanged. Then annotate it without editing the original: write one sentence beside each line describing its role. A useful annotation format is `input`, `transform`, `check`, `decision`, or `output`. After that, change only one value and rerun the program. If the output changes, explain which line observed the changed value. If it does not change, explain why the value was not used or why the rule filtered it. This habit is more valuable than memorizing a finished script because it teaches you to trace unfamiliar security code.

The expected output is evidence about the program, not proof about the outside world. A message such as `review` means that the local rule selected a review label. It does not prove that a person attacked a system. Keep these two statements separate in your notes. Also record failures. A `TypeError`, `ValueError`, timeout, missing-file error, or rejected configuration is often the program correctly refusing an unsafe or ambiguous input. The repair should make the policy clearer rather than hiding the error with a broad catch.

## Prediction experiments

Before each experiment, write a prediction in a comment or notebook. In Experiment A, run the smallest valid input from Example 1 and write the exact output. In Experiment B, replace one valid value with an empty, malformed, missing, or boundary value relevant to **Testing Security Utilities**. Predict whether the program returns a result, raises an exception, rejects the record, or takes a different branch. In Experiment C, repeat the same input twice and inspect whether the program is deterministic. If a timestamp, random value, file order, or shared mutable state changes the result, identify that source of variation explicitly.

Do not use real addresses, credentials, private logs, public targets, or downloaded payloads for these experiments. Use the repository's synthetic fixtures, loopback values, `.invalid` names, and small in-memory inputs. Keep a table with four columns: input, prediction, observed output, and explanation. If the prediction is wrong, do not erase it. The mismatch is the part that teaches you how Python and the rule actually behave.

## Broken example and repair

Start with a deliberately broken version of the lesson's idea. A common beginner mistake is to combine parsing, policy, output, and side effects in one untested block. Another is to trust a value because it has the right shape, to use an unbounded loop, to print raw evidence, or to catch every exception. Break one rule at a time in a local copy. Run the program and capture the exception type or incorrect output. State the invariant that was violated: for example, "the input must be bounded," "the field must be validated before comparison," or "the report must not reveal raw fixture data."

Repair the example in small steps. First separate raw input from the internal value. Second add the narrowest check that expresses the intended policy. Third return or report a safe result. Fourth test one valid case, one invalid case, and one boundary case. Do not claim the repair is secure merely because it runs. Explain what remains outside the lesson's scope, such as authenticity, authorization, deployment configuration, or the correctness of the underlying policy. A good repair is easier for another beginner to inspect because each assumption is visible.

## Guided practice walkthrough

Use the following sequence before attempting the independent numbered questions. Choose one synthetic record related to **Testing Security Utilities** and write down its allowed shape. For example, specify which fields are required, which values are bounded, and which fields must never be printed. Create the smallest input that satisfies the shape. Run the first example and compare the output with your prediction. Add one validation check, rerun the valid record, then test a malformed record. Keep the malformed record in the test set instead of deleting it.

Next, refactor one step into a small function or named stage. Give the stage one job and a name that describes the job. Add a print statement only while debugging, then remove it or replace it with a safe summary. Write one assertion about the result. Finally, explain the data flow in five sentences: where the fixture began, which transformation occurred, which check was applied, what label or value was produced, and what the program deliberately refused to do. Ask a peer to read the explanation without seeing the code and identify any assumption that was not documented.

## Bounded cybersecurity fixture walkthrough

The security application in this lesson uses a local, synthetic fixture. Treat the fixture as untrusted input even though it is stored in the repository. Set a maximum number of records, maximum field length, and maximum output size appropriate to the exercise. Preserve a safe source label such as `training-fixture`, but do not treat that label as proof that the data is authentic. If the fixture contains an indicator-like string, keep it inert and do not resolve, scan, connect to, upload, or enrich it from the network.

A defensible report should distinguish at least four things: what was observed, what rule matched, what uncertainty remains, and what action is permitted in this lab. For example, `observed=synthetic_event`, `rule=high_value`, `confidence=training-only`, and `action=write-local-report`. The last field is a laboratory boundary, not an operational recommendation. If your code cannot make that distinction, stop and improve the report before adding features. Security engineering is not only about detecting a pattern; it is also about limiting authority, preserving provenance, and communicating uncertainty.

At the end, perform a small review. Check that the program uses only local fixtures, has a finite workload, handles malformed input, avoids raw sensitive output, and leaves the fixture unchanged. Then write one residual-risk sentence. A useful form is: "This lesson demonstrates Testing Security Utilities on synthetic data, but it does not establish authenticity, authorization, production readiness, or the presence of a real attack.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples above as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run `python -m course_days.day019`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A test is a repeatable argument for one behavior; a suite becomes useful when it includes failure modes and security properties, not only successful output.

## Limitations

Passing tests do not prove absence of vulnerabilities, correctness of a threat model, or authorization to operate on a real system. They provide bounded evidence.


## References

[1]: https://docs.python.org/3/ "Python documentation"
[2]: https://docs.python.org/3/tutorial/ "The Python tutorial"
[3]: https://owasp.org/www-project-top-ten/ "OWASP Top 10"
[4]: https://csrc.nist.gov/glossary "NIST cybersecurity glossary"

[← Day 18](../day_18_classes_and_dataclasses/day_18_classes_and_dataclasses.md) · [Day index](../DAY_INDEX.md) · [Day 20 →](../day_20_project__log_triage_cli/day_20_project__log_triage_cli.md)
