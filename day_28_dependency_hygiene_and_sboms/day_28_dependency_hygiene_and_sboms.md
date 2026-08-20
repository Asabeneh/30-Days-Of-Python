# Day 28: Dependency Hygiene and SBOM Thinking

[← Day 27](../day_27_git_and_code_review/day_27_git_and_code_review.md) · [Day index](../DAY_INDEX.md) · [Day 29 →](../day_29_threat_modeling/day_29_threat_modeling.md)

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

Python packages expand what a tool can do and what it must trust. Dependency hygiene makes versions, origins, licenses, and update decisions visible.

## Prerequisites

Complete Day 27 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 28

## The problem

Produce a small inventory for the course tools without treating a package name as proof of safety.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Lesson

### Vocabulary

A **dependency** is code your project relies on. An **SBOM** is a machine-readable inventory of components. A **transitive dependency** is pulled in by another dependency.

## Worked examples

### Example 1: List dependencies

The project configuration is the starting point for an inventory.

```python
dependencies = ["pytest", "ruff", "mypy"]
for name in dependencies:
    print(name)
```

**What to observe:**

Each package is named explicitly.

### Example 2: Record a version

A version makes a test result more reproducible.

```python
package = {"name": "pytest", "version": "reviewed-version", "purpose": "tests"}
print(package)
```

**What to observe:**

The record has name, version, and purpose.

### Example 3: Separate runtime and development

A production tool should not ship every teaching utility.

```python
runtime = []
development = ["pytest", "ruff", "mypy"]
print(runtime, development)
```

**What to observe:**

The two sets have different deployment implications.

### Example 4: Check a lock-like record

A review can compare the declared record to the installed environment.

```python
declared = {"pytest"}
installed = {"pytest", "unexpected-package"}
print(installed - declared)
```

**What to observe:**

The unexpected package is visible for investigation.

### Example 5: State provenance questions

An inventory is a starting point for review.

```python
questions = [
    "Where was it obtained?",
    "Who maintains it?",
    "What license applies?",
    "When was it reviewed?",
]
print(questions)
```

**What to observe:**

The checklist prevents “it installed” from becoming “it is trusted.”

## Execution trace

The project declares components, the environment reports installed components, and a review compares the two while recording provenance and purpose.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| latest always | updates introduce surprises | review and test updates |
| package name only | typosquatting or confusion | verify source and provenance |
| ignore transitive packages | hidden code enters the build | inventory the full environment |
| no license record | distribution risk appears late | review license context |
| install into system | unrelated projects change | use the project environment |

## Security application

Create an SBOM-like table for the course environment only. Do not upload private dependency reports or install packages from unverified commands.

## Line-by-line walkthrough

Read the first worked example from top to bottom rather than treating it as a magic recipe. The topic of this lesson is **Dependency Hygiene and SBOM Thinking**. First identify the input: what value, file, record, command, or configuration enters the example? Next identify the operation that changes or examines it. Finally identify the output and ask whether that output is merely an observation or a security conclusion. Python executes statements in order, so the name created on one line must exist before a later line can use it. When a line is a function call, identify the arguments, the function's promised return value, and any visible side effect. When a line is a condition, translate it into an ordinary question before deciding whether the branch is correct.

For each example, copy the code into a fresh file and run it unchanged. Then annotate it without editing the original: write one sentence beside each line describing its role. A useful annotation format is `input`, `transform`, `check`, `decision`, or `output`. After that, change only one value and rerun the program. If the output changes, explain which line observed the changed value. If it does not change, explain why the value was not used or why the rule filtered it. This habit is more valuable than memorizing a finished script because it teaches you to trace unfamiliar security code.

The expected output is evidence about the program, not proof about the outside world. A message such as `review` means that the local rule selected a review label. It does not prove that a person attacked a system. Keep these two statements separate in your notes. Also record failures. A `TypeError`, `ValueError`, timeout, missing-file error, or rejected configuration is often the program correctly refusing an unsafe or ambiguous input. The repair should make the policy clearer rather than hiding the error with a broad catch.

## Prediction experiments

Before each experiment, write a prediction in a comment or notebook. In Experiment A, run the smallest valid input from Example 1 and write the exact output. In Experiment B, replace one valid value with an empty, malformed, missing, or boundary value relevant to **Dependency Hygiene and SBOM Thinking**. Predict whether the program returns a result, raises an exception, rejects the record, or takes a different branch. In Experiment C, repeat the same input twice and inspect whether the program is deterministic. If a timestamp, random value, file order, or shared mutable state changes the result, identify that source of variation explicitly.

