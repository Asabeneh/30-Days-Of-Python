# Day 7: Collections and an Indicator Catalog

[← Day 6](../day_06_loops_and_bounded_work/day_06_loops_and_bounded_work.md) · [Day index](../DAY_INDEX.md) · [Day 8 →](../day_08_strings_and_canonicalization/day_08_strings_and_canonicalization.md)





## Table of contents

- [Welcome](#welcome)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Vocabulary](#vocabulary)
- [Lesson](#lesson)
- [1. Lists preserve order and duplicates](#1-lists-preserve-order-and-duplicates)
- [2. Sets answer membership questions](#2-sets-answer-membership-questions)
- [3. Dictionaries label fields](#3-dictionaries-label-fields)
- [4. Tuples group fixed values](#4-tuples-group-fixed-values)
- [5. Mutation is a visible change](#5-mutation-is-a-visible-change)
- [Worked examples](#worked-examples)
  - [Example 1: A first runnable case](#example-1-a-first-runnable-case)
  - [Example 2: A boundary case](#example-2-a-boundary-case)
  - [Example 3: A deliberate experiment](#example-3-a-deliberate-experiment)
  - [Example 4: A bounded security fixture](#example-4-a-bounded-security-fixture)
  - [Example 5: Keep observation order and uniqueness separately](#example-5-keep-observation-order-and-uniqueness-separately)
- [Execution trace](#execution-trace)
- [Common mistakes and repairs](#common-mistakes-and-repairs)
- [Guided practice](#guided-practice)
- [Security application](#security-application)
- [Independent exercises](#independent-exercises)
  - [Additional beginner checkpoint](#additional-beginner-checkpoint)
- [Finish line](#finish-line)
- [References](#references)

## Welcome

One value is useful, but cybersecurity programs usually handle groups of values. Today you will learn lists, tuples, sets, and dictionaries by asking what each collection promises and when that promise matters.

This lesson is designed for a learner who may still need to look up how to create a file, run it, or read an error. Type the examples instead of reading them passively. Before running an experiment, write down what you expect. The difference between your prediction and Python's output is where learning happens.

## Prerequisites

Complete Day 6. Use the repository's local synthetic fixtures only. Keep a terminal open at the repository root and run each file with the Python command that worked on your computer.

## Outcomes

By the end of this lesson, you should be able to explain the new vocabulary in your own words, run and modify the examples, predict at least one boundary case, repair a deliberate mistake, and apply the idea to a bounded cybersecurity fixture.

## The problem

A small indicator catalog needs to preserve observations, remove duplicates when appropriate, and attach fields such as type and source. Choosing the wrong collection can lose order, overwrite values, or make a report hard to understand.

## Security boundary

This lesson is educational and local. It does not authorize public scanning, credential use, data collection, exploitation, interception, or changes to systems you do not own. The cybersecurity examples use invented names, loopback targets, or repository fixtures.

## Vocabulary

A **list** is an ordered, changeable collection. A **tuple** is an ordered collection commonly used for fixed groups. A **set** stores unique values without promising list-style order. A **dictionary** maps keys to values. A **membership test** asks whether a value is present.

## Lesson

A list preserves order:

```python
events = ["login_failed", "logout", "login_failed"]
print(events[0])
print(len(events))
```

The first item has index 0, not index 1. The list contains a duplicate because the same event occurred twice. Lists are appropriate when order and repeated observations matter.

A set removes duplicates:

```python
indicators = {"example.invalid", "example.invalid", "training.invalid"}
print(len(indicators))
print("training.invalid" in indicators)
```

The length is 2. A set is useful for asking whether a value has already been seen. Do not use it when the count or original order of observations is important.

A dictionary stores related fields:

```python
record = {
    "value": "example.invalid",
    "kind": "domain",
    "source": "training-fixture",
}
print(record["kind"])
```

The key `kind` retrieves the value `domain`. A missing key raises `KeyError` when accessed with brackets. You can use `.get` when missing data has a documented fallback:

```python
confidence = record.get("confidence")
print(confidence)
```

This prints `None` because the key is absent. Do not use a fallback simply to hide a required field; decide whether missing confidence should reject the record or mark it unknown.

Tuples are useful for fixed pairs:

```python
address = ("127.0.0.1", 8000)
host, port = address
print(host)
print(port)
```

The two assignments unpack the tuple. The address is not a real remote target; it is a local training value. The point is to learn how related values can travel together.

A catalog may combine collections:

```python
catalog = [
    {"value": "example.invalid", "kind": "domain"},
    {"value": "127.0.0.1", "kind": "address"},
]
for item in catalog:
    print(f"{item['kind']}={item['value']}")
```

Read the outer list as “many records” and each inner dictionary as “fields for one record.” This shape appears often in JSON and API responses.

Mutation changes a collection:

```python
items = ["a", "b"]
items.append("c")
print(items)
```

The list now contains three items. A name referring to a mutable list can observe changes made elsewhere. Later lessons will discuss copying and shared state; for now, remember that a collection can be changed after creation.

## 1. Lists preserve order and duplicates

```python
events = ["login_failed", "logout", "login_failed"]
print(events[0])
print(len(events))
```

Output:

```text
login_failed
3
```

The first item has index 0. The duplicate is meaningful: the event was observed twice. Use a list when order and repeated observations matter.

## 2. Sets answer membership questions

```python
known_events = {"login_failed", "access_denied", "login_failed"}
print(len(known_events))
print("logout" in known_events)
```

Output:

```text
2
False
```

The set removes duplicates. It is useful for asking whether a value has appeared or belongs to an allowlist. It cannot preserve the original sequence or prove that an event is malicious.

## 3. Dictionaries label fields

```python
record = {
    "event": "login_failed",
    "severity": 7,
    "source": "training-auth",
}
print(record["event"])
print(record.get("confidence"))
```

Output:

```text
login_failed
None
```

Square brackets require the key to exist. `.get` returns `None` when the optional key is absent. Decide deliberately whether a missing required key should be rejected instead.

## 4. Tuples group fixed values

```python
endpoint = ("127.0.0.1", 8000)
host, port = endpoint
print(host)
print(port)
```

A tuple can communicate that the two values belong together. The loopback address and port are local training values, not an instruction to connect to a remote service.

## 5. Mutation is a visible change

```python
items = ["a", "b"]
items.append("c")
print(items)
```

The list changes from two items to three. When two names refer to the same mutable list, one function can change what another function sees. Later lessons will use copying and contracts to make ownership clearer.

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

### Example 5: Keep observation order and uniqueness separately

```python
observed = ["login_failed", "logout", "login_failed"]
unique = set(observed)
print(len(observed))
print(len(unique))
```

The list preserves three observations and the set contains two unique values. Security reports often need both facts: frequency and uniqueness answer different questions.

## Execution trace

Trace a deduplication task:

```python
observed = ["a", "b", "a"]
unique = set(observed)
report = {"observed": len(observed), "unique": len(unique)}
print(report)
```

| Step | Name | Value |
| ---: | --- | --- |
| 1 | `observed` | three observations, including a duplicate |
| 2 | `unique` | two unique values |
| 3 | `report` | a dictionary containing both counts |

The set answers a uniqueness question but does not preserve the event sequence. Keep both collections when both facts matter.

## Common mistakes and repairs

| Mistake | Symptom | Repair |
| --- | --- | --- |
| Indexing at 1 | The first item is missed or an error occurs. | Remember that Python starts at 0. |
| Set for a timeline | Order and duplicate count disappear. | Keep a list for observations. |
| Dictionary key missing | `KeyError`. | Validate required keys or use a deliberate fallback. |
| Mutable list shared | One function changes another function's data. | Copy or document ownership. |
| Treating a value as trusted because it is in a set | Membership only answers presence. | Preserve source and confidence fields. |

## Guided practice

Create a small indicator catalog in stages. Begin with a list of three synthetic strings. Add a duplicate and count observations. Convert to a set and count unique values. Then create dictionaries containing `value`, `kind`, and `source`.

Write a report that prints both `observed_count` and `unique_count`. Add one record with a missing `confidence` key and decide whether your program should print `unknown` or reject the record. Explain your choice before coding it.

## Security application

Collections help organize evidence but do not make evidence true. A list preserves the observations your fixture contained. A set can help detect duplicates. A dictionary can label fields. None of them proves that an indicator is malicious, that a source is authentic, or that a real-world action is justified.

Use `.invalid` domains, loopback addresses, and invented hashes in exercises. Do not resolve, scan, or query these values against public services.

## Independent exercises

Complete these in [`practice/exercises.md`](practice/exercises.md) in order:

1. Create a list with three events and print the first and last item.
2. Explain why the first list index is 0.
3. Add a duplicate and calculate observed and unique counts.
4. Create a set and demonstrate membership.
5. Create a dictionary with `value`, `kind`, and `source`.
6. Access a missing dictionary key and record the exception.
7. Repair the missing-key behavior with a documented fallback.
8. Build a list of dictionaries representing synthetic indicators.
9. Add a tuple for a loopback host and port.
10. Explain which collection preserves order and which removes duplicates.
11. Write a report that includes source and confidence without claiming a verdict.
12. Safety question: explain why storing an indicator in a collection does not authorize acting on it.



### Additional beginner checkpoint

Pause before adding another feature. Read the current program aloud as a sequence of decisions: what enters, what is transformed, what is checked, and what leaves. Write down one value that is allowed, one value that must be rejected, and one value whose meaning is uncertain. This distinction matters in cybersecurity because an unknown observation should not silently become a safe conclusion. Run the allowed case, the rejected case, and the uncertain case separately. Keep the exact output in your notes and explain which line produced it.

Now make the smallest useful improvement. Give one name a clearer meaning, extract one repeated operation, or add one explicit boundary check. Run the same three cases again. If the behavior changed, explain whether the change was intended. If a test now fails, treat the failure as information about the contract rather than deleting the test. Finish by writing one sentence about the lesson's limitation: a local Python rule can organize synthetic evidence, but it cannot establish authorization, authenticity, or the truth of a real-world accusation.

## Finish line

Day 7 is complete when you can choose a collection based on order, uniqueness, mutability, and key-value structure, build a small catalog, handle missing fields, and preserve the difference between an observation and an interpretation.

## References

[1]: https://docs.python.org/3/tutorial/datastructures.html "Python data structures"
[2]: https://docs.python.org/3/library/stdtypes.html#dict "Python dictionary documentation"
[3]: https://docs.python.org/3/library/stdtypes.html#set "Python set documentation"
[4]: https://www.cisa.gov/topics/cyber-threats-and-advisories "CISA cyber threat guidance"

[← Day 6](../day_06_loops_and_bounded_work/day_06_loops_and_bounded_work.md) · [Day index](../DAY_INDEX.md) · [Day 8 →](../day_08_strings_and_canonicalization/day_08_strings_and_canonicalization.md)
