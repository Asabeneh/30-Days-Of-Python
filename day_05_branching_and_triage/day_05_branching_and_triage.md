# Day 5: Branching and a First Triage Classifier

[← Day 4](../day_04_operators_and_decisions/day_04_operators_and_decisions.md) · [Day index](../DAY_INDEX.md) · [Day 6 →](../day_06_loops_and_bounded_work/day_06_loops_and_bounded_work.md)

## Welcome

Yesterday you learned the symbols that produce decisions. Today you will slow down and design a branching program carefully. The goal is not to write clever conditions; it is to make the path a reader can predict, test, and explain.

This lesson is designed for a learner who may still need to look up how to create a file, run it, or read an error. Type the examples instead of reading them passively. Before running an experiment, write down what you expect. The difference between your prediction and Python's output is where learning happens.

## Prerequisites

Complete Day 4. Use the repository's local synthetic fixtures only. Keep a terminal open at the repository root and run each file with the Python command that worked on your computer.

## Outcomes

By the end of this lesson, you should be able to explain the new vocabulary in your own words, run and modify the examples, predict at least one boundary case, repair a deliberate mistake, and apply the idea to a bounded cybersecurity fixture.

## The problem

A classifier receives a synthetic record and must choose one label. If conditions overlap, if a field is missing, or if every unexpected value is treated as safe, the result becomes misleading. A branching design needs an order, a default, and a clear treatment of uncertainty.

## Security boundary

This lesson is educational and local. It does not authorize public scanning, credential use, data collection, exploitation, interception, or changes to systems you do not own. The cybersecurity examples use invented names, loopback targets, or repository fixtures.

## Vocabulary

A **branch** is one possible path through a program. A **classifier** assigns a label according to rules. A **default** is what happens when no special case matches. **Unknown** means the program lacks enough information; it should not automatically mean safe.

## Lesson

Start with one branch:

```python
severity = 8

if severity >= 7:
    print("review")
```

If the condition is false, Python prints nothing. That may be correct for a small experiment, but a reporting tool often needs an explicit default. Add `else`:

```python
if severity >= 7:
    print("review")
else:
    print("routine")
```

Now every numeric input receives a label, but the design still assumes the value is valid. Add validation before classification rather than hiding invalid data inside a normal label.

```python
severity = 12

if not 0 <= severity <= 10:
    label = "invalid"
elif severity >= 7:
    label = "review"
else:
    label = "routine"

print(label)
```

This ordering is important. The invalid check comes before the ordinary severity rules. Otherwise 12 would be classified as review even though it violates the documented range.

Add source quality:

```python
severity = 8
source = "unknown"

if source != "training-auth":
    label = "unknown-source"
elif severity >= 9:
    label = "urgent"
elif severity >= 7:
    label = "review"
else:
    label = "routine"

print(label)
```

This classifier chooses `unknown-source` before examining severity. That is a policy choice: an unknown source prevents this training classifier from making a severity decision. Another system might preserve both labels instead of choosing one. The important lesson is to document the choice.

Nested branches are sometimes readable, but they can become difficult to trace:

```python
if source == "training-auth":
    if severity >= 7:
        print("review")
    else:
        print("routine")
else:
    print("unknown-source")
```

The flat `if/elif/else` chain and the nested version can represent the same rule. Choose the form that makes the policy easiest to test. Do not nest conditions merely to look advanced.

You can also return a label from a function, but functions are tomorrow's main topic. For today, notice that storing the label in a name makes it available for a later report:

```python
label = "review"
print(f"classification={label}")
```

A branch can choose a value without immediately printing it. Separating decision from output makes later testing easier.

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

## Execution trace

Trace the classifier:

```python
severity = 12
source = "training-auth"

if not 0 <= severity <= 10:
    label = "invalid"
elif source != "training-auth":
    label = "unknown-source"
elif severity >= 9:
    label = "urgent"
elif severity >= 7:
    label = "review"
else:
    label = "routine"
```

Python checks the first condition. `12` is not between 0 and 10, so `label` becomes `invalid`. Python skips every later branch. If you move the invalid check below `severity >= 9`, the same input becomes urgent. That is a bug in policy order, not in Python syntax.

