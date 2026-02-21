import os
from binance.client import Client
from dotenv import load_dotenv
from src.utils.logger import logger

load_dotenv()


def get_client():
    try:
        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")
        base_url = os.getenv("BASE_URL")

        client = Client(api_key, api_secret)

        logger.info("Binance Futures client initialized successfully.")
        return client

    except Exception as e:
        logger.error(f"Error initializing Binance client: {str(e)}")
        raise
