# Applied lab: text statistics

This added activity packages a small function that counts whitespace-separated
words and distinct words. Tokens are compared exactly, including their case.
The only runtime dependencies are Python's standard library
(`dependencies = []` in `pyproject.toml`).

For a clean environment, run these commands from this directory:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install --no-deps .
.venv/bin/python -I -c "from example import text_statistics; print(text_statistics('one two two'))"
.venv/bin/python -m unittest discover -s . -p "test_*.py"
```

The isolated import prints
`{'word_count': 3, 'distinct_word_count': 2}`. `-I` excludes user-site
packages and the current directory from the import path, so this command
checks the installed module.

From the repository root, the test suite can also be run with:

```sh
python3 -m unittest discover -s 20_Day_Python_package_manager/applied-labs/r27-t011 -p "test_*.py"
```

The fixture input is `"one two two"`; its expected word count is `3` and its
expected distinct-word count is `2`.
