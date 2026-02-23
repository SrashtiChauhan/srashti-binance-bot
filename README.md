# Binance Futures Trading Bot

### CLI + Web-Based Simulation Trading Engine

A modular **Binance USDT-M Futures Trading Bot** built using Python and Flask, supporting both:

* 🖥 Command Line Interface (CLI)
* 🌐 Web-Based User Interface

The system implements core order types and advanced trading strategies in a safe **Simulation Mode (Paper Trading)** environment.

---

# 📌 Project Overview

This project simulates realistic Binance Futures trading behavior while maintaining clean architecture principles.

It supports:

* Core order types
* Advanced algorithmic strategies
* CLI execution
* Web-based UI interaction
* Structured logging
* Strict input validation
* Scalable modular design

---

# 🛠 Tech Stack

##  Backend

* Python 3
* Flask (Web Framework)
* Logging Module
* UUID (Order ID generation)
* Datetime (UTC tracking)

##  Frontend (Web UI)

* HTML5
* CSS3
* JavaScript (Vanilla JS)

##  Architecture

* Modular folder structure
* Strategy-based design
* Config-driven execution
* Simulation-first safety model

---

# 🏗 Project Structure

```
srashti-binance-bot/
│
├── src/
│   ├── config.py
│   ├── market_orders.py
│   ├── limit_orders.py
│   ├── advanced/
│   │     ├── stop_limit.py
│   │     ├── oco.py
│   │     ├── twap.py
│   │     └── grid_strategy.py
│   └── utils/
│         ├── logger.py
│         ├── validator.py
│         └── client.py
│
├── web/
│   ├── app.py
│   ├── templates/
│   │     └── index.html
│   └── static/
│         ├── style.css
│         └── script.js
│
├── bot.log
├── .env
├── report.pdf
└── README.md
```

---

#  Implemented Features

##  Core Orders

✔ Market Orders
✔ Limit Orders

Each order includes:

* CLI argument parsing
* Input validation
* Structured logging
* Simulation execution
* Unique order IDs
* Timestamped records

---

##  Advanced Orders & Strategies

✔ Stop-Limit Orders
✔ OCO (One-Cancels-the-Other)
✔ TWAP (Time-Weighted Average Price)
✔ Grid Trading Strategy

These simulate institutional-style execution logic and advanced trading mechanisms.

---

#  Web-Based Trading Interface

The project includes a browser-based interface built with Flask + HTML/CSS/JS.

### ▶ Run Web Application

From project root:

```bash
python web/app.py
```

Then open in browser:

```
http://127.0.0.1:5000
```

### Web UI Features

* Place Market Orders
* Place Limit Orders
* Execute Stop-Limit
* Execute OCO
* Run TWAP Strategy
* Initialize Grid Strategy
* Display execution results
* Show validation errors

---

#  CLI-Based Execution

Run all commands from the project root directory.

### Activate Virtual Environment (Windows)

```
venv\Scripts\activate
```

---

##  Market Order

```
python src/market_orders.py BTCUSDT BUY 0.01
```

##  Limit Order

```
python src/limit_orders.py BTCUSDT BUY 0.01 65000
```

##  Stop-Limit Order

```
python -m src.advanced.stop_limit BTCUSDT BUY 0.01 59000 58950
```

##  OCO Order

```
python -m src.advanced.oco BTCUSDT BUY 0.01 60500 59000
```

##  TWAP Strategy

```
python -m src.advanced.twap BTCUSDT BUY 1 5 1
```

##  Grid Strategy

```
python -m src.advanced.grid_strategy BTCUSDT 58000 62000 4 0.01
```

---

# 🔐 Simulation Mode (Paper Trading)

Due to API restrictions, the system runs in:

```
TEST_MODE = True
```

Simulation mode:

* Mimics Binance Futures responses
* Generates realistic order IDs
* Simulates market price behavior
* Executes full trading logic safely

The architecture allows easy migration to live Binance API integration.

---

# Logging System

All execution details are recorded in:

```
bot.log
```

Logs include:

* Order placement
* Strategy initialization
* Trigger conditions
* Validation failures
* Error traces

Log format:

```
Timestamp | Log Level | Module | Message
```

---

#  Input Validation

The system validates:

* Symbol format (e.g., BTCUSDT)
* Order side (BUY / SELL)
* Quantity > 0
* Price > 0
* Logical price relationships
* Grid & TWAP constraints

Invalid inputs are rejected before execution.

---

#  Design Principles Used

* Separation of concerns
* Modular utilities
* Config-driven execution
* Strategy abstraction
* CLI + Web integration
* Clean architecture
* Scalable folder structure

---

#  Future Enhancements

* Live Binance Futures API integration
* WebSocket live price feed
* Risk management automation
* Position tracking module
* Strategy performance analytics
* Backtesting framework
* Docker containerization
* Cloud deployment

---

#  Author
Srashti Chauhan |
B.Tech CSE |
Full Stack & AI Enthusiast

