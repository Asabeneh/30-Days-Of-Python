# Exercises: Day 5

1. Run the classifier with the normal and urgent examples. What label and reason does each return?
2. Write a table with the expected result for severities `0`, `4`, `5`, `9`, and `10` when the event is authenticated and when it is not.
3. Implement or extend `classify(severity, authenticated)` so that an unauthenticated high-severity event is not silently treated as safe.
4. Add a test for severity `5` and severity `9`. What evidence proves the boundary behavior?
5. Write one sentence distinguishing the observation “the event matched a rule” from the inference “an attack occurred.”

6. Apply the lesson to the supplied local synthetic fixture and state the expected artifact before running it.
7. Add a normal case and predict the result before executing the code.
8. Add a boundary case and explain the chosen behavior.
9. Add an invalid case and keep the failure visible and understandable.
10. Reproduce the deliberate mistake from the lesson and record the smallest repair.
11. Add a focused test or evidence note for the most important behavior.
12. Write one limitation and one review question for a teammate.

Use only the supplied local, synthetic, bounded fixtures. Do not use real credentials, private data, public targets, or systems outside explicit authorization.
