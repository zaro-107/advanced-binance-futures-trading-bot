from bot.core.constants import (
    VALID_SIDES,
    VALID_ORDER_TYPES,
    MIN_QUANTITY,
    MAX_QUANTITY
)

from bot.api.exceptions import ValidationException

def validate_order(
    symbol,
    side,
    order_type,
    quantity,
    price=None,
    stop_price=None
):

    if not symbol.endswith("USDT"):
        raise ValidationException(
            "Only USDT pairs supported"
        )

    if side.upper() not in VALID_SIDES:
        raise ValidationException(
            "Side must be BUY or SELL"
        )

    if order_type.upper() not in VALID_ORDER_TYPES:
        raise ValidationException(
            "Invalid order type"
        )

    if quantity < MIN_QUANTITY:
        raise ValidationException(
            f"Minimum quantity is {MIN_QUANTITY}"
        )

    if quantity > MAX_QUANTITY:
        raise ValidationException(
            f"Maximum quantity is {MAX_QUANTITY}"
        )

    if order_type.upper() == "LIMIT":

        if price is None:
            raise ValidationException(
                "LIMIT order requires price"
            )

    if order_type.upper() == "STOP_MARKET":

        if stop_price is None:
            raise ValidationException(
                "STOP_MARKET requires stop_price"
            )