Do not use real addresses, credentials, private logs, public targets, or downloaded payloads for these experiments. Use the repository's synthetic fixtures, loopback values, `.invalid` names, and small in-memory inputs. Keep a table with four columns: input, prediction, observed output, and explanation. If the prediction is wrong, do not erase it. The mismatch is the part that teaches you how Python and the rule actually behave.

## Broken example and repair

Start with a deliberately broken version of the lesson's idea. A common beginner mistake is to combine parsing, policy, output, and side effects in one untested block. Another is to trust a value because it has the right shape, to use an unbounded loop, to print raw evidence, or to catch every exception. Break one rule at a time in a local copy. Run the program and capture the exception type or incorrect output. State the invariant that was violated: for example, "the input must be bounded," "the field must be validated before comparison," or "the report must not reveal raw fixture data."

Repair the example in small steps. First separate raw input from the internal value. Second add the narrowest check that expresses the intended policy. Third return or report a safe result. Fourth test one valid case, one invalid case, and one boundary case. Do not claim the repair is secure merely because it runs. Explain what remains outside the lesson's scope, such as authenticity, authorization, deployment configuration, or the correctness of the underlying policy. A good repair is easier for another beginner to inspect because each assumption is visible.

## Guided practice walkthrough

Use the following sequence before attempting the independent numbered questions. Choose one synthetic record related to **Dependency Hygiene and SBOM Thinking** and write down its allowed shape. For example, specify which fields are required, which values are bounded, and which fields must never be printed. Create the smallest input that satisfies the shape. Run the first example and compare the output with your prediction. Add one validation check, rerun the valid record, then test a malformed record. Keep the malformed record in the test set instead of deleting it.

Next, refactor one step into a small function or named stage. Give the stage one job and a name that describes the job. Add a print statement only while debugging, then remove it or replace it with a safe summary. Write one assertion about the result. Finally, explain the data flow in five sentences: where the fixture began, which transformation occurred, which check was applied, what label or value was produced, and what the program deliberately refused to do. Ask a peer to read the explanation without seeing the code and identify any assumption that was not documented.

## Bounded cybersecurity fixture walkthrough

The security application in this lesson uses a local, synthetic fixture. Treat the fixture as untrusted input even though it is stored in the repository. Set a maximum number of records, maximum field length, and maximum output size appropriate to the exercise. Preserve a safe source label such as `training-fixture`, but do not treat that label as proof that the data is authentic. If the fixture contains an indicator-like string, keep it inert and do not resolve, scan, connect to, upload, or enrich it from the network.

A defensible report should distinguish at least four things: what was observed, what rule matched, what uncertainty remains, and what action is permitted in this lab. For example, `observed=synthetic_event`, `rule=high_value`, `confidence=training-only`, and `action=write-local-report`. The last field is a laboratory boundary, not an operational recommendation. If your code cannot make that distinction, stop and improve the report before adding features. Security engineering is not only about detecting a pattern; it is also about limiting authority, preserving provenance, and communicating uncertainty.

At the end, perform a small review. Check that the program uses only local fixtures, has a finite workload, handles malformed input, avoids raw sensitive output, and leaves the fixture unchanged. Then write one residual-risk sentence. A useful form is: "This lesson demonstrates Dependency Hygiene and SBOM Thinking on synthetic data, but it does not establish authenticity, authorization, production readiness, or the presence of a real attack.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run every requested command, create the requested artifact, and record the limitation the exercise asks you to name.

## Finish line

Run `python -m course_days.day028`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A dependency is part of the system’s trust boundary even when your code did not write it.

## Limitations

An inventory does not prove a package is secure. Vulnerabilities, maintainer compromise, build tampering, and configuration risk remain possible.


## References

[1]: https://docs.python.org/3/ "Python documentation"
[2]: https://docs.python.org/3/tutorial/ "The Python tutorial"
[3]: https://owasp.org/www-project-top-ten/ "OWASP Top 10"
[4]: https://csrc.nist.gov/glossary "NIST cybersecurity glossary"

[← Day 27](../day_27_git_and_code_review/day_27_git_and_code_review.md) · [Day index](../DAY_INDEX.md) · [Day 29 →](../day_29_threat_modeling/day_29_threat_modeling.md)
