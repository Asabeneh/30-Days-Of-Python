# Exercises: Day 26

1. Run `redact` on an event containing `actor` and `token`. Which value changes?
2. Add `password`, `secret`, and `api_key` to the sensitive-key policy. What output should each produce?
3. Test nested data or explain why the current function does not redact nested secrets.
4. Add a newline-neutralization rule for human-readable log messages.
5. Write a logging policy that says what the tool records, what it redacts, and who may access the log.

6. Apply the lesson to the supplied local synthetic fixture and state the expected artifact before running it.
7. Add a normal case and predict the result before executing the code.
8. Add a boundary case and explain the chosen behavior.
9. Add an invalid case and keep the failure visible and understandable.
10. Reproduce the deliberate mistake from the lesson and record the smallest repair.
11. Add a focused test or evidence note for the most important behavior.
12. Write one limitation and one review question for a teammate.

Use only the supplied local, synthetic, bounded fixtures. Do not use real credentials, private data, public targets, or systems outside explicit authorization.
