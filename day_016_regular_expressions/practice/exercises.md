# Exercises: Day 16

1. Run the candidate extractor on `src=203.0.113.8`. What candidate is returned?
2. What happens when the text contains `999.1.1.1`? Does a shape match prove that the address is valid?
3. Write a second validation function that checks each octet is between `0` and `255`.
4. Test a valid documentation address, an invalid octet, and an address embedded inside a longer number.
5. Explain why extraction and validation should be separate functions.

6. Apply the lesson to the supplied local synthetic fixture and state the expected artifact before running it.
7. Add a normal case and predict the result before executing the code.
8. Add a boundary case and explain the chosen behavior.
9. Add an invalid case and keep the failure visible and understandable.
10. Reproduce the deliberate mistake from the lesson and record the smallest repair.
11. Add a focused test or evidence note for the most important behavior.
12. Write one limitation and one review question for a teammate.

Use only the supplied local, synthetic, bounded fixtures. Do not use real credentials, private data, public targets, or systems outside explicit authorization.
