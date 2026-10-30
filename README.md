# Order Book Microstructure Engine

[![CI Pipeline](https://github.com/stefan931025-sys/order-book-microstructure-engine/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/stefan931025-sys/order-book-microstructure-engine/actions/workflows/ci.yml)

![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Description

Market microstructure analytics suite modeling Limit Order Book (LOB) dynamics, Order Flow Imbalance (OFI), and trade execution slippage.

## 📌 Microstructure & Execution Modules

* **Order Flow Imbalance (OFI):** Quantifies order book delta pressure across bid/ask volume queues.
* **Execution Slippage Simulator:** Applies market impact metrics (Kyle's Lambda approximation) to simulate realistic TWAP/VWAP execution costs.
* **Spread & Liquidity Analytics:** Monitors real-time depth and bid-ask spread dynamics.

## 🚀 Quickstart

```bash
git clone [https://github.com/stefan931025-sys/order-book-microstructure-engine.git](https://github.com/stefan931025-sys/order-book-microstructure-engine.git)
cd order-book-microstructure-engine
python src/microstructure_exec.py
