"""Author dense teaching chapters for Days 11–20."""

from __future__ import annotations

# ruff: noqa: E501
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DAY_DIRS = {
    10: "day_10_checkpoint_log_triage",
    11: "day_11_function_contracts",
    12: "day_12_modules_and_packages",
    13: "day_13_exceptions_and_error_taxonomy",
    14: "day_14_files_and_safe_paths",
    15: "day_15_iterators_and_generators",
    16: "day_16_regular_expressions",
    17: "day_17_dates_and_timelines",
    18: "day_18_classes_and_dataclasses",
    19: "day_19_testing_with_pytest",
    20: "day_20_project__log_triage_cli",
    21: "day_21_virtual_environments",
}


@dataclass(frozen=True)
class Lesson:
    day: int
    directory: str
    title: str
    why: str
    prerequisites: str
    outcomes: str
    problem: str
    vocabulary: str
    examples: list[tuple[str, str, str, str]]
    trace: str
    mistakes: str
    security: str
    mental_model: str
    limitations: str


LESSONS = [
    Lesson(
        11,
        "day_11_function_contracts",
        "Function Contracts and Explicit Security Decisions",
        "A function is where an idea becomes a reusable promise. Security utilities become trustworthy when their inputs, outputs, failures, and side effects are visible enough for another person to review.",
        "Complete Days 1–10. You should be able to write a function, return a value, and test a boundary.",
        "- write a precondition and postcondition\n- distinguish a return value from a side effect\n- use keyword-only arguments and immutable defaults\n- preserve failure information\n- test a contract rather than an implementation detail",
        "The phase-one classifier works, but its rules are hidden inside a script. A reviewer needs a small function whose contract says exactly which severity values are accepted, which label is returned, and what happens when the input is invalid.",
        "A **precondition** describes what must be true before a call. A **postcondition** describes what the caller can rely on after a successful return. A **side effect** changes something outside the returned value, such as a file, log, database, or network service.",
        [
            (
                "The smallest contract",
                "A function can make its accepted input and returned value obvious.",
                "def double(value):\n    return value * 2\n\nprint(double(4))",
                "8",
            ),
            (
                "A bounded contract",
                "Validation belongs at the boundary so every caller receives the same rule.",
                'def severity_label(severity):\n    if not isinstance(severity, int):\n        raise TypeError("severity must be an integer")\n    if not 0 <= severity <= 10:\n        raise ValueError("severity must be between 0 and 10")\n    return "high" if severity >= 7 else "normal"',
                "`severity_label(7)` returns `high`; `severity_label(11)` raises `ValueError`.",
            ),
            (
                "Keyword-only safety options",
                "Keyword-only parameters make an important option visible at the call site.",
                'def read_preview(path, *, max_bytes=4096):\n    if max_bytes <= 0:\n        raise ValueError("max_bytes must be positive")\n    return path.read_bytes()[:max_bytes]',
                "The caller must write `max_bytes=...`; an accidental positional limit is harder to review.",
            ),
            (
                "Return instead of print",
                "Returning a structured value lets tests and callers inspect the decision without capturing terminal output.",
                'def finding(label, reason):\n    return {"label": label, "reason": reason}\n\nresult = finding("review", "high severity")\nprint(result["label"])',
                "`review`",
            ),
            (
                "Keep effects at the edge",
                "File access is a side effect and should be separated from a pure parser.",
                "def format_report(event):\n    return f\"source={event['source']} severity={event['severity']}\"",
                "The function returns text and does not open a file or contact a service.",
            ),
        ],
        'For `severity_label(8)`, Python binds the argument, checks its type, checks the range, evaluates `8 >= 7`, and returns `high`. For `severity_label("8")`, the type precondition fails before policy logic runs.',
        "| Mistake | Symptom | Correction |\n| --- | --- | --- |\n| no return | caller receives `None` | return the promised value |\n| broad `except` | programming errors become ordinary bad input | catch only expected boundary errors |\n| mutable default | calls share hidden state | use `None` or an immutable default |\n| hidden file write | a pure function changes evidence | keep effects in a small boundary function |\n| undocumented range | callers guess the policy | state preconditions and test boundaries |",
        "Refactor one phase-one rule into a pure function and add a contract table. The exercise must use only synthetic events and must distinguish the observation `rule matched` from the conclusion `attack occurred`.",
        "A function contract is a small trust boundary: explicit input enters, a defined result leaves, and side effects are visible.",
        "A contract improves review but cannot prove that the caller supplied authentic data or that the policy is correct for a production environment.",
    ),
    Lesson(
        12,
        "day_12_modules_and_packages",
        "Modules, Packages, and Import Boundaries",
        "A security tool that grows in one file becomes difficult to test, review, and reuse. Modules let you separate parsing, policy, formatting, and command-line orchestration while keeping import behavior predictable.",
        "Complete Day 11 and know how a function contract is written.",
        '- create a module with a focused public function\n- import a name without running unrelated work\n- distinguish a module from a package\n- use `__name__ == "__main__"` correctly\n- avoid circular and wildcard imports',
        "A log utility should be importable by tests without printing a banner, reading a file, or starting a server. The command-line entry point should run only when the module is executed directly.",
        "A **module** is usually one `.py` file. A **package** is a directory of modules with an importable structure. An **import side effect** is work performed merely because another file imported a name.",
        [
            (
                "A focused module",
                "Keep one concept in one file and import the function elsewhere.",
                '# parsers.py\ndef parse_pair(text):\n    left, right = text.split(":", 1)\n    return left, right\n\n# main.py\nfrom parsers import parse_pair\nprint(parse_pair("auth:failed"))',
                "`('auth', 'failed')`",
            ),
            (
                "The main guard",
                "The guard prevents CLI-only behavior during tests and imports.",
                'def main():\n    print("running as a program")\n\nif __name__ == "__main__":\n    main()',
                "Importing the module defines `main` without printing; executing the file prints the message.",
            ),
            (
                "A package path",
                "A package gives related modules a stable namespace.",
                'from course_days.day12 import parse_pair\n\nprint(parse_pair("source:message"))',
                "The import name documents where the behavior lives.",
            ),
            (
                "Explicit exports",
                "An explicit `__all__` or documented public function helps reviewers distinguish supported API from helpers.",
                '__all__ = ["parse_pair"]\n\ndef parse_pair(text):\n    return tuple(text.split(":", 1))',
                "The public surface is intentionally small.",
            ),
            (
                "Avoid import-time file access",
                "Opening a file while importing makes tests depend on the current directory and hidden state.",
                'def load_fixture(path):\n    return path.read_text(encoding="utf-8")\n\n# no call occurs during import',
                "The caller chooses when and which authorized fixture to read.",
            ),
        ],
        'When `main.py` imports `parse_pair`, Python loads the module, creates the function, and skips the guarded `main()` call. When the same file is executed directly, `__name__` is `"__main__"` and the entry point runs.',
        "| Mistake | Symptom | Correction |\n| --- | --- | --- |\n| import-time work | tests print or read unexpected files | move work into functions |\n| wildcard imports | origin of a name is unclear | use explicit imports |\n| circular imports | partially initialized module error | invert the dependency or extract a third module |\n| running from the wrong directory | package cannot be found | use the project command and environment |\n| huge public surface | every helper becomes an accidental API | expose a small documented interface |",
        "Split the checkpoint into parser, policy, report, and CLI modules. The only target is the local repository fixture; importing any module must not contact the network or read outside the fixture.",
        "A module is a boundary for responsibility; importing it should define reusable behavior without surprising side effects.",
        "Module organization does not make unsafe behavior safe. A well-organized tool can still have a flawed parser or an unauthorized target.",
    ),
    Lesson(
        13,
        "day_13_exceptions_and_error_taxonomy",
        "Exceptions and Error Taxonomy",
        "Errors are part of a security tool’s output. If a program hides a malformed record, a permission failure, and a programming bug under one `except`, operators cannot know what happened or what to do next.",
        "Complete Days 1–12 and be comfortable with modules, functions, and conversion errors.",
        "- read a traceback from the bottom up\n- raise a precise exception at a boundary\n- catch only what the caller can handle\n- preserve context with exception chaining\n- separate rejected input from unavailable resources",
        "The log parser sees a missing field, the fixture path is outside the allowed directory, and the report file cannot be written. These are different failures and require different messages and tests.",
        "An **exception** is an object describing an abnormal condition. **Raising** transfers control to a handler. **Catching** says the current layer knows how to recover or report. An exception chain preserves the original cause.",
        [
            (
                "Catch the expected conversion error",
                "Handle malformed user input at the CLI boundary.",
                'try:\n    severity = int(raw)\nexcept ValueError:\n    print("severity must be an integer")',
                "The user sees a useful message instead of a traceback.",
            ),
            (
                "Raise a policy error",
                "A successful conversion can still violate a domain rule.",
                'def require_limit(value):\n    if not 1 <= value <= 1000:\n        raise ValueError("limit must be 1..1000")\n    return value',
                "`require_limit(1001)` raises a precise policy error.",
            ),
            (
                "Use separate exception types",
                "A caller can react differently to invalid data and a missing file.",
                "class InvalidRecord(ValueError):\n    pass\n\nclass FixtureNotFound(FileNotFoundError):\n    pass",
                "The type communicates the recovery path.",
            ),
            (
                "Chain a cause",
                "Translate a low-level exception while preserving why it happened.",
                'try:\n    value = int(raw)\nexcept ValueError as error:\n    raise InvalidRecord("severity is malformed") from error',
                "The message is domain-specific and the original `ValueError` remains available.",
            ),
            (
                "Do not hide failures",
                "A catch-all returning an empty list looks like a successful scan with no findings.",
                'try:\n    records = load_fixture(path)\nexcept FixtureNotFound:\n    return {"status": "unavailable"}\n',
                "The caller can distinguish unavailable input from an empty result.",
            ),
        ],
        'For `int("high")`, Python raises `ValueError`; the boundary catches it and raises `InvalidRecord` with the original error chained. A programming error such as a misspelled variable should remain visible instead of being converted into `invalid input`.',
        "| Mistake | Symptom | Correction |\n| --- | --- | --- |\n| `except Exception` everywhere | real bugs disappear | catch only recoverable types |\n| `except: pass` | evidence silently vanishes | report or re-raise with context |\n| one error for all cases | operators cannot choose a response | define a small error taxonomy |\n| leaking raw input | secrets appear in messages | use safe field names and redaction |\n| retrying every error | malformed data is processed repeatedly | retry only transient resource failures |",
        "Add a rejection report for malformed synthetic records and a separate unavailable-fixture result. Never include the full raw line or a secret in the exception message.",
        "An exception is information about a failed assumption; classify it so the correct layer can recover, report, or stop.",
        "Exception messages can be sensitive and exception types are not a complete observability strategy. Production systems also need structured logs, metrics, and ownership.",
    ),
    Lesson(
        14,
        "day_14_files_and_safe_paths",
        "Files, Paths, and Safe Evidence Boundaries",
        "Files are useful evidence sources and dangerous trust boundaries. A path supplied by a user can escape the intended directory, a large file can consume resources, and a report can overwrite something important.",
        "Complete Days 1–13 and know how to catch a boundary exception.",
        "- use `pathlib.Path` for readable path operations\n- resolve and constrain a path to a base directory\n- read text with an explicit encoding\n- bound file size and line length\n- write reports atomically in a fixture directory",
        "The checkpoint should read one supplied fixture and write one generated report without following `../` outside the training directory. The safety property must be testable.",
        "A **path** is a description of a location. A **resolved path** is the normalized location after following relative components and links. A **trust boundary** is where data changes from an external or less-trusted source into a sensitive operation.",
        [
            (
                "Build a path",
                "Joining path components is clearer with `Path` than string concatenation.",
                'from pathlib import Path\n\nbase = Path("training-fixtures")\npath = base / "events.log"\nprint(path)',
                "`training-fixtures/events.log` on POSIX-style output.",
            ),
            (
                "Resolve and constrain",
                "Compare resolved paths rather than searching for a literal `..`.",
                'def safe_path(base, user_value):\n    base = base.resolve()\n    candidate = (base / user_value).resolve()\n    if candidate != base and base not in candidate.parents:\n        raise ValueError("path escapes fixture directory")\n    return candidate',
                "`../secret.txt` is rejected after resolution.",
            ),
            (
                "Read with an encoding",
                "Text decoding is part of the file contract.",
                'text = path.read_text(encoding="utf-8")\nprint(text.splitlines()[:2])',
                "The first two lines are read as Unicode text.",
            ),
            (
                "Check size before reading",
                "A tool can refuse a fixture that exceeds its documented bound.",
                'maximum = 1_000_000\nif path.stat().st_size > maximum:\n    raise ValueError("fixture is too large")',
                "The file is rejected before its full content enters memory.",
            ),
            (
                "Write a controlled report",
                "Create output only beneath the chosen report directory.",
                'report_dir = Path("training-output")\nreport_dir.mkdir(exist_ok=True)\n(report_dir / "summary.txt").write_text("complete\\n", encoding="utf-8")',
                "The output is local and resettable.",
            ),
        ],
        "For base `/course/training-fixtures` and user value `../secret.txt`, the candidate resolves to `/course/secret.txt`. The candidate is not inside the resolved base, so the function raises before opening it.",
        "| Mistake | Symptom | Correction |\n| --- | --- | --- |\n| string prefix check | `/base-other` looks like `/base` | compare resolved path parents |\n| string concatenation | separators and `..` behave unexpectedly | use `Path` |\n| no encoding | platform-dependent decoding | specify UTF-8 or the documented encoding |\n| read before size check | memory spikes | inspect metadata first |\n| overwrite source | evidence is destroyed | write to a dedicated output directory |",
        "Use only `shared/fixtures` or a temporary directory under the repository. Add tests for a normal relative path, `../` escape, absolute path, oversized fixture, and output cleanup.",
        "A file operation is safe only when location, size, encoding, mode, and cleanup are explicit.",
        "Path checks can be affected by symlinks, permissions, races, and platform differences. A local helper is not a replacement for a hardened production file service.",
    ),
    Lesson(
        15,
        "day_15_iterators_and_generators",
        "Generators, Iterators, and Streaming Evidence",
        "A list loads everything before processing; a generator produces one item at a time. Streaming can reduce memory use, but it does not remove the need for bounds, error handling, or a completeness signal.",
        "Complete Days 1–14 and be able to read a bounded file path.",
        "- distinguish an iterable, iterator, and generator\n- use `yield` to stream records\n- preserve progress and truncation information\n- handle malformed lines without loading everything\n- explain when a generator is exhausted",
        "A fixture may contain many lines. The tool should inspect a small window and stop safely while telling the reviewer whether the window was complete.",
        "An **iterable** can produce an iterator. An **iterator** remembers its position. A **generator** is a convenient way to create an iterator with `yield`. A generator is lazy: its body runs when the caller asks for the next item.",
        [
            (
                "A generator function",
                "`yield` pauses the function and resumes it later.",
                "def numbers():\n    yield 1\n    yield 2\n\nitems = numbers()\nprint(next(items))\nprint(next(items))",
                "`1` then `2`; a later `next` raises `StopIteration`.",
            ),
            (
                "Stream matching lines",
                "Yield only matching synthetic lines instead of building a complete list.",
                "def matching(lines, needle):\n    for line in lines:\n        if needle in line:\n            yield line",
                "The caller controls how many matches it consumes.",
            ),
            (
                "Add a bound",
                "Streaming still needs a maximum to prevent endless input.",
                "def bounded(lines, limit):\n    for index, line in enumerate(lines):\n        if index >= limit:\n            return\n        yield line",
                "Only `limit` values are yielded.",
            ),
            (
                "Observe truncation",
                "Return status separately when a report needs to say whether input was complete.",
                "def preview(lines, limit):\n    values = list(bounded(lines, limit + 1))\n    return values[:limit], len(values) > limit",
                "The extra value lets the caller detect truncation.",
            ),
            (
                "Generator exhaustion",
                "An iterator is stateful and cannot be replayed without creating another one.",
                'items = iter(["a", "b"])\nprint(list(items))\nprint(list(items))',
                "The first list has values; the second is empty.",
            ),
        ],
        "A generator enters its body only when `next` or a loop requests a value. After yielding the final item, the next request raises `StopIteration`, which a `for` loop handles for you.",
        "| Mistake | Symptom | Correction |\n| --- | --- | --- |\n| converting the generator to a list | memory use returns to input size | consume with a bound |\n| reusing an exhausted iterator | second pass is empty | create a new iterator |\n| no truncation flag | output looks complete | report whether the bound stopped work |\n| swallowing malformed lines | evidence disappears | count and report rejected records |\n| generator with hidden network calls | iteration performs surprising effects | keep the source local and explicit |",
        "Stream the supplied synthetic log fixture, stop at a line limit, count matches and rejected lines, and mark `truncated=true` when the source exceeded the bound.",
        "A generator makes work lazy, not unlimited: the caller still owns the bound, progress, and completeness story.",
        "Streaming changes memory behavior but not the trustworthiness of the input. A generator cannot authenticate a line or prevent a malicious source from producing endless data.",
    ),
    Lesson(
        16,
        "day_16_regular_expressions",
        "Regular Expressions and Careful Indicator Extraction",
        "Regular expressions are useful for finding candidate shapes in text, such as an IP-like token or an event ID. They are not complete validators and must never turn a match into an accusation.",
        "Complete Days 1–15 and understand strings, generators, and bounded processing.",
        "- write a small regex with named groups\n- use `finditer` to preserve positions\n- distinguish candidate extraction from validation\n- avoid catastrophic patterns and excessive input\n- retain raw context and confidence",
        "A synthetic log line contains several tokens. Extract candidates with their positions, then validate the candidate using ordinary Python logic. The report must preserve the original line number without storing unnecessary raw data.",
        "A **pattern** describes text shape. A **match** is evidence that the shape occurred. A **capture group** returns part of a match. A **validator** applies domain rules that a pattern alone may not express.",
        [
            (
                "Find a simple field",
                "A named group makes the captured value readable.",
                'import re\n\npattern = re.compile(r"user=(?P<user>[a-z0-9_-]+)")\nmatch = pattern.search("user=alice status=ok")\nprint(match.group("user"))',
                "`alice`",
            ),
            (
                "Find every candidate",
                "`finditer` provides each match and its position.",
                'for match in re.finditer(r"id=(?P<id>\\d+)", "id=12 id=99"):\n    print(match.group("id"), match.start())',
                "`12 0` and `99 6` with positions relative to the string.",
            ),
            (
                "Validate an IP-like candidate",
                "A simple shape can be checked with numeric policy afterward.",
                'def valid_ipv4(text):\n    parts = text.split(".")\n    return len(parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)',
                "`203.0.113.8` is accepted; `999.1.1.1` is rejected.",
            ),
            (
                "Avoid a greedy match",
                "A narrow character class prevents a pattern from swallowing unrelated text.",
                'pattern = re.compile(r"token=(?P<token>[^\\s]+)")\nprint(pattern.search("token=abc next=value").group("token"))',
                "`abc`; the match stops at whitespace.",
            ),
            (
                "Bound the input",
                "A regex should not process an unbounded line supplied by an unknown source.",
                "line = line[:2000]\nif len(line) == 2000:\n    truncated = True",
                "The report can say that matching occurred on a bounded preview.",
            ),
        ],
        "For `user=alice`, the pattern first locates the literal `user=`, captures allowed characters into `user`, and returns the group. For a candidate IP, extraction finds text first and validation checks four numeric octets afterward.",
        "| Mistake | Symptom | Correction |\n| --- | --- | --- |\n| pattern is a validator | malformed candidate is trusted | validate with domain logic |\n| greedy `.*` | one match consumes too much | use narrow classes and test boundaries |\n| no input bound | expensive matching on huge data | cap line length |\n| losing positions | reviewer cannot locate evidence | store line and character positions |\n| printing full sensitive line | data leaks into output | report a redacted excerpt or identifier |",
        "Extract candidate IP-like values only from the synthetic fixture. Preserve line number and character position, validate octets, and label the result `candidate` rather than `malicious`.",
        "A regex finds a shape; a validator adds domain rules; neither one proves intent, ownership, or compromise.",
        "Regex syntax can become complex and expensive. Prefer small patterns, bounds, tests, and a standard library parser when a protocol already defines one.",
    ),
    Lesson(
        17,
        "day_17_dates_and_timelines",
        "Timestamps, Timezones, and Incident Timelines",
        "Security evidence is often ordered by time, but timestamps arrive in different formats and offsets. A timeline is only as reliable as its parsing, timezone policy, and provenance.",
        "Complete Days 1–16 and be able to parse strings at a boundary.",
        "- parse ISO timestamps\n- require timezone-aware values\n- compare events in a common timezone\n- preserve the raw timestamp\n- identify clock and ordering limitations",
        "Two synthetic records show `10:00+00:00` and `11:00+01:00`. They represent the same instant. A naive string sort can suggest the wrong order.",
        "A **naive datetime** has no timezone. An **aware datetime** includes enough offset information to identify an instant. **Normalization** converts values into a common representation while **provenance** preserves how the value originally arrived.",
        [
            (
                "Parse UTC",
                "The `Z` suffix means UTC when converted to `+00:00`.",
                'from datetime import datetime\n\nvalue = datetime.fromisoformat("2026-08-20T10:00:00+00:00")\nprint(value.tzinfo is not None)',
                "`True`",
            ),
            (
                "Reject a naive value",
                "A timestamp without an offset cannot be safely compared across sources.",
                'value = datetime.fromisoformat("2026-08-20T10:00:00")\nif value.tzinfo is None:\n    raise ValueError("timestamp needs a timezone")',
                "The explicit error prevents an ambiguous timeline.",
            ),
            (
                "Compare offsets",
                "Aware datetimes compare instants, not only displayed clock text.",
                'first = datetime.fromisoformat("2026-08-20T10:00:00+00:00")\nsecond = datetime.fromisoformat("2026-08-20T11:00:00+01:00")\nprint(first == second)',
                "`True`",
            ),
            (
                "Normalize to UTC",
                "A common display timezone makes a report easier to read.",
                "from datetime import timezone\nprint(second.astimezone(timezone.utc))",
                "The result displays the same instant in UTC.",
            ),
            (
                "Keep provenance",
                "Store the original string beside the parsed value.",
                'record = {"raw_timestamp": "2026-08-20T11:00:00+01:00", "parsed": second}',
                "The reviewer can check the transformation.",
            ),
        ],
        "The two example timestamps compare equal because their offsets describe the same instant. If one value is naive, Python should reject it before sorting rather than inventing a timezone.",
        "| Mistake | Symptom | Correction |\n| --- | --- | --- |\n| sorting strings | offset events appear misordered | parse aware datetimes |\n| assuming local time | results differ by machine | require or document timezone |\n| dropping raw values | transformation cannot be audited | preserve provenance |\n| treating order as causation | timeline overclaims | describe sequence and uncertainty |\n| accepting future or impossible dates | fixture quality is hidden | document clock policy and test it |",
        "Build a synthetic timeline from fixture events, normalize to UTC, preserve raw timestamps, and report when two events have equal instants or when input lacks a timezone.",
        "A timeline is an ordered interpretation of timestamped observations, not a complete story of causation.",
        "Clock skew, delayed collection, missing events, and forged timestamps can make a correct sort misleading. Production investigations need corroboration and chain-of-custody procedures.",
    ),
    Lesson(
        18,
        "day_18_classes_and_dataclasses",
        "Dataclasses and Evidence Models",
        "A dictionary is flexible but lets field names and types drift. A dataclass gives a security tool a visible model for a finding, its evidence reference, and its confidence without pretending that the model authenticates the data.",
        "Complete Days 1–17 and understand functions, validation, collections, and timestamps.",
        "- define a dataclass with typed fields\n- validate values in `__post_init__`\n- use frozen objects for immutable findings\n- serialize safely without leaking raw evidence\n- distinguish a model from proof",
        "A report needs a stable finding shape. Reviewers should know which fields are required, which are derived, and which identifier points back to a local fixture.",
        "A **dataclass** generates useful representation and comparison methods for a class. A **frozen** dataclass prevents reassignment after construction. A field type documents intent but does not validate arbitrary runtime input.",
        [
            (
                "The smallest dataclass",
                "Fields describe the model in one place.",
                "from dataclasses import dataclass\n\n@dataclass\nclass Finding:\n    title: str\n    severity: int",
                "`Finding(title='...', severity=...)` is readable when printed.",
            ),
            (
                "Validate on construction",
                "Reject invalid severity before the object enters the report pipeline.",
                '@dataclass\nclass Finding:\n    title: str\n    severity: int\n\n    def __post_init__(self):\n        if not self.title.strip():\n            raise ValueError("title is required")\n        if not 0 <= self.severity <= 10:\n            raise ValueError("severity is outside 0..10")',
                "An invalid object cannot be constructed.",
            ),
            (
                "Freeze a finding",
                "An immutable result prevents accidental mutation after review.",
                "@dataclass(frozen=True)\nclass EvidenceRef:\n    case_id: str\n    line: int",
                "Assigning `ref.line = 3` raises `FrozenInstanceError`.",
            ),
            (
                "Convert deliberately",
                "`asdict` produces data for a report, but the model should not contain secrets.",
                'from dataclasses import asdict\nfinding = Finding("training rule matched", 7)\nprint(asdict(finding))',
                "A dictionary with only the declared safe fields is produced.",
            ),
            (
                "Keep evidence references narrow",
                "Use a case and line identifier rather than embedding a whole raw record.",
                'ref = EvidenceRef("training-018", 2)\nprint(ref)',
                "The report points to local evidence without copying it everywhere.",
            ),
        ],
        "Construction calls the generated initializer, then `__post_init__` validates the fields. A frozen object can be read and serialized, but its attributes cannot be reassigned.",
        "| Mistake | Symptom | Correction |\n| --- | --- | --- |\n| trusting type hints | runtime strings enter integer fields | validate in construction or boundary parser |\n| storing raw secrets | reports leak sensitive data | store redacted references |\n| mutable finding | later code changes reviewed evidence | freeze when immutability is intended |\n| no equality tests | duplicate findings are unclear | define identity and compare deliberately |\n| model as proof | a clean object is mistaken for true evidence | state provenance and confidence |",
        "Model synthetic findings with title, severity, confidence, and an evidence reference. Do not embed private or real raw evidence. Add tests for invalid severity, blank title, and immutable references.",
        "A dataclass is a readable model for a decision or observation; it is not an authenticity guarantee.",
        "Dataclasses do not enforce trust, authorization, provenance, or serialization safety by themselves. A model can faithfully represent bad input.",
    ),
    Lesson(
        19,
        "day_19_testing_with_pytest",
        "Testing Security Utilities",
        "Tests turn a claim about code into a repeatable check. Security tests should cover ordinary behavior, boundaries, malformed inputs, and the absence of dangerous side effects.",
        "Complete Days 1–18 and run the existing pytest suite once.",
        "- write a focused test\n- use arrange, act, assert\n- test boundaries and rejection paths\n- isolate filesystem work with temporary paths\n- distinguish unit evidence from system confidence",
        "A parser that passes one happy-path test may still accept an invalid port, leak a token, or read outside its fixture. The test suite must make those failures visible.",
        "A **unit test** checks one small behavior. A **fixture** prepares repeatable input. A **negative test** proves that an invalid or unsafe case is rejected. A **regression test** preserves a behavior after a bug is fixed.",
        [
            (
                "Arrange, act, assert",
                "Keep the test readable by separating setup, call, and expectation.",
                'def test_severity_label_high():\n    result = severity_label(8)\n    assert result == "high"',
                "A failure points to the contract.",
            ),
            (
                "Parametrize boundaries",
                "Multiple boundary cases should share the same claim.",
                'import pytest\n\n@pytest.mark.parametrize("value", [0, 10])\ndef test_severity_boundaries(value):\n    assert severity_label(value) in {"normal", "high"}',
                "Both accepted endpoints are checked.",
            ),
            (
                "Assert rejection",
                "A test should prove an invalid value fails for the intended reason.",
                'def test_bad_port_rejected():\n    with pytest.raises(ValueError, match="1..65535"):\n        parse_port("70000")',
                "The test fails if the value is silently accepted.",
            ),
            (
                "Use a temporary path",
                "Filesystem tests should not write into the repository or a real home directory.",
                'def test_report(tmp_path):\n    path = tmp_path / "report.txt"\n    write_report(path, "training")\n    assert path.read_text(encoding="utf-8") == "training\\n"',
                "pytest cleans the temporary directory.",
            ),
            (
                "Test no secret leakage",
                "A report contract can assert that a token is absent.",
                'def test_report_redacts_token():\n    output = render({"token": "training-secret"})\n    assert "training-secret" not in output',
                "The negative property is explicit.",
            ),
        ],
        "A test first creates the fixture, calls one behavior, and then asserts the contract. A failure should tell you which claim broke; a test that only checks `result is not None` is weak evidence.",
        "| Mistake | Symptom | Correction |\n| --- | --- | --- |\n| testing implementation details | harmless refactor breaks tests | assert observable contracts |\n| only happy paths | malformed input is untested | add rejection and boundary cases |\n| shared real files | tests interfere or leak data | use `tmp_path` and fixtures |\n| giant integration test | failure location is unclear | keep units small and add focused integration tests |\n| trusting coverage alone | lines run without meaningful assertions | review the claims each test makes |",
        "Write tests for the phase-two tools: safe path rejection, bounded line handling, severity validation, timestamp timezone requirements, dataclass immutability, and redaction. Use only synthetic fixtures.",
        "A test is a repeatable argument for one behavior; a suite becomes useful when it includes failure modes and security properties, not only successful output.",
        "Passing tests do not prove absence of vulnerabilities, correctness of a threat model, or authorization to operate on a real system. They provide bounded evidence.",
    ),
    Lesson(
        20,
        "day_20_project__log_triage_cli",
        "Checkpoint: Build a Log-Triage CLI",
        "A command-line tool is where modules, errors, files, generators, regex, timelines, dataclasses, and tests meet. This checkpoint turns the phase into a small artifact that another learner can run and review.",
        "Complete Days 11–19. Run formatting, linting, compilation, and tests before starting the project.",
        "- design a CLI with explicit arguments and exit statuses\n- compose validated modules without hidden side effects\n- produce bounded, explainable output\n- test normal, malformed, missing, and out-of-scope cases\n- write a threat model and limitations section",
        "Build `log-triage` for the supplied synthetic fixture. It should accept an input path beneath a fixture root, process a maximum number of lines, classify only validated records, and write a report under a dedicated output directory.",
        "A **CLI** is a user-facing boundary around program behavior. An **exit status** communicates success or failure to a shell or automation. A **report** should distinguish raw observations, derived labels, rejected records, and truncation.",
        [
            (
                "Define the command",
                "Use explicit options instead of positional magic for security-sensitive bounds.",
                "python -m course_days.day20 --input shared/fixtures/events.log --limit 100 --output training-output/report.json",
                "The command states its input, limit, and output.",
            ),
            (
                "Parse arguments",
                "`argparse` provides help and type conversion, but application bounds still belong in validation.",
                'parser.add_argument("--limit", type=int, default=100)\nargs = parser.parse_args([])\nprint(args.limit)',
                "`100` is the documented default.",
            ),
            (
                "Compose the pipeline",
                "Each stage should have a single responsibility.",
                "raw_lines = read_lines(input_path, limit)\nrecords = (parse_line(line) for line in raw_lines)\nvalidated = (validate(record) for record in records)",
                "The pipeline is lazy and bounded; add rejection accounting before production.",
            ),
            (
                "Represent a report",
                "A structured report makes incomplete work visible.",
                'report = {"processed": 3, "accepted": 2, "rejected": 1, "truncated": False}',
                "The report does not pretend that rejected data was accepted.",
            ),
            (
                "Exit deliberately",
                "Automation needs a stable status contract.",
                'if report["rejected"]:\n    raise SystemExit(2)\nraise SystemExit(0)',
                "The project must document whether rejected records are an error, warning, or expected result.",
            ),
        ],
        "The CLI parses options, resolves and bounds the input, streams lines, parses and validates records, applies the pure classifier, writes a safe report, and exits with a documented status. A failure in one boundary should not become an empty successful report.",
        "| Mistake | Symptom | Correction |\n| --- | --- | --- |\n| arbitrary input path | fixture boundary is bypassed | resolve beneath an allowed root |\n| unlimited default | CLI can consume unexpected resources | choose a finite default |\n| hidden output location | reports overwrite source data | require a dedicated output directory |\n| mixed raw and derived data | users cannot audit decisions | label fields clearly |\n| no README | another learner cannot reproduce it | document setup, scope, examples, and reset |",
        "The checkpoint is local-only and synthetic. The README must name the allowed fixture root, maximum line and byte limits, output cleanup, test command, threat model, false-positive limitations, and the fact that a label is not proof of compromise.",
        "A CLI is a chain of explicit boundaries; its quality is the quality of its input contract, resource limits, evidence labels, and failure behavior.",
        "This is not a production SIEM, incident-response platform, or detector of real attacks. It demonstrates composition and safe evidence handling. Real deployments require operational ownership, authorization, monitoring, and review.",
    ),
]


