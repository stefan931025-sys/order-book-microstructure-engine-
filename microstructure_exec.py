import pandas as pd
import numpy as np

class OrderBookMicrostructure:
    """
    Models Limit Order Book (LOB) order flow imbalance (OFI) and simulates TWAP/VWAP execution slippage.
    """
    def __init__(self, bid_prices: list, bid_volumes: list, ask_prices: list, ask_volumes: list):
        self.df = pd.DataFrame({
            "bid_price": bid_prices,
            "bid_vol": bid_volumes,
            "ask_price": ask_prices,
            "ask_vol": ask_volumes
        })

    def calculate_order_flow_imbalance(self) -> float:
        """Calculates normalized Order Flow Imbalance (OFI)."""
        bid_delta = self.df["bid_vol"].diff().fillna(0)
        ask_delta = self.df["ask_vol"].diff().fillna(0)
        ofi = bid_delta - ask_delta
        return ofi.mean()

    def simulate_execution_slippage(self, order_size: float, is_buy: bool) -> dict:
        spread = self.df["ask_price"].mean() - self.df["bid_price"].mean()
        market_depth = self.df["bid_vol"].mean() + self.df["ask_vol"].mean()
        
        # Simple impact parameter model (Kyle's Lambda approximation)
        impact_factor = 0.0001
        estimated_slippage_bps = (order_size / market_depth) * impact_factor * 10000
        
        base_price = self.df["ask_price"].iloc[-1] if is_buy else self.df["bid_price"].iloc[-1]
        executed_price = base_price * (1 + (estimated_slippage_bps / 10000)) if is_buy else base_price * (1 - (estimated_slippage_bps / 10000))

        return {
            "Side": "BUY" if is_buy else "SELL",
            "Order_Size": order_size,
            "Bid_Ask_Spread": round(spread, 4),
            "Estimated_Slippage_bps": round(estimated_slippage_bps, 2),
            "Base_Price": base_price,
            "Simulated_Execution_Price": round(executed_price, 4)
        }

if __name__ == "__main__":
    # Simulated 5-tick Order Book Snapshot
    bids = [150.00, 150.01, 150.00, 149.99, 150.02]
    bid_vols = [1200, 1500, 1100, 900, 1600]
    asks = [150.03, 150.04, 150.03, 150.02, 150.05]
    ask_vols = [800, 1000, 750, 600, 1100]

    lob = OrderBookMicrostructure(bids, bid_vols, asks, ask_vols)
    ofi_score = lob.calculate_order_flow_imbalance()
    execution = lob.simulate_execution_slippage(order_size=5000, is_buy=True)

    print(f"--- Market Microstructure Engine ---")
    print(f"Order Flow Imbalance (OFI): {ofi_score:.2f}")
    for k, v in execution.items():
        print(f"{k}: {v}")
