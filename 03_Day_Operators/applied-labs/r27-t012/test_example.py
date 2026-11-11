import unittest
from decimal import Decimal

from example import calculate_discount


class CalculateDiscountTests(unittest.TestCase):
    def test_expected_discount_results(self):
        cases = (
            ("100.00", "15", "85.00"),
            ("100.00", "0", "100.00"),
            ("100.00", "100", "0.00"),
            ("10.00", "33.333", "6.67"),
        )
        for amount, percentage, expected in cases:
            with self.subTest(amount=amount, percentage=percentage):
                self.assertEqual(
                    calculate_discount(amount, percentage),
                    Decimal(expected),
                )

    def test_percentages_outside_inclusive_boundaries_are_rejected(self):
        for percentage in ("-0.01", "100.01"):
            with self.subTest(percentage=percentage):
                with self.assertRaises(ValueError):
                    calculate_discount("100.00", percentage)

    def test_empty_and_invalid_inputs_are_rejected(self):
        invalid_inputs = (
            ("", "15"),
            ("100.00", " "),
            ("not-a-number", "15"),
            ("100.00", "NaN"),
        )
        for amount, percentage in invalid_inputs:
            with self.subTest(amount=amount, percentage=percentage):
                with self.assertRaises(ValueError):
                    calculate_discount(amount, percentage)


if __name__ == "__main__":
    unittest.main()
