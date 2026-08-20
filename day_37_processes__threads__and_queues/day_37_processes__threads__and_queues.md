# Day 37: Processes, Threads, and Queues

[← Day 36](../day_36_timeouts_and_resource_limits/day_36_timeouts_and_resource_limits.md) · [Day index](../DAY_INDEX.md) · [Day 38 →](../day_38_async_i_o/day_38_async_i_o.md)









## Table of contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is Processes, Threads, and Queues?](#what-is-processes-threads-and-queues)
  - [Why is Processes, Threads, and Queues useful?](#why-is-processes-threads-and-queues-useful)
  - [How will Python use this idea?](#how-will-python-use-this-idea)
  - [What are the security limits?](#what-are-the-security-limits)
- [Worked examples](#worked-examples)
  - [Example 1: Use a thread pool](#example-1-use-a-thread-pool)
  - [Example 2: Use a process pool carefully](#example-2-use-a-process-pool-carefully)
  - [Example 3: Bound work](#example-3-bound-work)
  - [Example 4: Queue a result](#example-4-queue-a-result)
  - [Example 5: Preserve errors](#example-5-preserve-errors)
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

Concurrency can reduce waiting time, but it also creates shared state, ordering, cancellation, and resource problems. A security tool should prefer predictable bounded concurrency over maximum parallelism.

## Prerequisites

Complete Day 36 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 37

## The problem

Process several local fixture items with a small worker pool and preserve a safe result for each item.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Keywords and terms

A **thread** shares memory within one process. A **process** has a separate memory space. A **queue** coordinates producers and consumers. A **race condition** occurs when outcome depends on timing.

## Topics

### What is Processes, Threads, and Queues?

Concurrency can reduce waiting time, but it also creates shared state, ordering, cancellation, and resource problems. A security tool should prefer predictable bounded concurrency over maximum parallelism.

### Why is Processes, Threads, and Queues useful?

Process several local fixture items with a small worker pool and preserve a safe result for each item.

### How will Python use this idea?

Read the worked examples next. For each one, identify the input, the operation, the result, and the boundary that prevents the example from doing more than the lesson allows.

### What are the security limits?

The examples remain local, synthetic, bounded, and authorized. A successful program run demonstrates behavior on the fixture; it does not prove authenticity, compromise, or permission to act on a real target.

## Worked examples

### Example 1: Use a thread pool

Threads suit small I/O waits in a local fixture.

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(str.upper, ["a", "b"]))
print(results)
```

**What to observe:**

`['A', 'B']`

### Example 2: Use a process pool carefully

Separate processes have higher overhead and clearer memory boundaries.

```python
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(abs, [-2, 3]))
print(results)
```

**What to observe:**

`[2, 3]`

### Example 3: Bound work

The worker count is an explicit resource choice.

```python
max_workers = min(4, 2)
print(max_workers)
```

**What to observe:**

The tool never creates an unbounded number of workers.

### Example 4: Queue a result

A queue can separate collection from processing.

```python
from queue import Queue

queue = Queue()
queue.put({"status": "accepted"})
print(queue.get())
```

**What to observe:**

The result moves through the queue.

### Example 5: Preserve errors

A worker failure must be returned or raised, not silently discarded.

```python
def safe_call(function, value):
    try:
        return {"ok": True, "value": function(value)}
    except Exception as error:
        return {"ok": False, "error": type(error).__name__}
```

**What to observe:**

The caller can count failed work.

## Read the first example line by line

The first runnable example introduces **Processes, Threads, and Queues**. Copy it into a new file and run it before changing anything. Then use this table to read the same code slowly. A line-by-line explanation does not replace practice: it shows you what to look for when a program behaves differently from your prediction.

| Line | Code | What Python is doing |
| ---: | --- | --- |
| 1 | `from concurrent.futures import ThreadPoolExecutor` | Import statement: the program asks for code from a module. |
| 2 | `` | Blank line: it separates ideas for the human reader. |
| 3 | `with ThreadPoolExecutor(max_workers=2) as pool:` | Assignment: Python evaluates the right side and stores the result under the name on the left. |
| 4 | `results = list(pool.map(str.upper, ["a", "b"]))` | Assignment: Python evaluates the right side and stores the result under the name on the left. |
| 5 | `print(results)` | Output call: Python evaluates the argument and writes a representation to the terminal. |

After the run, write down the value created by each assignment, the condition tested by each branch, and the output that appeared. Change one input only. If the result changes, identify the line that used that input. If the result does not change, explain why the input was not part of the decision. This is the same tracing habit used later when reviewing security automation.
## Execution trace

The coordinator creates a bounded set of workers, submits local work, collects results, and shuts down the pool. Ordering and failure behavior are part of the report contract.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| one worker per item | resource exhaustion | cap workers |
| shared mutable state | results depend on timing | return values or protect state |
| swallow worker errors | incomplete report looks successful | preserve error records |
| assume order | output changes run to run | attach identifiers and sort explicitly |
| no shutdown | threads/processes remain | use a context manager |

## Security application

Run concurrency only over local synthetic records. Do not use it to increase scanning, guessing, or request volume against another system.

## Line-by-line walkthrough

Read the first worked example from top to bottom rather than treating it as a magic recipe. The topic of this lesson is **Processes, Threads, and Queues**. First identify the input: what value, file, record, command, or configuration enters the example? Next identify the operation that changes or examines it. Finally identify the output and ask whether that output is merely an observation or a security conclusion. Python executes statements in order, so the name created on one line must exist before a later line can use it. When a line is a function call, identify the arguments, the function's promised return value, and any visible side effect. When a line is a condition, translate it into an ordinary question before deciding whether the branch is correct.

For each example, copy the code into a fresh file and run it unchanged. Then annotate it without editing the original: write one sentence beside each line describing its role. A useful annotation format is `input`, `transform`, `check`, `decision`, or `output`. After that, change only one value and rerun the program. If the output changes, explain which line observed the changed value. If it does not change, explain why the value was not used or why the rule filtered it. This habit is more valuable than memorizing a finished script because it teaches you to trace unfamiliar security code.

The expected output is evidence about the program, not proof about the outside world. A message such as `review` means that the local rule selected a review label. It does not prove that a person attacked a system. Keep these two statements separate in your notes. Also record failures. A `TypeError`, `ValueError`, timeout, missing-file error, or rejected configuration is often the program correctly refusing an unsafe or ambiguous input. The repair should make the policy clearer rather than hiding the error with a broad catch.

## Prediction experiments

Before each experiment, write a prediction in a comment or notebook. In Experiment A, run the smallest valid input from Example 1 and write the exact output. In Experiment B, replace one valid value with an empty, malformed, missing, or boundary value relevant to **Processes, Threads, and Queues**. Predict whether the program returns a result, raises an exception, rejects the record, or takes a different branch. In Experiment C, repeat the same input twice and inspect whether the program is deterministic. If a timestamp, random value, file order, or shared mutable state changes the result, identify that source of variation explicitly.

Do not use real addresses, credentials, private logs, public targets, or downloaded payloads for these experiments. Use the repository's synthetic fixtures, loopback values, `.invalid` names, and small in-memory inputs. Keep a table with four columns: input, prediction, observed output, and explanation. If the prediction is wrong, do not erase it. The mismatch is the part that teaches you how Python and the rule actually behave.

## Broken example and repair

Start with a deliberately broken version of the lesson's idea. A common beginner mistake is to combine parsing, policy, output, and side effects in one untested block. Another is to trust a value because it has the right shape, to use an unbounded loop, to print raw evidence, or to catch every exception. Break one rule at a time in a local copy. Run the program and capture the exception type or incorrect output. State the invariant that was violated: for example, "the input must be bounded," "the field must be validated before comparison," or "the report must not reveal raw fixture data."

Repair the example in small steps. First separate raw input from the internal value. Second add the narrowest check that expresses the intended policy. Third return or report a safe result. Fourth test one valid case, one invalid case, and one boundary case. Do not claim the repair is secure merely because it runs. Explain what remains outside the lesson's scope, such as authenticity, authorization, deployment configuration, or the correctness of the underlying policy. A good repair is easier for another beginner to inspect because each assumption is visible.

## Guided practice walkthrough

Use the following sequence before attempting the independent numbered questions. Choose one synthetic record related to **Processes, Threads, and Queues** and write down its allowed shape. For example, specify which fields are required, which values are bounded, and which fields must never be printed. Create the smallest input that satisfies the shape. Run the first example and compare the output with your prediction. Add one validation check, rerun the valid record, then test a malformed record. Keep the malformed record in the test set instead of deleting it.

Next, refactor one step into a small function or named stage. Give the stage one job and a name that describes the job. Add a print statement only while debugging, then remove it or replace it with a safe summary. Write one assertion about the result. Finally, explain the data flow in five sentences: where the fixture began, which transformation occurred, which check was applied, what label or value was produced, and what the program deliberately refused to do. Ask a peer to read the explanation without seeing the code and identify any assumption that was not documented.

## Bounded cybersecurity fixture walkthrough

The security application in this lesson uses a local, synthetic fixture. Treat the fixture as untrusted input even though it is stored in the repository. Set a maximum number of records, maximum field length, and maximum output size appropriate to the exercise. Preserve a safe source label such as `training-fixture`, but do not treat that label as proof that the data is authentic. If the fixture contains an indicator-like string, keep it inert and do not resolve, scan, connect to, upload, or enrich it from the network.

A defensible report should distinguish at least four things: what was observed, what rule matched, what uncertainty remains, and what action is permitted in this lab. For example, `observed=synthetic_event`, `rule=high_value`, `confidence=training-only`, and `action=write-local-report`. The last field is a laboratory boundary, not an operational recommendation. If your code cannot make that distinction, stop and improve the report before adding features. Security engineering is not only about detecting a pattern; it is also about limiting authority, preserving provenance, and communicating uncertainty.

At the end, perform a small review. Check that the program uses only local fixtures, has a finite workload, handles malformed input, avoids raw sensitive output, and leaves the fixture unchanged. Then write one residual-risk sentence. A useful form is: "This lesson demonstrates Processes, Threads, and Queues on synthetic data, but it does not establish authenticity, authorization, production readiness, or the presence of a real attack.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run every requested command, create the requested artifact, and record the limitation the exercise asks you to name.

## Finish line

Run `python -m course_days.day37`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Concurrency is a coordination problem with a resource budget, not a magic speed switch.

## Limitations

Concurrency bugs can be nondeterministic and platform-dependent. Tests should use small deterministic fixtures and explicit synchronization.


## References

[1]: https://docs.python.org/3/ "Python documentation"
[2]: https://docs.python.org/3/tutorial/ "The Python tutorial"
[3]: https://owasp.org/www-project-top-ten/ "OWASP Top 10"
[4]: https://csrc.nist.gov/glossary "NIST cybersecurity glossary"

[← Day 36](../day_36_timeouts_and_resource_limits/day_36_timeouts_and_resource_limits.md) · [Day index](../DAY_INDEX.md) · [Day 38 →](../day_38_async_i_o/day_38_async_i_o.md)
