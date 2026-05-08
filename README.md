# Advanced Binance Futures Testnet Trading Bot

A professional Python-based trading bot for Binance USDT-M Futures Testnet built with modular architecture, structured logging, validation, and CLI support.

---

# Features

- Place MARKET Orders
- Place LIMIT Orders
- Place STOP_MARKET Orders
- BUY / SELL support
- Binance Futures Testnet integration
- Modular architecture
- Structured logging system
- Risk management layer
- Input validation
- Rich CLI output
- Exception handling
- Scalable service-based design

---

# Tech Stack

- Python 3.x
- python-binance
- Typer
- Rich
- python-dotenv

---

# Project Structure

```text
binance_futures_bot/
│
├── bot/
│   ├── api/
│   ├── core/
│   ├── services/
│   ├── trading/
│   └── validation/
│
├── logs/
│
├── cli.py
├── requirements.txt
├── .env
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/zaro-107/advanced-binance-futures-trading-bot.git

cd advanced-binance-futures-trading-bot
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Binance Futures Testnet Setup

Create a Binance Futures Testnet account:

https://testnet.binancefuture.com

Generate:
- API Key
- Secret Key

---

# Environment Variables

Create a `.env` file in the project root.

```env
BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key
BASE_URL=https://testnet.binancefuture.com/fapi
```

---

# Usage

## MARKET BUY Order

```bash
python cli.py BTCUSDT BUY MARKET 0.0001
```

---

## LIMIT SELL Order

```bash
python cli.py BTCUSDT SELL LIMIT 0.0001 --price 150000
```

---

## STOP_MARKET Order

```bash
python cli.py BTCUSDT SELL STOP_MARKET 0.0001 --stop-price 95000
```

---

# Example Output

```text
Placing Order...

┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ Field        ┃ Value         ┃
┣━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━┫
┃ Order ID     ┃ 123456789     ┃
┃ Symbol       ┃ BTCUSDT       ┃
┃ Status       ┃ FILLED        ┃
┃ Executed Qty ┃ 0.0001        ┃
┃ Average Price┃ 104500        ┃
┗━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━┛

Order Successful
```

---

# Logging

Logs are automatically generated inside the `logs/` directory.

## Log Files

- `logs/trading.log`
- `logs/api.log`
- `logs/errors.log`

## Logged Information

- API requests
- API responses
- Errors and exceptions
- Order execution details

---

# Validation & Error Handling

The application validates:

- order side
- order type
- quantity limits
- symbol format
- required LIMIT order price
- required STOP_MARKET stop price

Handles:
- invalid user input
- Binance API errors
- network failures
- insufficient margin errors

---

# Risk Management

Includes a basic risk management layer:
- max quantity validation
- notional value checks

---

# Assumptions

- Only USDT futures pairs are supported
- Binance Futures Testnet environment is used
- User has valid API credentials
- User has sufficient testnet balance

---

# Future Improvements

Possible future enhancements:
- WebSocket market streaming
- Automated trading strategies
- Backtesting engine
- Telegram notifications
- Database integration
- Docker deployment
- FastAPI dashboard

---

# Author

Pradhuman Singh Shekhawat

---

# Disclaimer

This project is for educational and evaluation purposes only.

Do not use this code directly for live trading without proper testing and risk management.
