# Exercises: Day 13

1. Run `parse_severity("7")`. What value and type are returned?
2. Trigger the malformed-input path with `"high"`. Which exception is raised and what context does its message provide?
3. Add a test for `"-1"` and `"11"`. Why are these different from a non-integer string even if all are rejected?
4. Write a caller that catches only the expected `ValueError` and prints a safe user-facing message without the raw input.
5. Explain why `except Exception: return None` could hide an evidence-collection failure.
