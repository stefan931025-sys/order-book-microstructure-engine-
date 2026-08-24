[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/stefan931025-sys/order-book-microstructure-engine-)

# Order Book Microstructure Engine

[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Description:**  
Market microstructure analytics suite modeling Limit Order Book (LOB) dynamics, Order Flow Imbalance (OFI), and trade execution slippage.

---

## 📌 Microstructure & Execution Modules

* **Order Flow Imbalance (OFI):** Quantifies order book delta pressure across bid/ask volume queues.
* **Execution Slippage Simulator:** Applies market impact metrics (Kyle's Lambda approximation) to simulate realistic TWAP/VWAP execution costs.
* **Spread & Liquidity Analytics:** Monitors real-time depth and bid-ask spread dynamics.

---

## 🛠️ Quickstart

git clone https://github.com/stefan931025-sys/order-book-microstructure-engine.git
cd order-book-microstructure-engine
python microstructure_exec.py
