# Day 120: Final Demonstration and Engineering Judgment

[← Day 119](../119_day_capstone_security_review/119_day_capstone_security_review.md) · [Day index](../DAY_INDEX.md) · [Day 121 →](../120_day_final_demonstration/120_day_final_demonstration.md)

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

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Record the evidence, output, edge case, and limitation requested by each question.

## Finish line

Run `python -m course_days.day120`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Engineering judgment is the ability to make, test, explain, and limit a decision under real constraints.

## Limitations

Completing the course does not make someone an advanced engineer by itself; continued practice, mentorship, university work, code review, and responsible experience remain essential.

[← Day 119](../119_day_capstone_security_review/119_day_capstone_security_review.md) · [Day index](../DAY_INDEX.md) · [Day 121 →](../120_day_final_demonstration/120_day_final_demonstration.md)
