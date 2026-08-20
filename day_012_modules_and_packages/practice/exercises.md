# Exercises: Day 12

1. Import one helper from the starter module and print its result. What code runs at import time?
2. Move a side-effecting print or file operation under `if __name__ == "__main__":`. What changes when another module imports it?
3. Create a small `parsers.py` module containing one parser and import it from `main.py`.
4. Which module owns the parsing decision, and which module owns the user-facing output? Explain the boundary.
5. Add a test that imports the helper without creating a file or contacting a service.

6. Apply the lesson to the supplied local synthetic fixture and state the expected artifact before running it.
7. Add a normal case and predict the result before executing the code.
8. Add a boundary case and explain the chosen behavior.
9. Add an invalid case and keep the failure visible and understandable.
10. Reproduce the deliberate mistake from the lesson and record the smallest repair.
11. Add a focused test or evidence note for the most important behavior.
12. Write one limitation and one review question for a teammate.

Use only the supplied local, synthetic, bounded fixtures. Do not use real credentials, private data, public targets, or systems outside explicit authorization.
