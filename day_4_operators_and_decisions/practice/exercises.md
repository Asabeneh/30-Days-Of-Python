# Day 4 Exercises: Python Operators, Comparisons, and Decisions

Work in a new file inside the repository. Before running each program, write down what you predict. Keep the fixtures synthetic and local.

1. Write one expression using `+`, one using `-`, one using `*`, and one using `/`. Predict and then print all four results.
2. Calculate `17 // 5` and `17 % 5`. Explain what each answer means in the language of complete groups and leftover records.
3. Start with `processed = 0` and use `+=` three times. Print the final value and explain each change.
4. Create variables `new_score = 95` and `previous_best = 88`. Store `new_score > previous_best` in `compare_scores` and assert that it is `True`.
5. Test the difference between `severity > 7` and `severity >= 7` for the values `6`, `7`, and `8`.
6. Create `meets_requirements` that is true only when experience is at least `3` and score is at least `85`.
7. Create `is_auth_event` that is true when an event is either `login_failed` or `access_denied`.
8. Use `not` to create `has_source` from a Boolean called `source_is_missing`.
9. Use `in` to check whether a synthetic event appears in a local set of two allowed event names.
10. Explain in your own words why `==` and `is` answer different questions. Demonstrate with `None` and two equal strings.
11. Evaluate `10 + 2 * 3` and `(10 + 2) * 3`. Explain why the answers differ.
12. Repair a broken triage expression that uses `or` when the written policy requires high severity, a non-empty source, and a known event.
13. Apply the Day 4 fixture rule and print only `record_number` and `label` for each record.
14. Add a boundary test for severity `6`, `7`, and `8`. Explain why the boundary test is more informative than testing only `10`.
15. Safety question: explain why a correct Boolean expression does not authorize scanning, connecting to, uploading to, or collecting data from a real system.
