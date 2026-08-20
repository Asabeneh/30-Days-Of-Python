# Day 120: Final Demonstration and Engineering Judgment

[← Day 119](../day_119_capstone_security_review/day_119_capstone_security_review.md) · [Day index](../DAY_INDEX.md) · [Day 121 →](../day_120_final_demonstration/day_120_final_demonstration.md)

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

The final day is not a victory lap over copied code. It demonstrates that the learner can explain a system, run it safely, show evidence, defend design choices, and state what the system cannot prove.

## Prerequisites

Complete Day 119. Work from a clean virtual environment and use only local synthetic fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using it
- run and modify all worked examples
- test normal, boundary, and failure behavior
- state scope, evidence, and residual risk
- complete the numbered exercises

## The problem

Prepare a final demonstration of the capstone from clean setup through tests, safe sample run, threat model, and retrospective.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, destructive actions, persistence, or processing of private data.

## Lesson

### Vocabulary

A demonstration is a repeatable presentation of behavior. Engineering judgment weighs trade-offs under constraints. A retrospective records learning and next improvements.

## Worked examples

### Example 1: Start clean

A demonstration should prove setup, not depend on hidden state.

```python
setup = {"clone": True, "venv": True, "tests": "pass", "fixtures": "present"}
print(setup)
```

**What to observe:**

The starting conditions are visible.

### Example 2: Explain architecture

Name input, core policy, effects, and output.

```python
architecture = ["fixture", "parser", "pure policy", "redacted report"]
print(" -> ".join(architecture))
```

**What to observe:**

The data flow is explainable.

### Example 3: Run a normal case

Show expected output and why it is correct.

```python
demo = {"input": "valid fixture", "status": "review", "evidence": ["line-2"]}
print(demo)
```

**What to observe:**

The run is reproducible.

### Example 4: Run a failure case

A mature demo shows safe rejection and incomplete states.

```python
failure = {"input": "invalid fixture", "status": "rejected", "secret_leaked": False}
print(failure)
```

**What to observe:**

The negative behavior is visible.

### Example 5: Give the retrospective

Explain one decision, one weakness, and one next step.

```python
retro = {
    "decision": "fixture-only",
    "weakness": "no production telemetry",
    "next": "improve schema tests",
}
print(retro)
```

**What to observe:**

The learner shows judgment instead of certainty.

## Execution trace

The demonstration starts from clean setup, explains architecture, runs normal and failure cases, shows tests and evidence, names safety boundaries, and closes with limitations and next work.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| demo only happy path | reliability is hidden | show rejection and failure |
| read slides only | understanding is untested | run and explain code |
| claim production ready | local evidence is overclaimed | state scope |
| hide trade-offs | judgment is invisible | explain decisions |
| no reset | demo cannot repeat | clean environment |

## Security application

The final demonstration remains local, synthetic, resettable, and authorized. It must never include real credentials, private data, public scanning, or destructive actions.

## Line-by-line walkthrough

Read the first worked example from top to bottom rather than treating it as a magic recipe. The topic of this lesson is **Final Demonstration and Engineering Judgment**. First identify the input: what value, file, record, command, or configuration enters the example? Next identify the operation that changes or examines it. Finally identify the output and ask whether that output is merely an observation or a security conclusion. Python executes statements in order, so the name created on one line must exist before a later line can use it. When a line is a function call, identify the arguments, the function's promised return value, and any visible side effect. When a line is a condition, translate it into an ordinary question before deciding whether the branch is correct.

For each example, copy the code into a fresh file and run it unchanged. Then annotate it without editing the original: write one sentence beside each line describing its role. A useful annotation format is `input`, `transform`, `check`, `decision`, or `output`. After that, change only one value and rerun the program. If the output changes, explain which line observed the changed value. If it does not change, explain why the value was not used or why the rule filtered it. This habit is more valuable than memorizing a finished script because it teaches you to trace unfamiliar security code.

The expected output is evidence about the program, not proof about the outside world. A message such as `review` means that the local rule selected a review label. It does not prove that a person attacked a system. Keep these two statements separate in your notes. Also record failures. A `TypeError`, `ValueError`, timeout, missing-file error, or rejected configuration is often the program correctly refusing an unsafe or ambiguous input. The repair should make the policy clearer rather than hiding the error with a broad catch.

## Prediction experiments

