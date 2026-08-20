# Exercises: Day 3

1. Run the starter with a valid status such as `200`. What type does the parser return?
2. Which inputs should be rejected: `"200"`, `"two hundred"`, `"-1"`, or `"999"`? Explain each answer before running the tests.
3. Write `parse_port(text)` that returns an integer only when the value is between `1` and `65535`; otherwise raise `ValueError`.
4. Test `parse_port("443")`, `parse_port("0")`, and `parse_port("not-a-port")`. What output or exception should each case produce?
5. Explain why validation at the input boundary is safer than letting malformed data reach a later security decision.
