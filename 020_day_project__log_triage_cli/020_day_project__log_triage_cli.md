# Day 20: Checkpoint: Build a Log-Triage CLI

[← Day 19](../019_day_testing_with_pytest/019_day_testing_with_pytest.md) · [Day index](../DAY_INDEX.md) · [Day 21 →](../021_day_virtual_environments/021_day_virtual_environments.md)

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

A command-line tool is where modules, errors, files, generators, regex, timelines, dataclasses, and tests meet. This checkpoint turns the phase into a small artifact that another learner can run and review.

## Prerequisites

Complete Days 11–19. Run formatting, linting, compilation, and tests before starting the project.

## Outcomes

By the end of this lesson, you can:

- design a CLI with explicit arguments and exit statuses
- compose validated modules without hidden side effects
- produce bounded, explainable output
- test normal, malformed, missing, and out-of-scope cases
- write a threat model and limitations section

## The problem

Build `log-triage` for the supplied synthetic fixture. It should accept an input path beneath a fixture root, process a maximum number of lines, classify only validated records, and write a report under a dedicated output directory.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples do not authorize access to public systems, university systems, employer systems, or accounts that you do not own.

## Lesson

### Vocabulary

A **CLI** is a user-facing boundary around program behavior. An **exit status** communicates success or failure to a shell or automation. A **report** should distinguish raw observations, derived labels, rejected records, and truncation.

## Worked examples

### Example 1: Define the command

Use explicit options instead of positional magic for security-sensitive bounds.

```python
python -m course_days.day020 --input shared/fixtures/events.log --limit 100 --output training-output/report.json
```

**What to observe:**

The command states its input, limit, and output.

### Example 2: Parse arguments

`argparse` provides help and type conversion, but application bounds still belong in validation.

```python
parser.add_argument("--limit", type=int, default=100)
args = parser.parse_args([])
print(args.limit)
```

**What to observe:**

`100` is the documented default.

### Example 3: Compose the pipeline

Each stage should have a single responsibility.

```python
raw_lines = read_lines(input_path, limit)
records = (parse_line(line) for line in raw_lines)
validated = (validate(record) for record in records)
```

**What to observe:**

The pipeline is lazy and bounded; add rejection accounting before production.

### Example 4: Represent a report

A structured report makes incomplete work visible.

```python
report = {"processed": 3, "accepted": 2, "rejected": 1, "truncated": False}
```

**What to observe:**

The report does not pretend that rejected data was accepted.

### Example 5: Exit deliberately

Automation needs a stable status contract.

```python
if report["rejected"]:
    raise SystemExit(2)
raise SystemExit(0)
```

**What to observe:**

The project must document whether rejected records are an error, warning, or expected result.

## Execution trace

The CLI parses options, resolves and bounds the input, streams lines, parses and validates records, applies the pure classifier, writes a safe report, and exits with a documented status. A failure in one boundary should not become an empty successful report.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| arbitrary input path | fixture boundary is bypassed | resolve beneath an allowed root |
| unlimited default | CLI can consume unexpected resources | choose a finite default |
| hidden output location | reports overwrite source data | require a dedicated output directory |
| mixed raw and derived data | users cannot audit decisions | label fields clearly |
| no README | another learner cannot reproduce it | document setup, scope, examples, and reset |

## Security application

The checkpoint is local-only and synthetic. The README must name the allowed fixture root, maximum line and byte limits, output cleanup, test command, threat model, false-positive limitations, and the fact that a label is not proof of compromise.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples above as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run `python -m course_days.day020`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A CLI is a chain of explicit boundaries; its quality is the quality of its input contract, resource limits, evidence labels, and failure behavior.

## Limitations

This is not a production SIEM, incident-response platform, or detector of real attacks. It demonstrates composition and safe evidence handling. Real deployments require operational ownership, authorization, monitoring, and review.

[← Day 19](../019_day_testing_with_pytest/019_day_testing_with_pytest.md) · [Day index](../DAY_INDEX.md) · [Day 21 →](../021_day_virtual_environments/021_day_virtual_environments.md)
