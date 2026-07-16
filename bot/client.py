from binance.client import Client
from dotenv import load_dotenv
from bot.logging_config import logger
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


def get_client():
    try:
        client = Client(
            api_key=API_KEY,
            api_secret=API_SECRET,
            testnet=True
        )

        logger.info("Connected to Binance Futures Testnet")
        return client

    except Exception as e:
        logger.error(f"Connection Error: {e}")
        raise