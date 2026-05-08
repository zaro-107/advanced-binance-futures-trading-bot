from bot.api.client import BinanceFuturesClient
from bot.core.logger import trade_logger

client = BinanceFuturesClient()

class OrderExecutor:

    @staticmethod
    def execute(payload):

        trade_logger.info(
            f"Executing Order: {payload}"
        )

        response = client.create_order(payload)

        trade_logger.info(
            f"Execution Response: {response}"
        )

        return response