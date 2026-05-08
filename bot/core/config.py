from dotenv import load_dotenv
import os

load_dotenv()

class Settings:

    API_KEY = os.getenv("BINANCE_API_KEY")
    API_SECRET = os.getenv("BINANCE_SECRET_KEY")

    BASE_URL = "https://testnet.binancefuture.com/fapi"

settings = Settings()