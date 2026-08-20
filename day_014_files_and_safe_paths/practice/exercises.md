# Exercises: Day 14

1. Create a temporary `evidence` directory and call `safe_path(base, "case.txt")`. Which path is returned?
2. What should happen for `safe_path(base, "../secret.txt")`? Test the rejection.
3. Add a fixture file and read it with an explicit UTF-8 encoding and a context manager.
4. Add a maximum file-size check before reading. What should happen when the file exceeds the limit?
5. Explain why comparing resolved paths is safer than checking whether the input string contains `..`.

6. Apply the lesson to the supplied local synthetic fixture and state the expected artifact before running it.
7. Add a normal case and predict the result before executing the code.
8. Add a boundary case and explain the chosen behavior.
9. Add an invalid case and keep the failure visible and understandable.
10. Reproduce the deliberate mistake from the lesson and record the smallest repair.
11. Add a focused test or evidence note for the most important behavior.
12. Write one limitation and one review question for a teammate.

Use only the supplied local, synthetic, bounded fixtures. Do not use real credentials, private data, public targets, or systems outside explicit authorization.
