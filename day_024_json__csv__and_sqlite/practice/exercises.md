# Exercises: Day 24

1. Validate `{"severity": 5}`. What dictionary is returned?
2. Test missing severity, string severity, and a JSON list. Which inputs should be rejected?
3. Add a `source` field and require it to be non-empty text.
4. Store two validated synthetic records in SQLite using a parameterized statement. What query retrieves them?
5. Write one test that would fail if user input were concatenated into SQL.

6. Apply the lesson to the supplied local synthetic fixture and state the expected artifact before running it.
7. Add a normal case and predict the result before executing the code.
8. Add a boundary case and explain the chosen behavior.
9. Add an invalid case and keep the failure visible and understandable.
10. Reproduce the deliberate mistake from the lesson and record the smallest repair.
11. Add a focused test or evidence note for the most important behavior.
12. Write one limitation and one review question for a teammate.

Use only the supplied local, synthetic, bounded fixtures. Do not use real credentials, private data, public targets, or systems outside explicit authorization.
