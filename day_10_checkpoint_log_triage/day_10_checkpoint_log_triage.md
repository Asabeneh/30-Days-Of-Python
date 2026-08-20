# Day 10: Checkpoint: Build a Safe Log-Triage Classifier

[← Day 9](../day_9_functions_and_validation/day_9_functions_and_validation.md) · [Day index](../DAY_INDEX.md) · [Day 11 →](../day_11_function_contracts/day_11_function_contracts.md)








## Table of contents

- [Welcome](#welcome)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
- [1. A pipeline is a sequence of small stages](#1-a-pipeline-is-a-sequence-of-small-stages)
- [2. Parse a simple key-value line](#2-parse-a-simple-key-value-line)
- [3. Classify without making accusations](#3-classify-without-making-accusations)
- [4. Count outcomes explicitly](#4-count-outcomes-explicitly)
- [5. Report completeness](#5-report-completeness)
- [Worked examples](#worked-examples)
  - [Example 1: A first runnable case](#example-1-a-first-runnable-case)
  - [Example 2: A boundary case](#example-2-a-boundary-case)
  - [Example 3: A deliberate experiment](#example-3-a-deliberate-experiment)
  - [Example 4: A bounded security fixture](#example-4-a-bounded-security-fixture)
  - [Example 5: Invalid input remains visible in the summary](#example-5-invalid-input-remains-visible-in-the-summary)
- [Execution trace](#execution-trace)
- [Common mistakes and repairs](#common-mistakes-and-repairs)
- [Guided practice](#guided-practice)
- [Security application](#security-application)
- [Independent exercises](#independent-exercises)
- [Finish line](#finish-line)
- [References](#references)

## Welcome

Today you will combine the first nine days into one small program. This is not a leap into advanced security tooling. It is a controlled checkpoint that proves you can move from text to values, validate them, choose a label, count records, and report what happened without exposing sensitive-looking fields.

This lesson is designed for a learner who may still need to look up how to create a file, run it, or read an error. Type the examples instead of reading them passively. Before running an experiment, write down what you expect. The difference between your prediction and Python's output is where learning happens.

## Prerequisites

Complete Day 9. Use the repository's local synthetic fixtures only. Keep a terminal open at the repository root and run each file with the Python command that worked on your computer.

## Outcomes

By the end of this lesson, you should be able to explain the new vocabulary in your own words, run and modify the examples, predict at least one boundary case, repair a deliberate mistake, and apply the idea to a bounded cybersecurity fixture.

## The problem

A log-triage program must accept a small synthetic fixture, parse each line, classify it according to a documented rule, count outcomes, and tell the learner if processing stopped or completed. The program must be honest about malformed lines and bounded in its work.

## Security boundary

This lesson is educational and local. It does not authorize public scanning, credential use, data collection, exploitation, interception, or changes to systems you do not own. The cybersecurity examples use invented names, loopback targets, or repository fixtures.

## Keywords and terms

A **fixture** is a supplied test input. A **pipeline** is a sequence of transformations. **Triage** is prioritizing items for review, not declaring guilt. A **summary** is a compact report. **Completeness** says whether all permitted input was processed.

## Topics

Start with a fixture represented as a list of strings:

```python
lines = [
    "severity=8 source=training-auth event=login_failed",
    "severity=2 source=training-auth event=logout",
    "severity=high source=training-auth event=login_failed",
]
```

This is not a real log and it does not come from a network. It is a small, visible input. Begin with one line and split it:

```python
line = lines[0]
fields = {}
for part in line.split():
    key, value = part.split("=", 1)
    fields[key] = value

print(fields)
```

Expected output is a dictionary containing three text fields. Notice that the severity is still text. Pass it through the parser from Day 9:

```python
severity = parse_severity(fields["severity"])
```

The third line contains `severity=high`, so the parser will raise an expected conversion error. A checkpoint program should not crash the whole report because one synthetic line is malformed. Decide on a policy: count the line as `invalid`, record a safe reason, and continue.

A small classification function might look like this:

```python
def classify(severity_text, source):
    try:
        severity = parse_severity(severity_text)
    except (TypeError, ValueError):
        return "invalid"

    if source != "training-auth":
        return "unknown-source"
    if severity >= 7:
        return "review"
    return "routine"
```

This function does not print, access files, or contact a network. It receives values and returns one label. The caller can count the labels and decide how to report them.

Build a counter:

```python
counts = {"review": 0, "routine": 0, "invalid": 0, "unknown-source": 0}
label = classify("8", "training-auth")
counts[label] += 1
print(counts)
```

The dictionary contains every expected label before processing starts. That means a zero count is visible in the final report. A report that omits zero categories can be harder to compare across runs.

Add a bounded loop:

```python
limit = 100
processed = 0

for line in lines:
    if processed >= limit:
        break
    processed += 1
    print(f"processing line {processed}")
```

The limit is much larger than this fixture, but it demonstrates the policy. A real tool should also bound line length, total bytes, and output size.

A complete checkpoint design has stages:

| Stage | Question |
| --- | --- |
| Read | Which fixture is permitted? |
| Parse | Can this line become fields? |
| Convert | Can severity become an integer? |
| Validate | Is severity within 0–10? |
| Classify | Which documented label applies? |
| Count | How many labels occurred? |
| Report | What happened, and was processing complete? |

Do not hide all stages in one enormous function. Give each stage a small job and test it with a tiny input before composing the pipeline.

The final report might look like:

```text
source=synthetic-fixture
processed=3
complete=True
review=1
routine=1
invalid=1
unknown-source=0
```

The report says what the classifier did. It does not say that a real attack happened or that any person is dangerous.

## 1. A pipeline is a sequence of small stages

A log-triage program becomes easier to explain when it has separate stages:

| Stage | Question |
| --- | --- |
| Read | Which local fixture is permitted? |
| Parse | Can the text become fields? |
| Convert | Can the severity become an integer? |
| Validate | Is the value inside the allowed range? |
| Classify | Which documented label applies? |
| Report | What happened, and was processing complete? |

Do not hide all six questions inside one giant function. A beginner can test one stage at a time, and a reviewer can identify where a failure occurred.

## 2. Parse a simple key-value line

```python
line = "severity=8 source=training-auth event=login_failed"
fields = {}
for part in line.split():
    key, value = part.split("=", 1)
    fields[key] = value
print(fields)
```

Output:

```text
{'severity': '8', 'source': 'training-auth', 'event': 'login_failed'}
```

Notice that severity is still text. Parsing fields and converting values are separate tasks. The `1` in `split("=", 1)` prevents a later equals sign from being split into too many pieces.

## 3. Classify without making accusations

```python
def classify(severity_text, source, known_events, event):
    try:
        severity = int(severity_text)
    except ValueError:
        return "invalid"
    if not 0 <= severity <= 10:
        return "out-of-range"
    if source == "":
        return "missing-source"
    if event not in known_events:
        return "unknown-event"
    if severity >= 7:
        return "review"
    return "routine"
```

The labels describe what the local rule found. They do not identify an attacker or prove compromise.

## 4. Count outcomes explicitly

```python
counts = {"review": 0, "routine": 0, "invalid": 0}
label = "review"
counts[label] += 1
print(counts)
```

Initialize every expected category so zero values remain visible. A report that omits `invalid=0` can be harder to compare with another run.

## 5. Report completeness

A finite limit is not the same as complete processing. If the fixture contains more records than the permitted limit, say so:

```python
limit = 2
processed = 0
complete = True
for line in ["a", "b", "c"]:
    if processed >= limit:
        complete = False
        break
    processed += 1
print(processed, complete)
```

Output:

```text
2 False
```

The safe report tells the reader what the program actually processed.

## Worked examples

Run the examples in order. Each one changes only a small part of the previous idea.

### Example 1: A first runnable case

Run the smallest version first and explain what each line contributes.

### Example 2: A boundary case

Change exactly one input to an empty, malformed, or out-of-range value. Predict the result before running it.

### Example 3: A deliberate experiment

Make one controlled change, record the output, and compare it with your prediction. Do not change several lines at once.

### Example 4: A bounded security fixture

Apply the idea to the synthetic fixture in this lesson. The fixture is local, finite, and invented; it is not permission to inspect real systems.

### Example 5: Invalid input remains visible in the summary

```python
results = ["review", "routine", "invalid"]
counts = {"review": 0, "routine": 0, "invalid": 0}
for result in results:
    counts[result] += 1
print(counts)
```

The summary keeps `invalid` separate from `routine`. A malformed record should not silently become a reassuring result.

## Execution trace

Trace the three-line fixture:

| Line | Raw severity | Source | Result | Count change |
| ---: | --- | --- | --- | --- |
| 1 | `8` | `training-auth` | `review` | review +1 |
| 2 | `2` | `training-auth` | `routine` | routine +1 |
| 3 | `high` | `training-auth` | `invalid` | invalid +1 |

After the loop, `processed` is 3 and `complete` is true because the fixture ended before the limit. If the fixture contains 150 lines and the limit is 100, `complete` must be false. Do not report that the entire source was clean when only the first 100 permitted records were processed.

## Common mistakes and repairs

| Mistake | Symptom | Repair |
| --- | --- | --- |
| One malformed line crashes all processing | The report is incomplete without saying why. | Catch expected input errors per line. |
| Invalid becomes routine | Bad data receives a reassuring label. | Keep `invalid` separate. |
| No processing limit | Work grows with untrusted input. | Bound records and bytes. |
| Print raw lines | Sensitive fields may leak. | Report line number and safe reason. |
| Count only positive labels | Zero categories disappear. | Initialize every expected category. |
| Classifier claims an attack | A rule becomes an accusation. | Say `review` or `needs-review`. |

## Guided practice

Build the project in seven checkpoints:

1. Create a three-line in-memory fixture.
2. Write a parser for space-separated `key=value` fields.
3. Test the parser with one missing equals sign and one extra equals sign.
4. Reuse a bounded severity parser.
5. Write a classifier with `review`, `routine`, `invalid`, and `unknown-source` outcomes.
6. Process the fixture with a finite record limit and count every outcome.
7. Print a safe summary containing source label, counts, processed count, and completeness.

At each checkpoint, run the smallest test possible. Keep raw lines out of the final report. If you need to debug a line, use a synthetic fixture and print only a redacted representation.

## Security application

This checkpoint demonstrates defensive programming habits rather than offensive capability. The input is synthetic. The work is finite. The parser and validator are explicit. Invalid data is not silently treated as safe. The report distinguishes review from routine and does not identify a person or contact a target.

A real log-triage system would need authenticated collection, schema versioning, time handling, access control, retention, tests against realistic formats, and human review. This checkpoint teaches only the small programming foundation required before those topics.

## Independent exercises

Complete these in [`practice/exercises.md`](practice/exercises.md) in order:

1. Run the starter and explain each printed field.
2. Parse one valid fixture line into a dictionary.
3. Parse a line with an extra equals sign using `split("=", 1)`.
4. Handle a line without an equals sign as invalid.
5. Reuse `parse_severity` and classify valid and invalid severities.
6. Add a known-source and unknown-source fixture.
7. Count each result category, including categories with zero results.
8. Add a processing limit and a `complete` field.
9. Write a safe summary that never prints a raw line.
10. Add tests for empty input, malformed input, valid high severity, and a source mismatch.
11. Explain why a `review` label is not an attack verdict.
12. Explain how a bounded loop protects resources but may reduce completeness.
13. Write a short threat model listing asset, input, trust boundary, and residual risk.
14. Safety question: state exactly what this project is allowed to read and what it is forbidden to touch.

Use [hints](practice/hints.md) before [solutions](practice/solutions.md), and write a short explanation beside every code change.

## Finish line

Day 10 is complete when you can explain the pipeline from fixture to report, process valid and invalid lines without losing the distinction, enforce a finite limit, test edge cases, and state the safety boundary without being prompted.

## References

[1]: https://docs.python.org/3/tutorial/datastructures.html "Python data structures"
[2]: https://docs.python.org/3/tutorial/controlflow.html "Python control flow"
[3]: https://docs.python.org/3/library/exceptions.html "Python exceptions"
[4]: https://csrc.nist.gov/glossary/term/log_analysis "NIST log analysis glossary"
[5]: https://owasp.org/www-community/attacks/Denial_of_Service "OWASP denial of service overview"

[← Day 9](../day_9_functions_and_validation/day_9_functions_and_validation.md) · [Day index](../DAY_INDEX.md) · [Day 11 →](../day_11_function_contracts/day_11_function_contracts.md)
