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

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples above as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run `python -m course_days.day019`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A test is a repeatable argument for one behavior; a suite becomes useful when it includes failure modes and security properties, not only successful output.

## Limitations

Passing tests do not prove absence of vulnerabilities, correctness of a threat model, or authorization to operate on a real system. They provide bounded evidence.

[← Day 18](../day_18_classes_and_dataclasses/day_18_classes_and_dataclasses.md) · [Day index](../DAY_INDEX.md) · [Day 20 →](../day_20_project__log_triage_cli/day_20_project__log_triage_cli.md)
