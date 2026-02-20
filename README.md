# Binance Futures Order Bot (CLI-Based)

##  Project Overview

A modular CLI-based trading bot for Binance USDT-M Futures designed with:

- Clean architecture
- Structured logging
- Input validation
- Simulation (Paper Trading) mode
- Advanced order extensibility

This project follows professional software design principles and supports scalable order execution logic.

---

##  Implemented Features

### 🔹 Core Orders (Completed)

✔ Market Orders  
✔ Limit Orders  

Both order types include:

- CLI argument parsing
- Strict input validation
- Structured logging (`bot.log`)
- Simulation mode execution
- Unique order IDs
- Timestamped order records

---

##  Architecture Design

srashti-binance-bot/
├── src/
│   ├── market_orders.py
│   ├── limit_orders.py
│   ├── config.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   ├── validator.py
│   │   └── client.py
│   │
│   └── advanced/
│       ├── __init__.py
│       ├── stop_limit.py
│       ├── oco.py
│       ├── twap.py
│       └── grid_strategy.py
│
├── bot.log
├── README.md
└── report.pdf


### 🔹 Design Principles Used

- Separation of concerns
- Modular utilities
- Reusable validation logic
- Config-driven execution mode
- Scalable advanced strategy folder

---

##  Simulation Mode (Paper Trading)

Due to regional restrictions on Futures API access, the bot currently runs in:


TEST_MODE = True


Simulation mode:

- Mimics Binance API response
- Generates unique order IDs
- Logs execution details
- Maintains realistic order structure

This allows safe testing without real capital.

---

## 📥 How To Run

### ▶ Market Order


python src/market_orders.py BTCUSDT BUY 0.01


### ▶ Limit Order


python src/limit_orders.py BTCUSDT BUY 0.01 65000


---

##  Logging System

All actions are logged in:


bot.log


Log format:


Timestamp | Log Level | Module | Message


Includes:

- Order placement
- Validation failures
- Execution status
- Error traces

---

## 🔒 Validation Features

The bot validates:

- Symbol format (e.g., BTCUSDT)
- Side (BUY / SELL)
- Quantity > 0
- Price > 0 (for limit orders)

Invalid inputs are rejected before execution.

---

## 🚀 Advanced Orders (In Progress)

The following advanced features are currently under development:

- Stop-Limit Orders
- OCO (One-Cancels-the-Other)
- TWAP Strategy
- Grid Trading Strategy

The architecture is already structured to support seamless integration of these modules.

---

## 🛠 Tech Stack

- Python 3
- python-binance
- Logging module
- CLI-based interface
- Modular architecture

---

## 📈 Future Enhancements

- Real Binance Futures API integration
- Risk management module
- Order history tracking
- Strategy backtesting framework

---

## 👩‍💻 Author

Srashti Chauhan  
B.Tech CSE  
Full Stack & AI Enthusiast  
