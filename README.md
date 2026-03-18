#  Trading Bot – Binance Futures Testnet

##  Overview

This project is a Python-based CLI trading bot that interacts with the Binance Futures Testnet (USDT-M). It allows users to place MARKET and LIMIT orders with proper validation, logging, and error handling.

---

##  Features

* ✅ Place MARKET orders
* ✅ Place LIMIT orders
* ✅ Supports BUY and SELL
* ✅ Command Line Interface (CLI)
* ✅ Input validation
* ✅ Logging of requests, responses, and errors
* ✅ Exception handling (API + user input)

---

## 🛠️ Tech Stack

* Python 3.x
* python-binance
* typer (CLI)
* loguru (logging)
* python-dotenv

---

## 📁 Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── .env
├── requirements.txt
├── README.md
├── trading_bot.log
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```
git clone <your-repo-link>
cd trading_bot
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variables

Create a `.env` file:

```
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
BASE_URL=https://testnet.binancefuture.com
```

---

## 🔑 Binance Testnet Setup

1. Register at: https://testnet.binancefuture.com
2. Generate API keys
3. Enable Futures trading permissions

---

## ▶️ How to Run

### ✅ MARKET Order

```
py cli.py BTCUSDT BUY MARKET 0.002
```

### ✅ LIMIT Order

```
py cli.py BTCUSDT SELL LIMIT 0.002 --price 70000
```

---

## 📊 Output Example

```
📊 Order Summary:
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.002

✅ Order Successful!
Order ID: 12345678
Status: NEW
Executed Qty: 0.002
```

---

## 📝 Logging

All logs are stored in:

```
trading_bot.log
```

Includes:

* API requests
* Responses
* Errors

---

## ⚠️ Assumptions

* Minimum order value must be ≥ 100 USDT (Binance rule)
* LIMIT orders must follow market price constraints
* Only USDT-M Futures supported

---

## 👨‍💻 Author

Abhishek Verma

---

## 📬 Submission

Please find attached:

* Source code (GitHub)
* Log files (MARKET + LIMIT orders)
* README with setup instructions

---
