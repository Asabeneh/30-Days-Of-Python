# Exercises: Day 18

1. Create a `Finding` with a title, severity, and evidence identifier. What representation does the dataclass print?
2. Try to change the severity on a frozen finding. Which exception occurs?
3. Add validation so a finding rejects an empty title and a severity outside `0` through `10`.
4. Create two findings from synthetic evidence and sort them by severity without changing the original objects.
5. Explain why a model should distinguish an evidence identifier from raw private evidence.
