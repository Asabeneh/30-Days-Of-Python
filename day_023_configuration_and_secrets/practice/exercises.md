# Exercises: Day 23

1. Run `load_timeout()` with no environment variable. What default is used?
2. Set `APP_TIMEOUT=10` for one command and run the loader. What changes?
3. Test `APP_TIMEOUT=0`, `APP_TIMEOUT=61`, and `APP_TIMEOUT=not-a-number`. Which errors should appear?
4. Add a fake API key to a local environment variable and prove that your program never prints its value.
5. Explain why a secret should not be stored in source code, a README, or shell history.
