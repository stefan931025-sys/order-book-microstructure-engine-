# Order Book Microstructure Engine

[![CI Pipeline](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/stefan931025-sys/order-book-microstructure-engine)
[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A high-performance market microstructure analytics suite modeling Limit Order Book (LOB) queue dynamics, Order Flow Imbalance (OFI), and trade execution slippage for quantitative trading strategies.

---

## Core Microstructure & Execution Modules

* **Order Flow Imbalance (OFI):** Quantifies order book delta pressure across bid/ask volume queues to forecast short-term price movements.
* **Execution Slippage Simulator:** Applies market impact metrics (Kyle’s Lambda approximation) to simulate realistic TWAP/VWAP and block execution costs.
* **Spread & Liquidity Analytics:** Monitors real-time depth, bid-ask spread evolution, and book resilience under simulated volume shocks.

---

## Mathematical Specifications

### 1. Order Flow Imbalance (OFI)
$$\text{OFI}_t = I(B_t \ge B_{t-1}) \cdot W(B_t) - I(B_t \le B_{t-1}) \cdot W(B_{t-1}) - \dots$$
Quantifying the net change in top-of-book bid and ask volumes and prices between consecutive states.

### 2. Kyle’s Lambda (Market Impact)
$$\Delta P_t = \alpha + \lambda \cdot Q_t + \varepsilon_t$$
Where $\lambda$ (Kyle's Lambda) measures illiquidity as the price response per unit of net order flow $Q_t$.

---

## System Architecture & Data Flow

