from binance.client import Client
from binance.exceptions import BinanceAPIException

from bot.core.config import settings
from bot.core.logger import api_logger

class BinanceFuturesClient:

    def __init__(self):

        self.client = Client(
            settings.API_KEY,
            settings.API_SECRET
        )

        self.client.FUTURES_URL = settings.BASE_URL

    def create_order(self, payload):

        try:

            api_logger.info(
                f"Sending Request: {payload}"
            )

            response = self.client.futures_create_order(
                **payload
            )

            api_logger.info(
                f"Response: {response}"
            )

            return response

        except BinanceAPIException as e:

            api_logger.error(
                f"Binance API Error: {e}"
            )

            raise

        except Exception as e:

            api_logger.error(
                f"Unexpected Error: {e}"
            )

            raise