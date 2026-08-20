# Hints: Day 4 Operators, Comparisons, and Decisions

Use one question at a time. Write your prediction before running the code. If an error appears, read the last line first; it usually names the kind of problem Python found.

1. Put the two operands on either side of each arithmetic operator. Print each expression separately.
2. `//` counts complete groups. `%` reports what is left after those groups.
3. Initialize `processed` to zero. Each `+= 1` changes the stored value and can be traced on paper.
4. Store the result of `new_score > previous_best` in the exact name requested, then use `assert` to check it.
5. Print the value and both comparisons on the same line. Pay special attention to `7`.
6. Write the two comparisons in parentheses and connect them with `and`.
7. Compare the event name with the first allowed string, then use `or` for the second allowed string. A local set plus `in` is another clear option.
8. If `source_is_missing` is `False`, then `not source_is_missing` is `True`.
9. Create a set such as `{"login_failed", "access_denied"}` and ask whether the event is `in` it.
10. `==` asks whether contents are equal. `is` asks whether two names refer to the same object. `is None` is the common missing-value check.
11. Run both expressions. Parentheses force addition to happen before multiplication.
12. Translate the policy into English first. The word “and” requires `and`; the phrase “one of these alternatives” often requires `or`.
13. Keep the output to a record number and label. Do not print the full dictionary.
14. A boundary test includes the value just below the boundary, the boundary itself, and the value just above it.
15. A Python expression only processes values already supplied to the program. Authorization and scope come from people, policies, and system controls, not from syntax.
