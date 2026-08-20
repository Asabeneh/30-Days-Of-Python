# Day 41: Addresses, Ports, and Sockets

[← Day 40](../day_40_project__host_baseline_auditor/day_40_project__host_baseline_auditor.md) · [Day index](../DAY_INDEX.md) · [Day 42 →](../day_42_tcp_clients_and_servers/day_42_tcp_clients_and_servers.md)

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

Network programs begin with names and endpoints. A learner must understand what an address identifies, what a port represents, and why a socket operation is not automatically authorized.

## Prerequisites

Complete Day 40. Run the repository checks and use only the local fixtures and explicitly authorized loopback services.

## Outcomes

By the end of this lesson, you can:

- explain the protocol or security property in plain language
- run and modify every worked example
- test a normal, boundary, and failure case
- identify the trust boundary and residual risk
- connect the concept to the numbered cybersecurity exercises

## The problem

Describe a local service endpoint and create a socket object without scanning or connecting to an unknown host.

## Security boundary

Use synthetic data, local fixtures, and loopback-only demonstrations. This lesson does not authorize scanning, interception, credential use, remote command execution, or changes to systems you do not own.

## Lesson

### Vocabulary

An IP address identifies an interface in a network context. A port identifies a transport endpoint. A socket is a program object representing communication settings.

## Worked examples

### Example 1: Represent an endpoint

Keep host and port as separate typed values.

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Endpoint:
    host: str
    port: int


print(Endpoint("127.0.0.1", 8000))
```

**What to observe:**

`Endpoint(host='127.0.0.1', port=8000)`

### Example 2: Validate a port

Conversion and range policy are separate steps.

```python
def port(value: str) -> int:
    number = int(value)
    if not 1 <= number <= 65535:
        raise ValueError("port outside TCP/UDP range")
    return number
```

**What to observe:**

`port('8000')` returns 8000; 0 and 65536 are rejected.

### Example 3: Create a socket

Creating a socket does not send traffic.

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(sock.family, sock.type)
sock.close()
```

**What to observe:**

The object is IPv4/TCP and is closed without connecting.

### Example 4: Use a context manager

Cleanup should happen even when later code fails.

```python
with socket.socket() as sock:
    sock.settimeout(1.0)
    print(sock.gettimeout())
```

**What to observe:**

`1.0` seconds.

### Example 5: State scope

A network operation should carry its authorization boundary.

```python
scope = {"host": "127.0.0.1", "purpose": "course fixture", "remote": False}
print(scope)
```

**What to observe:**

The scope is local and explicit.

## Execution trace

The endpoint is validated, the socket is created, options are set, and cleanup happens. No network operation occurs until a connect, bind, send, or receive call is made.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| port as a string everywhere | comparisons behave unexpectedly | convert at the boundary |
| socket never closed | resources remain open | use `with` |
| localhost equals harmless | a local service may contain private data | define authorization and fixture |
| address equals identity | IP data is overinterpreted | record source and confidence |
| connect in a test | external side effect | use a fake or local controlled service |

## Security application

Use loopback or a fake socket in tests. Do not enumerate ports or connect to systems not explicitly supplied by the course.

## Line-by-line walkthrough

Read the first worked example from top to bottom rather than treating it as a magic recipe. The topic of this lesson is **Addresses, Ports, and Sockets**. First identify the input: what value, file, record, command, or configuration enters the example? Next identify the operation that changes or examines it. Finally identify the output and ask whether that output is merely an observation or a security conclusion. Python executes statements in order, so the name created on one line must exist before a later line can use it. When a line is a function call, identify the arguments, the function's promised return value, and any visible side effect. When a line is a condition, translate it into an ordinary question before deciding whether the branch is correct.

For each example, copy the code into a fresh file and run it unchanged. Then annotate it without editing the original: write one sentence beside each line describing its role. A useful annotation format is `input`, `transform`, `check`, `decision`, or `output`. After that, change only one value and rerun the program. If the output changes, explain which line observed the changed value. If it does not change, explain why the value was not used or why the rule filtered it. This habit is more valuable than memorizing a finished script because it teaches you to trace unfamiliar security code.

The expected output is evidence about the program, not proof about the outside world. A message such as `review` means that the local rule selected a review label. It does not prove that a person attacked a system. Keep these two statements separate in your notes. Also record failures. A `TypeError`, `ValueError`, timeout, missing-file error, or rejected configuration is often the program correctly refusing an unsafe or ambiguous input. The repair should make the policy clearer rather than hiding the error with a broad catch.

## Prediction experiments

