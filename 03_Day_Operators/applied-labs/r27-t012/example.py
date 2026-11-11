"""Calculate a currency discount using Decimal arithmetic."""

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from typing import Union

CENT = Decimal("0.01")
HUNDRED = Decimal("100")


def _decimal_input(value: Union[str, Decimal], name: str) -> Decimal:
    if isinstance(value, Decimal):
        number = value
    elif isinstance(value, str):
        if not value.strip():
            raise ValueError(f"{name} must not be empty")
        try:
            number = Decimal(value.strip())
        except InvalidOperation as error:
            raise ValueError(f"{name} must be a valid decimal number") from error
    else:
        raise TypeError(f"{name} must be a string or Decimal")

    if not number.is_finite():
        raise ValueError(f"{name} must be finite")
    return number


def calculate_discount(
    amount: Union[str, Decimal], percentage: Union[str, Decimal]
) -> Decimal:
    """Return the post-discount amount, rounded half-up to the nearest cent."""
    currency_amount = _decimal_input(amount, "amount")
    discount_percentage = _decimal_input(percentage, "percentage")

    # The valid percentage boundary is inclusive: 0 <= percentage <= 100.
    if not Decimal("0") <= discount_percentage <= HUNDRED:
        raise ValueError("percentage must be between 0 and 100 inclusive")

    discounted_amount = currency_amount * (HUNDRED - discount_percentage) / HUNDRED
    return discounted_amount.quantize(CENT, rounding=ROUND_HALF_UP)


if __name__ == "__main__":
    print(calculate_discount("100.00", "15"))
