# Day 15: Generators, Iterators, and Streaming Evidence

[← Day 14](../day_14_files_and_safe_paths/day_14_files_and_safe_paths.md) · [Day index](../DAY_INDEX.md) · [Day 16 →](../day_16_regular_expressions/day_16_regular_expressions.md)

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

A list loads everything before processing; a generator produces one item at a time. Streaming can reduce memory use, but it does not remove the need for bounds, error handling, or a completeness signal.

## Prerequisites

Complete Days 1–14 and be able to read a bounded file path.

## Outcomes

By the end of this lesson, you can:

- distinguish an iterable, iterator, and generator
- use `yield` to stream records
- preserve progress and truncation information
- handle malformed lines without loading everything
- explain when a generator is exhausted

## The problem

A fixture may contain many lines. The tool should inspect a small window and stop safely while telling the reviewer whether the window was complete.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples do not authorize access to public systems, university systems, employer systems, or accounts that you do not own.

## Lesson

### Vocabulary

An **iterable** can produce an iterator. An **iterator** remembers its position. A **generator** is a convenient way to create an iterator with `yield`. A generator is lazy: its body runs when the caller asks for the next item.

## Worked examples

### Example 1: A generator function

`yield` pauses the function and resumes it later.

```python
def numbers():
    yield 1
    yield 2


items = numbers()
print(next(items))
print(next(items))
```

**What to observe:**

`1` then `2`; a later `next` raises `StopIteration`.

### Example 2: Stream matching lines

Yield only matching synthetic lines instead of building a complete list.

```python
def matching(lines, needle):
    for line in lines:
        if needle in line:
            yield line
```

**What to observe:**

The caller controls how many matches it consumes.

### Example 3: Add a bound

Streaming still needs a maximum to prevent endless input.

```python
def bounded(lines, limit):
    for index, line in enumerate(lines):
        if index >= limit:
            return
        yield line
```

**What to observe:**

Only `limit` values are yielded.

### Example 4: Observe truncation

Return status separately when a report needs to say whether input was complete.

```python
def preview(lines, limit):
    values = list(bounded(lines, limit + 1))
    return values[:limit], len(values) > limit
```

**What to observe:**

The extra value lets the caller detect truncation.

### Example 5: Generator exhaustion

An iterator is stateful and cannot be replayed without creating another one.

```python
items = iter(["a", "b"])
print(list(items))
print(list(items))
```

**What to observe:**

The first list has values; the second is empty.

## Execution trace

A generator enters its body only when `next` or a loop requests a value. After yielding the final item, the next request raises `StopIteration`, which a `for` loop handles for you.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| converting the generator to a list | memory use returns to input size | consume with a bound |
| reusing an exhausted iterator | second pass is empty | create a new iterator |
| no truncation flag | output looks complete | report whether the bound stopped work |
| swallowing malformed lines | evidence disappears | count and report rejected records |
| generator with hidden network calls | iteration performs surprising effects | keep the source local and explicit |

## Security application

Stream the supplied synthetic log fixture, stop at a line limit, count matches and rejected lines, and mark `truncated=true` when the source exceeded the bound.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples above as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run `python -m course_days.day015`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A generator makes work lazy, not unlimited: the caller still owns the bound, progress, and completeness story.

## Limitations

Streaming changes memory behavior but not the trustworthiness of the input. A generator cannot authenticate a line or prevent a malicious source from producing endless data.

[← Day 14](../day_14_files_and_safe_paths/day_14_files_and_safe_paths.md) · [Day index](../DAY_INDEX.md) · [Day 16 →](../day_16_regular_expressions/day_16_regular_expressions.md)
