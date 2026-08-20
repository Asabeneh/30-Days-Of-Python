# Exercises: Day 4

1. Evaluate `2 + 3 * 4` and `(2 + 3) * 4`. Which result demonstrates operator precedence?
2. Write a boolean expression that is true only when a severity is at least `7` and the event source is not empty.
3. Implement `should_review(severity, source)` and return `True` or `False` for three synthetic events.
4. Test the boundary values `6` and `7`. What changes at the boundary, and why should a security rule test both sides?
5. Add a case where the source is an empty string. Does your function review it? Document the decision in one sentence.

6. Apply the lesson to the supplied local synthetic fixture and state the expected artifact before running it.
7. Add a normal case and predict the result before executing the code.
8. Add a boundary case and explain the chosen behavior.
9. Add an invalid case and keep the failure visible and understandable.
10. Reproduce the deliberate mistake from the lesson and record the smallest repair.
11. Add a focused test or evidence note for the most important behavior.
12. Write one limitation and one review question for a teammate.

Use only the supplied local, synthetic, bounded fixtures. Do not use real credentials, private data, public targets, or systems outside explicit authorization.
