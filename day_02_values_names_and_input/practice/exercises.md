# Exercises: Day 2 — Values, Names, Input, and Output

Read the lesson first. For prediction questions, write your prediction before running the program. If your prediction is wrong, that is useful evidence: write the rule you misunderstood and try again.

1. Create `practice/value_inventory.py` with one string, one integer, one float, and one Boolean. Print each value and its type name. Copy the exact output into your answer.
2. Write three assignment statements for `count`: first assign `0`, then add `1`, then add `1` again. Predict the final output before running the program. Explain why `count = count + 1` is valid Python.
3. Create a variable named `event_name` containing `"login_failed"`. Print it once by itself and once inside an f-string labelled `event=`. Explain the difference between the two lines.
4. Write a program containing `left = "7"` and `right = 1`. First try `left + right` and record the exception type. Then repair the program in two ways: one that produces the text `71`, and one that produces the number `8`.
5. Ask the user for a severity with `input()`. Print the value using `repr()` and its type name. Type `7`. Is the result an `int` or a `str`? Explain why.
6. Convert the input from Question 5 to an integer. Try the input `high`. Copy the useful error line and explain what “invalid literal” means in this situation.
7. Add a range check for 0 through 10. Test `0`, `10`, `-1`, and `11`. Record which inputs are accepted and which are rejected. Explain why testing only `7` would not be enough.
8. Write a one-line f-string containing `case_id`, `severity`, and `review_required`. Change only the values, run the file again, and explain which parts of the output changed.
9. Create a synthetic record with `source`, `severity`, `authenticated`, and `token`. Print a safe summary that includes `token_present=True` or `False` but never prints the token value. Use a test or a captured-output check to prove that the token value is absent.
10. Write a program that asks for a maximum number of records. Convert the input to an integer and reject values less than 1 or greater than 100. Explain why a bound is safer than accepting any integer.
11. Make a deliberate mistake by printing a name before assigning it. Copy the exception type. Then assign the name before printing it and explain the repair.
12. Change a valid severity from the integer `7` to the string `"7"`. Make the program print both the representation and type. Explain why the output can look similar while the program’s future behavior is different.
13. Write a short paragraph answering this question: why is “the input looks like a number” not enough reason to trust it? Include conversion, range, and missing-input concerns.
14. In your own words, define value, type, name, assignment, input, and output. Give one Python example for each word and one cybersecurity example where confusing the word could cause a problem.
15. Safety question: list three kinds of information that must not be entered into today’s files and explain why local synthetic fixtures are used instead.

Use only this repository and synthetic text. Do not enter a real password, private log, API key, or public target.
