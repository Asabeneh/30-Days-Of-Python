# Contributing

Thank you for helping improve the course. Contributions should make the material clearer for a complete beginner while preserving technical accuracy, safe scope, and reproducibility.

## Before opening a change

Read [COURSE_QUALITY_STANDARD.md](COURSE_QUALITY_STANDARD.md) and [SAFETY_AND_LAB_RULES.md](SAFETY_AND_LAB_RULES.md). Check whether the lesson already has a starter, tests, practice prompts, hints, solutions, and a lab scope. Small, focused changes are easier to review than a large rewrite.

## For lesson changes

State the learner problem, prerequisites, outcomes, expected commands, and finish line. Include a runnable example and at least one negative or edge case. Security-heavy changes must state authorization, scope, fixture, evidence, and cleanup. Do not embed secrets, private data, destructive payloads, or instructions for testing unapproved systems.

## Checks before review

```text
ruff format .
ruff check .
python -m compileall -q course_days scripts
python -m pytest -q
python scripts/course_doctor.py --strict
```

If a check cannot run on your machine, record the command and the exact error in the pull request. Do not hide a failing check by deleting the test.

## Writing and accessibility

Use plain language before jargon, meaningful headings, short code examples, descriptive link text, and alt text for diagrams. Do not use color alone to communicate a security state. Keep the main learning path in English until a deliberate translation workflow is approved.
