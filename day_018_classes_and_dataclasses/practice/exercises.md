# Exercises: Day 18

1. Create a `Finding` with a title, severity, and evidence identifier. What representation does the dataclass print?
2. Try to change the severity on a frozen finding. Which exception occurs?
3. Add validation so a finding rejects an empty title and a severity outside `0` through `10`.
4. Create two findings from synthetic evidence and sort them by severity without changing the original objects.
5. Explain why a model should distinguish an evidence identifier from raw private evidence.

6. Apply the lesson to the supplied local synthetic fixture and state the expected artifact before running it.
7. Add a normal case and predict the result before executing the code.
8. Add a boundary case and explain the chosen behavior.
9. Add an invalid case and keep the failure visible and understandable.
10. Reproduce the deliberate mistake from the lesson and record the smallest repair.
11. Add a focused test or evidence note for the most important behavior.
12. Write one limitation and one review question for a teammate.

Use only the supplied local, synthetic, bounded fixtures. Do not use real credentials, private data, public targets, or systems outside explicit authorization.
