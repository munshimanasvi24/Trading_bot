import os
from dotenv import load_dotenv
from bot import BasicBot

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")


def main():
    bot = BasicBot(API_KEY, API_SECRET)

    symbol = input("Symbol (e.g. BTCUSDT): ").upper()
    side = input("Side (BUY / SELL): ").upper()
    order_type = input("Order type (MARKET / LIMIT / STOP): ").upper()
    quantity = float(input("Quantity: "))

    bot.set_leverage(symbol, leverage=10)

    if order_type == "MARKET":
        bot.place_market_order(symbol, side, quantity)

    elif order_type == "LIMIT":
        price = float(input("Limit Price: "))
        bot.place_limit_order(symbol, side, quantity, price)

    elif order_type == "STOP":
        price = float(input("Limit Price: "))
        stop_price = float(input("Stop Price: "))
        bot.place_stop_limit_order(symbol, side, quantity, price, stop_price)

    else:
        print("Invalid order type")


if __name__ == "__main__":
    main()
