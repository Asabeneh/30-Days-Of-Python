# Exercises: Day 20

1. Run the log-triage starter against the supplied synthetic fixture. What is the first observation and what is the final classification?
2. Draw or write the data flow: path validation → bounded read → parsing → classification → report.
3. Add one malformed line. Does the CLI preserve the raw line and continue, or does it stop? Make the behavior explicit.
4. Add a test for a path outside the fixture directory and a test for the maximum line limit.
5. Write a README paragraph naming the tool's scope, what it can conclude, and what it cannot conclude.

6. Apply the lesson to the supplied local synthetic fixture and state the expected artifact before running it.
7. Add a normal case and predict the result before executing the code.
8. Add a boundary case and explain the chosen behavior.
9. Add an invalid case and keep the failure visible and understandable.
10. Reproduce the deliberate mistake from the lesson and record the smallest repair.
11. Add a focused test or evidence note for the most important behavior.
12. Write one limitation and one review question for a teammate.

Use only the supplied local, synthetic, bounded fixtures. Do not use real credentials, private data, public targets, or systems outside explicit authorization.
