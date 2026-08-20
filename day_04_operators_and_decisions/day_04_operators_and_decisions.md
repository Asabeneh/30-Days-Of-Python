# Day 4: Operators, Comparisons, and Decisions

[← Day 3](../day_03_types_and_parsing/day_03_types_and_parsing.md) · [Day index](../DAY_INDEX.md) · [Day 5 →](../day_05_branching_and_triage/day_05_branching_and_triage.md)

## Welcome

A program becomes useful when it can do more than print fixed text. It can calculate, compare, and choose. Today you will learn the symbols that express those actions and how Python turns a comparison into a Boolean decision.

This lesson is designed for a learner who may still need to look up how to create a file, run it, or read an error. Type the examples instead of reading them passively. Before running an experiment, write down what you expect. The difference between your prediction and Python's output is where learning happens.

## Prerequisites

Complete Day 3. Use the repository's local synthetic fixtures only. Keep a terminal open at the repository root and run each file with the Python command that worked on your computer.

## Outcomes

By the end of this lesson, you should be able to explain the new vocabulary in your own words, run and modify the examples, predict at least one boundary case, repair a deliberate mistake, and apply the idea to a bounded cybersecurity fixture.

## The problem

A triage tool might need to ask whether a severity is high enough for review, whether a record is empty, or whether two values are equal. If you confuse assignment with comparison or misunderstand `and` and `or`, the tool may take the wrong branch.

## Security boundary

This lesson is educational and local. It does not authorize public scanning, credential use, data collection, exploitation, interception, or changes to systems you do not own. The cybersecurity examples use invented names, loopback targets, or repository fixtures.

## Vocabulary

An **operator** is a symbol or word that performs an operation. An **expression** is code that produces a value. A **comparison** produces `True` or `False`. A **condition** is an expression used to choose a path. **Precedence** is the order Python uses when several operators appear together.

## Lesson

Begin with arithmetic:

```python
failed = 7
allowed = 3
remaining = failed - allowed
print(remaining)
```

Expected output is `4`. The expression `failed - allowed` is evaluated before assignment to `remaining`. Addition, subtraction, multiplication, division, floor division, remainder, and exponentiation have different meanings:

```python
print(7 + 2)
print(7 - 2)
print(7 * 2)
print(7 / 2)
print(7 // 2)
print(7 % 2)
print(7**2)
```

Expected output:

```text
9
5
14
3.5
3
1
49
```

The remainder operator `%` is useful for asking whether a number divides evenly. It is not a security detector by itself; it is just arithmetic.

Comparisons answer questions:

```python
severity = 7
print(severity == 7)
print(severity != 4)
print(severity > 5)
print(severity <= 10)
```

The comparison operator is `==`; assignment is `=`. This distinction is one of the most common beginner errors. `severity = 7` changes the stored value. `severity == 7` asks whether the current value equals 7.

Combine questions with Boolean operators:

```python
severity = 7
is_known_source = True
needs_review = severity >= 7 and is_known_source
print(needs_review)
```

`and` requires both sides to be true. `or` requires at least one side to be true. `not` reverses a Boolean result. Read the condition in plain English before reading it as code.

Decisions use `if`:

```python
severity = 7

if severity >= 7:
    print("review")
else:
    print("record")
```

The colon begins the block controlled by the condition. Indentation shows which statements belong to the block. If severity is 7, Python runs the indented `print("review")`. Otherwise it runs the `else` block.

Add a third path with `elif`:

```python
if severity >= 9:
    label = "urgent"
elif severity >= 7:
    label = "review"
else:
    label = "routine"

print(label)
```

Python tests the branches from top to bottom and stops at the first true branch. The order matters. If you put `severity >= 7` first, a severity of 9 will be labelled review and never reach urgent. Conditions must be ordered from the more specific or urgent case to the broader case.

Precedence can surprise you:

```python
result = False or True and False
print(result)
```

Python evaluates `and` before `or`, so this behaves like `False or (True and False)`, which is `False`. When a condition matters, use parentheses even if you know the precedence:

```python
result = (False or True) and False
print(result)
```

This is now `False` for a different reason. Parentheses make the intended grouping visible to a future reader.

Truthiness is another decision rule. Empty strings, empty lists, zero, and `None` are commonly false in a Boolean context; non-empty values are commonly true. Do not use truthiness as a replacement for a precise policy when the difference between missing and zero matters.

