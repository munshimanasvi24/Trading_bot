# Binance Futures Testnet Trading Bot

## Overview
This project is a simplified crypto trading bot built in Python using the official Binance API.  
It places trades on the **Binance Futures Testnet (USDT-M)** and is designed to demonstrate API usage, order execution, logging, and error handling.

The bot accepts user input via the command line and supports multiple order types.

---

## Features
- Binance Futures Testnet (USDT-M)
- Market orders
- Limit orders
- Stop-Limit orders
- Buy and Sell support
- Command-line interface (CLI)
- Logging of API requests, responses, and errors
- Proper error handling using Binance exceptions

---

## Tech Stack
- Python
- python-binance
- Binance Futures REST API
- dotenv for environment variables

---

## Project Structure

trading_bot/
│
├── bot.py # Core trading logic
├── main.py # CLI entry point
├── logger.py # Logging configuration
├── test_connection.py # Testnet connection validation
├── requirements.txt # Dependencies
├── .env.example # Environment variable template
└── logs/
└── bot.log # Application logs


---

## Setup Instructions

### 1. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate

2. Install dependencies
pip install -r requirements.txt

3. Configure environment variables

Create a .env file in the project root using the format below:

BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_secret_key_here


Note: Use Binance Futures Testnet API credentials only.

Running the Bot

Start the bot using:

python main.py


Example input:

Symbol: BTCUSDT
Side: BUY
Order type: MARKET
Quantity: 0.002


The bot will place the order and display the execution result.

Logging

All application activity is logged to:

logs/bot.log


Logs include:

API connection status

Order placement requests

Successful responses

Error messages

Testnet Only

This project is strictly for Binance Futures Testnet.
No real funds are used.

Notes

Minimum order notional and margin requirements are enforced by Binance

Leverage is configurable within the bot

API keys should never be committed to source control


---

### What to do now
1. Create `README.md`
2. Paste this content
3. Save
4. Commit and push to GitHub

If you want, I can:
- review your GitHub structure
- help you choose which log lines to keep
- prepare interview questions based on this project

Just tell me.
