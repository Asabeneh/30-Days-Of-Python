# Day 48: Rate Limits, Retries, and Backoff

[← Day 47](../047_day_packet_capture_fixtures/047_day_packet_capture_fixtures.md) · [Day index](../DAY_INDEX.md) · [Day 49 →](../049_day_network_baselines/049_day_network_baselines.md)

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

Retries can recover from transient local failures or amplify load. A security engineer must distinguish a bounded retry policy from a loop that turns one failure into an outage.

## Prerequisites

Complete Day 47. Run the repository checks and use only the local fixtures and explicitly authorized loopback services.

## Outcomes

By the end of this lesson, you can:

- explain the protocol or security property in plain language
- run and modify every worked example
- test a normal, boundary, and failure case
- identify the trust boundary and residual risk
- connect the concept to the numbered cybersecurity exercises

## The problem

Implement a local retry helper that stops after a finite number of attempts and reports the final state.

## Security boundary

Use synthetic data, local fixtures, and loopback-only demonstrations. This lesson does not authorize scanning, interception, credential use, remote command execution, or changes to systems you do not own.

## Lesson

### Vocabulary

A **rate limit** bounds operations per time. A **retry** repeats a failed operation. **Backoff** spaces attempts. **Jitter** varies wait time to avoid synchronized retries.

## Worked examples

### Example 1: Bound attempts

The attempt count is part of the contract.

```python
def attempts(max_attempts=3):
    for number in range(1, max_attempts + 1):
        yield number


print(list(attempts()))
```

**What to observe:**

`[1, 2, 3]`

### Example 2: Retry a local function

Only retry an explicitly transient error.

```python
def retry(function, attempts=3):
    for number in range(attempts):
        try:
            return function()
        except TimeoutError:
            if number == attempts - 1:
                raise
```

**What to observe:**

The final timeout is not hidden.

### Example 3: Calculate capped backoff

A cap prevents wait time from growing without bound.

```python
def delay(attempt, cap=8):
    return min(cap, 2**attempt)


print([delay(n) for n in range(4)])
```

**What to observe:**

`[1, 2, 4, 8]`

### Example 4: Respect a budget

Retries share a total time budget.

```python
budget = {"attempts": 3, "seconds": 10}
print(budget)
```

**What to observe:**

The caller can stop when either budget is exhausted.

### Example 5: Report partial work

No response after retries is an explicit outcome.

```python
print({"status": "unavailable_after_retries", "complete": False})
```

**What to observe:**

The report does not claim the target was down or malicious.

## Execution trace

The operation checks whether the error is retryable, increments a finite attempt count, waits within a cap, and returns success or an incomplete result with the reason.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| retry every exception | bugs repeat | classify transient failures |
| no cap | delays or attempts grow | cap count and time |
| synchronized clients | load spike | add jitter where appropriate |
| retry unsafe action | duplicate side effects | require idempotency |
| no status | failure looks empty | report attempts and final state |

## Security application

Demonstrate with a local function that fails predictably. Do not use retries to increase request volume against any external service.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested local command, inspect its output, and record the limitation asked for by the exercise.

## Finish line

Run `python -m course_days.day048`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Reliability controls are bounded decisions about when to stop; a retry is not a permission to keep trying.

## Limitations

Backoff tuning depends on the service and workload. It cannot repair a broken authorization or protocol design.

[← Day 47](../047_day_packet_capture_fixtures/047_day_packet_capture_fixtures.md) · [Day index](../DAY_INDEX.md) · [Day 49 →](../049_day_network_baselines/049_day_network_baselines.md)
