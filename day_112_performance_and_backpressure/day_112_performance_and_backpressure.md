# Day 112: Performance and Backpressure

[← Day 111](../day_111_security_tool_architecture/day_111_security_tool_architecture.md) · [Day index](../DAY_INDEX.md) · [Day 113 →](../day_113_advanced_concurrency/day_113_advanced_concurrency.md)









## Table of contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is Performance and Backpressure?](#what-is-performance-and-backpressure)
  - [Why is Performance and Backpressure useful?](#why-is-performance-and-backpressure-useful)
  - [How will Python use this idea?](#how-will-python-use-this-idea)
  - [What are the security limits?](#what-are-the-security-limits)
- [Worked examples](#worked-examples)
  - [Example 1: Measure a count](#example-1-measure-a-count)
  - [Example 2: Bound a queue](#example-2-bound-a-queue)
  - [Example 3: Reject or wait](#example-3-reject-or-wait)
  - [Example 4: Batch work](#example-4-batch-work)
  - [Example 5: Report incomplete work](#example-5-report-incomplete-work)
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

Performance is a security property when slow or oversized work can exhaust a service. Measure first, then choose bounded queues, batching, streaming, and rejection policies.

## Prerequisites

Complete Day 111. Work from a clean virtual environment and use only local synthetic fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using it
- run and modify all worked examples
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Process a synthetic stream with a bounded queue and explain what happens when the consumer is slower than the producer.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, destructive actions, persistence, or processing of private data.

## Keywords and terms

Throughput is work per time. Latency is time per operation. Backpressure limits producers. A queue is a buffer. Rejection is an explicit resource policy.

## Topics

### What is Performance and Backpressure?

Performance is a security property when slow or oversized work can exhaust a service. Measure first, then choose bounded queues, batching, streaming, and rejection policies.

### Why is Performance and Backpressure useful?

Process a synthetic stream with a bounded queue and explain what happens when the consumer is slower than the producer.

### How will Python use this idea?

Read the worked examples next. For each one, identify the input, the operation, the result, and the boundary that prevents the example from doing more than the lesson allows.

### What are the security limits?

The examples remain local, synthetic, bounded, and authorized. A successful program run demonstrates behavior on the fixture; it does not prove authenticity, compromise, or permission to act on a real target.

## Worked examples

### Example 1: Measure a count

Begin with a simple workload measurement.

```python
processed = 100
seconds = 2
print(processed / seconds)
```

**What to observe:**

50 records per second.

### Example 2: Bound a queue

A finite queue prevents unlimited memory growth.

```python
from queue import Queue

queue = Queue(maxsize=3)
print(queue.maxsize)
```

**What to observe:**

The capacity is explicit.

### Example 3: Reject or wait

When full, the producer needs a policy.

```python
policy = {"full_queue": "wait briefly then reject", "report": "backpressure"}
print(policy)
```

**What to observe:**

The behavior is documented.

### Example 4: Batch work

Batches can reduce overhead but increase latency and memory.

```python
batch = [1, 2, 3]
print({"size": len(batch), "max": 100})
```

**What to observe:**

The batch has a bound.

### Example 5: Report incomplete work

Dropped or rejected work must be visible.

```python
print({"accepted": 98, "rejected": 2, "complete": False})
```

**What to observe:**

The result does not look perfect.

## Read the first example line by line

The first runnable example introduces **Performance and Backpressure**. Copy it into a new file and run it before changing anything. Then use this table to read the same code slowly. A line-by-line explanation does not replace practice: it shows you what to look for when a program behaves differently from your prediction.

| Line | Code | What Python is doing |
| ---: | --- | --- |
| 1 | `processed = 100` | Assignment: Python evaluates the right side and stores the result under the name on the left. |
| 2 | `seconds = 2` | Assignment: Python evaluates the right side and stores the result under the name on the left. |
| 3 | `print(processed / seconds)` | Output call: Python evaluates the argument and writes a representation to the terminal. |

After the run, write down the value created by each assignment, the condition tested by each branch, and the output that appeared. Change one input only. If the result changes, identify the line that used that input. If the result does not change, explain why the input was not part of the decision. This is the same tracing habit used later when reviewing security automation.
## Execution trace

The producer creates bounded work, the queue applies backpressure, the consumer processes within a resource budget, and the report records accepted, rejected, and incomplete items.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| benchmark synthetic only | real workload differs | state assumptions |
| unbounded queue | memory exhaustion | cap capacity |
| drop silently | detection gaps | report rejection |
| batch unlimited | latency/memory grows | cap batch |
| optimize before measure | complexity without benefit | measure first |

## Security application

Use small synthetic workloads and local timing. Do not generate load against any external system.

## Line-by-line walkthrough

Read the first worked example from top to bottom rather than treating it as a magic recipe. The topic of this lesson is **Performance and Backpressure**. First identify the input: what value, file, record, command, or configuration enters the example? Next identify the operation that changes or examines it. Finally identify the output and ask whether that output is merely an observation or a security conclusion. Python executes statements in order, so the name created on one line must exist before a later line can use it. When a line is a function call, identify the arguments, the function's promised return value, and any visible side effect. When a line is a condition, translate it into an ordinary question before deciding whether the branch is correct.

For each example, copy the code into a fresh file and run it unchanged. Then annotate it without editing the original: write one sentence beside each line describing its role. A useful annotation format is `input`, `transform`, `check`, `decision`, or `output`. After that, change only one value and rerun the program. If the output changes, explain which line observed the changed value. If it does not change, explain why the value was not used or why the rule filtered it. This habit is more valuable than memorizing a finished script because it teaches you to trace unfamiliar security code.

The expected output is evidence about the program, not proof about the outside world. A message such as `review` means that the local rule selected a review label. It does not prove that a person attacked a system. Keep these two statements separate in your notes. Also record failures. A `TypeError`, `ValueError`, timeout, missing-file error, or rejected configuration is often the program correctly refusing an unsafe or ambiguous input. The repair should make the policy clearer rather than hiding the error with a broad catch.

## Prediction experiments

Before each experiment, write a prediction in a comment or notebook. In Experiment A, run the smallest valid input from Example 1 and write the exact output. In Experiment B, replace one valid value with an empty, malformed, missing, or boundary value relevant to **Performance and Backpressure**. Predict whether the program returns a result, raises an exception, rejects the record, or takes a different branch. In Experiment C, repeat the same input twice and inspect whether the program is deterministic. If a timestamp, random value, file order, or shared mutable state changes the result, identify that source of variation explicitly.

Do not use real addresses, credentials, private logs, public targets, or downloaded payloads for these experiments. Use the repository's synthetic fixtures, loopback values, `.invalid` names, and small in-memory inputs. Keep a table with four columns: input, prediction, observed output, and explanation. If the prediction is wrong, do not erase it. The mismatch is the part that teaches you how Python and the rule actually behave.

## Broken example and repair

Start with a deliberately broken version of the lesson's idea. A common beginner mistake is to combine parsing, policy, output, and side effects in one untested block. Another is to trust a value because it has the right shape, to use an unbounded loop, to print raw evidence, or to catch every exception. Break one rule at a time in a local copy. Run the program and capture the exception type or incorrect output. State the invariant that was violated: for example, "the input must be bounded," "the field must be validated before comparison," or "the report must not reveal raw fixture data."

Repair the example in small steps. First separate raw input from the internal value. Second add the narrowest check that expresses the intended policy. Third return or report a safe result. Fourth test one valid case, one invalid case, and one boundary case. Do not claim the repair is secure merely because it runs. Explain what remains outside the lesson's scope, such as authenticity, authorization, deployment configuration, or the correctness of the underlying policy. A good repair is easier for another beginner to inspect because each assumption is visible.

## Guided practice walkthrough

Use the following sequence before attempting the independent numbered questions. Choose one synthetic record related to **Performance and Backpressure** and write down its allowed shape. For example, specify which fields are required, which values are bounded, and which fields must never be printed. Create the smallest input that satisfies the shape. Run the first example and compare the output with your prediction. Add one validation check, rerun the valid record, then test a malformed record. Keep the malformed record in the test set instead of deleting it.

Next, refactor one step into a small function or named stage. Give the stage one job and a name that describes the job. Add a print statement only while debugging, then remove it or replace it with a safe summary. Write one assertion about the result. Finally, explain the data flow in five sentences: where the fixture began, which transformation occurred, which check was applied, what label or value was produced, and what the program deliberately refused to do. Ask a peer to read the explanation without seeing the code and identify any assumption that was not documented.

## Bounded cybersecurity fixture walkthrough

The security application in this lesson uses a local, synthetic fixture. Treat the fixture as untrusted input even though it is stored in the repository. Set a maximum number of records, maximum field length, and maximum output size appropriate to the exercise. Preserve a safe source label such as `training-fixture`, but do not treat that label as proof that the data is authentic. If the fixture contains an indicator-like string, keep it inert and do not resolve, scan, connect to, upload, or enrich it from the network.

A defensible report should distinguish at least four things: what was observed, what rule matched, what uncertainty remains, and what action is permitted in this lab. For example, `observed=synthetic_event`, `rule=high_value`, `confidence=training-only`, and `action=write-local-report`. The last field is a laboratory boundary, not an operational recommendation. If your code cannot make that distinction, stop and improve the report before adding features. Security engineering is not only about detecting a pattern; it is also about limiting authority, preserving provenance, and communicating uncertainty.

At the end, perform a small review. Check that the program uses only local fixtures, has a finite workload, handles malformed input, avoids raw sensitive output, and leaves the fixture unchanged. Then write one residual-risk sentence. A useful form is: "This lesson demonstrates Performance and Backpressure on synthetic data, but it does not establish authenticity, authorization, production readiness, or the presence of a real attack.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the evidence, output, edge case, and limitation requested by each question.

## Finish line

Run `python -m course_days.day112`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Performance safety is bounded work plus honest accounting of what was rejected or delayed.

## Limitations

Benchmarks vary by hardware, input, Python version, and contention; capacity needs production measurement.


## References

[1]: https://docs.python.org/3/ "Python documentation"
[2]: https://docs.python.org/3/tutorial/ "The Python tutorial"
[3]: https://owasp.org/www-project-top-ten/ "OWASP Top 10"
[4]: https://csrc.nist.gov/glossary "NIST cybersecurity glossary"

[← Day 111](../day_111_security_tool_architecture/day_111_security_tool_architecture.md) · [Day index](../DAY_INDEX.md) · [Day 113 →](../day_113_advanced_concurrency/day_113_advanced_concurrency.md)
