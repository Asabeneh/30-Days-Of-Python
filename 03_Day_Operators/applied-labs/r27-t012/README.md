# Added activity: Decimal discount

Run `python3 example.py` to see `85.00` for an amount of `100.00` discounted by `15%`.

`calculate_discount(amount, percentage)` accepts decimal strings or `Decimal` values. Inputs must be non-empty, valid, finite decimal numbers. Percentage values are valid at the inclusive boundaries `0` and `100`; values below `0` or above `100` raise `ValueError`. The result is rounded to two decimal places using `ROUND_HALF_UP`.

Run the tests from the repository root:

```sh
python3 -m unittest discover -s 03_Day_Operators/applied-labs/r27-t012 -p "test_*.py"
```