Before each experiment, write a prediction in a comment or notebook. In Experiment A, run the smallest valid input from Example 1 and write the exact output. In Experiment B, replace one valid value with an empty, malformed, missing, or boundary value relevant to **Addresses, Ports, and Sockets**. Predict whether the program returns a result, raises an exception, rejects the record, or takes a different branch. In Experiment C, repeat the same input twice and inspect whether the program is deterministic. If a timestamp, random value, file order, or shared mutable state changes the result, identify that source of variation explicitly.

Do not use real addresses, credentials, private logs, public targets, or downloaded payloads for these experiments. Use the repository's synthetic fixtures, loopback values, `.invalid` names, and small in-memory inputs. Keep a table with four columns: input, prediction, observed output, and explanation. If the prediction is wrong, do not erase it. The mismatch is the part that teaches you how Python and the rule actually behave.

## Broken example and repair

Start with a deliberately broken version of the lesson's idea. A common beginner mistake is to combine parsing, policy, output, and side effects in one untested block. Another is to trust a value because it has the right shape, to use an unbounded loop, to print raw evidence, or to catch every exception. Break one rule at a time in a local copy. Run the program and capture the exception type or incorrect output. State the invariant that was violated: for example, "the input must be bounded," "the field must be validated before comparison," or "the report must not reveal raw fixture data."

Repair the example in small steps. First separate raw input from the internal value. Second add the narrowest check that expresses the intended policy. Third return or report a safe result. Fourth test one valid case, one invalid case, and one boundary case. Do not claim the repair is secure merely because it runs. Explain what remains outside the lesson's scope, such as authenticity, authorization, deployment configuration, or the correctness of the underlying policy. A good repair is easier for another beginner to inspect because each assumption is visible.

## Guided practice walkthrough

Use the following sequence before attempting the independent numbered questions. Choose one synthetic record related to **Addresses, Ports, and Sockets** and write down its allowed shape. For example, specify which fields are required, which values are bounded, and which fields must never be printed. Create the smallest input that satisfies the shape. Run the first example and compare the output with your prediction. Add one validation check, rerun the valid record, then test a malformed record. Keep the malformed record in the test set instead of deleting it.

Next, refactor one step into a small function or named stage. Give the stage one job and a name that describes the job. Add a print statement only while debugging, then remove it or replace it with a safe summary. Write one assertion about the result. Finally, explain the data flow in five sentences: where the fixture began, which transformation occurred, which check was applied, what label or value was produced, and what the program deliberately refused to do. Ask a peer to read the explanation without seeing the code and identify any assumption that was not documented.

## Bounded cybersecurity fixture walkthrough

The security application in this lesson uses a local, synthetic fixture. Treat the fixture as untrusted input even though it is stored in the repository. Set a maximum number of records, maximum field length, and maximum output size appropriate to the exercise. Preserve a safe source label such as `training-fixture`, but do not treat that label as proof that the data is authentic. If the fixture contains an indicator-like string, keep it inert and do not resolve, scan, connect to, upload, or enrich it from the network.

A defensible report should distinguish at least four things: what was observed, what rule matched, what uncertainty remains, and what action is permitted in this lab. For example, `observed=synthetic_event`, `rule=high_value`, `confidence=training-only`, and `action=write-local-report`. The last field is a laboratory boundary, not an operational recommendation. If your code cannot make that distinction, stop and improve the report before adding features. Security engineering is not only about detecting a pattern; it is also about limiting authority, preserving provenance, and communicating uncertainty.

At the end, perform a small review. Check that the program uses only local fixtures, has a finite workload, handles malformed input, avoids raw sensitive output, and leaves the fixture unchanged. Then write one residual-risk sentence. A useful form is: "This lesson demonstrates Addresses, Ports, and Sockets on synthetic data, but it does not establish authenticity, authorization, production readiness, or the presence of a real attack.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested local command, inspect its output, and record the limitation asked for by the exercise.

## Finish line

Run `python -m course_days.day041`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> An endpoint is data; a socket is a capability; authorization must exist before the capability is used.

## Limitations

Addresses and ports change, can be spoofed, and do not identify a person or authorize access.


## References

[1]: https://docs.python.org/3/ "Python documentation"
[2]: https://docs.python.org/3/tutorial/ "The Python tutorial"
[3]: https://owasp.org/www-project-top-ten/ "OWASP Top 10"
[4]: https://csrc.nist.gov/glossary "NIST cybersecurity glossary"

[← Day 40](../day_40_project__host_baseline_auditor/day_40_project__host_baseline_auditor.md) · [Day index](../DAY_INDEX.md) · [Day 42 →](../day_42_tcp_clients_and_servers/day_42_tcp_clients_and_servers.md)
