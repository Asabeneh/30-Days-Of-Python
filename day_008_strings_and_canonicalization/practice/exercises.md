# Exercises: Day 8

1. Run `normalize_username("  Admin ")`. What is returned, and why is case normalization useful for comparison?
2. Write `normalize_indicator(text)` that strips surrounding whitespace and lowercases a domain-like fixture.
3. Test an empty string, a string containing only spaces, and a mixed-case value. Which inputs should be rejected or accepted?
4. Preserve the raw value next to the normalized value in a dictionary. What information would be lost if you stored only the normalized value?
5. Add one Unicode or punctuation edge case and explain whether your normalization rule is sufficient.

6. Apply the lesson to the supplied local synthetic fixture and state the expected artifact before running it.
7. Add a normal case and predict the result before executing the code.
8. Add a boundary case and explain the chosen behavior.
9. Add an invalid case and keep the failure visible and understandable.
10. Reproduce the deliberate mistake from the lesson and record the smallest repair.
11. Add a focused test or evidence note for the most important behavior.
12. Write one limitation and one review question for a teammate.

Use only the supplied local, synthetic, bounded fixtures. Do not use real credentials, private data, public targets, or systems outside explicit authorization.
