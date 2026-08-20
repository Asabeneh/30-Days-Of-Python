# Exercises: Day 11

1. Run `severity_label(8)` and record the returned string. What should `severity_label(6)` return?
2. What exception should be raised for `severity_label(-1)` and `severity_label(11)`? Test both values.
3. Write `label_event(event)` that reads an integer `severity` field and returns a label without printing or changing global state.
4. Add tests for missing severity, a string severity, and the boundary values `6` and `7`.
5. Write the function contract in three lines: accepted input, returned output, and rejected input.

6. Apply the lesson to the supplied local synthetic fixture and state the expected artifact before running it.
7. Add a normal case and predict the result before executing the code.
8. Add a boundary case and explain the chosen behavior.
9. Add an invalid case and keep the failure visible and understandable.
10. Reproduce the deliberate mistake from the lesson and record the smallest repair.
11. Add a focused test or evidence note for the most important behavior.
12. Write one limitation and one review question for a teammate.

Use only the supplied local, synthetic, bounded fixtures. Do not use real credentials, private data, public targets, or systems outside explicit authorization.
