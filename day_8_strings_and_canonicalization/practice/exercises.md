# Exercises: Day 8

1. Run `normalize_username("  Admin ")`. What is returned, and why is case normalization useful for comparison?
2. Write `normalize_indicator(text)` that strips surrounding whitespace and lowercases a domain-like fixture.
3. Test an empty string, a string containing only spaces, and a mixed-case value. Which inputs should be rejected or accepted?
4. Preserve the raw value next to the normalized value in a dictionary. What information would be lost if you stored only the normalized value?
5. Add one Unicode or punctuation edge case and explain whether your normalization rule is sufficient.
