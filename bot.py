from binance import Client
from binance.exceptions import BinanceAPIException
from logger import logger


class BasicBot:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)

        # Futures Testnet URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        logger.info("Connected to Binance Futures Testnet")

    def set_leverage(self, symbol, leverage=10):
        try:
            self.client.futures_change_leverage(
                symbol=symbol,
                leverage=leverage
            )
            logger.info(f"Leverage set to {leverage}x for {symbol}")
        except BinanceAPIException as e:
            logger.error(f"Failed to set leverage: {e}")

    def place_market_order(self, symbol, side, quantity):
        try:
            logger.info(f"Placing MARKET order | {side} {quantity} {symbol}")

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            logger.info(f"Order success: {order}")
            return order

        except BinanceAPIException as e:
            logger.error(f"API Error: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            logger.info(f"Placing LIMIT order | {side} {quantity} {symbol} @ {price}")

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            logger.info(f"Order success: {order}")
            return order

        except BinanceAPIException as e:
            logger.error(f"API Error: {e}")
            return None

    def place_stop_limit_order(self, symbol, side, quantity, price, stop_price):
        try:
            logger.info(
                f"Placing STOP-LIMIT order | {side} {quantity} {symbol} "
                f"@ {price} stop {stop_price}"
            )

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                quantity=quantity,
                price=price,
                stopPrice=stop_price,
                timeInForce="GTC"
            )

            logger.info(f"Order success: {order}")
            return order

        except BinanceAPIException as e:
            logger.error(f"API Error: {e}")
            return None
