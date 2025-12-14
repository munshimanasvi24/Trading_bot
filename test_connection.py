import os
from dotenv import load_dotenv
from binance import Client

load_dotenv()

print("API KEY:", os.getenv("BINANCE_API_KEY"))
print("API SECRET:", os.getenv("BINANCE_API_SECRET"))

client = Client(
    os.getenv("BINANCE_API_KEY"),
    os.getenv("BINANCE_API_SECRET"),
    testnet=True
)

client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

account = client.futures_account()
print("Connected. Available balance:", account["availableBalance"])
