# Day 34: Safe Subprocess Allowlisting

[← Day 33](../day_33_paths_and_file_metadata/day_33_paths_and_file_metadata.md) · [Day index](../DAY_INDEX.md) · [Day 35 →](../day_35_users_and_permissions/day_35_users_and_permissions.md)

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

Day 31 showed how to start a process; this day turns that knowledge into a safer design. A command runner should allow a small set of known operations instead of accepting arbitrary executable input.

## Prerequisites

Complete Day 33 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 34

## The problem

Build a local command adapter that supports one or two harmless inventory commands and rejects everything else.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Lesson

### Vocabulary

An **allowlist** permits named safe cases. A **denylist** tries to enumerate unsafe cases. An **argv list** keeps arguments separate from shell parsing.

## Worked examples

### Example 1: Allow one command

Map a friendly operation to a fixed argv list.

```python
COMMANDS = {"python-version": ["python", "--version"]}
print(COMMANDS["python-version"])
```

**What to observe:**

The user chooses a key, not an executable string.

### Example 2: Reject unknown keys

Fail before starting a process.

```python
def command_for(name):
    try:
        return COMMANDS[name].copy()
    except KeyError as error:
        raise ValueError("operation is not allowed") from error
```

**What to observe:**

An unknown operation is rejected.

### Example 3: Constrain arguments

Even an allowed executable may accept unsafe arguments.

```python
def python_check(script):
    if script != "import sys; print(sys.version_info[:2])":
        raise ValueError("script is not allowed")
    return ["python", "-c", script]
```

**What to observe:**

Only the exact local check is accepted.

### Example 4: Set environment

Do not inherit more environment than necessary.

```python
safe_env = {"PATH": "/usr/bin:/bin"}
print(sorted(safe_env))
```

**What to observe:**

The child receives a deliberately small environment.

### Example 5: Bound output

Capture only a limited amount of output before reporting truncation.

```python
def preview(text, limit=4096):
    return text[:limit], len(text) > limit
```

**What to observe:**

The caller can display `truncated=True`.

## Execution trace

The friendly operation maps to fixed data, the adapter validates the key and arguments, starts with an explicit cwd/environment, and caps output and lifetime.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| denylist | a new dangerous command bypasses it | allowlist |
| executable from input | arbitrary code runs | map names to fixed argv |
| inherited environment | secrets enter child | pass a minimal environment |
| inherited privileges | child can do too much | drop privilege or refuse |
| output stored forever | sensitive output persists | cap, redact, and clean up |

## Security application

The adapter may run only harmless local inventory commands. It must reject shell metacharacters, remote destinations, arbitrary scripts, and unknown operation names.

## Line-by-line walkthrough

Read the first worked example from top to bottom rather than treating it as a magic recipe. The topic of this lesson is **Safe Subprocess Allowlisting**. First identify the input: what value, file, record, command, or configuration enters the example? Next identify the operation that changes or examines it. Finally identify the output and ask whether that output is merely an observation or a security conclusion. Python executes statements in order, so the name created on one line must exist before a later line can use it. When a line is a function call, identify the arguments, the function's promised return value, and any visible side effect. When a line is a condition, translate it into an ordinary question before deciding whether the branch is correct.

For each example, copy the code into a fresh file and run it unchanged. Then annotate it without editing the original: write one sentence beside each line describing its role. A useful annotation format is `input`, `transform`, `check`, `decision`, or `output`. After that, change only one value and rerun the program. If the output changes, explain which line observed the changed value. If it does not change, explain why the value was not used or why the rule filtered it. This habit is more valuable than memorizing a finished script because it teaches you to trace unfamiliar security code.

The expected output is evidence about the program, not proof about the outside world. A message such as `review` means that the local rule selected a review label. It does not prove that a person attacked a system. Keep these two statements separate in your notes. Also record failures. A `TypeError`, `ValueError`, timeout, missing-file error, or rejected configuration is often the program correctly refusing an unsafe or ambiguous input. The repair should make the policy clearer rather than hiding the error with a broad catch.

## Prediction experiments

Before each experiment, write a prediction in a comment or notebook. In Experiment A, run the smallest valid input from Example 1 and write the exact output. In Experiment B, replace one valid value with an empty, malformed, missing, or boundary value relevant to **Safe Subprocess Allowlisting**. Predict whether the program returns a result, raises an exception, rejects the record, or takes a different branch. In Experiment C, repeat the same input twice and inspect whether the program is deterministic. If a timestamp, random value, file order, or shared mutable state changes the result, identify that source of variation explicitly.

