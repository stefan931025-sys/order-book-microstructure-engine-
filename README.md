![CI Pipeline](https://github.com/stefan931025-sys/order-book-microstructure-engine/actions/workflows/ci.yml/badge.svg)

# Order Book Microstructure Engine[span_2](start_span)[span_2](end_span)

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description[span_3](start_span)[span_3](end_span)
Market microstructure analytics suite modeling Limit Order Book (LOB) dynamics, Order Flow Imbalance (OFI), and trade execution slippage[span_4](start_span)[span_4](end_span).

---

## 📌 Microstructure & Execution Modules[span_5](start_span)[span_5](end_span)

* **Order Flow Imbalance (OFI):** Quantifies order book delta pressure across bid/ask volume queues[span_6](start_span)[span_6](end_span).
* **Execution Slippage Simulator:** Applies market impact metrics (Kyle's Lambda approximation) to simulate realistic TWAP/VWAP execution costs[span_7](start_span)[span_7](end_span).
* **Spread & Liquidity Analytics:** Monitors real-time depth and bid-ask spread dynamics[span_8](start_span)[span_8](end_span).

---

## 🚀 Quickstart[span_9](start_span)[span_9](end_span)

```bash
# Clone repository
git clone [https://github.com/stefan931025-sys/order-book-microstructure-engine.git](https://github.com/stefan931025-sys/order-book-microstructure-engine.git)
cd order-book-microstructure-engine

# Run microstructure execution script from src directory
python src/microstructure_exec.py