Before each experiment, write a prediction in a comment or notebook. In Experiment A, run the smallest valid input from Example 1 and write the exact output. In Experiment B, replace one valid value with an empty, malformed, missing, or boundary value relevant to **Final Demonstration and Engineering Judgment**. Predict whether the program returns a result, raises an exception, rejects the record, or takes a different branch. In Experiment C, repeat the same input twice and inspect whether the program is deterministic. If a timestamp, random value, file order, or shared mutable state changes the result, identify that source of variation explicitly.

Do not use real addresses, credentials, private logs, public targets, or downloaded payloads for these experiments. Use the repository's synthetic fixtures, loopback values, `.invalid` names, and small in-memory inputs. Keep a table with four columns: input, prediction, observed output, and explanation. If the prediction is wrong, do not erase it. The mismatch is the part that teaches you how Python and the rule actually behave.

## Broken example and repair

Start with a deliberately broken version of the lesson's idea. A common beginner mistake is to combine parsing, policy, output, and side effects in one untested block. Another is to trust a value because it has the right shape, to use an unbounded loop, to print raw evidence, or to catch every exception. Break one rule at a time in a local copy. Run the program and capture the exception type or incorrect output. State the invariant that was violated: for example, "the input must be bounded," "the field must be validated before comparison," or "the report must not reveal raw fixture data."

Repair the example in small steps. First separate raw input from the internal value. Second add the narrowest check that expresses the intended policy. Third return or report a safe result. Fourth test one valid case, one invalid case, and one boundary case. Do not claim the repair is secure merely because it runs. Explain what remains outside the lesson's scope, such as authenticity, authorization, deployment configuration, or the correctness of the underlying policy. A good repair is easier for another beginner to inspect because each assumption is visible.

## Guided practice walkthrough

Use the following sequence before attempting the independent numbered questions. Choose one synthetic record related to **Final Demonstration and Engineering Judgment** and write down its allowed shape. For example, specify which fields are required, which values are bounded, and which fields must never be printed. Create the smallest input that satisfies the shape. Run the first example and compare the output with your prediction. Add one validation check, rerun the valid record, then test a malformed record. Keep the malformed record in the test set instead of deleting it.

Next, refactor one step into a small function or named stage. Give the stage one job and a name that describes the job. Add a print statement only while debugging, then remove it or replace it with a safe summary. Write one assertion about the result. Finally, explain the data flow in five sentences: where the fixture began, which transformation occurred, which check was applied, what label or value was produced, and what the program deliberately refused to do. Ask a peer to read the explanation without seeing the code and identify any assumption that was not documented.

## Bounded cybersecurity fixture walkthrough

The security application in this lesson uses a local, synthetic fixture. Treat the fixture as untrusted input even though it is stored in the repository. Set a maximum number of records, maximum field length, and maximum output size appropriate to the exercise. Preserve a safe source label such as `training-fixture`, but do not treat that label as proof that the data is authentic. If the fixture contains an indicator-like string, keep it inert and do not resolve, scan, connect to, upload, or enrich it from the network.

A defensible report should distinguish at least four things: what was observed, what rule matched, what uncertainty remains, and what action is permitted in this lab. For example, `observed=synthetic_event`, `rule=high_value`, `confidence=training-only`, and `action=write-local-report`. The last field is a laboratory boundary, not an operational recommendation. If your code cannot make that distinction, stop and improve the report before adding features. Security engineering is not only about detecting a pattern; it is also about limiting authority, preserving provenance, and communicating uncertainty.

At the end, perform a small review. Check that the program uses only local fixtures, has a finite workload, handles malformed input, avoids raw sensitive output, and leaves the fixture unchanged. Then write one residual-risk sentence. A useful form is: "This lesson demonstrates Final Demonstration and Engineering Judgment on synthetic data, but it does not establish authenticity, authorization, production readiness, or the presence of a real attack.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the evidence, output, edge case, and limitation requested by each question.

## Finish line

Run `python -m course_days.day120`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Engineering judgment is the ability to make, test, explain, and limit a decision under real constraints.

## Limitations

Completing the course does not make someone an advanced engineer by itself; continued practice, mentorship, university work, code review, and responsible experience remain essential.


## References

[1]: https://docs.python.org/3/ "Python documentation"
[2]: https://docs.python.org/3/tutorial/ "The Python tutorial"
[3]: https://owasp.org/www-project-top-ten/ "OWASP Top 10"
[4]: https://csrc.nist.gov/glossary "NIST cybersecurity glossary"

[← Day 119](../day_119_capstone_security_review/day_119_capstone_security_review.md) · [Day index](../DAY_INDEX.md) · [Day 121 →](../day_120_final_demonstration/day_120_final_demonstration.md)
