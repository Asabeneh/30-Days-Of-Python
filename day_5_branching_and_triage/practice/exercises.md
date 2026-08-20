# Exercises: Day 5

1. Run the classifier with the normal and urgent examples. What label and reason does each return?
2. Write a table with the expected result for severities `0`, `4`, `5`, `9`, and `10` when the event is authenticated and when it is not.
3. Implement or extend `classify(severity, authenticated)` so that an unauthenticated high-severity event is not silently treated as safe.
4. Add a test for severity `5` and severity `9`. What evidence proves the boundary behavior?
5. Write one sentence distinguishing the observation “the event matched a rule” from the inference “an attack occurred.”
