# Binance Futures Testnet Trading Bot

A Python-based CLI trading bot that places Market and Limit orders on the Binance Futures Testnet using the Binance API.

## Features

- Place Market Orders
- Place Limit Orders
- Input Validation
- Logging Support
- Environment Variable Support (.env)
- Binance Futures Testnet Integration

## Project Structure

```
training-bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── cli.py
│
├── logs/
├── .env
├── requirements.txt
└── README.md
```

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
API_KEY=YOUR_API_KEY
API_SECRET=YOUR_API_SECRET
BASE_URL=https://testnet.binancefuture.com
```

## Usage

### Market Order

```bash
python -m bot.cli \
--symbol BTCUSDT \
--side BUY \
--type MARKET \
--quantity 0.001
```

### Limit Order

```bash
python -m bot.cli \
--symbol BTCUSDT \
--side BUY \
--type LIMIT \
--quantity 0.001 \
--price 60000
```

## Technologies Used

- Python
- Binance API
- python-binance
- python-dotenv

## Note

This project uses the Binance Futures Testnet for testing purposes only. No real funds are used.