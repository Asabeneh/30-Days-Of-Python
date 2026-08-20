# Exercises: Day 9

1. Run the non-empty text check with `"event"`, `" "`, and `None`. What does each return?
2. Write `require_text(value, field_name)` that returns stripped text or raises `ValueError` with the field name.
3. Test a valid source, a blank source, and a non-string value. What exception message should a learner see?
4. Use the validator in a synthetic event parser. Which fields are required before classification?
5. Explain why a clear error is better than silently replacing missing evidence with a default value.

6. Apply the lesson to the supplied local synthetic fixture and state the expected artifact before running it.
7. Add a normal case and predict the result before executing the code.
8. Add a boundary case and explain the chosen behavior.
9. Add an invalid case and keep the failure visible and understandable.
10. Reproduce the deliberate mistake from the lesson and record the smallest repair.
11. Add a focused test or evidence note for the most important behavior.
12. Write one limitation and one review question for a teammate.

Use only the supplied local, synthetic, bounded fixtures. Do not use real credentials, private data, public targets, or systems outside explicit authorization.
