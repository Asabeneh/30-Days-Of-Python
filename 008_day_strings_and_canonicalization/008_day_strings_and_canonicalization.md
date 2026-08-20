# Day 8: Strings, Encoding, and Canonicalization

[← Day 7](../007_day_collections_and_iocs/007_day_collections_and_iocs.md) · [Day index](../DAY_INDEX.md) · [Day 9 →](../009_day_functions_and_validation/009_day_functions_and_validation.md)

## Table of Contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Lesson](#lesson)
- [Worked examples](#worked-examples)
- [Execution trace](#execution-trace)
- [Common mistakes](#common-mistakes)
- [Security application](#security-application)
- [Exercises](#exercises)
- [Finish line](#finish-line)

## Why this lesson exists

Text is where logs, usernames, URLs, commands, and evidence meet the program. Small differences in whitespace, case, Unicode, or encoding can cause duplicate records or incorrect comparisons.

## Prerequisites

Complete Day 7. Be able to iterate through a list and preserve raw values.

## Outcomes

By the end of this lesson, you can:

- inspect and transform strings
- distinguish raw text from normalized keys
- explain Unicode text and UTF-8 bytes
- canonicalize without destroying evidence
- avoid unsafe assumptions about text

## The problem

Two records contain `Admin`, ` admin `, and `Ａｄｍｉｎ`. A comparison policy may treat them as the same key, but an investigator may still need the original spellings.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples may describe security signals, but they do not identify attackers, authorize testing, or justify touching public systems. Keep real credentials, private logs, and university or employer data out of the lesson.

## Lesson

### Strings are sequences of text

```python
message = "login_failed"
print(len(message))
print(message[0])
print(message[-1])
print(message[0:5])
```

Indexes begin at zero. Slicing creates a new string and excludes the stop index. Do not assume that one visible character always equals one byte.

### Whitespace and case

```python
raw = "  Admin  "
print(raw.strip())
print(raw.strip().casefold())
```

`strip` removes surrounding whitespace. `casefold` is designed for case-insensitive comparison. Keep `raw` if the original representation is evidence.

### Replace is not validation

```python
value = "example.invalid/path"
print(value.replace("/", "_"))
```

Replacement creates a transformed value. It does not prove that the original path or domain is valid, safe, or authorized.

### Text and bytes

```python
text = "café"
data = text.encode("utf-8")
print(data)
print(data.decode("utf-8"))
```

The string is Unicode text. UTF-8 encodes it as bytes for storage or transport. Decode with the encoding you expect; arbitrary decoding can corrupt or reject data.

### Raw and canonical forms

```python
def canonical_key(text):
    return " ".join(text.strip().casefold().split())


raw = "  ADMIN   user "
print(raw)
print(canonical_key(raw))
```

The canonical key is useful for comparison, but it must not replace the raw observation in an evidence record.
## Worked examples

### Example 1: empty versus whitespace

```python
for value in ["", " ", "
", "admin"]:
    print(repr(value), bool(value), bool(value.strip()))
```

A whitespace string is non-empty but has no visible content after stripping. Test the rule you actually intend.

### Example 2: Unicode normalization

```python
import unicodedata

value = "Ａｄｍｉｎ"
normalized = unicodedata.normalize("NFKC", value)
print(normalized)
```

Unicode normalization can make visually equivalent forms comparable. It can also change representation, so retain the raw input.

### Example 3: safe display

```python
line = "user=alice token=training-secret"
print(line.replace("training-secret", "[REDACTED]"))
```

This is a demonstration only. Real redaction should identify fields structurally and test that secrets cannot appear through alternate formatting.

### Example 4: bounded string input

```python
def accept_message(text, maximum=2000):
    if len(text) > maximum:
        raise ValueError("message is too long")
    return text
```

Length limits protect later processing. They do not guarantee that the content is harmless.

### Example 5: canonicalization with provenance

```python
record = {
    "raw_username": "  Admin ",
    "canonical_username": canonical_key("  Admin "),
}
print(record)
```

A reviewer can see both the original and the comparison key.

## Execution trace

For `canonical_key("  ADMIN   user ")`:

| Step | Operation | Result |
| ---: | --- | --- |
| 1 | `strip()` | `"ADMIN   user"` |
| 2 | `casefold()` | `"admin   user"` |
| 3 | `split()` | `["admin", "user"]` |
| 4 | `" ".join(...)` | `"admin user"` |

The transformation is deterministic and explainable.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| normalizing in place | original evidence is lost | store raw and canonical values separately |
| assuming ASCII | names or paths fail for Unicode | define encoding and test representative text |
| using `lower` everywhere | some Unicode cases compare poorly | use `casefold` for comparison when appropriate |
| stripping internal spaces | distinct values collapse | define whether internal whitespace is meaningful |
| redacting only one spelling | a secret leaks in another form | model fields and test variants |

## Security application

Build a local normalizer for synthetic usernames or indicator keys. Produce a table with raw value, canonical key, and reason for normalization. Never resolve or contact a normalized indicator.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples from this lesson as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run the starter, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> Canonicalization creates a comparison representation; evidence handling requires preserving the original text and documenting every transformation.

## Limitations

No text normalization can determine intent or prove identity. Encoding errors, confusable characters, and lossy transformations require careful policy and review.

## Optional video support

Watch [CS50P Lecture 0](https://www.youtube.com/watch?v=JP7ITIXGpHk&t=24s) from `00:24` for the first program, then return to the local string examples.

Use the [timestamped video catalog](../VIDEO_RESOURCES.md) only after running the local examples. The written lesson and Python documentation remain authoritative.


[← Day 7](../007_day_collections_and_iocs/007_day_collections_and_iocs.md) · [Day index](../DAY_INDEX.md) · [Day 9 →](../009_day_functions_and_validation/009_day_functions_and_validation.md)
