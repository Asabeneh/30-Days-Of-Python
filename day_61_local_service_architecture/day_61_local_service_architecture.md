# Day 61: Local Service Architecture

[← Day 60](../day_60_project__tamper_evident_case_bundle/day_60_project__tamper_evident_case_bundle.md) · [Day index](../DAY_INDEX.md) · [Day 62 →](../day_62_request_parsing_and_validation/day_62_request_parsing_and_validation.md)

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

A web service is a pipeline of request parsing, validation, authorization, business logic, and response construction. Drawing those boundaries before coding makes security behavior testable.

## Prerequisites

Complete Day 60. Use only the local course fixtures, loopback services, and synthetic records described by the lesson.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using the tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state the trust boundary and residual risk
- complete the numbered cybersecurity exercises

## The problem

Sketch a local case API that accepts a request, validates it, checks authorization, and returns a safe response without touching a real account.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, interception, exploit delivery, real-user profiling, or changes to systems you do not own.

## Lesson

### Vocabulary

A request is untrusted input. A handler coordinates work. A service layer applies policy. A repository stores data. A response is an output boundary.

## Worked examples

### Example 1: Draw the flow

Make the stages visible before implementation.

```python
stages = ["request", "parse", "validate", "authorize", "service", "response"]
print(" -> ".join(stages))
```

**What to observe:**

The request path is explicit.

### Example 2: Use a typed request

A boundary object separates raw data from internal fields.

```python
request = {"case_id": "training-061", "action": "read"}
print(request)
```

**What to observe:**

The raw input is still subject to validation.

### Example 3: Return a result

Handlers should return data and status rather than print.

```python
response = {"status": 200, "body": {"case_id": "training-061"}}
print(response)
```

**What to observe:**

The response is structured.

### Example 4: Name a trust boundary

The service should state where authorization is checked.

```python
boundary = {
    "untrusted": "HTTP body",
    "trusted_after": "validated authorization decision",
}
print(boundary)
```

**What to observe:**

The policy location is visible.

### Example 5: Keep local scope

A training service needs an explicit target and reset.

```python
scope = {"host": "127.0.0.1", "data": "synthetic", "reset": "delete training DB"}
print(scope)
```

**What to observe:**

The service is bounded.

## Execution trace

The request enters as bytes or text, becomes a parsed object, passes schema and authorization checks, reaches a service function, and returns a minimal response. No stage should silently skip the previous boundary.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| auth in UI only | direct calls bypass it | enforce at service boundary |
| handler does everything | tests and review are hard | separate layers |
| return raw exception | internal data leaks | safe error response |
| global mutable state | tests affect each other | explicit dependencies |
| local API becomes public | scope expands | bind to loopback and document |

## Security application

Build only a local synthetic API. Do not add account management, public deployment, credential collection, or real case data.

## Line-by-line walkthrough

Read the first worked example from top to bottom rather than treating it as a magic recipe. The topic of this lesson is **Local Service Architecture**. First identify the input: what value, file, record, command, or configuration enters the example? Next identify the operation that changes or examines it. Finally identify the output and ask whether that output is merely an observation or a security conclusion. Python executes statements in order, so the name created on one line must exist before a later line can use it. When a line is a function call, identify the arguments, the function's promised return value, and any visible side effect. When a line is a condition, translate it into an ordinary question before deciding whether the branch is correct.

For each example, copy the code into a fresh file and run it unchanged. Then annotate it without editing the original: write one sentence beside each line describing its role. A useful annotation format is `input`, `transform`, `check`, `decision`, or `output`. After that, change only one value and rerun the program. If the output changes, explain which line observed the changed value. If it does not change, explain why the value was not used or why the rule filtered it. This habit is more valuable than memorizing a finished script because it teaches you to trace unfamiliar security code.

The expected output is evidence about the program, not proof about the outside world. A message such as `review` means that the local rule selected a review label. It does not prove that a person attacked a system. Keep these two statements separate in your notes. Also record failures. A `TypeError`, `ValueError`, timeout, missing-file error, or rejected configuration is often the program correctly refusing an unsafe or ambiguous input. The repair should make the policy clearer rather than hiding the error with a broad catch.

## Prediction experiments

Before each experiment, write a prediction in a comment or notebook. In Experiment A, run the smallest valid input from Example 1 and write the exact output. In Experiment B, replace one valid value with an empty, malformed, missing, or boundary value relevant to **Local Service Architecture**. Predict whether the program returns a result, raises an exception, rejects the record, or takes a different branch. In Experiment C, repeat the same input twice and inspect whether the program is deterministic. If a timestamp, random value, file order, or shared mutable state changes the result, identify that source of variation explicitly.

