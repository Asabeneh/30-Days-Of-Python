# Day 93: Safe Service Discovery

[← Day 92](../day_92_asset_inventory/day_92_asset_inventory.md) · [Day index](../DAY_INDEX.md) · [Day 94 →](../day_94_cve_and_severity_reasoning/day_94_cve_and_severity_reasoning.md)









## Table of contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is Safe Service Discovery?](#what-is-safe-service-discovery)
  - [Why is Safe Service Discovery useful?](#why-is-safe-service-discovery-useful)
  - [How will Python use this idea?](#how-will-python-use-this-idea)
  - [What are the security limits?](#what-are-the-security-limits)
- [Worked examples](#worked-examples)
  - [Example 1: Read targets](#example-1-read-targets)
  - [Example 2: Validate endpoint](#example-2-validate-endpoint)
  - [Example 3: Check one service](#example-3-check-one-service)
  - [Example 4: Classify result](#example-4-classify-result)
  - [Example 5: Stop after inventory](#example-5-stop-after-inventory)
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

Discovery can be useful in a disposable lab and dangerous on an unowned network. The safe pattern is to use a supplied target list and verify one endpoint rather than scan ranges.

## Prerequisites

Complete Day 92. Use only the local fixtures and explicit loopback assessment scope supplied by the course.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using a tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Check one approved local service from an explicit inventory and report unavailable versus closed without scanning.

## Security boundary

This lesson is educational and authorized-lab-only. It does not authorize public scanning, credential guessing, exploitation, interception, persistence, or changes to systems you do not own.

## Keywords and terms

Discovery identifies reachable services. An allowlist is a fixed target set. A health check is a known request. A timeout limits waiting.

## Topics

### What is Safe Service Discovery?

Discovery can be useful in a disposable lab and dangerous on an unowned network. The safe pattern is to use a supplied target list and verify one endpoint rather than scan ranges.

### Why is Safe Service Discovery useful?

Check one approved local service from an explicit inventory and report unavailable versus closed without scanning.

### How will Python use this idea?

Read the worked examples next. For each one, identify the input, the operation, the result, and the boundary that prevents the example from doing more than the lesson allows.

### What are the security limits?

The examples remain local, synthetic, bounded, and authorized. A successful program run demonstrates behavior on the fixture; it does not prove authenticity, compromise, or permission to act on a real target.

## Worked examples

### Example 1: Read targets

Discovery begins with approved inventory, not guesses.

```python
targets = [{"host": "127.0.0.1", "port": 8000, "purpose": "training"}]
print(targets)
```

**What to observe:**

The target is explicit.

### Example 2: Validate endpoint

Reject targets outside the lab policy.

```python
target = targets[0]
print(target["host"] == "127.0.0.1")
```

**What to observe:**

Only loopback passes this example.

### Example 3: Check one service

A connection attempt is still an authorized action.

```python
check = {"target": "127.0.0.1:8000", "timeout": 1, "request": "health"}
print(check)
```

**What to observe:**

The operation is bounded.

### Example 4: Classify result

Unavailable and refused are different observations.

```python
print({"status": "unavailable", "meaning": "no conclusion about cause"})
```

**What to observe:**

The interpretation is neutral.

### Example 5: Stop after inventory

Do not turn one check into a range scan.

```python
print({"targets_checked": 1, "range_scan": False})
```

**What to observe:**

Scope is recorded.

## Read the first example line by line

The first runnable example introduces **Safe Service Discovery**. Copy it into a new file and run it before changing anything. Then use this table to read the same code slowly. A line-by-line explanation does not replace practice: it shows you what to look for when a program behaves differently from your prediction.

| Line | Code | What Python is doing |
| ---: | --- | --- |
| 1 | `targets = [{"host": "127.0.0.1", "port": 8000, "purpose": "training"}]` | Assignment: Python evaluates the right side and stores the result under the name on the left. |
| 2 | `print(targets)` | Output call: Python evaluates the argument and writes a representation to the terminal. |

After the run, write down the value created by each assignment, the condition tested by each branch, and the output that appeared. Change one input only. If the result changes, identify the line that used that input. If the result does not change, explain why the input was not part of the decision. This is the same tracing habit used later when reviewing security automation.
## Execution trace

The tool loads an approved target, validates the host and port, performs one finite health check, records the transport result, and exits without expanding the target set.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| scan subnet | unauthorized reconnaissance | use one supplied target |
| retry many ports | scope expands | fixed endpoint |
| timeout means closed | cause is overclaimed | report unknown/unavailable |
| follow redirects | target changes | revalidate or disable |
| no log of scope | review cannot verify | record target count |

## Security application

Use loopback and a disposable service only. No range scans, port sweeps, banner grabbing, or public targets.

## Line-by-line walkthrough

Read the first worked example from top to bottom rather than treating it as a magic recipe. The topic of this lesson is **Safe Service Discovery**. First identify the input: what value, file, record, command, or configuration enters the example? Next identify the operation that changes or examines it. Finally identify the output and ask whether that output is merely an observation or a security conclusion. Python executes statements in order, so the name created on one line must exist before a later line can use it. When a line is a function call, identify the arguments, the function's promised return value, and any visible side effect. When a line is a condition, translate it into an ordinary question before deciding whether the branch is correct.

For each example, copy the code into a fresh file and run it unchanged. Then annotate it without editing the original: write one sentence beside each line describing its role. A useful annotation format is `input`, `transform`, `check`, `decision`, or `output`. After that, change only one value and rerun the program. If the output changes, explain which line observed the changed value. If it does not change, explain why the value was not used or why the rule filtered it. This habit is more valuable than memorizing a finished script because it teaches you to trace unfamiliar security code.

The expected output is evidence about the program, not proof about the outside world. A message such as `review` means that the local rule selected a review label. It does not prove that a person attacked a system. Keep these two statements separate in your notes. Also record failures. A `TypeError`, `ValueError`, timeout, missing-file error, or rejected configuration is often the program correctly refusing an unsafe or ambiguous input. The repair should make the policy clearer rather than hiding the error with a broad catch.

## Prediction experiments

Before each experiment, write a prediction in a comment or notebook. In Experiment A, run the smallest valid input from Example 1 and write the exact output. In Experiment B, replace one valid value with an empty, malformed, missing, or boundary value relevant to **Safe Service Discovery**. Predict whether the program returns a result, raises an exception, rejects the record, or takes a different branch. In Experiment C, repeat the same input twice and inspect whether the program is deterministic. If a timestamp, random value, file order, or shared mutable state changes the result, identify that source of variation explicitly.

Do not use real addresses, credentials, private logs, public targets, or downloaded payloads for these experiments. Use the repository's synthetic fixtures, loopback values, `.invalid` names, and small in-memory inputs. Keep a table with four columns: input, prediction, observed output, and explanation. If the prediction is wrong, do not erase it. The mismatch is the part that teaches you how Python and the rule actually behave.

## Broken example and repair

Start with a deliberately broken version of the lesson's idea. A common beginner mistake is to combine parsing, policy, output, and side effects in one untested block. Another is to trust a value because it has the right shape, to use an unbounded loop, to print raw evidence, or to catch every exception. Break one rule at a time in a local copy. Run the program and capture the exception type or incorrect output. State the invariant that was violated: for example, "the input must be bounded," "the field must be validated before comparison," or "the report must not reveal raw fixture data."

Repair the example in small steps. First separate raw input from the internal value. Second add the narrowest check that expresses the intended policy. Third return or report a safe result. Fourth test one valid case, one invalid case, and one boundary case. Do not claim the repair is secure merely because it runs. Explain what remains outside the lesson's scope, such as authenticity, authorization, deployment configuration, or the correctness of the underlying policy. A good repair is easier for another beginner to inspect because each assumption is visible.

## Guided practice walkthrough

Use the following sequence before attempting the independent numbered questions. Choose one synthetic record related to **Safe Service Discovery** and write down its allowed shape. For example, specify which fields are required, which values are bounded, and which fields must never be printed. Create the smallest input that satisfies the shape. Run the first example and compare the output with your prediction. Add one validation check, rerun the valid record, then test a malformed record. Keep the malformed record in the test set instead of deleting it.

Next, refactor one step into a small function or named stage. Give the stage one job and a name that describes the job. Add a print statement only while debugging, then remove it or replace it with a safe summary. Write one assertion about the result. Finally, explain the data flow in five sentences: where the fixture began, which transformation occurred, which check was applied, what label or value was produced, and what the program deliberately refused to do. Ask a peer to read the explanation without seeing the code and identify any assumption that was not documented.

## Bounded cybersecurity fixture walkthrough

The security application in this lesson uses a local, synthetic fixture. Treat the fixture as untrusted input even though it is stored in the repository. Set a maximum number of records, maximum field length, and maximum output size appropriate to the exercise. Preserve a safe source label such as `training-fixture`, but do not treat that label as proof that the data is authentic. If the fixture contains an indicator-like string, keep it inert and do not resolve, scan, connect to, upload, or enrich it from the network.

A defensible report should distinguish at least four things: what was observed, what rule matched, what uncertainty remains, and what action is permitted in this lab. For example, `observed=synthetic_event`, `rule=high_value`, `confidence=training-only`, and `action=write-local-report`. The last field is a laboratory boundary, not an operational recommendation. If your code cannot make that distinction, stop and improve the report before adding features. Security engineering is not only about detecting a pattern; it is also about limiting authority, preserving provenance, and communicating uncertainty.

At the end, perform a small review. Check that the program uses only local fixtures, has a finite workload, handles malformed input, avoids raw sensitive output, and leaves the fixture unchanged. Then write one residual-risk sentence. A useful form is: "This lesson demonstrates Safe Service Discovery on synthetic data, but it does not establish authenticity, authorization, production readiness, or the presence of a real attack.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the requested evidence, expected behavior, edge case, and limitation.

## Finish line

Run `python -m course_days.day93`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Safe discovery is an approved inventory check with a finite target and neutral result interpretation.

## Limitations

A failed connection can be caused by policy, routing, service state, or timeout; it does not reveal intent.


## References

[1]: https://docs.python.org/3/ "Python documentation"
[2]: https://docs.python.org/3/tutorial/ "The Python tutorial"
[3]: https://owasp.org/www-project-top-ten/ "OWASP Top 10"
[4]: https://csrc.nist.gov/glossary "NIST cybersecurity glossary"

[← Day 92](../day_92_asset_inventory/day_92_asset_inventory.md) · [Day index](../DAY_INDEX.md) · [Day 94 →](../day_94_cve_and_severity_reasoning/day_94_cve_and_severity_reasoning.md)