Make a decision table before coding:

| Input | Expected label |
| --- | --- |
| severity 12 | invalid |
| severity 8, unknown source | unknown-source |
| severity 9, known source | urgent |
| severity 7, known source | review |
| severity 3, known source | routine |

The table is a small specification. The code is an implementation of that specification.

## Common mistakes and repairs

| Mistake | Symptom | Repair |
| --- | --- | --- |
| No invalid branch | Bad data receives a normal label. | Validate before classifying. |
| `else` means safe | Unknown conditions are treated as routine. | Use an explicit unknown label. |
| Overlapping conditions | The first matching rule wins unexpectedly. | Order and test the rules. |
| Printing inside every branch | The decision cannot be reused or tested easily. | Store a label, then report it. |
| Nested code too deeply | The path is hard to trace. | Use a table or flat chain where clearer. |

## Guided practice

Create a decision table on paper for a fictional event. Include fields `severity`, `source`, and `authenticated`. Decide what should happen when each field is invalid or missing. Then implement only the first five rows.

Run one test per row. If a result is wrong, do not change the table to match the program. Treat the table as the intended behavior and repair the code. Add a print statement showing which input row you are testing so that a failure is easy to locate.

Finally, change the program so it returns or stores a label before printing. This small separation will prepare you for functions and tests on Day 9.

## Security application

A defensive classifier should preserve uncertainty. For synthetic logs, an invalid severity should not become a low-priority event, and a missing source should not become a trusted source. A label such as `unknown` is not a weakness in the program; it is a truthful statement about incomplete information.

Never use this training classifier to make decisions about a real person. It has no trustworthy collection path, identity proof, context, or organizational policy. It demonstrates branching and safe uncertainty only.

## Independent exercises

Complete these in [`practice/exercises.md`](practice/exercises.md) in order:

1. Write a two-branch classifier for a number being inside or outside 0–10.
2. Add an explicit `unknown` path for missing source text.
3. Create a five-row decision table before writing code.
4. Implement urgent, review, routine, invalid, and unknown-source labels.
5. Test every boundary and copy the observed result.
6. Create an overlapping-rule bug and explain why the first matching branch wins.
7. Rewrite a nested classifier as a flat chain and compare readability.
8. Store a label before printing it.
9. Add a safe message that reports `classification=unknown` without making an accusation.
10. Explain why `else` should not automatically mean safe.
11. Add a test case for a missing field and describe the desired behavior.
12. Safety question: identify one way an automated classifier could cause harm if treated as a verdict.



### Additional beginner checkpoint

Pause before adding another feature. Read the current program aloud as a sequence of decisions: what enters, what is transformed, what is checked, and what leaves. Write down one value that is allowed, one value that must be rejected, and one value whose meaning is uncertain. This distinction matters in cybersecurity because an unknown observation should not silently become a safe conclusion. Run the allowed case, the rejected case, and the uncertain case separately. Keep the exact output in your notes and explain which line produced it.

Now make the smallest useful improvement. Give one name a clearer meaning, extract one repeated operation, or add one explicit boundary check. Run the same three cases again. If the behavior changed, explain whether the change was intended. If a test now fails, treat the failure as information about the contract rather than deleting the test. Finish by writing one sentence about the lesson's limitation: a local Python rule can organize synthetic evidence, but it cannot establish authorization, authenticity, or the truth of a real-world accusation.

## Finish line

Day 5 is complete when you can design a decision table, implement ordered branches, preserve unknown and invalid states, test every boundary, and explain why a classifier is not an accusation.

## References

[1]: https://docs.python.org/3/tutorial/controlflow.html#if-statements "Python conditional statements"
[2]: https://docs.python.org/3/reference/compound_stmts.html "Python compound statements"
[3]: https://csrc.nist.gov/glossary/term/risk "NIST risk glossary"
[4]: https://www.cisa.gov/topics/cyber-threats-and-advisories "CISA cyber threat guidance"

[← Day 4](../day_04_operators_and_decisions/day_04_operators_and_decisions.md) · [Day index](../DAY_INDEX.md) · [Day 6 →](../day_06_loops_and_bounded_work/day_06_loops_and_bounded_work.md)
