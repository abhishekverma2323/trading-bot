from binance.client import Client
import os
from dotenv import load_dotenv
import time

load_dotenv()

def get_client():
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    client = Client(api_key, api_secret)

    # Force Binance Futures Testnet URL
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    server_time = client.get_server_time()
    system_time = int(time.time() * 1000)
    offset = server_time['serverTime'] - system_time

    client.timestamp_offset = offset

    return client