# Day 75: MITRE ATT&CK Mapping as Documentation

[← Day 74](../day_74_detection_thresholds/day_74_detection_thresholds.md) · [Day index](../DAY_INDEX.md) · [Day 76 →](../day_76_alert_triage/day_76_alert_triage.md)

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

Framework mappings can help analysts communicate behavior, but a technique label is not proof that an adversary used it. The mapping should link observable evidence to a cautious hypothesis.

## Prerequisites

Complete Day 74. Use only the local course fixtures, loopback services, and synthetic records described by the lesson.

## Outcomes

By the end of this lesson, you can:

- explain the concept before using the tool
- run and modify every worked example
- test normal, boundary, and failure behavior
- state the trust boundary and residual risk
- complete the numbered cybersecurity exercises

## The problem

Map synthetic behavior descriptions to a documented technique reference without claiming attribution.

## Security boundary

This lesson is educational and bounded. It does not authorize public scanning, credential use, interception, exploit delivery, real-user profiling, or changes to systems you do not own.

## Lesson

### Vocabulary

A tactic describes a goal. A technique describes a behavior. Mapping links evidence to a framework entry. Attribution claims actor identity and requires much more evidence.

## Worked examples

### Example 1: Describe behavior

Start with what the fixture actually shows.

```python
observation = {
    "event": "process_started",
    "command": "python --version",
    "source": "fixture",
}
print(observation)
```

**What to observe:**

The observation is concrete.

### Example 2: Map cautiously

A mapping is a hypothesis about behavior.

```python
mapping = {
    "observation": "process_started",
    "technique": "training-reference",
    "confidence": "low",
}
print(mapping)
```

**What to observe:**

The confidence is not certainty.

### Example 3: Separate tactic

A broad goal and a specific behavior are different fields.

```python
mapping["tactic"] = "execution-like"
print(mapping)
```

**What to observe:**

The fields communicate different levels.

### Example 4: Attach evidence

A mapping without evidence is decorative.

```python
mapping["evidence_ref"] = {"case_id": "training-75", "line": 1}
print(mapping)
```

**What to observe:**

The reviewer can return to the fixture.

### Example 5: Reject attribution

A framework match does not identify a person or group.

```python
mapping["attribution"] = "not assessed"
print(mapping)
```

**What to observe:**

The report avoids overclaiming.

## Execution trace

The analyst records observation, selects a cautious framework reference, attaches evidence and confidence, and explicitly leaves attribution unassessed.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| technique equals attacker | attribution is invented | label mapping as hypothesis |
| no evidence reference | mapping cannot be reviewed | link case and line |
| framework name only | behavior is not explained | write observation first |
| force a mapping | every event becomes a technique | allow unmapped |
| ignore version | framework changes | record version/date |

## Security application

Use fictional observations and framework documentation as a vocabulary aid. Do not publish accusations or map real people from thin evidence.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples as a starting point, then record the requested output, edge case, and limitation.

## Finish line

Run `python -m course_days.day075`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Framework mapping improves shared language; evidence and uncertainty remain the foundation.

## Limitations

Frameworks are descriptive and versioned; they do not replace investigation, detection engineering, or legal standards.

[← Day 74](../day_74_detection_thresholds/day_74_detection_thresholds.md) · [Day index](../DAY_INDEX.md) · [Day 76 →](../day_76_alert_triage/day_76_alert_triage.md)
