# Exercises: Day 23

1. Run `load_timeout()` with no environment variable. What default is used?
2. Set `APP_TIMEOUT=10` for one command and run the loader. What changes?
3. Test `APP_TIMEOUT=0`, `APP_TIMEOUT=61`, and `APP_TIMEOUT=not-a-number`. Which errors should appear?
4. Add a fake API key to a local environment variable and prove that your program never prints its value.
5. Explain why a secret should not be stored in source code, a README, or shell history.

6. Apply the lesson to the supplied local synthetic fixture and state the expected artifact before running it.
7. Add a normal case and predict the result before executing the code.
8. Add a boundary case and explain the chosen behavior.
9. Add an invalid case and keep the failure visible and understandable.
10. Reproduce the deliberate mistake from the lesson and record the smallest repair.
11. Add a focused test or evidence note for the most important behavior.
12. Write one limitation and one review question for a teammate.

Use only the supplied local, synthetic, bounded fixtures. Do not use real credentials, private data, public targets, or systems outside explicit authorization.
