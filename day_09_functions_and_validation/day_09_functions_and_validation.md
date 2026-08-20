# Day 9: Functions, Contracts, and Validation

[← Day 8](../day_08_strings_and_canonicalization/day_08_strings_and_canonicalization.md) · [Day index](../DAY_INDEX.md) · [Day 10 →](../day_10_checkpoint_log_triage/day_10_checkpoint_log_triage.md)

## Welcome

Your programs are now long enough that copying blocks creates mistakes. A function gives a named job a boundary: it receives inputs, performs one responsibility, and returns a result. Today you will write small functions and state what each one promises.

This lesson is designed for a learner who may still need to look up how to create a file, run it, or read an error. Type the examples instead of reading them passively. Before running an experiment, write down what you expect. The difference between your prediction and Python's output is where learning happens.

## Prerequisites

Complete Day 8. Use the repository's local synthetic fixtures only. Keep a terminal open at the repository root and run each file with the Python command that worked on your computer.

## Outcomes

By the end of this lesson, you should be able to explain the new vocabulary in your own words, run and modify the examples, predict at least one boundary case, repair a deliberate mistake, and apply the idea to a bounded cybersecurity fixture.

## The problem

A parser, classifier, and report formatter should be testable separately. If one giant script reads input, validates it, decides a label, and prints output, it is difficult to locate a failure or reuse one piece safely.

## Security boundary

This lesson is educational and local. It does not authorize public scanning, credential use, data collection, exploitation, interception, or changes to systems you do not own. The cybersecurity examples use invented names, loopback targets, or repository fixtures.

## Vocabulary

A **function** is a reusable named block. A **parameter** is a name in the function definition. An **argument** is the value supplied when calling it. `return` sends a result back. A **contract** describes accepted inputs, produced outputs, and failure behavior. **Scope** describes where a name exists.

## Lesson

Define the smallest function:

```python
def add_one(number):
    return number + 1


result = add_one(4)
print(result)
```

The `def` line creates the function. `number` is a parameter. The indented body adds one. `return` sends 5 back to the caller. The function does not print by itself; the caller decides what to do with the result.

A parameter can have a default:

```python
def label_source(source="unknown"):
    return source.strip().casefold()


print(label_source())
print(label_source(" Training-Auth "))
```

The first call uses the default. The second supplies an argument. Defaults are useful only when “missing” really has a documented meaning.

Write a function that validates a range:

```python
def validate_severity(value):
    if not isinstance(value, int):
        raise TypeError("severity must be an integer")
    if not 0 <= value <= 10:
        raise ValueError("severity must be between 0 and 10")
    return value
```

This function has a contract. It accepts an integer in the range 0–10 and returns that integer. It raises `TypeError` when the type is wrong and `ValueError` when the type is right but the value is outside the allowed range.

Why distinguish those errors? Because they describe different repairs. A type error may mean the caller forgot to convert input. A value error may mean the caller supplied a number outside policy. A user-facing program may display the same safe message, but a developer needs the distinction while debugging.

A function can call another function:

```python
def parse_severity(text):
    value = int(text.strip())
    return validate_severity(value)
```

The parser converts representation. The validator checks the internal value. Keeping those jobs separate makes each one easier to test.

Scope surprises beginners:

```python
def create_label():
    label = "review"
    return label


result = create_label()
print(result)
```

The name `label` exists inside the function. The caller can use `result` because the function returned the value. A name created inside the function is not automatically available outside it.

Avoid hidden side effects when possible:

```python
def format_summary(source, severity):
    return f"source={source} severity={severity}"
```

This function returns text and does not write a file, contact a network, or modify a global list. Pure or mostly pure functions are easier to test because the same inputs produce the same result.

A function contract should state edge cases. For `parse_severity`, decide what empty text means, whether spaces are accepted, and whether a plus sign such as `+7` is allowed. Python will have behavior even when you have not written a policy; your job is to decide whether that behavior matches the program's purpose.

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
def parse_severity(text):
    cleaned = text.strip()
    value = int(cleaned)
    if not 0 <= value <= 10:
        raise ValueError("outside range")
    return value