```python
value = ""
if value:
    print("has text")
else:
    print("empty")
```

The output is `empty`. The condition did not compare `value` to a word; Python asked whether the value was considered true.

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

Trace:

```python
severity = 8
known = True

if severity >= 9:
    decision = "urgent"
elif severity >= 7 and known:
    decision = "review"
else:
    decision = "routine"
```

| Step | Question | Result |
| ---: | --- | --- |
| 1 | Is `8 >= 9`? | `False`, continue. |
| 2 | Is `8 >= 7`? | `True`. |
| 3 | Is `known` true? | `True`. |
| 4 | Is `True and True`? | `True`, choose review. |
| 5 | Run `else`? | No, the chain already chose a branch. |

Change `known` to `False`. Step 3 becomes false, so the combined condition becomes false and the decision becomes routine. The number did not change; the second piece of evidence changed the path.

## Common mistakes and repairs

| Mistake | Why it happens | Repair |
| --- | --- | --- |
| `if severity = 7` | Assignment and comparison look similar. | Use `==` for a question. |
| Broad condition first | A later urgent branch becomes unreachable. | Order branches deliberately. |
| Missing indentation | Python cannot identify the block. | Indent the controlled statements consistently. |
| Long condition without parentheses | Precedence is hidden. | Add parentheses and explain the grouping. |
| Treating `0` as missing | Truthiness is confused with meaning. | Compare explicitly when zero is valid. |
| Using `or` when both facts are required | One true side is enough. | Use `and` for “both must hold.” |

## Guided practice

Build a triage decision in checkpoints. Start with a `severity` value and a Boolean `source_is_known` value. First print each input. Then write three branches: urgent for 9–10, review for 7–8 from a known source, and routine otherwise. Test 10 known, 8 known, 8 unknown, 4 known, and -1.

Before each run, write the expected label. When a result surprises you, inspect the comparison values separately:

```python
print(severity >= 9)
print(severity >= 7)
print(source_is_known)
```

This is often easier than staring at one long condition. A good debugger breaks a complicated question into smaller questions.

## Security application

In defensive tooling, a condition should express a documented policy rather than a feeling. For a synthetic event, you might decide that a record needs review only when the severity is at least 7 **and** the record passed a source-quality check. That rule is not universal. It is a local training policy.

Write the policy in English first, then translate it:

> Review this synthetic record when its severity is 7 or higher and its source label is known.

```python
review = severity >= 7 and source_is_known
```

The code is easier to review because the variable names carry the policy. It still does not prove that a record is malicious, that a source is authentic, or that an alert deserves a real-world response.

## Independent exercises

Complete these in [`practice/exercises.md`](practice/exercises.md) in order:

1. Predict the output of each arithmetic operator in a small program.
2. Explain the difference between `=` and `==` using a sentence and code.
3. Write comparisons for severity equal to 7, greater than 7, and between 0 and 10.
4. Build an `if/elif/else` classifier for urgent, review, and routine.
5. Test the classifier at every boundary: 0, 6, 7, 8, 9, and 10.
6. Write one condition that requires two facts with `and` and one that accepts either fact with `or`.
7. Add parentheses to a mixed `and`/`or` expression and explain why.
8. Demonstrate the difference between an empty string, zero, and `None` in an `if` statement.
9. Write a safe decision for a synthetic event and explain what the decision cannot prove.
10. Create a deliberate branch-order bug, demonstrate it with severity 9, and repair it.
11. Write a short explanation of operator precedence for a beginner.
12. Safety question: explain why a decision rule should not be used to accuse a person automatically.

## Finish line

Day 4 is complete when you can predict a comparison, choose between `and` and `or`, explain the difference between assignment and equality, order branches correctly, and state the limits of a synthetic triage decision.

## References

[1]: https://docs.python.org/3/reference/expressions.html#operator-precedence "Python operator precedence"
[2]: https://docs.python.org/3/tutorial/controlflow.html#if-statements "Python conditional statements"
[3]: https://docs.python.org/3/library/stdtypes.html#truth-value-testing "Python truth-value testing"
[4]: https://owasp.org/www-community/controls/Logging "OWASP logging guidance"

[← Day 3](../day_03_types_and_parsing/day_03_types_and_parsing.md) · [Day index](../DAY_INDEX.md) · [Day 5 →](../day_05_branching_and_triage/day_05_branching_and_triage.md)
