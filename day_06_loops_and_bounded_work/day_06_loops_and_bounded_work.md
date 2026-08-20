# Day 6: Loops, Bounds, and Resource Safety

[← Day 5](../day_05_branching_and_triage/day_05_branching_and_triage.md) · [Day index](../DAY_INDEX.md) · [Day 7 →](../day_07_collections_and_iocs/day_07_collections_and_iocs.md)





## Table of contents

- [Welcome](#welcome)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Vocabulary](#vocabulary)
- [Lesson](#lesson)
- [1. A `for` loop repeats a known sequence](#1-a-for-loop-repeats-a-known-sequence)
- [2. `range` creates a predictable counting sequence](#2-range-creates-a-predictable-counting-sequence)
- [3. A `while` loop needs a changing condition](#3-a-while-loop-needs-a-changing-condition)
- [4. Bounds protect time and memory](#4-bounds-protect-time-and-memory)
- [5. `break` and `continue` change the path](#5-break-and-continue-change-the-path)
- [Worked examples](#worked-examples)
  - [Example 1: A first runnable case](#example-1-a-first-runnable-case)
  - [Example 2: A boundary case](#example-2-a-boundary-case)
  - [Example 3: A deliberate experiment](#example-3-a-deliberate-experiment)
  - [Example 4: A bounded security fixture](#example-4-a-bounded-security-fixture)
  - [Example 5: A limit changes completeness, not truth](#example-5-a-limit-changes-completeness-not-truth)
- [Execution trace](#execution-trace)
- [Common mistakes and repairs](#common-mistakes-and-repairs)
- [Guided practice](#guided-practice)
- [Security application](#security-application)
- [Independent exercises](#independent-exercises)
  - [Additional beginner checkpoint](#additional-beginner-checkpoint)
- [Finish line](#finish-line)
- [References](#references)

## Welcome

A loop repeats work. Repetition is powerful because security tools often process many records, but repetition is also a place where a beginner can accidentally create an infinite loop, read an unbounded file, or produce an enormous report. Today you will learn repetition with an explicit stopping rule.

This lesson is designed for a learner who may still need to look up how to create a file, run it, or read an error. Type the examples instead of reading them passively. Before running an experiment, write down what you expect. The difference between your prediction and Python's output is where learning happens.

## Prerequisites

Complete Day 5. Use the repository's local synthetic fixtures only. Keep a terminal open at the repository root and run each file with the Python command that worked on your computer.

## Outcomes

By the end of this lesson, you should be able to explain the new vocabulary in your own words, run and modify the examples, predict at least one boundary case, repair a deliberate mistake, and apply the idea to a bounded cybersecurity fixture.

## The problem

A program needs to inspect several synthetic events without copying the same line five times. It also needs to stop. A loop without a bound or a progress rule can consume time, memory, and attention indefinitely.

## Security boundary

This lesson is educational and local. It does not authorize public scanning, credential use, data collection, exploitation, interception, or changes to systems you do not own. The cybersecurity examples use invented names, loopback targets, or repository fixtures.

## Vocabulary

A **loop** repeats a block. A `for` loop visits items in a sequence. A `while` loop continues while a condition is true. A **bound** is a deliberate maximum. `break` stops a loop; `continue` skips to the next iteration. An **iteration** is one pass through the body.

## Lesson

Start with a `for` loop:

```python
for number in [1, 2, 3]:
    print(number)
```

Expected output is one number per line. Python takes the first item, assigns it to `number`, runs the indented body, then repeats for the next item. The name `number` changes during the loop, but the list is finite.

The `range` function creates a sequence of numbers for a loop:

```python
for index in range(3):
    print(f"index={index}")
```

The output is 0, 1, and 2. The stop value 3 is not included. This is a common source of off-by-one mistakes. Read `range(3)` as “produce three positions starting at zero,” not “count from one to three.”

Use a counter when you need a total:

```python
failed = ["a", "b", "c"]
count = 0

for event in failed:
    count += 1
    print(f"examining={event}")

print(f"total={count}")
```

The counter starts at zero and increases once per item. The list is already finite, so this loop has a natural bound.

A `while` loop needs a progress rule:

```python
attempt = 0
while attempt < 3:
    print(f"attempt={attempt}")
    attempt += 1
```

If you forget `attempt += 1`, the condition remains true forever. A safe `while` loop should make its changing state and maximum attempts visible.

You can add a second safety bound:

```python
items_seen = 0
for event in events:
    if items_seen >= 100:
        break
    print(event)
    items_seen += 1
```

This protects the consumer even if `events` is larger than expected. A bound is not an invitation to ignore the data source; it is a last line of resource control.

`continue` can skip an item, but use it carefully:

```python
for event in ["", "login_failed", "", "logout"]:
    if event == "":
        continue
    print(event)
```

The empty values are skipped. If you skip too much, your report may look clean because the program discarded the evidence. Record how many items were skipped when that matters.

Nested loops multiply work. A loop over 100 files containing a loop over 1,000 lines may inspect 100,000 combinations. Before adding nesting, estimate the work and set a bound.

## 1. A `for` loop repeats a known sequence

A loop repeats work. Start with a short list:

```python
events = ["login_failed", "logout", "access_denied"]
for event in events:
    print(event)
```

Python takes the first item, stores it under `event`, runs the indented body, then repeats for the next item. The loop ends when the sequence has no more items.

## 2. `range` creates a predictable counting sequence

```python
for record_number in range(1, 4):
    print(record_number)
```

Output:

```text
1
2
3
```

The stop value `4` is not included. This “stop before” rule is common and worth testing with a tiny range before using a larger one.

## 3. A `while` loop needs a changing condition

```python
attempt = 1
while attempt <= 3:
    print(attempt)
    attempt += 1
```

The update `attempt += 1` is what allows the loop to finish. If you remove it, the condition remains true forever. Never test an unknown loop against a real large input until you have proved that the loop has a limit.

## 4. Bounds protect time and memory

A bound is a maximum amount of permitted work:

```python
items = ["a", "b", "c", "d"]
limit = 3
processed = 0
for item in items:
    if processed >= limit:
        break
    print(item)
    processed += 1
print(f"processed={processed}")
```

Output:

```text
a
b
c
processed=3
```

The loop did not claim that the fourth item was safe or unsafe. It stopped because the exercise allowed only three records. In security automation, a bounded result should say whether processing was complete.

## 5. `break` and `continue` change the path

`break` ends the loop. `continue` skips the rest of the current iteration and moves to the next item. Use both only when the reason is clear. A hidden `continue` can accidentally skip evidence; a hidden `break` can make a report incomplete.

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

### Example 5: A limit changes completeness, not truth

```python
items = ["a", "b", "c"]
limit = 2
processed = items[:limit]
print(processed)
print(len(processed) == len(items))
```

The program processed two items and reports that processing was not complete. A bounded result should never be described as a complete inspection when the limit stopped the work.

## Execution trace

Trace:

```python
items = ["a", "b", "c"]
count = 0
for item in items:
    count += 1
    print(item, count)
```

| Iteration | `item` | `count` before | `count` after |
| ---: | --- | ---: | ---: |
| 1 | `a` | 0 | 1 |
| 2 | `b` | 1 | 2 |
| 3 | `c` | 2 | 3 |

For a `while` loop, trace both the condition and the changing value. If the value never changes toward the stopping condition, the loop is unsafe. The fastest way to debug a loop is often to print a small state value and add a temporary maximum iteration count.

## Common mistakes and repairs

| Mistake | Symptom | Repair |
| --- | --- | --- |
| Forgetting progress in `while` | Infinite loop. | Update the state every iteration. |
| Assuming `range(3)` includes 3 | Missing or extra work. | Test the endpoints explicitly. |
| No maximum input count | Resource use depends on an untrusted source. | Set a finite bound. |
| `continue` hides evidence | The report silently loses records. | Count and explain skipped items. |
| Nested loops without estimating work | Slow or exhausting processing. | Bound each dimension or redesign. |

## Guided practice

Write a loop in checkpoints. First loop over three literal event names and print them. Then count them. Then skip empty strings while incrementing a `skipped` counter. Finally, add a maximum of three processed items to a list containing five items.

For each change, write the expected processed count and skipped count before running. If your program produces a different answer, inspect the state at the start and end of each iteration. Do not begin with a file or network source; learn the loop with a small list first.

## Security application

A log tool may need to process many records, but “many” must be turned into a documented resource policy. A training parser can accept at most 100 lines, 1 MB, or 10 seconds of work. These numbers are examples, not universal security thresholds.

When a bound is reached, report that processing was incomplete. Do not silently present the first 100 records as if they were the entire source. A bounded report is more honest when it says `complete=False` or `truncated=True`.

## Independent exercises

Complete these in [`practice/exercises.md`](practice/exercises.md) in order:

1. Loop over three event names and predict the output order.
2. Use `range(5)` and write down the exact values it produces.
3. Count a list without using `len`.
4. Write a `while` loop with a maximum of five attempts.
5. Deliberately remove the progress statement and explain why the loop would not end.
6. Skip empty events and count how many were skipped.
7. Stop after three processed events and report truncation.
8. Estimate the work in a nested loop of 10 files and 100 lines.
9. Build a synthetic bounded log summary.
10. Explain why a loop limit protects availability but can reduce completeness.
11. Write a test for an empty list and a list larger than the bound.
12. Safety question: explain why an unbounded loop over an untrusted file can become a security problem.



### Additional beginner checkpoint

Pause before adding another feature. Read the current program aloud as a sequence of decisions: what enters, what is transformed, what is checked, and what leaves. Write down one value that is allowed, one value that must be rejected, and one value whose meaning is uncertain. This distinction matters in cybersecurity because an unknown observation should not silently become a safe conclusion. Run the allowed case, the rejected case, and the uncertain case separately. Keep the exact output in your notes and explain which line produced it.

Now make the smallest useful improvement. Give one name a clearer meaning, extract one repeated operation, or add one explicit boundary check. Run the same three cases again. If the behavior changed, explain whether the change was intended. If a test now fails, treat the failure as information about the contract rather than deleting the test. Finish by writing one sentence about the lesson's limitation: a local Python rule can organize synthetic evidence, but it cannot establish authorization, authenticity, or the truth of a real-world accusation.

## Finish line

Day 6 is complete when you can explain one `for` loop and one `while` loop step by step, identify their stopping rule, add a finite work bound, account for skipped data, and report incomplete processing honestly.

## References

[1]: https://docs.python.org/3/tutorial/controlflow.html#for-statements "Python for statements"
[2]: https://docs.python.org/3/reference/compound_stmts.html#while "Python while statements"
[3]: https://docs.python.org/3/library/functions.html#range "Python range documentation"
[4]: https://owasp.org/www-community/attacks/Denial_of_Service "OWASP denial of service overview"

[← Day 5](../day_05_branching_and_triage/day_05_branching_and_triage.md) · [Day index](../DAY_INDEX.md) · [Day 7 →](../day_07_collections_and_iocs/day_07_collections_and_iocs.md)
