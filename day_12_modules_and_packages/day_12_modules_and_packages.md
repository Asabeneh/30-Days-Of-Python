# Day 12: Modules, Packages, and Import Boundaries

[← Day 11](../day_11_function_contracts/day_11_function_contracts.md) · [Day index](../DAY_INDEX.md) · [Day 13 →](../day_13_exceptions_and_error_taxonomy/day_13_exceptions_and_error_taxonomy.md)

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

A security tool that grows in one file becomes difficult to test, review, and reuse. Modules let you separate parsing, policy, formatting, and command-line orchestration while keeping import behavior predictable.

## Prerequisites

Complete Day 11 and know how a function contract is written.

## Outcomes

By the end of this lesson, you can:

- create a module with a focused public function
- import a name without running unrelated work
- distinguish a module from a package
- use `__name__ == "__main__"` correctly
- avoid circular and wildcard imports

## The problem

A log utility should be importable by tests without printing a banner, reading a file, or starting a server. The command-line entry point should run only when the module is executed directly.

## Security boundary

Use only the repository, synthetic examples, and local fixtures. The examples do not authorize access to public systems, university systems, employer systems, or accounts that you do not own.

## Lesson

### Vocabulary

A **module** is usually one `.py` file. A **package** is a directory of modules with an importable structure. An **import side effect** is work performed merely because another file imported a name.

## Worked examples

### Example 1: A focused module

Keep one concept in one file and import the function elsewhere.

```python
# parsers.py
def parse_pair(text):
    left, right = text.split(":", 1)
    return left, right


# main.py
from parsers import parse_pair

print(parse_pair("auth:failed"))
```

**What to observe:**

`('auth', 'failed')`

### Example 2: The main guard

The guard prevents CLI-only behavior during tests and imports.

```python
def main():
    print("running as a program")


if __name__ == "__main__":
    main()
```

**What to observe:**

Importing the module defines `main` without printing; executing the file prints the message.

### Example 3: A package path

A package gives related modules a stable namespace.

```python
from course_days.day012 import parse_pair

print(parse_pair("source:message"))
```

**What to observe:**

The import name documents where the behavior lives.

### Example 4: Explicit exports

An explicit `__all__` or documented public function helps reviewers distinguish supported API from helpers.

```python
__all__ = ["parse_pair"]


def parse_pair(text):
    return tuple(text.split(":", 1))
```

**What to observe:**

The public surface is intentionally small.

### Example 5: Avoid import-time file access

Opening a file while importing makes tests depend on the current directory and hidden state.

```python
def load_fixture(path):
    return path.read_text(encoding="utf-8")


# no call occurs during import
```

**What to observe:**

The caller chooses when and which authorized fixture to read.

## Execution trace

When `main.py` imports `parse_pair`, Python loads the module, creates the function, and skips the guarded `main()` call. When the same file is executed directly, `__name__` is `"__main__"` and the entry point runs.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| import-time work | tests print or read unexpected files | move work into functions |
| wildcard imports | origin of a name is unclear | use explicit imports |
| circular imports | partially initialized module error | invert the dependency or extract a third module |
| running from the wrong directory | package cannot be found | use the project command and environment |
| huge public surface | every helper becomes an accidental API | expose a small documented interface |

## Security application

Split the checkpoint into parser, policy, report, and CLI modules. The only target is the local repository fixture; importing any module must not contact the network or read outside the fixture.

## Line-by-line walkthrough

Read the first worked example from top to bottom rather than treating it as a magic recipe. The topic of this lesson is **Modules, Packages, and Import Boundaries**. First identify the input: what value, file, record, command, or configuration enters the example? Next identify the operation that changes or examines it. Finally identify the output and ask whether that output is merely an observation or a security conclusion. Python executes statements in order, so the name created on one line must exist before a later line can use it. When a line is a function call, identify the arguments, the function's promised return value, and any visible side effect. When a line is a condition, translate it into an ordinary question before deciding whether the branch is correct.

For each example, copy the code into a fresh file and run it unchanged. Then annotate it without editing the original: write one sentence beside each line describing its role. A useful annotation format is `input`, `transform`, `check`, `decision`, or `output`. After that, change only one value and rerun the program. If the output changes, explain which line observed the changed value. If it does not change, explain why the value was not used or why the rule filtered it. This habit is more valuable than memorizing a finished script because it teaches you to trace unfamiliar security code.

The expected output is evidence about the program, not proof about the outside world. A message such as `review` means that the local rule selected a review label. It does not prove that a person attacked a system. Keep these two statements separate in your notes. Also record failures. A `TypeError`, `ValueError`, timeout, missing-file error, or rejected configuration is often the program correctly refusing an unsafe or ambiguous input. The repair should make the policy clearer rather than hiding the error with a broad catch.