answer = parse_severity(" 7 ")
print(answer)
```

| Step | Event | State |
| ---: | --- | --- |
| 1 | Define function | Python stores the function definition. |
| 2 | Call with `" 7 "` | `text` refers to the raw string. |
| 3 | `strip()` | `cleaned` becomes `"7"`. |
| 4 | `int()` | `value` becomes `7`. |
| 5 | Range check | `7` is accepted. |
| 6 | `return value` | caller receives `7` as `answer`. |

If the call is `parse_severity("high")`, the function stops at `int(cleaned)` and never reaches the range check. If the call is `parse_severity("99")`, conversion succeeds but the range check raises `ValueError`.

## Common mistakes and repairs

| Mistake | Symptom | Repair |
| --- | --- | --- |
| Function prints instead of returning | Caller cannot reuse the value. | Return the result and print at the boundary. |
| No contract | Different callers assume different behavior. | State types, ranges, and failures. |
| One giant function | Errors are hard to isolate. | Separate parsing, validation, decision, and output. |
| Hidden global state | Calls affect one another. | Pass inputs explicitly. |
| Catching errors inside the validator | The caller cannot distinguish failure. | Raise expected exceptions or return a documented result. |

## Guided practice

Write three functions in order. First, `parse_severity(text)` converts text. Second, `validate_severity(value)` checks type and range. Third, `format_summary(source, severity)` returns a labelled string.

Test each function independently before composing them. Use one valid value, one malformed value, one out-of-range value, and one missing or empty value. For every failure, write which function should own the failure and why.

## Security application

Functions are useful in security engineering because they let you place controls at explicit boundaries. A parser can refuse malformed text. A validator can enforce a finite range. A formatter can avoid printing secrets. A classifier can return `unknown` instead of making a verdict.

A function contract is not authorization. A perfectly tested function can still be used against a system without permission. Keep all examples local and synthetic.

## Independent exercises

Complete these in [`practice/exercises.md`](practice/exercises.md) in order:

1. Write `add_one` and explain parameter, argument, and return value.
2. Write a function with a default source label.
3. Implement and test `validate_severity`.
4. Separate parsing from validation.
5. Write a formatter that returns rather than prints.
6. Demonstrate a `TypeError` and a `ValueError` with different inputs.
7. Explain local scope using a small function.
8. Test empty, whitespace-only, valid, and out-of-range text.
9. Write a function contract in a comment or docstring.
10. Compose parser, validator, and formatter for a synthetic record.
11. Explain why pure functions are easier to test.
12. Safety question: explain why a safe function still needs a safe caller and authorized target.



### Additional beginner checkpoint

Pause before adding another feature. Read the current program aloud as a sequence of decisions: what enters, what is transformed, what is checked, and what leaves. Write down one value that is allowed, one value that must be rejected, and one value whose meaning is uncertain. This distinction matters in cybersecurity because an unknown observation should not silently become a safe conclusion. Run the allowed case, the rejected case, and the uncertain case separately. Keep the exact output in your notes and explain which line produced it.

Now make the smallest useful improvement. Give one name a clearer meaning, extract one repeated operation, or add one explicit boundary check. Run the same three cases again. If the behavior changed, explain whether the change was intended. If a test now fails, treat the failure as information about the contract rather than deleting the test. Finish by writing one sentence about the lesson's limitation: a local Python rule can organize synthetic evidence, but it cannot establish authorization, authenticity, or the truth of a real-world accusation.

## Finish line

Day 9 is complete when you can write a small function with a clear contract, explain the difference between parameters and arguments, return a result, separate conversion from validation, and test expected failures.

## References

[1]: https://docs.python.org/3/tutorial/controlflow.html#defining-functions "Python function tutorial"
[2]: https://docs.python.org/3/library/exceptions.html "Python built-in exceptions"
[3]: https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces "Python scopes and namespaces"
[4]: https://owasp.org/www-community/attacks/Improper_Input_Validation "OWASP input validation overview"

[← Day 8](../day_08_strings_and_canonicalization/day_08_strings_and_canonicalization.md) · [Day index](../DAY_INDEX.md) · [Day 10 →](../day_10_checkpoint_log_triage/day_10_checkpoint_log_triage.md)