Do not use real addresses, credentials, private logs, public targets, or downloaded payloads for these experiments. Use the repository's synthetic fixtures, loopback values, `.invalid` names, and small in-memory inputs. Keep a table with four columns: input, prediction, observed output, and explanation. If the prediction is wrong, do not erase it. The mismatch is the part that teaches you how Python and the rule actually behave.

## Broken example and repair

Start with a deliberately broken version of the lesson's idea. A common beginner mistake is to combine parsing, policy, output, and side effects in one untested block. Another is to trust a value because it has the right shape, to use an unbounded loop, to print raw evidence, or to catch every exception. Break one rule at a time in a local copy. Run the program and capture the exception type or incorrect output. State the invariant that was violated: for example, "the input must be bounded," "the field must be validated before comparison," or "the report must not reveal raw fixture data."

Repair the example in small steps. First separate raw input from the internal value. Second add the narrowest check that expresses the intended policy. Third return or report a safe result. Fourth test one valid case, one invalid case, and one boundary case. Do not claim the repair is secure merely because it runs. Explain what remains outside the lesson's scope, such as authenticity, authorization, deployment configuration, or the correctness of the underlying policy. A good repair is easier for another beginner to inspect because each assumption is visible.

## Guided practice walkthrough

Use the following sequence before attempting the independent numbered questions. Choose one synthetic record related to **Safe Subprocess Allowlisting** and write down its allowed shape. For example, specify which fields are required, which values are bounded, and which fields must never be printed. Create the smallest input that satisfies the shape. Run the first example and compare the output with your prediction. Add one validation check, rerun the valid record, then test a malformed record. Keep the malformed record in the test set instead of deleting it.

Next, refactor one step into a small function or named stage. Give the stage one job and a name that describes the job. Add a print statement only while debugging, then remove it or replace it with a safe summary. Write one assertion about the result. Finally, explain the data flow in five sentences: where the fixture began, which transformation occurred, which check was applied, what label or value was produced, and what the program deliberately refused to do. Ask a peer to read the explanation without seeing the code and identify any assumption that was not documented.

## Bounded cybersecurity fixture walkthrough

The security application in this lesson uses a local, synthetic fixture. Treat the fixture as untrusted input even though it is stored in the repository. Set a maximum number of records, maximum field length, and maximum output size appropriate to the exercise. Preserve a safe source label such as `training-fixture`, but do not treat that label as proof that the data is authentic. If the fixture contains an indicator-like string, keep it inert and do not resolve, scan, connect to, upload, or enrich it from the network.

A defensible report should distinguish at least four things: what was observed, what rule matched, what uncertainty remains, and what action is permitted in this lab. For example, `observed=synthetic_event`, `rule=high_value`, `confidence=training-only`, and `action=write-local-report`. The last field is a laboratory boundary, not an operational recommendation. If your code cannot make that distinction, stop and improve the report before adding features. Security engineering is not only about detecting a pattern; it is also about limiting authority, preserving provenance, and communicating uncertainty.

At the end, perform a small review. Check that the program uses only local fixtures, has a finite workload, handles malformed input, avoids raw sensitive output, and leaves the fixture unchanged. Then write one residual-risk sentence. A useful form is: "This lesson demonstrates Safe Subprocess Allowlisting on synthetic data, but it does not establish authenticity, authorization, production readiness, or the presence of a real attack.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run every requested command, create the requested artifact, and record the limitation the exercise asks you to name.

## Finish line

Run `python -m course_days.day034`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Safe automation narrows the language accepted at the process boundary until only the intended operation remains.

## Limitations

Allowlisting is a design control, not proof that the allowed command is safe on every platform or with every dependency.


## References

[1]: https://docs.python.org/3/ "Python documentation"
[2]: https://docs.python.org/3/tutorial/ "The Python tutorial"
[3]: https://owasp.org/www-project-top-ten/ "OWASP Top 10"
[4]: https://csrc.nist.gov/glossary "NIST cybersecurity glossary"

[← Day 33](../day_33_paths_and_file_metadata/day_33_paths_and_file_metadata.md) · [Day index](../DAY_INDEX.md) · [Day 35 →](../day_35_users_and_permissions/day_35_users_and_permissions.md)
