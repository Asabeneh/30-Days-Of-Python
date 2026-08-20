# Exercise Redesign Notes

## What the original course actually does

The original 30 Days of Python material places an `Exercises: Day N` section at the end of each day. Exercises are numbered learner questions and coding tasks, not abstract prompts. They commonly begin with a direct verification task such as opening the Python shell and trying the examples from the section, then ask the learner to write or transform concrete values, inspect data, or build a small result.

The original questions use ordinary numbered Markdown lists, often with several related items in one sequence. Data-heavy days ask direct operations such as reading a CSV, getting the first and last rows, selecting a column, counting rows and columns, filtering values, and exploring the data. The learner is expected to perform the action and observe the result. The exercise section is part of the lesson flow rather than a separate prompt-card abstraction.

## What the redesign should preserve

Each lesson should end with `## Exercises` followed by explicit numbered questions. Questions should use the exact concept taught that day, require a runnable answer, and include enough input or fixture information to begin without guessing. A good day can include a short “check your understanding” group, a practical Python task, a cybersecurity application task using synthetic or local data, and a challenge task. The exercise should state what the learner should print, return, save, or test when an output matters.

Hints and solutions may remain separate, but they should answer the numbered questions in order. The learner should not have to translate “build a utility” into an assignment before starting. The course should preserve safety wording for security exercises without replacing the exercise with a vague prompt.

## What should be removed

Replace headings such as `Level 1 — Mechanical`, `Level 2 — Applied`, `Level 3 — Synthesis`, and generic `prompts.md` wording. Those labels can be used internally for difficulty mapping, but the learner-facing practice should read like the original course: “1. Do …”, “2. Write …”, “3. What is …?”, and “4. Build …”.
