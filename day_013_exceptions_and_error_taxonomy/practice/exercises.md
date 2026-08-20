# Exercises: Day 13

1. Run `parse_severity("7")`. What value and type are returned?
2. Trigger the malformed-input path with `"high"`. Which exception is raised and what context does its message provide?
3. Add a test for `"-1"` and `"11"`. Why are these different from a non-integer string even if all are rejected?
4. Write a caller that catches only the expected `ValueError` and prints a safe user-facing message without the raw input.
5. Explain why `except Exception: return None` could hide an evidence-collection failure.

6. Apply the lesson to the supplied local synthetic fixture and state the expected artifact before running it.
7. Add a normal case and predict the result before executing the code.
8. Add a boundary case and explain the chosen behavior.
9. Add an invalid case and keep the failure visible and understandable.
10. Reproduce the deliberate mistake from the lesson and record the smallest repair.
11. Add a focused test or evidence note for the most important behavior.
12. Write one limitation and one review question for a teammate.

Use only the supplied local, synthetic, bounded fixtures. Do not use real credentials, private data, public targets, or systems outside explicit authorization.
