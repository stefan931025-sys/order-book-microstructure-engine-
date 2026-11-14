"""
Limit Order Book & Matching Engine Test Suite (`tests/test_order_matching.py`)
Validates price-time priority, book depth updates, and deterministic execution 
matching for high-throughput quantitative order flow simulations.
"""

import pytest
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Order:
    order_id: str
    side: str  # 'BUY' or 'SELL'
    price: float
    quantity: float
    timestamp: int


@dataclass
class Trade:
    buy_order_id: str
    sell_order_id: str
    price: float
    quantity: float


class LimitOrderBook:
    """Core matching engine simulating price-time priority order book dynamics."""
    def __init__(self):
        self.bids: List[Order] = []  # Sorted descending by price
        self.asks: List[Order] = []  # Sorted ascending by price
        self.trade_history: List[Trade] = []

    def add_order(self, order: Order) -> List[Trade]:
        trades = []
        if order.side == 'BUY':
            # Match against asks
            while order.quantity > 0 and self.asks and self.asks[0].price <= order.price:
                best_ask = self.asks[0]
                matched_qty = min(order.quantity, best_ask.quantity)
                
                trades.append(Trade(
                    buy_order_id=order.order_id,
                    sell_order_id=best_ask.order_id,
                    price=best_ask.price,
                    quantity=matched_qty
                ))
                
                order.quantity -= matched_qty
                best_ask.quantity -= matched_qty
                
                if best_ask.quantity == 0:
                    self.asks.pop(0)
            
            # If quantity remains, add to bids (Price-Time Priority)
            if order.quantity > 0:
                self.bids.append(order)
                self.bids.sort(key=lambda x: (-x.price, x.timestamp))

        else:  # SELL order
            # Match against bids
            while order.quantity > 0 and self.bids and self.bids[0].price >= order.price:
                best_bid = self.bids[0]
                matched_qty = min(order.quantity, best_bid.quantity)
                
                trades.append(Trade(
                    buy_order_id=best_bid.order_id,
                    sell_order_id=order.order_id,
                    price=best_bid.price,
                    quantity=matched_qty
                ))
                
                order.quantity -= matched_qty
                best_bid.quantity -= matched_qty
                
                if best_bid.quantity == 0:
                    self.bids.pop(0)
            
            # If quantity remains, add to asks
            if order.quantity > 0:
                self.asks.append(order)
                self.asks.sort(key=lambda x: (x.price, x.timestamp))

        self.trade_history.extend(trades)
        return trades


def test_price_time_priority_matching():
    """Verifies that orders execute strictly according to price-time priority rules."""
    book = LimitOrderBook()

    # Seed book with resting asks
    book.add_order(Order(order_id="ASK-1", side="SELL", price=100.50, quantity=100.0, timestamp=1))
    book.add_order(Order(order_id="ASK-2", side="SELL", price=100.50, quantity=200.0, timestamp=2))

    # Incoming aggressive buy order crossing the spread
    incoming_buy = Order(order_id="BUY-1", side="BUY", price=100.50, quantity=150.0, timestamp=3)
    trades = book.add_order(incoming_buy)

    # Assertions
    assert len(trades) == 2
    # First trade should match ASK-1 completely due to time priority (timestamp 1 vs 2)
    assert trades[0].sell_order_id == "ASK-1"
    assert trades[0].quantity == 100.0
    
    # Second trade should match ASK-2 partially for the remainder (50.0 units)
    assert trades[1].sell_order_id == "ASK-2"
    assert trades[1].quantity == 50.0

    # Remaining book state: ASK-2 should have 150.0 units left
    assert len(book.asks) == 1
    assert book.asks[0].order_id == "ASK-2"
    assert book.asks[0].quantity == 150.0