Do not use real addresses, credentials, private logs, public targets, or downloaded payloads for these experiments. Use the repository's synthetic fixtures, loopback values, `.invalid` names, and small in-memory inputs. Keep a table with four columns: input, prediction, observed output, and explanation. If the prediction is wrong, do not erase it. The mismatch is the part that teaches you how Python and the rule actually behave.

## Broken example and repair

Start with a deliberately broken version of the lesson's idea. A common beginner mistake is to combine parsing, policy, output, and side effects in one untested block. Another is to trust a value because it has the right shape, to use an unbounded loop, to print raw evidence, or to catch every exception. Break one rule at a time in a local copy. Run the program and capture the exception type or incorrect output. State the invariant that was violated: for example, "the input must be bounded," "the field must be validated before comparison," or "the report must not reveal raw fixture data."

Repair the example in small steps. First separate raw input from the internal value. Second add the narrowest check that expresses the intended policy. Third return or report a safe result. Fourth test one valid case, one invalid case, and one boundary case. Do not claim the repair is secure merely because it runs. Explain what remains outside the lesson's scope, such as authenticity, authorization, deployment configuration, or the correctness of the underlying policy. A good repair is easier for another beginner to inspect because each assumption is visible.

## Guided practice walkthrough

Use the following sequence before attempting the independent numbered questions. Choose one synthetic record related to **Local Service Architecture** and write down its allowed shape. For example, specify which fields are required, which values are bounded, and which fields must never be printed. Create the smallest input that satisfies the shape. Run the first example and compare the output with your prediction. Add one validation check, rerun the valid record, then test a malformed record. Keep the malformed record in the test set instead of deleting it.

Next, refactor one step into a small function or named stage. Give the stage one job and a name that describes the job. Add a print statement only while debugging, then remove it or replace it with a safe summary. Write one assertion about the result. Finally, explain the data flow in five sentences: where the fixture began, which transformation occurred, which check was applied, what label or value was produced, and what the program deliberately refused to do. Ask a peer to read the explanation without seeing the code and identify any assumption that was not documented.

## Bounded cybersecurity fixture walkthrough

The security application in this lesson uses a local, synthetic fixture. Treat the fixture as untrusted input even though it is stored in the repository. Set a maximum number of records, maximum field length, and maximum output size appropriate to the exercise. Preserve a safe source label such as `training-fixture`, but do not treat that label as proof that the data is authentic. If the fixture contains an indicator-like string, keep it inert and do not resolve, scan, connect to, upload, or enrich it from the network.

A defensible report should distinguish at least four things: what was observed, what rule matched, what uncertainty remains, and what action is permitted in this lab. For example, `observed=synthetic_event`, `rule=high_value`, `confidence=training-only`, and `action=write-local-report`. The last field is a laboratory boundary, not an operational recommendation. If your code cannot make that distinction, stop and improve the report before adding features. Security engineering is not only about detecting a pattern; it is also about limiting authority, preserving provenance, and communicating uncertainty.

At the end, perform a small review. Check that the program uses only local fixtures, has a finite workload, handles malformed input, avoids raw sensitive output, and leaves the fixture unchanged. Then write one residual-risk sentence. A useful form is: "This lesson demonstrates Local Service Architecture on synthetic data, but it does not establish authenticity, authorization, production readiness, or the presence of a real attack.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples as a starting point, then record the requested output, edge case, and limitation.

## Finish line

Run `python -m course_days.day061`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A service is a sequence of trust-boundary transitions; each transition must validate, authorize, and preserve evidence.

## Limitations

Architecture diagrams are hypotheses until tests and deployment configuration enforce the boundaries.


## References

[1]: https://docs.python.org/3/ "Python documentation"
[2]: https://docs.python.org/3/tutorial/ "The Python tutorial"
[3]: https://owasp.org/www-project-top-ten/ "OWASP Top 10"
[4]: https://csrc.nist.gov/glossary "NIST cybersecurity glossary"

[← Day 60](../day_60_project__tamper_evident_case_bundle/day_60_project__tamper_evident_case_bundle.md) · [Day index](../DAY_INDEX.md) · [Day 62 →](../day_62_request_parsing_and_validation/day_62_request_parsing_and_validation.md)
