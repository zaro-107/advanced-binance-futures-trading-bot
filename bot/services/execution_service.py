from bot.validation.validators import validate_order
from bot.trading.risk_manager import check_risk
from bot.trading.orders import OrderExecutor

class ExecutionService:

    @staticmethod
    def place_trade(
        symbol,
        side,
        order_type,
        quantity,
        price=None,
        stop_price=None
    ):

        validate_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
            stop_price=stop_price
        )

        check_risk(
            quantity=quantity,
            price=price or 0
        )

        payload = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity,
        }

        if order_type.upper() == "LIMIT":

            payload["price"] = price
            payload["timeInForce"] = "GTC"

        if order_type.upper() == "STOP_MARKET":

            payload["stopPrice"] = stop_price

        return OrderExecutor.execute(payload)