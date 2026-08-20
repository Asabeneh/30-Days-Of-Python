# Day 8: Strings, Encoding, and Canonicalization

[← Day 7](../day_07_collections_and_iocs/day_07_collections_and_iocs.md) · [Day index](../DAY_INDEX.md) · [Day 9 →](../day_09_functions_and_validation/day_09_functions_and_validation.md)

## Welcome

Security data often arrives as text, but text is not one simple thing. Case, whitespace, Unicode, separators, and encoding can make two strings look similar while comparing differently. Today you will learn to normalize text deliberately without destroying the original evidence.

This lesson is designed for a learner who may still need to look up how to create a file, run it, or read an error. Type the examples instead of reading them passively. Before running an experiment, write down what you expect. The difference between your prediction and Python's output is where learning happens.

## Prerequisites

Complete Day 7. Use the repository's local synthetic fixtures only. Keep a terminal open at the repository root and run each file with the Python command that worked on your computer.

## Outcomes

By the end of this lesson, you should be able to explain the new vocabulary in your own words, run and modify the examples, predict at least one boundary case, repair a deliberate mistake, and apply the idea to a bounded cybersecurity fixture.

## The problem

A tool wants to compare event labels consistently, but input may contain spaces, different capitalization, or different textual representations. If it silently changes the evidence, it may make a useful comparison while losing the original context.

## Security boundary

This lesson is educational and local. It does not authorize public scanning, credential use, data collection, exploitation, interception, or changes to systems you do not own. The cybersecurity examples use invented names, loopback targets, or repository fixtures.

## Vocabulary

A **string** is a sequence of text characters. **Whitespace** includes spaces, tabs, and line breaks. **Encoding** maps characters to bytes. **Canonicalization** turns equivalent representations into one comparison form. **Normalization** should be recorded when the original matters.

## Lesson

Start with string methods:

```python
raw = "  Login_Failed  "
print(raw.strip())
print(raw.lower())
print(raw.strip().casefold())
```

`strip()` removes edge whitespace. `lower()` changes letters to lowercase. `casefold()` is designed for more complete case-insensitive comparisons. Neither method changes `raw`; strings are immutable, so each method returns a new string.

Splitting turns one string into pieces:

```python
line = "level=7 source=training-auth"
parts = line.split()
print(parts)
```

Expected output is a list of two pieces. `split()` uses whitespace by default. You can specify a separator:

```python
pair = "severity:7"
key, value = pair.split(":", 1)
print(key)
print(value)
```

The second argument `1` limits the number of splits. Without a limit, a value containing a colon could produce more pieces than expected. Parsing rules should state what happens when the delimiter is missing.

Joining performs the opposite movement:

```python
fields = ["source=training-auth", "severity=7"]
line = " ".join(fields)
print(line)
```

Use `repr()` when debugging invisible characters:

```python
value = "login_failed
"
print(value)
print(repr(value))
```

The first print creates a line break from the value. The second shows the escape sequence so you can see it.

Canonicalization should be narrow. If you want to compare event labels, define the comparison form:

```python
def canonical_label(text):
    return text.strip().casefold().replace("-", "_")


print(canonical_label(" Login-Failed "))
```

The result is `login_failed`. Keep the raw label if you need to report exactly what arrived. Canonicalization for comparison is not permission to overwrite evidence.

Encoding matters when text becomes bytes:

```python
text = "café"
encoded = text.encode("utf-8")
print(encoded)
print(encoded.decode("utf-8"))
```

UTF-8 is a common encoding, but a decoder must use the encoding that matches the data source. Decoding bytes with the wrong encoding can raise `UnicodeDecodeError` or produce the wrong characters.

