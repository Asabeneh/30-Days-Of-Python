"""Rewrite generic prompt cards as numbered, question-driven exercises."""

# ruff: noqa: E501
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SPECIFIC: dict[int, str] = {
    1: """# Exercises: Day 1

1. Run `python -m course_days.day001`. What text does the program print? Write the command you used and the final line of output.
2. Create `practice/hello_security.py` that prints your name, your course goal, and the sentence `Only authorized practice is safe practice.` What does each `print` call output?
3. Change one string in your program without changing its structure. Run it again. What changed, and what stayed the same?
4. Add a comment explaining why the course uses local, synthetic, bounded fixtures. Does the comment change the program output?
5. Add a test or a written check that confirms your program contains the authorization sentence. What would a learner need to see before calling Day 1 complete?

Use only this repository and synthetic text. Do not enter a real password, private log, or public target.
""",
    2: """# Exercises: Day 2

1. Run the starter and write down the value, type, and printed representation of each example.
2. What is the difference between a variable name and the value stored under that name? Explain using one string and one integer from the lesson.
3. Write a program that stores an event name, source label, and severity number, then prints one sentence containing all three values.
4. What happens when you concatenate a string and an integer without converting the integer? Trigger the error in a small file and name the exception.
5. Convert the severity to text safely and print `severity=<value>`. Add one synthetic event with severity `0` and one with severity `10`. What does each line show?
""",
    3: """# Exercises: Day 3

1. Run the starter with a valid status such as `200`. What type does the parser return?
2. Which inputs should be rejected: `"200"`, `"two hundred"`, `"-1"`, or `"999"`? Explain each answer before running the tests.
3. Write `parse_port(text)` that returns an integer only when the value is between `1` and `65535`; otherwise raise `ValueError`.
4. Test `parse_port("443")`, `parse_port("0")`, and `parse_port("not-a-port")`. What output or exception should each case produce?
5. Explain why validation at the input boundary is safer than letting malformed data reach a later security decision.
""",
    4: """# Exercises: Day 4

1. Evaluate `2 + 3 * 4` and `(2 + 3) * 4`. Which result demonstrates operator precedence?
2. Write a boolean expression that is true only when a severity is at least `7` and the event source is not empty.
3. Implement `should_review(severity, source)` and return `True` or `False` for three synthetic events.
4. Test the boundary values `6` and `7`. What changes at the boundary, and why should a security rule test both sides?
5. Add a case where the source is an empty string. Does your function review it? Document the decision in one sentence.
""",
    5: """# Exercises: Day 5

1. Run the classifier with the normal and urgent examples. What label and reason does each return?
2. Write a table with the expected result for severities `0`, `4`, `5`, `9`, and `10` when the event is authenticated and when it is not.
3. Implement or extend `classify(severity, authenticated)` so that an unauthenticated high-severity event is not silently treated as safe.
4. Add a test for severity `5` and severity `9`. What evidence proves the boundary behavior?
5. Write one sentence distinguishing the observation “the event matched a rule” from the inference “an attack occurred.”
""",
    6: """# Exercises: Day 6

1. Run the bounded matching example with a limit of `2`. How many records are returned?
2. Why is an explicit limit important when input could be much larger than the example fixture?
3. Write `first_matches(lines, needle, limit)` and return no more than `limit` matching lines.
4. Test an empty list, a limit of `0`, and three matching lines with a limit of `2`. What should each case return?
5. Add a test that proves the function does not read beyond the requested bound. State the resource assumption in the test comment.
""",
    7: """# Exercises: Day 7

1. Create a list of three synthetic indicators and print its first, last, and middle item.
2. What is the difference between `append`, `remove`, and slicing? Demonstrate each with non-sensitive fixture values.
3. Write `unique_indicators(values)` that preserves first-seen order while removing duplicates.
4. Test the function with repeated IP-like documentation addresses and an empty list. What should the results be?
5. Explain why retaining order and the original value can matter during evidence review.
""",
    8: """# Exercises: Day 8

1. Run `normalize_username("  Admin ")`. What is returned, and why is case normalization useful for comparison?
2. Write `normalize_indicator(text)` that strips surrounding whitespace and lowercases a domain-like fixture.
3. Test an empty string, a string containing only spaces, and a mixed-case value. Which inputs should be rejected or accepted?
4. Preserve the raw value next to the normalized value in a dictionary. What information would be lost if you stored only the normalized value?
5. Add one Unicode or punctuation edge case and explain whether your normalization rule is sufficient.
""",
    9: """# Exercises: Day 9

1. Run the non-empty text check with `"event"`, `" "`, and `None`. What does each return?
2. Write `require_text(value, field_name)` that returns stripped text or raises `ValueError` with the field name.
3. Test a valid source, a blank source, and a non-string value. What exception message should a learner see?
4. Use the validator in a synthetic event parser. Which fields are required before classification?
5. Explain why a clear error is better than silently replacing missing evidence with a default value.
""",
    10: """# Exercises: Day 10

1. Run the classifier with `(9, True)` and `(9, False)`. What label and explanation does each return?
2. Write three synthetic events and predict their classifications before running the starter.
3. Add a function that returns both a label and a human-readable reason. Why is the reason part of the evidence?
4. Write tests for a normal event, a high-severity authenticated event, and a high-severity unauthenticated event.
5. Which conclusion is outside the tool's authority: “this rule matched” or “this person committed an attack”? Explain.
""",
    11: """# Exercises: Day 11

1. Run `severity_label(8)` and record the returned string. What should `severity_label(6)` return?
2. What exception should be raised for `severity_label(-1)` and `severity_label(11)`? Test both values.
3. Write `label_event(event)` that reads an integer `severity` field and returns a label without printing or changing global state.
4. Add tests for missing severity, a string severity, and the boundary values `6` and `7`.
5. Write the function contract in three lines: accepted input, returned output, and rejected input.
""",
    12: """# Exercises: Day 12

1. Import one helper from the starter module and print its result. What code runs at import time?
2. Move a side-effecting print or file operation under `if __name__ == "__main__":`. What changes when another module imports it?
3. Create a small `parsers.py` module containing one parser and import it from `main.py`.
4. Which module owns the parsing decision, and which module owns the user-facing output? Explain the boundary.
5. Add a test that imports the helper without creating a file or contacting a service.
""",
    13: """# Exercises: Day 13

1. Run `parse_severity("7")`. What value and type are returned?
2. Trigger the malformed-input path with `"high"`. Which exception is raised and what context does its message provide?
3. Add a test for `"-1"` and `"11"`. Why are these different from a non-integer string even if all are rejected?
4. Write a caller that catches only the expected `ValueError` and prints a safe user-facing message without the raw input.
5. Explain why `except Exception: return None` could hide an evidence-collection failure.
""",
    14: """# Exercises: Day 14

1. Create a temporary `evidence` directory and call `safe_path(base, "case.txt")`. Which path is returned?
2. What should happen for `safe_path(base, "../secret.txt")`? Test the rejection.
3. Add a fixture file and read it with an explicit UTF-8 encoding and a context manager.
4. Add a maximum file-size check before reading. What should happen when the file exceeds the limit?
5. Explain why comparing resolved paths is safer than checking whether the input string contains `..`.
""",
    15: """# Exercises: Day 15

1. Convert `matching_lines(["ok", "login_failed", "ok"], "login")` to a list. What is returned?
2. What is the difference between a list and a generator in this example?
3. Write a generator that yields at most three matching synthetic log lines.
4. Test an exhausted iterator. What happens when you request another value after all lines are consumed?
5. Add a line-length guard and explain why lazy processing does not remove the need for resource limits.
""",
    16: """# Exercises: Day 16

1. Run the candidate extractor on `src=203.0.113.8`. What candidate is returned?
2. What happens when the text contains `999.1.1.1`? Does a shape match prove that the address is valid?
3. Write a second validation function that checks each octet is between `0` and `255`.
4. Test a valid documentation address, an invalid octet, and an address embedded inside a longer number.
5. Explain why extraction and validation should be separate functions.
""",
    17: """# Exercises: Day 17

1. Parse `2026-08-20T12:00:00Z`. What timezone does the returned value use?
2. What should happen when a timestamp has no timezone offset? Test the rejection.
3. Parse two timestamps with different offsets and sort them in UTC. Which event occurred first?
4. Preserve the original timestamp string beside the normalized datetime. Why is provenance useful?
5. List two reasons a sorted timeline might still be an incomplete incident explanation.
""",
    18: """# Exercises: Day 18

1. Create a `Finding` with a title, severity, and evidence identifier. What representation does the dataclass print?
2. Try to change the severity on a frozen finding. Which exception occurs?
3. Add validation so a finding rejects an empty title and a severity outside `0` through `10`.
4. Create two findings from synthetic evidence and sort them by severity without changing the original objects.
5. Explain why a model should distinguish an evidence identifier from raw private evidence.
""",
    19: """# Exercises: Day 19

1. Run the existing tests and identify one test that checks a rejection path.
2. Write a test for `parse_severity("11")`. What behavior is the test claiming?
3. Add a test for an empty evidence source and a test for a valid source with surrounding whitespace.
4. Intentionally break one boundary condition, run pytest, and read the failure before restoring the code.
5. Explain why a passing unit test is evidence for one claim, not proof that the whole tool is secure.
""",
    20: """# Exercises: Day 20

1. Run the log-triage starter against the supplied synthetic fixture. What is the first observation and what is the final classification?
2. Draw or write the data flow: path validation → bounded read → parsing → classification → report.
3. Add one malformed line. Does the CLI preserve the raw line and continue, or does it stop? Make the behavior explicit.
4. Add a test for a path outside the fixture directory and a test for the maximum line limit.
5. Write a README paragraph naming the tool's scope, what it can conclude, and what it cannot conclude.
""",
    21: """# Exercises: Day 21

1. Run the environment summary. Which interpreter, environment directory, and install command does the project expect?
2. Create a fresh `.venv` and verify it with `python -c "import sys; print(sys.executable)"`. What path is printed?
3. Install the development dependencies using the project instructions. Which command proves the selected interpreter owns the installation?
4. Deactivate the environment and compare the interpreter path. What changed?
5. Write a short recovery note for a learner whose terminal cannot find the activated interpreter.
""",
    22: """# Exercises: Day 22

1. Run the argument parser with no arguments. What default limit is produced?
2. Run it with `--limit 5`. What value and type are stored?
3. Add a rejection for `--limit 0` and for a non-integer value. What error should the CLI show?
4. Write a command that accepts a fixture path and a maximum number of lines without accepting a shell command.
5. State what exit status should indicate invalid user input.
""",
    23: """# Exercises: Day 23

1. Run `load_timeout()` with no environment variable. What default is used?
2. Set `APP_TIMEOUT=10` for one command and run the loader. What changes?
3. Test `APP_TIMEOUT=0`, `APP_TIMEOUT=61`, and `APP_TIMEOUT=not-a-number`. Which errors should appear?
4. Add a fake API key to a local environment variable and prove that your program never prints its value.
5. Explain why a secret should not be stored in source code, a README, or shell history.
""",
    24: """# Exercises: Day 24

1. Validate `{"severity": 5}`. What dictionary is returned?
2. Test missing severity, string severity, and a JSON list. Which inputs should be rejected?
3. Add a `source` field and require it to be non-empty text.
4. Store two validated synthetic records in SQLite using a parameterized statement. What query retrieves them?
5. Write one test that would fail if user input were concatenated into SQL.
""",
    25: """# Exercises: Day 25

1. Run `event_summary` with a valid typed event. What string is returned?
2. Which mistakes can a static type checker catch before runtime, and which malformed JSON values still require runtime validation?
3. Add a `TypedDict` for a finding with `title`, `severity`, and `evidence_id`.
4. Write one valid and one invalid fixture. Document which error is caught by the type checker and which is caught by a runtime test.
5. Explain why type hints improve review but do not authenticate data from outside the program.
""",
    26: """# Exercises: Day 26

1. Run `redact` on an event containing `actor` and `token`. Which value changes?
2. Add `password`, `secret`, and `api_key` to the sensitive-key policy. What output should each produce?
3. Test nested data or explain why the current function does not redact nested secrets.
4. Add a newline-neutralization rule for human-readable log messages.
5. Write a logging policy that says what the tool records, what it redacts, and who may access the log.
""",
    27: """# Exercises: Day 27

1. Run the review checklist. Which check would catch a whitespace-only diff?
2. Make a small change to a starter and inspect `git diff`. What changed and why?
3. Add a test for the changed behavior before committing it.
4. Write a review question for input validation, dependency changes, and security impact.
5. Explain why a clean commit history helps rollback and incident investigation.
""",
    28: """# Exercises: Day 28

1. Create a dependency record for `pytest`. What are its name, version, and purpose?
2. What should happen when one of the dependency fields is empty?
3. Inspect the project's declared development dependencies. Which are runtime dependencies and which are tools?
4. Write a small inventory table for the packages used by the course and include a reason for each package.
5. Explain why a package name alone does not prove provenance or safety.
""",
    29: """# Exercises: Day 29

1. Create a threat entry for a synthetic case record and a parser boundary.
2. Name one asset, one threat, one control, and one residual risk for the log-triage CLI.
3. Add a second threat involving malformed input. Which test provides evidence for the control?
4. Draw the trust boundary between a fixture file and a classification function.
5. Explain why “secure” is not a sufficient description of a control.
""",
    30: """# Exercises: Day 30

1. Create a `JournalEntry` for a synthetic event and print it.
2. Add a validator for timezone-aware timestamps, non-empty sources, and bounded raw text.
3. Write two JSON Lines entries and read them back without changing the raw observation.
4. Redact a synthetic token before writing a report. What should the report contain and what should it omit?
5. Write the project README sections: setup, data format, threat model, sample output, limitations, and reset procedure.
""",
}


