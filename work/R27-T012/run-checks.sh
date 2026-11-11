#!/bin/sh

set -u

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_root=$(git -C "$script_dir/../.." rev-parse --show-toplevel) || exit 1
report="$script_dir/results.txt"
test_status=0
example_status=0

cd "$repo_root" || exit 1
{
    printf 'Check: python3 -m unittest discover -s 03_Day_Operators/applied-labs/r27-t012 -p "test_*.py"\n'
    printf 'Python: '
    python3 --version
    printf 'Git: '
    git --version
    printf '\nInputs, expected results, and actual results:\n'
} > "$report"

python3 -m unittest discover -s 03_Day_Operators/applied-labs/r27-t012 -p "test_*.py" >> "$report" 2>&1 || test_status=$?
python3 - <<'PY' >> "$report" 2>&1 || example_status=$?
import sys
from decimal import Decimal

sys.path.insert(0, "03_Day_Operators/applied-labs/r27-t012")
from example import calculate_discount

cases = (
    ("100.00", "15", "85.00"),
    ("100.00", "0", "100.00"),
    ("100.00", "100", "0.00"),
    ("10.00", "33.333", "6.67"),
)
for amount, percentage, expected in cases:
    actual = calculate_discount(amount, percentage)
    print(
        f"amount={amount}, percentage={percentage}: "
        f"expected={Decimal(expected)}, actual={actual}"
    )
PY

cat "$report"
if [ "$test_status" -ne 0 ]; then
    exit "$test_status"
fi
exit "$example_status"