Never normalize paths, URLs, identifiers, or security tokens with a generic string function without understanding the context. A comparison form for labels is not automatically safe for a filesystem path or a URL.

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
raw = "  Login-Failed 
"
comparison = raw.strip().casefold().replace("-", "_")
print(repr(raw))
print(comparison)
```

| Step | Value |
| ---: | --- |
| 1 | raw text includes spaces and a newline |
| 2 | `strip()` removes the edge whitespace |
| 3 | `casefold()` changes letter case |
| 4 | `replace()` changes the selected separator |
| 5 | `repr(raw)` still shows the original representation |

The comparison value is useful for matching. The raw value remains useful for provenance and debugging.

## Common mistakes and repairs

| Mistake | Symptom | Repair |
| --- | --- | --- |
| `lower()` used as universal security normalization | Context-specific rules are ignored. | Define the exact comparison policy. |
| Discarding raw input | The original evidence cannot be reviewed. | Preserve a safe reference or original fixture. |
| `split()` without a rule | Unexpected field counts. | Limit splits and handle missing separators. |
| Decoding with a guess | Errors or corrupted text. | Use documented source encoding. |
| Replacing every symbol | Meaning changes silently. | Canonicalize only the intended field. |

## Guided practice

Take the string `"  Login-Failed "` through checkpoints: inspect it with `repr`, strip it, casefold it, replace the dash, and compare it with `"login_failed"`. Then add a second label that should not match and prove the result.

Create a small parser for `key=value` fields. Test a normal field, a field with extra `=`, a missing separator, and an empty value. Write down which cases your parser accepts and why.

## Security application

In security tools, canonicalization can prevent duplicate labels or inconsistent comparisons, but it can also hide meaningful differences if applied too broadly. Keep raw synthetic text separate from its normalized comparison form. A report might contain `raw_label` as a redacted or fixture reference and `canonical_label` as the value used for a rule.

Do not normalize or inspect real personal identifiers, URLs, tokens, or private logs in this lesson.

## Independent exercises

Complete these in [`practice/exercises.md`](practice/exercises.md) in order:

1. Show the difference between `strip`, `lower`, and `casefold` on a sample.
2. Use `repr` to reveal a newline and a tab.
3. Split a key-value pair at the first colon only.
4. Join three fields with a separator.
5. Write `canonical_label` for a documented label policy.
6. Preserve both raw and canonical values in a synthetic record.
7. Encode and decode a non-ASCII string using UTF-8.
8. Trigger and explain a missing-separator case.
9. Explain why generic replacement is dangerous for a URL or path.
10. Build a small text normalizer and test empty, spaced, and mixed-case input.
11. Describe the difference between characters and bytes.
12. Safety question: explain why retaining raw text can be a privacy concern and how fixtures reduce that risk.



### Additional beginner checkpoint

Pause before adding another feature. Read the current program aloud as a sequence of decisions: what enters, what is transformed, what is checked, and what leaves. Write down one value that is allowed, one value that must be rejected, and one value whose meaning is uncertain. This distinction matters in cybersecurity because an unknown observation should not silently become a safe conclusion. Run the allowed case, the rejected case, and the uncertain case separately. Keep the exact output in your notes and explain which line produced it.

Now make the smallest useful improvement. Give one name a clearer meaning, extract one repeated operation, or add one explicit boundary check. Run the same three cases again. If the behavior changed, explain whether the change was intended. If a test now fails, treat the failure as information about the contract rather than deleting the test. Finish by writing one sentence about the lesson's limitation: a local Python rule can organize synthetic evidence, but it cannot establish authorization, authenticity, or the truth of a real-world accusation.

## Finish line

Day 8 is complete when you can inspect invisible text, choose a narrow canonicalization rule, preserve original context, explain encoding, and handle malformed text without silently changing its meaning.

## References

[1]: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "Python string documentation"
[2]: https://docs.python.org/3/library/stdtypes.html#str.casefold "Python casefold documentation"
[3]: https://docs.python.org/3/library/stdtypes.html#str.encode "Python string encoding documentation"
[4]: https://owasp.org/www-community/attacks/Unicode_Encoding "OWASP Unicode encoding considerations"

[← Day 7](../day_07_collections_and_iocs/day_07_collections_and_iocs.md) · [Day index](../DAY_INDEX.md) · [Day 9 →](../day_09_functions_and_validation/day_09_functions_and_validation.md)
