# Exercises: Day 20

1. Run the log-triage starter against the supplied synthetic fixture. What is the first observation and what is the final classification?
2. Draw or write the data flow: path validation → bounded read → parsing → classification → report.
3. Add one malformed line. Does the CLI preserve the raw line and continue, or does it stop? Make the behavior explicit.
4. Add a test for a path outside the fixture directory and a test for the maximum line limit.
5. Write a README paragraph naming the tool's scope, what it can conclude, and what it cannot conclude.
