# Day 16: Regular Expressions and Careful Indicator Extraction

[← Day 15](../day_15_iterators_and_generators/day_15_iterators_and_generators.md) · [Day index](../DAY_INDEX.md) · [Day 17 →](../day_17_dates_and_timelines/day_17_dates_and_timelines.md)






## Table of contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Lesson](#lesson)
  - [Vocabulary](#vocabulary)
- [Worked examples](#worked-examples)
  - [Example 1: Find a simple field](#example-1-find-a-simple-field)
  - [Example 2: Find every candidate](#example-2-find-every-candidate)
  - [Example 3: Validate an IP-like candidate](#example-3-validate-an-ip-like-candidate)
  - [Example 4: Avoid a greedy match](#example-4-avoid-a-greedy-match)
  - [Example 5: Bound the input](#example-5-bound-the-input)
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

Regular expressions are useful for finding candidate shapes in text, such as an IP-like token or an event ID. They are not complete validators and must never turn a match into an accusation.

## Prerequisites

Complete Days 1–15 and understand strings, generators, and bounded processing.

## Outcomes

By the end of this lesson, you can:

- write a small regex with named groups
- use `finditer` to preserve positions
- distinguish candidate extraction from validation
- avoid catastrophic patterns and excessive input
- retain raw context and confidence

## The problem

A synthetic log line contains several tokens. Extract candidates with their positions, then validate the candidate using ordinary Python logic. The report must preserve the original line number without storing unnecessary raw data.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples do not authorize access to public systems, university systems, employer systems, or accounts that you do not own.

## Lesson

### Vocabulary

A **pattern** describes text shape. A **match** is evidence that the shape occurred. A **capture group** returns part of a match. A **validator** applies domain rules that a pattern alone may not express.

## Worked examples

### Example 1: Find a simple field

A named group makes the captured value readable.

```python
import re

pattern = re.compile(r"user=(?P<user>[a-z0-9_-]+)")
match = pattern.search("user=alice status=ok")
print(match.group("user"))
```

**What to observe:**

`alice`

### Example 2: Find every candidate

`finditer` provides each match and its position.

```python
for match in re.finditer(r"id=(?P<id>\d+)", "id=12 id=99"):
    print(match.group("id"), match.start())
```

**What to observe:**

`12 0` and `99 6` with positions relative to the string.

### Example 3: Validate an IP-like candidate

A simple shape can be checked with numeric policy afterward.

```python
def valid_ipv4(text):
    parts = text.split(".")
    return len(parts) == 4 and all(
        part.isdigit() and 0 <= int(part) <= 255 for part in parts
    )
```

**What to observe:**

`203.0.113.8` is accepted; `999.1.1.1` is rejected.

### Example 4: Avoid a greedy match

A narrow character class prevents a pattern from swallowing unrelated text.

```python
pattern = re.compile(r"token=(?P<token>[^\s]+)")
print(pattern.search("token=abc next=value").group("token"))
```

**What to observe:**

`abc`; the match stops at whitespace.

### Example 5: Bound the input

A regex should not process an unbounded line supplied by an unknown source.

```python
line = line[:2000]
if len(line) == 2000:
    truncated = True
```

**What to observe:**

The report can say that matching occurred on a bounded preview.

## Read the first example line by line

The first runnable example introduces **Regular Expressions and Careful Indicator Extraction**. Copy it into a new file and run it before changing anything. Then use this table to read the same code slowly. A line-by-line explanation does not replace practice: it shows you what to look for when a program behaves differently from your prediction.

| Line | Code | What Python is doing |
| ---: | --- | --- |
| 1 | `import re` | Import statement: the program asks for code from a module. |
| 2 | `` | Blank line: it separates ideas for the human reader. |
| 3 | `pattern = re.compile(r"user=(?P<user>[a-z0-9_-]+)")` | Assignment: Python evaluates the right side and stores the result under the name on the left. |
| 4 | `match = pattern.search("user=alice status=ok")` | Assignment: Python evaluates the right side and stores the result under the name on the left. |
| 5 | `print(match.group("user"))` | Output call: Python evaluates the argument and writes a representation to the terminal. |

After the run, write down the value created by each assignment, the condition tested by each branch, and the output that appeared. Change one input only. If the result changes, identify the line that used that input. If the result does not change, explain why the input was not part of the decision. This is the same tracing habit used later when reviewing security automation.
## Execution trace

For `user=alice`, the pattern first locates the literal `user=`, captures allowed characters into `user`, and returns the group. For a candidate IP, extraction finds text first and validation checks four numeric octets afterward.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| pattern is a validator | malformed candidate is trusted | validate with domain logic |
| greedy `.*` | one match consumes too much | use narrow classes and test boundaries |
| no input bound | expensive matching on huge data | cap line length |
| losing positions | reviewer cannot locate evidence | store line and character positions |
| printing full sensitive line | data leaks into output | report a redacted excerpt or identifier |

## Security application

Extract candidate IP-like values only from the synthetic fixture. Preserve line number and character position, validate octets, and label the result `candidate` rather than `malicious`.

## Line-by-line walkthrough

Read the first worked example from top to bottom rather than treating it as a magic recipe. The topic of this lesson is **Regular Expressions and Careful Indicator Extraction**. First identify the input: what value, file, record, command, or configuration enters the example? Next identify the operation that changes or examines it. Finally identify the output and ask whether that output is merely an observation or a security conclusion. Python executes statements in order, so the name created on one line must exist before a later line can use it. When a line is a function call, identify the arguments, the function's promised return value, and any visible side effect. When a line is a condition, translate it into an ordinary question before deciding whether the branch is correct.

For each example, copy the code into a fresh file and run it unchanged. Then annotate it without editing the original: write one sentence beside each line describing its role. A useful annotation format is `input`, `transform`, `check`, `decision`, or `output`. After that, change only one value and rerun the program. If the output changes, explain which line observed the changed value. If it does not change, explain why the value was not used or why the rule filtered it. This habit is more valuable than memorizing a finished script because it teaches you to trace unfamiliar security code.

The expected output is evidence about the program, not proof about the outside world. A message such as `review` means that the local rule selected a review label. It does not prove that a person attacked a system. Keep these two statements separate in your notes. Also record failures. A `TypeError`, `ValueError`, timeout, missing-file error, or rejected configuration is often the program correctly refusing an unsafe or ambiguous input. The repair should make the policy clearer rather than hiding the error with a broad catch.

## Prediction experiments

Before each experiment, write a prediction in a comment or notebook. In Experiment A, run the smallest valid input from Example 1 and write the exact output. In Experiment B, replace one valid value with an empty, malformed, missing, or boundary value relevant to **Regular Expressions and Careful Indicator Extraction**. Predict whether the program returns a result, raises an exception, rejects the record, or takes a different branch. In Experiment C, repeat the same input twice and inspect whether the program is deterministic. If a timestamp, random value, file order, or shared mutable state changes the result, identify that source of variation explicitly.

Do not use real addresses, credentials, private logs, public targets, or downloaded payloads for these experiments. Use the repository's synthetic fixtures, loopback values, `.invalid` names, and small in-memory inputs. Keep a table with four columns: input, prediction, observed output, and explanation. If the prediction is wrong, do not erase it. The mismatch is the part that teaches you how Python and the rule actually behave.

## Broken example and repair

Start with a deliberately broken version of the lesson's idea. A common beginner mistake is to combine parsing, policy, output, and side effects in one untested block. Another is to trust a value because it has the right shape, to use an unbounded loop, to print raw evidence, or to catch every exception. Break one rule at a time in a local copy. Run the program and capture the exception type or incorrect output. State the invariant that was violated: for example, "the input must be bounded," "the field must be validated before comparison," or "the report must not reveal raw fixture data."

Repair the example in small steps. First separate raw input from the internal value. Second add the narrowest check that expresses the intended policy. Third return or report a safe result. Fourth test one valid case, one invalid case, and one boundary case. Do not claim the repair is secure merely because it runs. Explain what remains outside the lesson's scope, such as authenticity, authorization, deployment configuration, or the correctness of the underlying policy. A good repair is easier for another beginner to inspect because each assumption is visible.

## Guided practice walkthrough

Use the following sequence before attempting the independent numbered questions. Choose one synthetic record related to **Regular Expressions and Careful Indicator Extraction** and write down its allowed shape. For example, specify which fields are required, which values are bounded, and which fields must never be printed. Create the smallest input that satisfies the shape. Run the first example and compare the output with your prediction. Add one validation check, rerun the valid record, then test a malformed record. Keep the malformed record in the test set instead of deleting it.

Next, refactor one step into a small function or named stage. Give the stage one job and a name that describes the job. Add a print statement only while debugging, then remove it or replace it with a safe summary. Write one assertion about the result. Finally, explain the data flow in five sentences: where the fixture began, which transformation occurred, which check was applied, what label or value was produced, and what the program deliberately refused to do. Ask a peer to read the explanation without seeing the code and identify any assumption that was not documented.

## Bounded cybersecurity fixture walkthrough

The security application in this lesson uses a local, synthetic fixture. Treat the fixture as untrusted input even though it is stored in the repository. Set a maximum number of records, maximum field length, and maximum output size appropriate to the exercise. Preserve a safe source label such as `training-fixture`, but do not treat that label as proof that the data is authentic. If the fixture contains an indicator-like string, keep it inert and do not resolve, scan, connect to, upload, or enrich it from the network.

A defensible report should distinguish at least four things: what was observed, what rule matched, what uncertainty remains, and what action is permitted in this lab. For example, `observed=synthetic_event`, `rule=high_value`, `confidence=training-only`, and `action=write-local-report`. The last field is a laboratory boundary, not an operational recommendation. If your code cannot make that distinction, stop and improve the report before adding features. Security engineering is not only about detecting a pattern; it is also about limiting authority, preserving provenance, and communicating uncertainty.

At the end, perform a small review. Check that the program uses only local fixtures, has a finite workload, handles malformed input, avoids raw sensitive output, and leaves the fixture unchanged. Then write one residual-risk sentence. A useful form is: "This lesson demonstrates Regular Expressions and Careful Indicator Extraction on synthetic data, but it does not establish authenticity, authorization, production readiness, or the presence of a real attack.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples above as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run `python -m course_days.day016`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A regex finds a shape; a validator adds domain rules; neither one proves intent, ownership, or compromise.

## Limitations

Regex syntax can become complex and expensive. Prefer small patterns, bounds, tests, and a standard library parser when a protocol already defines one.


## References

[1]: https://docs.python.org/3/ "Python documentation"
[2]: https://docs.python.org/3/tutorial/ "The Python tutorial"
[3]: https://owasp.org/www-project-top-ten/ "OWASP Top 10"
[4]: https://csrc.nist.gov/glossary "NIST cybersecurity glossary"

[← Day 15](../day_15_iterators_and_generators/day_15_iterators_and_generators.md) · [Day index](../DAY_INDEX.md) · [Day 17 →](../day_17_dates_and_timelines/day_17_dates_and_timelines.md)
