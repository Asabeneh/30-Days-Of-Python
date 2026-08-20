# Exercises: Day 24

1. Validate `{"severity": 5}`. What dictionary is returned?
2. Test missing severity, string severity, and a JSON list. Which inputs should be rejected?
3. Add a `source` field and require it to be non-empty text.
4. Store two validated synthetic records in SQLite using a parameterized statement. What query retrieves them?
5. Write one test that would fail if user input were concatenated into SQL.
