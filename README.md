# Binance Futures Order Bot (CLI-Based)

## 📌 Project Overview

A modular CLI-based trading bot for Binance USDT-M Futures supporting:

- Core order types
- Advanced trading strategies
- Structured logging
- Strict input validation
- Simulation (Paper Trading) mode

The system follows clean architecture principles and is designed to be scalable, extensible, and production-ready.

---

## 🚀 Implemented Features

### 🔹 Core Orders

✔ Market Orders  
✔ Limit Orders  

Each core order includes:

- CLI argument parsing
- Strict input validation
- Structured logging (`bot.log`)
- Simulation mode execution
- Unique order IDs
- Timestamped execution records

---

### 🔹 Advanced Orders

✔ Stop-Limit Orders  
✔ OCO (One-Cancels-the-Other)  
✔ TWAP (Time-Weighted Average Price)  
✔ Grid Trading Strategy  

These strategies simulate realistic trading behavior and institutional-style execution logic.

---

## 🧠 Project Structure

- **src/** → Core application logic  
  - `market_orders.py` → Market order execution  
  - `limit_orders.py` → Limit order execution  
  - `config.py` → Global configuration (`TEST_MODE`)  

- **utils/** → Reusable components  
  - `logger.py` → Structured logging configuration  
  - `validator.py` → Input validation logic  
  - `client.py` → Binance client structure (ready for live integration)  

- **advanced/** → Strategy implementations  
  - `stop_limit.py`  
  - `oco.py`  
  - `twap.py`  
  - `grid_strategy.py`  

- `bot.log` → Execution logs  
- `report.pdf` → Detailed documentation  

---

## 🔐 Simulation Mode (Paper Trading)

Due to regional API restrictions, the system runs in:

`TEST_MODE = True`

Simulation mode:

- Mimics Binance Futures responses
- Generates realistic order IDs
- Simulates market price conditions
- Executes complete trading logic safely

The architecture supports seamless migration to live API mode.

---

## 📊 Order Logic Summary

### 🟢 Market Order
Executes immediately at current simulated market price.

### 🔵 Limit Order
Executes only when specified price is reached.

### 🟣 Stop-Limit
Triggers a limit order once the stop condition is satisfied.

### 🟠 OCO
Places Take-Profit and Stop-Loss simultaneously.  
If one executes → the other cancels automatically.

### 🟡 TWAP
Splits large orders into smaller slices executed over time to reduce market impact.

### 🔴 Grid Strategy
Divides a price range into equal intervals and places buy/sell orders across levels to profit from sideways market movement.

---

## ▶ How To Run

All commands should be executed from the project root directory:


C:\Projects\srashti-binance-bot


### 🔧 Prerequisites

- Python 3.x installed
- Virtual environment created
- Simulation mode enabled (`TEST_MODE = True`)

---

### ▶ Activate Virtual Environment (Windows)


venv\Scripts\activate


---

### 🟢 Market Order


python src/market_orders.py BTCUSDT BUY 0.01


---

### 🔵 Limit Order


python src/limit_orders.py BTCUSDT BUY 0.01 65000


---

### 🟣 Stop-Limit Order


python -m src.advanced.stop_limit BTCUSDT BUY 0.01 59000 58950


---

### 🟠 OCO Order


python -m src.advanced.oco BTCUSDT BUY 0.01 60500 59000


---

### 🟡 TWAP Strategy


python -m src.advanced.twap BTCUSDT BUY 1 5 1


---

### 🔴 Grid Strategy


python -m src.advanced.grid_strategy BTCUSDT 58000 62000 4 0.01


---

## 📁 Logging System

All actions are recorded in `bot.log`.

Logs include:

- Order placement
- Trigger conditions
- Strategy execution
- Validation failures
- Error traces

Log Format:

Timestamp | Log Level | Module | Message

---

## 🔒 Input Validation

The bot validates:

- Symbol format (e.g., BTCUSDT)
- Order side (BUY / SELL)
- Quantity > 0
- Price > 0
- Logical price ranges

Invalid inputs are rejected before execution.

---

## 🏗 Design Principles Used

- Separation of concerns
- Modular utilities
- Absolute imports
- Config-driven execution
- Strategy-based abstraction
- Scalable folder structure

---

## 📈 Future Enhancements

- Live Binance Futures API integration
- Position tracking module
- Risk management automation
- Strategy performance metrics
- Backtesting framework

---

## 👩‍💻 Author

Srashti Chauhan  
B.Tech CSE  
Full Stack & AI Enthusiast  