def lesson_path(day: int) -> Path:
    matches = sorted(ROOT.glob(f"{day:03d}_day_*/{day:03d}_day_*.md"))
    if not matches:
        raise FileNotFoundError(f"missing lesson for day {day}")
    return matches[0]


def title_for(day: int) -> str:
    return (
        lesson_path(day).read_text(encoding="utf-8").splitlines()[0].removeprefix("# ")
    )


def generic_exercises(day: int) -> str:
    title = title_for(day)
    return f"""# Exercises: Day {day}\n\n1. Run the starter for **{title}** unchanged. What does it print or return? Record the command and output.\n2. Which input, state, or boundary does today's lesson ask you to observe? Answer in one sentence before changing the code.\n3. Write a small function, script, test, or report that applies today's concept to the supplied synthetic fixture. What file or output should it produce?\n4. Add one normal case, one boundary case, and one invalid case. What should happen in each case?\n5. Add a test or evidence note that proves the tool remains local, bounded, and explainable.\n6. What can your result show, and what can it not prove about a real system?\n\nUse only the supplied fixtures or a local resettable example. Do not use real credentials, private data, or systems outside explicit authorization.\n"""


def main() -> int:
    for day in range(1, 121):
        lesson = lesson_path(day)
        practice = lesson.parent / "practice"
        practice.mkdir(exist_ok=True)
        exercise_file = practice / "exercises.md"
        exercise_file.write_text(
            SPECIFIC.get(day, generic_exercises(day)), encoding="utf-8"
        )
        hints = practice / "hints.md"
        hints.write_text(
            "# Hints\n\nUse the exercise numbers in order. Start by running the starter. Name the input and expected output before writing code. Test a normal value, a boundary value, and an invalid value. Keep security work local, synthetic, bounded, and authorized.\n",
            encoding="utf-8",
        )
        solutions = practice / "solutions.md"
        solutions.write_text(
            "# Solution route\n\nUse the exercise numbers in order. Compare your implementation with the requested artifact and acceptance behavior. A strong solution explains its input contract, keeps failure visible, includes a negative test, and states a limitation.\n",
            encoding="utf-8",
        )
        text = lesson.read_text(encoding="utf-8")
        text = text.replace("practice/prompts.md", "practice/exercises.md")
        text = re.sub(r"\n## Practice\n", "\n## Exercises\n", text, count=1)
        text = text.replace(
            "Use [practice/exercises.md](practice/exercises.md), then",
            "Complete [practice/exercises.md](practice/exercises.md), then",
        )
        lesson.write_text(text, encoding="utf-8")
    for markdown in ROOT.rglob("*.md"):
        if ".git" in markdown.parts:
            continue
        text = markdown.read_text(encoding="utf-8")
        text = text.replace("practice/prompts.md", "practice/exercises.md")
        text = text.replace("generic prompt cards", "generic practice cards")
        markdown.write_text(text, encoding="utf-8")
    print("Rewrote 120 learner practice files as numbered exercises.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
