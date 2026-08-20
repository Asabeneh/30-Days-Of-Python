# Exercises: Day 6

1. Run the bounded matching example with a limit of `2`. How many records are returned?
2. Why is an explicit limit important when input could be much larger than the example fixture?
3. Write `first_matches(lines, needle, limit)` and return no more than `limit` matching lines.
4. Test an empty list, a limit of `0`, and three matching lines with a limit of `2`. What should each case return?
5. Add a test that proves the function does not read beyond the requested bound. State the resource assumption in the test comment.

6. Apply the lesson to the supplied local synthetic fixture and state the expected artifact before running it.
7. Add a normal case and predict the result before executing the code.
8. Add a boundary case and explain the chosen behavior.
9. Add an invalid case and keep the failure visible and understandable.
10. Reproduce the deliberate mistake from the lesson and record the smallest repair.
11. Add a focused test or evidence note for the most important behavior.
12. Write one limitation and one review question for a teammate.

Use only the supplied local, synthetic, bounded fixtures. Do not use real credentials, private data, public targets, or systems outside explicit authorization.
