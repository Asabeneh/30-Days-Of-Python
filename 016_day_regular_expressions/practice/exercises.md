# Exercises: Day 16

1. Run the candidate extractor on `src=203.0.113.8`. What candidate is returned?
2. What happens when the text contains `999.1.1.1`? Does a shape match prove that the address is valid?
3. Write a second validation function that checks each octet is between `0` and `255`.
4. Test a valid documentation address, an invalid octet, and an address embedded inside a longer number.
5. Explain why extraction and validation should be separate functions.