def render(lesson: Lesson) -> str:
    previous = lesson.day - 1
    next_day = lesson.day + 1
    previous_link = (
        "../DAY_INDEX.md"
        if previous == 0
        else f"../{DAY_DIRS[previous]}/{DAY_DIRS[previous]}.md"
    )
    next_link = f"../{DAY_DIRS[next_day]}/{DAY_DIRS[next_day]}.md"
    lines = [
        f"# Day {lesson.day}: {lesson.title}",
        "",
        f"[← Day {previous if previous else 'Index'}]({previous_link}) · [Day index](../DAY_INDEX.md) · [Day {next_day} →]({next_link})",
        "",
        "## Table of Contents",
        "",
        "- [Why this lesson exists](#why-this-lesson-exists)",
        "- [Prerequisites](#prerequisites)",
        "- [Outcomes](#outcomes)",
        "- [The problem](#the-problem)",
        "- [Security boundary](#security-boundary)",
        "- [Lesson](#lesson)",
        "- [Vocabulary](#vocabulary)",
        "- [Worked examples](#worked-examples)",
        "- [Execution trace](#execution-trace)",
        "- [Common mistakes](#common-mistakes)",
        "- [Security application](#security-application)",
        "- [Exercises](#exercises)",
        "- [Finish line](#finish-line)",
        "",
        "## Why this lesson exists",
        "",
        lesson.why,
        "",
        "## Prerequisites",
        "",
        lesson.prerequisites,
        "",
        "## Outcomes",
        "",
        "By the end of this lesson, you can:",
        "",
        lesson.outcomes,
        "",
        "## The problem",
        "",
        lesson.problem,
        "",
        "## Security boundary",
        "",
        "Use only the repository, synthetic examples, and local fixtures. The examples do not authorize access to public systems, university systems, employer systems, or accounts that you do not own.",
        "",
        "## Lesson",
        "",
        "### Vocabulary",
        "",
        lesson.vocabulary,
        "",
        "## Worked examples",
        "",
    ]
    for index, (title, explanation, code, output) in enumerate(lesson.examples, 1):
        lines.extend(
            [
                f"### Example {index}: {title}",
                "",
                explanation,
                "",
                "```python",
                code,
                "```",
                "",
                "**What to observe:**",
                "",
                output,
                "",
            ]
        )
    lines.extend(
        [
            "## Execution trace",
            "",
            lesson.trace,
            "",
            "## Common mistakes",
            "",
            lesson.mistakes,
            "",
            "## Security application",
            "",
            lesson.security,
            "",
            "## Exercises",
            "",
            "Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Use the examples above as your starting point. Use [hints](practice/hints.md) only after a genuine attempt and [solutions](practice/solutions.md) only to compare your reasoning.",
            "",
            "## Finish line",
            "",
            f"Run `python -m course_days.day{lesson.day}`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.",
            "",
            "## Mental model",
            "",
            f"> {lesson.mental_model}",
            "",
            "## Limitations",
            "",
            lesson.limitations,
            "",
            f"[← Day {previous if previous else 'Index'}]({previous_link}) · [Day index](../DAY_INDEX.md) · [Day {next_day} →]({next_link})",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    for lesson in LESSONS:
        directory = ROOT / lesson.directory
        path = directory / f"{lesson.directory}.md"
        path.write_text(render(lesson), encoding="utf-8")
    print("Authored dense teaching chapters for Days 11–20.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