## Prediction experiments

Before each experiment, write a prediction in a comment or notebook. In Experiment A, run the smallest valid input from Example 1 and write the exact output. In Experiment B, replace one valid value with an empty, malformed, missing, or boundary value relevant to **Modules, Packages, and Import Boundaries**. Predict whether the program returns a result, raises an exception, rejects the record, or takes a different branch. In Experiment C, repeat the same input twice and inspect whether the program is deterministic. If a timestamp, random value, file order, or shared mutable state changes the result, identify that source of variation explicitly.

Do not use real addresses, credentials, private logs, public targets, or downloaded payloads for these experiments. Use the repository's synthetic fixtures, loopback values, `.invalid` names, and small in-memory inputs. Keep a table with four columns: input, prediction, observed output, and explanation. If the prediction is wrong, do not erase it. The mismatch is the part that teaches you how Python and the rule actually behave.

## Broken example and repair

Start with a deliberately broken version of the lesson's idea. A common beginner mistake is to combine parsing, policy, output, and side effects in one untested block. Another is to trust a value because it has the right shape, to use an unbounded loop, to print raw evidence, or to catch every exception. Break one rule at a time in a local copy. Run the program and capture the exception type or incorrect output. State the invariant that was violated: for example, "the input must be bounded," "the field must be validated before comparison," or "the report must not reveal raw fixture data."

Repair the example in small steps. First separate raw input from the internal value. Second add the narrowest check that expresses the intended policy. Third return or report a safe result. Fourth test one valid case, one invalid case, and one boundary case. Do not claim the repair is secure merely because it runs. Explain what remains outside the lesson's scope, such as authenticity, authorization, deployment configuration, or the correctness of the underlying policy. A good repair is easier for another beginner to inspect because each assumption is visible.

## Guided practice walkthrough

Use the following sequence before attempting the independent numbered questions. Choose one synthetic record related to **Modules, Packages, and Import Boundaries** and write down its allowed shape. For example, specify which fields are required, which values are bounded, and which fields must never be printed. Create the smallest input that satisfies the shape. Run the first example and compare the output with your prediction. Add one validation check, rerun the valid record, then test a malformed record. Keep the malformed record in the test set instead of deleting it.

Next, refactor one step into a small function or named stage. Give the stage one job and a name that describes the job. Add a print statement only while debugging, then remove it or replace it with a safe summary. Write one assertion about the result. Finally, explain the data flow in five sentences: where the fixture began, which transformation occurred, which check was applied, what label or value was produced, and what the program deliberately refused to do. Ask a peer to read the explanation without seeing the code and identify any assumption that was not documented.

## Bounded cybersecurity fixture walkthrough

The security application in this lesson uses a local, synthetic fixture. Treat the fixture as untrusted input even though it is stored in the repository. Set a maximum number of records, maximum field length, and maximum output size appropriate to the exercise. Preserve a safe source label such as `training-fixture`, but do not treat that label as proof that the data is authentic. If the fixture contains an indicator-like string, keep it inert and do not resolve, scan, connect to, upload, or enrich it from the network.

A defensible report should distinguish at least four things: what was observed, what rule matched, what uncertainty remains, and what action is permitted in this lab. For example, `observed=synthetic_event`, `rule=high_value`, `confidence=training-only`, and `action=write-local-report`. The last field is a laboratory boundary, not an operational recommendation. If your code cannot make that distinction, stop and improve the report before adding features. Security engineering is not only about detecting a pattern; it is also about limiting authority, preserving provenance, and communicating uncertainty.

At the end, perform a small review. Check that the program uses only local fixtures, has a finite workload, handles malformed input, avoids raw sensitive output, and leaves the fixture unchanged. Then write one residual-risk sentence. A useful form is: "This lesson demonstrates Modules, Packages, and Import Boundaries on synthetic data, but it does not establish authenticity, authorization, production readiness, or the presence of a real attack.
## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples above as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.

## Finish line

Run `python -m course_days.day012`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> A module is a boundary for responsibility; importing it should define reusable behavior without surprising side effects.

## Limitations

Module organization does not make unsafe behavior safe. A well-organized tool can still have a flawed parser or an unauthorized target.


## References

[1]: https://docs.python.org/3/ "Python documentation"
[2]: https://docs.python.org/3/tutorial/ "The Python tutorial"
[3]: https://owasp.org/www-project-top-ten/ "OWASP Top 10"
[4]: https://csrc.nist.gov/glossary "NIST cybersecurity glossary"

[← Day 11](../day_11_function_contracts/day_11_function_contracts.md) · [Day index](../DAY_INDEX.md) · [Day 13 →](../day_13_exceptions_and_error_taxonomy/day_13_exceptions_and_error_taxonomy.md)
