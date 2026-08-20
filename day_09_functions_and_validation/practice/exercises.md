# Exercises: Day 9

1. Run the non-empty text check with `"event"`, `" "`, and `None`. What does each return?
2. Write `require_text(value, field_name)` that returns stripped text or raises `ValueError` with the field name.
3. Test a valid source, a blank source, and a non-string value. What exception message should a learner see?
4. Use the validator in a synthetic event parser. Which fields are required before classification?
5. Explain why a clear error is better than silently replacing missing evidence with a default value.
