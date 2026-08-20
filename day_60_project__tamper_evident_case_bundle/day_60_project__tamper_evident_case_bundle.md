# Day 60: Project: Tamper-Evident Case Bundle

[← Day 59](../day_59_secure_errors_and_logging/day_59_secure_errors_and_logging.md) · [Day index](../DAY_INDEX.md) · [Day 61 →](../day_61_local_service_architecture/day_61_local_service_architecture.md)









## Table of contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is Project: Tamper-Evident Case Bundle?](#what-is-project-tamper-evident-case-bundle)
  - [Why is Project: Tamper-Evident Case Bundle useful?](#why-is-project-tamper-evident-case-bundle-useful)
  - [How will Python use this idea?](#how-will-python-use-this-idea)
  - [What are the security limits?](#what-are-the-security-limits)
- [Worked examples](#worked-examples)
  - [Example 1: Create canonical JSON](#example-1-create-canonical-json)
  - [Example 2: Digest a member](#example-2-digest-a-member)
  - [Example 3: Build a manifest](#example-3-build-a-manifest)
  - [Example 4: Authenticate the manifest](#example-4-authenticate-the-manifest)
  - [Example 5: Verify before reading](#example-5-verify-before-reading)
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

This project combines encoding, hashes, HMAC, serialization, error policy, and provenance into a local case bundle that can detect modification without pretending to be legal chain of custody.

## Prerequisites

Complete Day 59. Run the repository checks and use only the local fixtures and explicitly authorized loopback services.

## Outcomes

By the end of this lesson, you can:

- explain the protocol or security property in plain language
- run and modify every worked example
- test a normal, boundary, and failure case
- identify the trust boundary and residual risk
- connect the concept to the numbered cybersecurity exercises

## The problem

Build a bundle of synthetic JSON records with canonical bytes, a manifest digest, an HMAC tag, and a verification command.

## Security boundary

Use synthetic data, local fixtures, and loopback-only demonstrations. This lesson does not authorize scanning, interception, credential use, remote command execution, or changes to systems you do not own.

## Keywords and terms

A manifest lists bundle members. Canonical bytes make hashing reproducible. Tamper-evident means change is detectable under a protected verification key.

## Topics

### What is Project: Tamper-Evident Case Bundle?

This project combines encoding, hashes, HMAC, serialization, error policy, and provenance into a local case bundle that can detect modification without pretending to be legal chain of custody.

### Why is Project: Tamper-Evident Case Bundle useful?

Build a bundle of synthetic JSON records with canonical bytes, a manifest digest, an HMAC tag, and a verification command.

### How will Python use this idea?

Read the worked examples next. For each one, identify the input, the operation, the result, and the boundary that prevents the example from doing more than the lesson allows.

### What are the security limits?

The examples remain local, synthetic, bounded, and authorized. A successful program run demonstrates behavior on the fixture; it does not prove authenticity, compromise, or permission to act on a real target.

## Worked examples

### Example 1: Create canonical JSON

Stable key ordering and encoding make bytes reproducible.

```python
import json

record = {"severity": 7, "case_id": "training-060"}
canonical = json.dumps(record, sort_keys=True, separators=(",", ":")).encode("utf-8")
print(canonical)
```

**What to observe:**

The canonical bytes have no incidental spaces.

### Example 2: Digest a member

The manifest can store a digest for each member.

```python
import hashlib

member_hash = hashlib.sha256(canonical).hexdigest()
print(member_hash[:12])
```

**What to observe:**

A stable digest prefix.

### Example 3: Build a manifest

The manifest names scope and members.

```python
manifest = {
    "version": 1,
    "members": {"record.json": member_hash},
    "scope": "training-only",
}
print(manifest)
```

**What to observe:**

The bundle structure is visible.

### Example 4: Authenticate the manifest

HMAC protects the manifest under the training key.

```python
import hmac

key = b"training-bundle-key"
manifest_bytes = json.dumps(manifest, sort_keys=True).encode()
tag = hmac.new(key, manifest_bytes, hashlib.sha256).hexdigest()
print(tag[:12])
```

**What to observe:**

The tag is stored separately from the secret key.

### Example 5: Verify before reading

Verification must precede interpreting members as trusted.

```python
ok = hmac.compare_digest(tag, hmac.new(key, manifest_bytes, hashlib.sha256).hexdigest())
print(ok)
```

**What to observe:**

`True` for the unchanged training manifest.

## Read the first example line by line

The first runnable example introduces **Project: Tamper-Evident Case Bundle**. Copy it into a new file and run it before changing anything. Then use this table to read the same code slowly. A line-by-line explanation does not replace practice: it shows you what to look for when a program behaves differently from your prediction.

| Line | Code | What Python is doing |
| ---: | --- | --- |
| 1 | `import json` | Import statement: the program asks for code from a module. |
| 2 | `` | Blank line: it separates ideas for the human reader. |
| 3 | `record = {"severity": 7, "case_id": "training-060"}` | Assignment: Python evaluates the right side and stores the result under the name on the left. |
| 4 | `canonical = json.dumps(record, sort_keys=True, separators=(",", ":")).encode("utf-8")` | Assignment: Python evaluates the right side and stores the result under the name on the left. |
| 5 | `print(canonical)` | Output call: Python evaluates the argument and writes a representation to the terminal. |

After the run, write down the value created by each assignment, the condition tested by each branch, and the output that appeared. Change one input only. If the result changes, identify the line that used that input. If the result does not change, explain why the input was not part of the decision. This is the same tracing habit used later when reviewing security automation.
## Execution trace

The project canonicalizes data, hashes each member, authenticates the manifest, writes a bounded bundle, and verifies the tag and member digests before reporting a result.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| hash noncanonical JSON | equivalent data hashes differently | define canonical bytes |
| store key with bundle | attacker gets verification key | separate key lifecycle |
| parse before verify | tampered content controls code | verify manifest first |
| claim legal evidence | technical check is overclaimed | state training limitations |
| no version | future parser guesses | version the bundle schema |

## Security application

The bundle is local, synthetic, resettable, and verified with a disposable training key. The README must document exact bytes, key handling, tamper test, cleanup, and limitations.

## Line-by-line walkthrough

Read the first worked example from top to bottom rather than treating it as a magic recipe. The topic of this lesson is **Project: Tamper-Evident Case Bundle**. First identify the input: what value, file, record, command, or configuration enters the example? Next identify the operation that changes or examines it. Finally identify the output and ask whether that output is merely an observation or a security conclusion. Python executes statements in order, so the name created on one line must exist before a later line can use it. When a line is a function call, identify the arguments, the function's promised return value, and any visible side effect. When a line is a condition, translate it into an ordinary question before deciding whether the branch is correct.

For each example, copy the code into a fresh file and run it unchanged. Then annotate it without editing the original: write one sentence beside each line describing its role. A useful annotation format is `input`, `transform`, `check`, `decision`, or `output`. After that, change only one value and rerun the program. If the output changes, explain which line observed the changed value. If it does not change, explain why the value was not used or why the rule filtered it. This habit is more valuable than memorizing a finished script because it teaches you to trace unfamiliar security code.

The expected output is evidence about the program, not proof about the outside world. A message such as `review` means that the local rule selected a review label. It does not prove that a person attacked a system. Keep these two statements separate in your notes. Also record failures. A `TypeError`, `ValueError`, timeout, missing-file error, or rejected configuration is often the program correctly refusing an unsafe or ambiguous input. The repair should make the policy clearer rather than hiding the error with a broad catch.

## Prediction experiments

Before each experiment, write a prediction in a comment or notebook. In Experiment A, run the smallest valid input from Example 1 and write the exact output. In Experiment B, replace one valid value with an empty, malformed, missing, or boundary value relevant to **Project: Tamper-Evident Case Bundle**. Predict whether the program returns a result, raises an exception, rejects the record, or takes a different branch. In Experiment C, repeat the same input twice and inspect whether the program is deterministic. If a timestamp, random value, file order, or shared mutable state changes the result, identify that source of variation explicitly.

Do not use real addresses, credentials, private logs, public targets, or downloaded payloads for these experiments. Use the repository's synthetic fixtures, loopback values, `.invalid` names, and small in-memory inputs. Keep a table with four columns: input, prediction, observed output, and explanation. If the prediction is wrong, do not erase it. The mismatch is the part that teaches you how Python and the rule actually behave.

## Broken example and repair

Start with a deliberately broken version of the lesson's idea. A common beginner mistake is to combine parsing, policy, output, and side effects in one untested block. Another is to trust a value because it has the right shape, to use an unbounded loop, to print raw evidence, or to catch every exception. Break one rule at a time in a local copy. Run the program and capture the exception type or incorrect output. State the invariant that was violated: for example, "the input must be bounded," "the field must be validated before comparison," or "the report must not reveal raw fixture data."

Repair the example in small steps. First separate raw input from the internal value. Second add the narrowest check that expresses the intended policy. Third return or report a safe result. Fourth test one valid case, one invalid case, and one boundary case. Do not claim the repair is secure merely because it runs. Explain what remains outside the lesson's scope, such as authenticity, authorization, deployment configuration, or the correctness of the underlying policy. A good repair is easier for another beginner to inspect because each assumption is visible.

## Guided practice walkthrough

Use the following sequence before attempting the independent numbered questions. Choose one synthetic record related to **Project: Tamper-Evident Case Bundle** and write down its allowed shape. For example, specify which fields are required, which values are bounded, and which fields must never be printed. Create the smallest input that satisfies the shape. Run the first example and compare the output with your prediction. Add one validation check, rerun the valid record, then test a malformed record. Keep the malformed record in the test set instead of deleting it.

Next, refactor one step into a small function or named stage. Give the stage one job and a name that describes the job. Add a print statement only while debugging, then remove it or replace it with a safe summary. Write one assertion about the result. Finally, explain the data flow in five sentences: where the fixture began, which transformation occurred, which check was applied, what label or value was produced, and what the program deliberately refused to do. Ask a peer to read the explanation without seeing the code and identify any assumption that was not documented.

## Bounded cybersecurity fixture walkthrough

The security application in this lesson uses a local, synthetic fixture. Treat the fixture as untrusted input even though it is stored in the repository. Set a maximum number of records, maximum field length, and maximum output size appropriate to the exercise. Preserve a safe source label such as `training-fixture`, but do not treat that label as proof that the data is authentic. If the fixture contains an indicator-like string, keep it inert and do not resolve, scan, connect to, upload, or enrich it from the network.

A defensible report should distinguish at least four things: what was observed, what rule matched, what uncertainty remains, and what action is permitted in this lab. For example, `observed=synthetic_event`, `rule=high_value`, `confidence=training-only`, and `action=write-local-report`. The last field is a laboratory boundary, not an operational recommendation. If your code cannot make that distinction, stop and improve the report before adding features. Security engineering is not only about detecting a pattern; it is also about limiting authority, preserving provenance, and communicating uncertainty.

At the end, perform a small review. Check that the program uses only local fixtures, has a finite workload, handles malformed input, avoids raw sensitive output, and leaves the fixture unchanged. Then write one residual-risk sentence. A useful form is: "This lesson demonstrates Project: Tamper-Evident Case Bundle on synthetic data, but it does not establish authenticity, authorization, production readiness, or the presence of a real attack.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested local command, inspect its output, and record the limitation asked for by the exercise.

## Finish line

Run `python -m course_days.day60`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A tamper-evident bundle makes changes detectable under a defined byte and key policy; it does not make data true.

## Limitations

This is not a production evidence system, secure archival service, or legal chain-of-custody implementation.


## References

[1]: https://docs.python.org/3/ "Python documentation"
[2]: https://docs.python.org/3/tutorial/ "The Python tutorial"
[3]: https://owasp.org/www-project-top-ten/ "OWASP Top 10"
[4]: https://csrc.nist.gov/glossary "NIST cybersecurity glossary"

[← Day 59](../day_59_secure_errors_and_logging/day_59_secure_errors_and_logging.md) · [Day index](../DAY_INDEX.md) · [Day 61 →](../day_61_local_service_architecture/day_61_local_service_architecture.md)
