# Exercises: Day 12

1. Import one helper from the starter module and print its result. What code runs at import time?
2. Move a side-effecting print or file operation under `if __name__ == "__main__":`. What changes when another module imports it?
3. Create a small `parsers.py` module containing one parser and import it from `main.py`.
4. Which module owns the parsing decision, and which module owns the user-facing output? Explain the boundary.
5. Add a test that imports the helper without creating a file or contacting a service.
