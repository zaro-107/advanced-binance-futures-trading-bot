from bot.api.exceptions import ValidationException

MAX_NOTIONAL_VALUE = 100000

def check_risk(quantity, price=0):

    notional = quantity * price

    if notional > MAX_NOTIONAL_VALUE:

        raise ValidationException(
            "Risk limit exceeded"
        )