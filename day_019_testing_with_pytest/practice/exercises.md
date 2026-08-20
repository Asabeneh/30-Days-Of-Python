# Exercises: Day 19

1. Run the existing tests and identify one test that checks a rejection path.
2. Write a test for `parse_severity("11")`. What behavior is the test claiming?
3. Add a test for an empty evidence source and a test for a valid source with surrounding whitespace.
4. Intentionally break one boundary condition, run pytest, and read the failure before restoring the code.
5. Explain why a passing unit test is evidence for one claim, not proof that the whole tool is secure.

6. Apply the lesson to the supplied local synthetic fixture and state the expected artifact before running it.
7. Add a normal case and predict the result before executing the code.
8. Add a boundary case and explain the chosen behavior.
9. Add an invalid case and keep the failure visible and understandable.
10. Reproduce the deliberate mistake from the lesson and record the smallest repair.
11. Add a focused test or evidence note for the most important behavior.
12. Write one limitation and one review question for a teammate.

Use only the supplied local, synthetic, bounded fixtures. Do not use real credentials, private data, public targets, or systems outside explicit authorization.
