# Exercises: Day 3

1. Run the starter with a valid status such as `200`. What type does the parser return?
2. Which inputs should be rejected: `"200"`, `"two hundred"`, `"-1"`, or `"999"`? Explain each answer before running the tests.
3. Write `parse_port(text)` that returns an integer only when the value is between `1` and `65535`; otherwise raise `ValueError`.
4. Test `parse_port("443")`, `parse_port("0")`, and `parse_port("not-a-port")`. What output or exception should each case produce?
5. Explain why validation at the input boundary is safer than letting malformed data reach a later security decision.

6. Apply the lesson to the supplied local synthetic fixture and state the expected artifact before running it.
7. Add a normal case and predict the result before executing the code.
8. Add a boundary case and explain the chosen behavior.
9. Add an invalid case and keep the failure visible and understandable.
10. Reproduce the deliberate mistake from the lesson and record the smallest repair.
11. Add a focused test or evidence note for the most important behavior.
12. Write one limitation and one review question for a teammate.

Use only the supplied local, synthetic, bounded fixtures. Do not use real credentials, private data, public targets, or systems outside explicit authorization.
