# Day 27: Git and Code Review for Security Changes

[← Previous lesson](../day_026_structured_logging/day_026_structured_logging.md) · [README](../README.md) · [Setup](../SETUP.md) · [VS Code](../VS_CODE_SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_028_dependency_hygiene_and_sboms/day_028_dependency_hygiene_and_sboms.md)









## Start here

Read the [course README](../README.md), complete the [setup guide](../SETUP.md) and [VS Code setup](../VS_CODE_SETUP.md), then use the [day index](../DAY_INDEX.md) to confirm where this lesson fits. Run the linked local starter before attempting the the numbered exercises in this lesson, then use [hints](practice/hints.md) and [solutions](practice/solutions.md) only after an honest attempt.

## Table of contents

- [Start here](#start-here)

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is Git and Code Review for Security Changes?](#what-is-git-and-code-review-for-security-changes)
  - [Why is Git and Code Review for Security Changes useful?](#why-is-git-and-code-review-for-security-changes-useful)
  - [How will Python use this idea?](#how-will-python-use-this-idea)
  - [What are the security limits?](#what-are-the-security-limits)
- [Worked examples](#worked-examples)
  - [Example 1: Inspect status](#example-1-inspect-status)
  - [Example 2: Read a diff](#example-2-read-a-diff)
  - [Example 3: Make a focused commit](#example-3-make-a-focused-commit)
  - [Example 4: Review security questions](#example-4-review-security-questions)
  - [Example 5: Compare before and after](#example-5-compare-before-and-after)
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

Version control is part of engineering evidence. A small reviewable commit helps a team understand what changed, why it changed, and how to revert it.

## Prerequisites

Complete Day 26 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 27

## The problem

Review a change to a parser or security rule without trusting the author’s description alone.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Keywords and terms

A **diff** is a line-level change. A **commit** is a recorded snapshot. A **review** checks behavior, tests, scope, and risk before integration.

## Topics

### What is Git and Code Review for Security Changes?

Version control is part of engineering evidence. A small reviewable commit helps a team understand what changed, why it changed, and how to revert it.

### Why is Git and Code Review for Security Changes useful?

Review a change to a parser or security rule without trusting the author’s description alone.

### How will Python use this idea?

Read the worked examples next. For each one, identify the input, the operation, the result, and the boundary that prevents the example from doing more than the lesson allows.

### What are the security limits?

The examples remain local, synthetic, bounded, and authorized. A successful program run demonstrates behavior on the fixture; it does not prove authenticity, compromise, or permission to act on a real target.

## Worked examples

### Example 1: Inspect status

Start with the repository state before modifying anything.

```python
git status --short
git branch --show-current
```

**What to observe:**

You see changed files and the active branch.

### Example 2: Read a diff

A diff shows additions, deletions, and context.

```python
git diff -- course_days/day027.py
```

**What to observe:**

The reviewer can focus on the actual changed lines.

### Example 3: Make a focused commit

A commit should tell one coherent story.

```python
git add course_days/day027.py tests/test_day27.py
git commit -m "Validate evidence source"
```

**What to observe:**

The source and its tests move together.

### Example 4: Review security questions

A checklist prevents “tests pass” from being the only question.

```python
questions = [
    "What input is new?",
    "What is the trust boundary?",
    "What can leak?",
    "What is the rollback?",
]
print(len(questions))
```

**What to observe:**

Four review questions are visible.

### Example 5: Compare before and after

A reviewer should inspect behavior, not only formatting.

```python
before = {"accepted": ["443"], "rejected": ["70000"]}
after = {"accepted": ["443"], "rejected": ["70000", "abc"]}
print(after)
```

**What to observe:**

The added rejection is an observable behavior change.

## Read the first example line by line

The first runnable example introduces **Git and Code Review for Security Changes**. Copy it into a new file and run it before changing anything. Then use this table to read the same code slowly. A line-by-line explanation does not replace practice: it shows you what to look for when a program behaves differently from your prediction.

| Line | Code | What Python is doing |
| ---: | --- | --- |
| 1 | `git status --short` | Expression or data declaration: read the names, values, and operators and predict the result. |
| 2 | `git branch --show-current` | Expression or data declaration: read the names, values, and operators and predict the result. |

After the run, write down the value created by each assignment, the condition tested by each branch, and the output that appeared. Change one input only. If the result changes, identify the line that used that input. If the result does not change, explain why the input was not part of the decision. This is the same tracing habit used later when reviewing security automation.
## Execution trace

The review moves from status to diff to tests to threat questions to a focused commit. The repository becomes a record of engineering decisions.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| review only the title | dangerous line is missed | inspect the diff |
| giant mixed commit | rollback is risky | split coherent changes |
| no negative test | security claim is unproved | add rejection tests |
| commit secrets | history retains them | scan and remove before commit |
| approve based on authority | reviewer skips evidence | require reproducible checks |

## Security application

Practice on the course branch and synthetic fixtures. Never commit tokens, private logs, or generated evidence. If a secret enters Git history, stop and follow the repository security policy.

## Line-by-line walkthrough

Read the first worked example from top to bottom rather than treating it as a magic recipe. The topic of this lesson is **Git and Code Review for Security Changes**. First identify the input: what value, file, record, command, or configuration enters the example? Next identify the operation that changes or examines it. Finally identify the output and ask whether that output is merely an observation or a security conclusion. Python executes statements in order, so the name created on one line must exist before a later line can use it. When a line is a function call, identify the arguments, the function's promised return value, and any visible side effect. When a line is a condition, translate it into an ordinary question before deciding whether the branch is correct.

For each example, copy the code into a fresh file and run it unchanged. Then annotate it without editing the original: write one sentence beside each line describing its role. A useful annotation format is `input`, `transform`, `check`, `decision`, or `output`. After that, change only one value and rerun the program. If the output changes, explain which line observed the changed value. If it does not change, explain why the value was not used or why the rule filtered it. This habit is more valuable than memorizing a finished script because it teaches you to trace unfamiliar security code.

The expected output is evidence about the program, not proof about the outside world. A message such as `review` means that the local rule selected a review label. It does not prove that a person attacked a system. Keep these two statements separate in your notes. Also record failures. A `TypeError`, `ValueError`, timeout, missing-file error, or rejected configuration is often the program correctly refusing an unsafe or ambiguous input. The repair should make the policy clearer rather than hiding the error with a broad catch.

## Prediction experiments

Before each experiment, write a prediction in a comment or notebook. In Experiment A, run the smallest valid input from Example 1 and write the exact output. In Experiment B, replace one valid value with an empty, malformed, missing, or boundary value relevant to **Git and Code Review for Security Changes**. Predict whether the program returns a result, raises an exception, rejects the record, or takes a different branch. In Experiment C, repeat the same input twice and inspect whether the program is deterministic. If a timestamp, random value, file order, or shared mutable state changes the result, identify that source of variation explicitly.

Do not use real addresses, credentials, private logs, public targets, or downloaded payloads for these experiments. Use the repository's synthetic fixtures, loopback values, `.invalid` names, and small in-memory inputs. Keep a table with four columns: input, prediction, observed output, and explanation. If the prediction is wrong, do not erase it. The mismatch is the part that teaches you how Python and the rule actually behave.

## Broken example and repair

Start with a deliberately broken version of the lesson's idea. A common beginner mistake is to combine parsing, policy, output, and side effects in one untested block. Another is to trust a value because it has the right shape, to use an unbounded loop, to print raw evidence, or to catch every exception. Break one rule at a time in a local copy. Run the program and capture the exception type or incorrect output. State the invariant that was violated: for example, "the input must be bounded," "the field must be validated before comparison," or "the report must not reveal raw fixture data."

Repair the example in small steps. First separate raw input from the internal value. Second add the narrowest check that expresses the intended policy. Third return or report a safe result. Fourth test one valid case, one invalid case, and one boundary case. Do not claim the repair is secure merely because it runs. Explain what remains outside the lesson's scope, such as authenticity, authorization, deployment configuration, or the correctness of the underlying policy. A good repair is easier for another beginner to inspect because each assumption is visible.

## Guided practice walkthrough

Use the following sequence before attempting the independent numbered questions. Choose one synthetic record related to **Git and Code Review for Security Changes** and write down its allowed shape. For example, specify which fields are required, which values are bounded, and which fields must never be printed. Create the smallest input that satisfies the shape. Run the first example and compare the output with your prediction. Add one validation check, rerun the valid record, then test a malformed record. Keep the malformed record in the test set instead of deleting it.

Next, refactor one step into a small function or named stage. Give the stage one job and a name that describes the job. Add a print statement only while debugging, then remove it or replace it with a safe summary. Write one assertion about the result. Finally, explain the data flow in five sentences: where the fixture began, which transformation occurred, which check was applied, what label or value was produced, and what the program deliberately refused to do. Ask a peer to read the explanation without seeing the code and identify any assumption that was not documented.

## Bounded cybersecurity fixture walkthrough

The security application in this lesson uses a local, synthetic fixture. Treat the fixture as untrusted input even though it is stored in the repository. Set a maximum number of records, maximum field length, and maximum output size appropriate to the exercise. Preserve a safe source label such as `training-fixture`, but do not treat that label as proof that the data is authentic. If the fixture contains an indicator-like string, keep it inert and do not resolve, scan, connect to, upload, or enrich it from the network.

A defensible report should distinguish at least four things: what was observed, what rule matched, what uncertainty remains, and what action is permitted in this lab. For example, `observed=synthetic_event`, `rule=high_value`, `confidence=training-only`, and `action=write-local-report`. The last field is a laboratory boundary, not an operational recommendation. If your code cannot make that distinction, stop and improve the report before adding features. Security engineering is not only about detecting a pattern; it is also about limiting authority, preserving provenance, and communicating uncertainty.

At the end, perform a small review. Check that the program uses only local fixtures, has a finite workload, handles malformed input, avoids raw sensitive output, and leaves the fixture unchanged. Then write one residual-risk sentence. A useful form is: "This lesson demonstrates Git and Code Review for Security Changes on synthetic data, but it does not establish authenticity, authorization, production readiness, or the presence of a real attack.
## Exercises


The following numbered exercises are the canonical practice for this lesson. Attempt them here in order; use the separate hints and solutions only after a genuine attempt.

1. Run the review checklist. Which check would catch a whitespace-only diff?
2. Make a small change to a starter and inspect `git diff`. What changed and why?
3. Add a test for the changed behavior before committing it.
4. Write a review question for input validation, dependency changes, and security impact.
5. Explain why a clean commit history helps rollback and incident investigation.

6. Apply the lesson to the supplied local synthetic fixture and state the expected artifact before running it.
7. Add a normal case and predict the result before executing the code.
8. Add a boundary case and explain the chosen behavior.
9. Add an invalid case and keep the failure visible and understandable.
10. Reproduce the deliberate mistake from the lesson and record the smallest repair.
11. Add a focused test or evidence note for the most important behavior.
12. Write one limitation and one review question for a teammate.

Use only the supplied local, synthetic, bounded fixtures. Do not use real credentials, private data, public targets, or systems outside explicit authorization.

## Finish line

Run `python -m course_days.day027`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A code review is a structured challenge to the change’s assumptions, not a vote on the author.

## Limitations

Git records changes but does not make secrets disappear from history or guarantee that a review found every flaw.


## References

[1]: https://docs.python.org/3/ "Python documentation"
[2]: https://docs.python.org/3/tutorial/ "The Python tutorial"
[3]: https://owasp.org/www-project-top-ten/ "OWASP Top 10"
[4]: https://csrc.nist.gov/glossary "NIST cybersecurity glossary"

[← Day 26](../day_026_structured_logging/day_026_structured_logging.md) · [Day index](../DAY_INDEX.md) · [Day 28 →](../day_028_dependency_hygiene_and_sboms/day_028_dependency_hygiene_and_sboms.md)
