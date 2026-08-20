# Exercises: Day 14

1. Create a temporary `evidence` directory and call `safe_path(base, "case.txt")`. Which path is returned?
2. What should happen for `safe_path(base, "../secret.txt")`? Test the rejection.
3. Add a fixture file and read it with an explicit UTF-8 encoding and a context manager.
4. Add a maximum file-size check before reading. What should happen when the file exceeds the limit?
5. Explain why comparing resolved paths is safer than checking whether the input string contains `..`.
