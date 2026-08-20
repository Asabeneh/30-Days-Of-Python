# Day 4: Python Operators, Comparisons, and Decisions

[← Day 3](../day_03_types_and_parsing/day_03_types_and_parsing.md) · [Day index](../DAY_INDEX.md) · [Day 5 →](../day_05_branching_and_triage/day_05_branching_and_triage.md)





## Table of contents

- [Welcome](#welcome)
- [What you will learn](#what-you-will-learn)
- [The problem: asking Python a question](#the-problem-asking-python-a-question)
- [Vocabulary](#vocabulary)
- [1. What an operator is](#1-what-an-operator-is)
- [2. Arithmetic operators](#2-arithmetic-operators)
  - [Addition and subtraction](#addition-and-subtraction)
  - [Multiplication and division](#multiplication-and-division)
  - [Floor division, remainder, and powers](#floor-division-remainder-and-powers)
- [3. Assignment operators](#3-assignment-operators)
- [4. Comparison operators](#4-comparison-operators)
- [5. Logical operators](#5-logical-operators)
- [6. Membership and identity](#6-membership-and-identity)
- [7. Conditional expressions](#7-conditional-expressions)
- [8. Precedence and parentheses](#8-precedence-and-parentheses)
- [Worked examples](#worked-examples)
  - [Example 1: Compare two synthetic scores](#example-1-compare-two-synthetic-scores)
  - [Example 2: Test every boundary](#example-2-test-every-boundary)
  - [Example 3: Combine three requirements](#example-3-combine-three-requirements)
  - [Example 4: Use an allowlist](#example-4-use-an-allowlist)
  - [Example 5: Repair a mistaken rule](#example-5-repair-a-mistaken-rule)
- [Execution trace](#execution-trace)
- [Common mistakes and repairs](#common-mistakes-and-repairs)
- [Guided practice](#guided-practice)
- [Security application: a bounded triage rule](#security-application-a-bounded-triage-rule)
- [Independent exercises](#independent-exercises)
- [Finish line](#finish-line)
- [References](#references)

## Welcome

Today Python learns how to **calculate**, **compare**, and **make a choice**. Those three abilities appear in almost every useful program. A calculator calculates. A form validator compares a value with a rule. A security report makes a cautious choice such as `review`, `routine`, or `invalid`.

The word *operator* may sound advanced, but you already use operators in ordinary life. The plus sign adds prices. The greater-than sign compares scores. The word “and” combines requirements. Python gives these ideas a precise spelling.

Do not try to memorize every symbol in one sitting. Instead, follow the same routine for every operator:

1. Read what the operator means in plain English.
2. Run the smallest example.
3. Look at the output and its type.
4. Change one input and predict the new output.
5. Use the operator in a small, local cybersecurity fixture.

The reference tutorials that inspired this lesson follow this same progression: introduce a decision in familiar language, show a table of operators, demonstrate small examples, combine the ideas, and finish with exercises.[1] [2] [3]

## What you will learn

By the end of this lesson, you will be able to explain the difference between an operand and an operator, use arithmetic and assignment operators, compare values with `==`, `!=`, `<`, `>`, `<=`, and `>=`, combine Boolean expressions with `and`, `or`, and `not`, distinguish membership from identity, use parentheses to make an expression clear, and write a bounded rule that produces a cautious triage label.

You will also learn what operators **do not** prove. If a synthetic string matches a rule, the rule has matched a string. It has not proved that an attacker exists, that a machine is compromised, or that you are authorized to contact a target.

## The problem: asking Python a question

Imagine a local training fixture containing one event:

```python
event_name = "login_failed"
severity = 8
```

A human can ask, “Is this event's severity high?” Python needs the question written precisely:

```python
is_high = severity >= 7
print(is_high)
```

Output:

```text
True
```

The expression `severity >= 7` is a **comparison**. It asks whether the value stored in `severity` is greater than or equal to `7`. The answer is a Boolean value: either `True` or `False`.

That answer can be stored in a variable, printed, combined with another answer, or used later by an `if` statement. Today we concentrate on producing and understanding the answer. Tomorrow you will use conditions to choose different blocks of code.

## Vocabulary

An **operator** is a symbol or keyword that tells Python to perform an operation. Examples include `+`, `>=`, `and`, and `in`.

An **operand** is a value that an operator works on. In `7 + 2`, the operands are `7` and `2`.

An **expression** is code that produces a value. `7 + 2` is an expression whose value is `9`.

An **assignment** gives a value to a name. In `severity = 8`, the single equals sign stores `8` under the name `severity`.

A **comparison** asks a question and produces `True` or `False`.

A **Boolean** is one of exactly two values: `True` or `False`. The word must begin with a capital letter in Python.

A **condition** is an expression used to make a decision. `severity >= 7` is a condition.

**Precedence** is the rule that tells Python which operation to perform first when an expression contains several operators.

**Identity** asks whether two names refer to the very same object. **Equality** asks whether two values have the same contents. These questions are related, but they are not the same question.

## 1. What an operator is

Look at this expression:

```python
result = 10 + 5
print(result)
```

Python reads the right side first. The `+` operator receives the operands `10` and `5`, calculates `15`, and the assignment operator stores that result in `result`. Finally, `print` displays the value.

Expected output:

```text
15
```

A helpful reading is: “Create the value produced by `10 + 5`, then assign it to `result`.” Do not read `=` as “is equal to” in this context. In Python, `=` means “store the value on the right under the name on the left.”

Try changing only the second operand:

```python
result = 10 + 8
print(result)
```

The output becomes `18`. The operator stayed the same; an operand changed.

## 2. Arithmetic operators

Arithmetic operators work with numbers. The table below is a reference, not a demand that you memorize everything immediately.[2]

| Operator | Plain-English meaning | Example | Result |
| --- | --- | --- | ---: |
| `+` | add | `7 + 2` | `9` |
| `-` | subtract | `7 - 2` | `5` |
| `*` | multiply | `7 * 2` | `14` |
| `/` | divide and produce a float | `7 / 2` | `3.5` |
| `//` | floor division | `7 // 2` | `3` |
| `%` | remainder after division | `7 % 2` | `1` |
| `**` | raise to a power | `7 ** 2` | `49` |

### Addition and subtraction

Suppose a training report contains seven failed events and three events that have already been reviewed:

```python
failed_events = 7
reviewed_events = 3
remaining_events = failed_events - reviewed_events
print(remaining_events)
```

Output:

```text
4
```

Line by line, Python stores `7`, stores `3`, subtracts `3` from `7`, stores `4` in `remaining_events`, and prints `4`. The name `remaining_events` is clearer than a name such as `x`, because the name tells the reader what the number represents.

Addition combines quantities:

```python
new_events = 4
old_events = 6
total_events = new_events + old_events
print(total_events)
```

Output:

```text
10
```

These are counts in a synthetic fixture. They are not a measurement of a real environment.

### Multiplication and division

```python
records_per_batch = 5
number_of_batches = 3
total_records = records_per_batch * number_of_batches
print(total_records)
```

Output:

```text
15
```

Division uses `/` and produces a decimal value when necessary:

```python
records = 7
batches = 2
average = records / batches
print(average)
print(type(average).__name__)
```

Output:

```text
3.5
float
```

If you need a whole-number grouping instead of an average, `/` may not be the operator you want. Use `//` or `%`, and explain why.

### Floor division, remainder, and powers

Floor division answers, “How many complete groups fit?” Remainder answers, “How many are left over?”

```python
records = 17
batch_size = 5
complete_batches = records // batch_size
leftover_records = records % batch_size
print(complete_batches)
print(leftover_records)
```

Output:

```text
3
2
```

This is useful when designing a bounded processor. Three complete batches of five use fifteen records; two records remain. It does not mean a program should process an untrusted file forever. The total work still needs a maximum.

The power operator raises one number to another power:

```python
base = 2
exponent = 3
print(base**exponent)
```

Output:

```text
8
```

Do not use arithmetic as a substitute for security reasoning. A calculation can be correct while the input is untrusted, the unit is wrong, or the result is outside a safe range.

## 3. Assignment operators

The basic assignment operator is `=`:

```python
attempts = 1
attempts = attempts + 1
print(attempts)
```

Output:

```text
2
```

The second line reads the old value, adds one, and stores the new value. Python also provides combined assignment operators:

| Operator | Longer form | Meaning |
| --- | --- | --- |
| `+=` | `value = value + amount` | add and store |
| `-=` | `value = value - amount` | subtract and store |
| `*=` | `value = value * amount` | multiply and store |
| `/=` | `value = value / amount` | divide and store |
| `//=` | `value = value // amount` | floor-divide and store |
| `%=` | `value = value % amount` | store the remainder |

Example:

```python
processed = 0
processed += 1
processed += 1
print(processed)
```

Output:

```text
2
```

A common beginner mistake is trying to use a name before assigning it:

```python
processed += 1
```

Python raises `NameError` because it has not seen a value for `processed`. Repair it by initializing the name first:

```python
processed = 0
processed += 1
```

Initialization is especially important in security automation. A counter, limit, or result should have a deliberate starting value rather than depending on hidden state.

## 4. Comparison operators

Comparison operators produce Booleans. Here is the complete core comparison table:

| Operator | Meaning | Example | Result |
| --- | --- | --- | --- |
| `==` | equal to | `8 == 8` | `True` |
| `!=` | not equal to | `8 != 7` | `True` |
| `<` | less than | `6 < 7` | `True` |
| `>` | greater than | `8 > 7` | `True` |
| `<=` | less than or equal to | `7 <= 7` | `True` |
| `>=` | greater than or equal to | `8 >= 7` | `True` |

Run this complete example:

```python
severity = 8
print(severity == 8)
print(severity != 4)
print(severity < 7)
print(severity > 7)
print(severity <= 8)
print(severity >= 7)
```

Output:

```text
True
True
False
True
True
True
```

Read `severity >= 7` as “severity is greater than or equal to seven.” The boundary matters. If the rule says “at least seven,” then `7` must be accepted. Test `6`, `7`, and `8`, not only an easy value such as `10`.

Equality works with strings too:

```python
event_name = "login_failed"
print(event_name == "login_failed")
print(event_name == "logout")
```

Output:

```text
True
False
```

Do not confuse `=` with `==`. This is wrong when you intend to ask a question:

```python
# severity == 7 is a question.
# severity = 7 changes the stored value.
```

The single equals sign does not compare. It assigns.

## 5. Logical operators

Logical operators combine Boolean expressions.[3] [4]

| Operator | Plain-English meaning | Example |
| --- | --- | --- |
| `and` | both sides must be true | `severity >= 7 and source != ""` |
| `or` | at least one side must be true | `event == "login_failed" or event == "access_denied"` |
| `not` | reverse a Boolean result | `not is_empty` |

Start with `and`:

```python
severity = 8
source = "training-auth"
review = severity >= 7 and source != ""
print(review)
```

Output:

```text
True
```

Both comparisons are true, so `and` produces `True`. Change the severity to `6`:

```python
severity = 6
source = "training-auth"
review = severity >= 7 and source != ""
print(review)
```

Output:

```text
False
```

The source is still present, but the first comparison is false. With `and`, one false requirement makes the combined condition false.

Now use `or`:

```python
event_name = "access_denied"
is_auth_event = event_name == "login_failed" or event_name == "access_denied"
print(is_auth_event)
```

Output:

```text
True
```

At least one comparison is true. `or` does not mean “both”; it means “one or more.”

Finally, use `not`:

```python
source = ""
is_missing_source = source == ""
print(is_missing_source)
print(not is_missing_source)
```

Output:

```text
True
False
```

Use parentheses when they make the rule easier to read:

```python
is_auth_event = (event_name == "login_failed") or (event_name == "access_denied")
```

The parentheses are not always required, but they show the reader which comparisons are being combined.

## 6. Membership and identity

The membership operators `in` and `not in` ask whether a value occurs inside a collection or string:

```python
allowed_events = ["login_failed", "access_denied"]
event_name = "access_denied"
print(event_name in allowed_events)
print("logout" not in allowed_events)
```

Output:

```text
True
True
```

This is useful for a small allowlist. It does not prove that the event came from a trustworthy source. It only answers whether the value appears in the local collection.

The identity operators are `is` and `is not`. Use them when you need to ask whether two names refer to the same object. For a missing value, the conventional test is:

```python
confidence = None
print(confidence is None)
```

Output:

```text
True
```

Use `==` for value equality and `is` for identity. This distinction prevents confusing “these values contain the same text” with “these names refer to the same object.”

## 7. Conditional expressions

A conditional expression chooses one of two values in a single line:

```python
severity = 8
label = "review" if severity >= 7 else "routine"
print(label)
```

Output:

```text
review
```

Read it as: “Use `review` if the comparison is true; otherwise use `routine`.” It is convenient for a short, clear choice. Do not force a complicated policy into one line. A multi-line `if` statement is often easier for a beginner and a reviewer to understand.

## 8. Precedence and parentheses

When several operators appear together, Python follows precedence rules. Multiplication happens before addition:

```python
result = 10 + 2 * 3
print(result)
```

Output:

```text
16
```

Python calculates `2 * 3` first, then adds `10`. Parentheses make a different order explicit:

```python
result = (10 + 2) * 3
print(result)
```

Output:

```text
36
```

Logical operators also have an order: `not` is evaluated before `and`, and `and` before `or`.[2] Even when you remember this, parentheses are a kindness to the next reader:

```python
needs_review = (severity >= 7) and (source != "")
```

Write the expression as a sentence before you trust it. If the sentence is unclear, the code probably needs smaller named Boolean variables.

## Worked examples

### Example 1: Compare two synthetic scores

```python
current_score = 85
best_score = 82
is_better = current_score > best_score
print(is_better)
```

Output: `True`. Python compares the two integers and stores the Boolean answer in `is_better`.

### Example 2: Test every boundary

```python
for_severity = [6, 7, 8]
for severity in for_severity:
    print(severity, severity >= 7)
```

Output:

```text
6 False
7 True
8 True
```

The loop syntax is introduced formally on Day 6. For today, focus on the comparison: the rule changes between `6` and `7` because the operator says “greater than or equal to.”

### Example 3: Combine three requirements

```python
experience = 4
score = 90
source = "training-auth"
meets_rule = (experience >= 3) and (score >= 85) and (source != "")
print(meets_rule)
```

Output: `True`. All three comparisons are true. If any one becomes false, the combined result becomes false.

### Example 4: Use an allowlist

```python
known_events = {"login_failed", "access_denied"}
event_name = "access_denied"
print(event_name in known_events)
```

Output: `True`. The set is local and synthetic. Membership is not evidence of maliciousness.

### Example 5: Repair a mistaken rule

Broken code:

```python
severity = 8
source = ""
needs_review = severity >= 7 or source != ""
print(needs_review)
```

This prints `True` because the severity is high. But suppose the policy says a record should be reviewable only when the severity is high **and** a source label exists. Repair it:

```python
needs_review = (severity >= 7) and (source != "")
print(needs_review)
```

The repaired code prints `False`. The important lesson is not that `and` is always safer than `or`; it is that the operator must match the written policy.

## Execution trace

Trace this program before running it:

```python
severity = 8
source = "training-auth"
event_name = "login_failed"
known_events = {"login_failed", "access_denied"}
needs_review = severity >= 7 and source != "" and event_name in known_events
print(needs_review)
```

| Step | Python evaluates | Result |
| ---: | --- | --- |
| 1 | assign `severity` | `8` |
| 2 | assign `source` | `"training-auth"` |
| 3 | assign `event_name` | `"login_failed"` |
| 4 | create `known_events` | two local strings |
| 5 | `severity >= 7` | `True` |
| 6 | `source != ""` | `True` |
| 7 | `event_name in known_events` | `True` |
| 8 | combine with `and` | `True` |
| 9 | print | `True` |

Now change `event_name` to `"logout"`. The first two checks stay true, but membership becomes false, so the final result becomes false. The program has not discovered an attack. It has only applied a local rule to a synthetic record.

## Common mistakes and repairs

| Mistake | What the beginner sees | Smallest repair |
| --- | --- | --- |
| `=` instead of `==` | The value changes instead of being compared | Use `==` for an equality question |
| `>` instead of `>=` | The exact boundary is rejected | Test the rule's wording and include equality when required |
| `or` instead of `and` | One satisfied requirement is enough when all were required | Write the policy sentence first, then use `and` |
| `and` instead of `or` | A valid alternative is rejected | Ask whether all conditions or at least one condition is required |
| `bool("false")` | The string becomes `True` because it is non-empty | Parse accepted words explicitly |
| `is` instead of `==` | Equal values behave unexpectedly | Use `==` for contents and `is None` for missing values |
| Missing parentheses | The reader cannot see the intended grouping | Add parentheses or name each comparison |
| Division by zero | `ZeroDivisionError` | Validate the divisor before dividing |
| Unbounded arithmetic from input | A program consumes too much time or memory | Validate sizes and impose limits |

## Guided practice

Create a file named `day04_guided.py`. Type this starter exactly:

```python
severity = 7
source = "training-auth"
event_name = "login_failed"
known_events = {"login_failed", "access_denied"}

is_high = severity >= 7
has_source = source != ""
is_known = event_name in known_events

print(is_high)
print(has_source)
print(is_known)
```

Before running it, predict the three lines. Then run it and compare your prediction. Change only `severity` to `6`. Predict again. Next change only `source` to `""`. Finally change only `event_name` to `"logout"`.

Now combine the three named results:

```python
needs_review = is_high and has_source and is_known
print(needs_review)
```

Write one sentence explaining why the result changed after each modification. The goal is not to produce a clever one-line expression. The goal is to see how a decision is assembled from small, inspectable facts.

## Security application: a bounded triage rule

Use the following local fixture. It contains no real usernames, addresses, credentials, or network targets:

```python
fixture = [
    {"severity": 8, "source": "training-auth", "event": "login_failed"},
    {"severity": 3, "source": "training-auth", "event": "logout"},
    {"severity": 7, "source": "", "event": "access_denied"},
]
known_events = {"login_failed", "access_denied"}
```

For each record, calculate three Booleans: whether severity is at least `7`, whether the source is non-empty, and whether the event is in the local allowlist. Combine them with `and`. Print only a safe summary such as the record number and the resulting label. Do not print an entire raw record.

The asset is the training fixture. The input is the three dictionaries. The trust boundary is the Python program reading data supplied by the exercise. Authorization is limited to reading and writing files inside this repository. Expected evidence is a short local report showing three record numbers and labels. Cleanup means deleting temporary output if the exercise asks you to create it. Residual risk remains because the rule is synthetic and does not establish authenticity or compromise.

A suitable policy might be:

```python
def triage_label(record):
    severity_is_high = record["severity"] >= 7
    source_is_present = record["source"] != ""
    event_is_known = record["event"] in known_events

    if severity_is_high and source_is_present and event_is_known:
        return "review"
    return "routine-or-incomplete"
```

This function returns a label; it does not accuse anyone. The third fixture record has high severity and a known event, but its source is empty, so it receives `routine-or-incomplete` under this deliberately simple rule. A different policy could choose `needs-context`. What matters is that the choice is documented and tested.

## Independent exercises

Complete the numbered questions in [`practice/exercises.md`](practice/exercises.md) in order. Use hints only after a genuine attempt and solutions only to compare your reasoning.

1. Write one expression using `+`, one using `-`, one using `*`, and one using `/`. Predict and then print all four results.
2. Calculate `17 // 5` and `17 % 5`. Explain what each answer means in the language of complete groups and leftover records.
3. Start with `processed = 0` and use `+=` three times. Print the final value and explain each change.
4. Create variables `new_score = 95` and `previous_best = 88`. Store `new_score > previous_best` in `compare_scores` and assert that it is `True`.
5. Test the difference between `severity > 7` and `severity >= 7` for the values `6`, `7`, and `8`.
6. Create `meets_requirements` that is true only when experience is at least `3` and score is at least `85`.
7. Create `is_auth_event` that is true when an event is either `login_failed` or `access_denied`.
8. Use `not` to create `has_source` from a Boolean called `source_is_missing`.
9. Use `in` to check whether a synthetic event appears in a local set of two allowed event names.
10. Explain in your own words why `==` and `is` answer different questions. Demonstrate with `None` and two equal strings.
11. Evaluate `10 + 2 * 3` and `(10 + 2) * 3`. Explain why the answers differ.
12. Repair a broken triage expression that uses `or` when the written policy requires high severity, a non-empty source, and a known event.
13. Apply the rule to the three-record fixture and print only `record_number` and `label`.
14. Add a boundary test for severity `6`, `7`, and `8`. Explain why the boundary test is more informative than testing only `10`.
15. Safety question: explain why a correct Boolean expression does not authorize scanning, connecting to, uploading to, or collecting data from a real system.

## Finish line

You are finished when you can explain every operator in the reference tables, run the guided practice, show the output for the normal and boundary cases, repair the broken rule, complete the numbered practice, and state the security limitation of the synthetic triage application.

## References

[1]: https://beyondsimulations.github.io/Programming-Everyday-Decisions/tutorials/tut_01_02_comparisons.html "Comparison operators tutorial"
[2]: https://www.geeksforgeeks.org/python/python-operators/ "Python operators reference"
[3]: https://www.w3schools.com/python/python_operators_logical.asp "Python logical operators"
[4]: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not "Python Boolean operations"
[5]: https://docs.python.org/3/reference/expressions.html#operator-precedence "Python operator precedence"
[6]: https://www.freecodecamp.org/learn/python-v9/lecture-understanding-variables-and-data-types/how-do-you-declare-variables-and-what-are-naming-conventions-to-name-variables "Python variables and naming conventions"

[← Day 3](../day_03_types_and_parsing/day_03_types_and_parsing.md) · [Day index](../DAY_INDEX.md) · [Day 5 →](../day_05_branching_and_triage/day_05_branching_and_triage.md)
