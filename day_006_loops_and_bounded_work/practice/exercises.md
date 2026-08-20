# Exercises: Day 6

1. Run the bounded matching example with a limit of `2`. How many records are returned?
2. Why is an explicit limit important when input could be much larger than the example fixture?
3. Write `first_matches(lines, needle, limit)` and return no more than `limit` matching lines.
4. Test an empty list, a limit of `0`, and three matching lines with a limit of `2`. What should each case return?
5. Add a test that proves the function does not read beyond the requested bound. State the resource assumption in the test comment.
