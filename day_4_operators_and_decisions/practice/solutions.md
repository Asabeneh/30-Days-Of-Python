# Solutions: Day 4 Operators, Comparisons, and Decisions

Use these only after making a genuine attempt. The important part is being able to explain why the answer works, not merely copying the final line.

1. Example answers are `7 + 2 == 9`, `7 - 2 == 5`, `7 * 2 == 14`, and `7 / 2 == 3.5`. The division result is a `float`.
2. `17 // 5` is `3` complete groups. `17 % 5` is `2` leftover records.
3. `processed = 0; processed += 1; processed += 1; processed += 1` leaves `processed == 3`.
4. `compare_scores = new_score > previous_best`; the assertion passes because `95 > 88` is `True`.
5. For `6`, both `> 7` and `>= 7` are false. For `7`, `> 7` is false but `>= 7` is true. For `8`, both are true. This demonstrates why boundary values matter.
6. `meets_requirements = (experience >= 3) and (score >= 85)`.
7. `is_auth_event = event_name == "login_failed" or event_name == "access_denied"`. Parentheses can make the two comparisons easier to read.
8. `has_source = not source_is_missing`.
9. `known_events = {"login_failed", "access_denied"}` followed by `is_known = event_name in known_events`.
10. `"same" == "same"` asks whether the contents are equal. `confidence is None` asks whether the value is the singleton used for missing data. Do not use `is` as a general replacement for `==`.
11. `10 + 2 * 3` is `16` because multiplication happens first. `(10 + 2) * 3` is `36` because the parentheses force addition first.
12. A repaired rule is `needs_review = (severity >= 7) and (source != "") and (event_name in known_events)`. The exact expression should follow the written policy.
13. A safe loop can produce `record_number=1 label=review` without printing the raw record. The label depends on the rule and fixture values taught in the lesson.
14. A useful test table is `6 -> False`, `7 -> True`, and `8 -> True` for `severity >= 7`.
15. A Boolean expression is only a calculation over supplied values. It does not grant permission, authenticate a source, identify an attacker, or authorize network activity.

If your answers differ from these, compare the policy sentence, input values, operator, and output separately. A different implementation can be correct when it satisfies the same contract and remains readable.
