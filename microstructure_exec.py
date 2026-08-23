import argparse
import time
import numpy as np
import pandas as pd

class OrderBookMicrostructureProgram:
    """
    Live Execution Microstructure & Order Flow Imbalance Simulator.
    """
    def __init__(self, base_price: float = 150.0):
        self.base_price = base_price

    def generate_lob_snapshot(self) -> pd.DataFrame:
        ticks = 10
        bid_prices = np.sort(self.base_price - np.random.uniform(0.01, 0.20, ticks))[::-1]
        ask_prices = np.sort(self.base_price + np.random.uniform(0.01, 0.20, ticks))
        bid_vols = np.random.randint(100, 2500, ticks)
        ask_vols = np.random.randint(100, 2500, ticks)

        return pd.DataFrame({
            "bid_price": bid_prices,
            "bid_vol": bid_vols,
            "ask_price": ask_prices,
            "ask_vol": ask_vols
        })

    def run_simulation(self, order_size: int, is_buy: bool, steps: int = 5) -> str:
        logs = []
        print(f"\n--- Initiating Microstructure Simulation for {order_size} shares ({'BUY' if is_buy else 'SELL'}) ---")

        for i in range(steps):
            lob = self.generate_lob_snapshot()
            ofi = (lob["bid_vol"].sum() - lob["ask_vol"].sum()) / (lob["bid_vol"].sum() + lob["ask_vol"].sum())
            
            # Kyle's Lambda Slippage Estimation
            spread = lob["ask_price"].iloc[0] - lob["bid_price"].iloc[0]
            slippage_bps = (order_size / lob["ask_vol"].sum()) * 0.05 * 10000
            
            executed_price = lob["ask_price"].iloc[0] * (1 + slippage_bps / 10000) if is_buy else lob["bid_price"].iloc[0] * (1 - slippage_bps / 10000)

            logs.append({
                "Step": i + 1,
                "Spread": round(spread, 4),
                "OFI_Metric": round(ofi, 4),
                "Slippage_bps": round(slippage_bps, 2),
                "Executed_Price": round(executed_price, 4)
            })
            time.sleep(0.3)

        df_logs = pd.DataFrame(logs)
        output_file = "execution_microstructure_log.csv"
        df_logs.to_csv(output_file, index=False)
        print(df_logs.to_string(index=False))
        return output_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Order Book Microstructure Simulator")
    parser.add_argument("--size", type=int, default=10000, help="Order execution size")
    args = parser.parse_args()

    prog = OrderBookMicrostructureProgram(base_price=175.50)
    log_file = prog.run_simulation(order_size=args.size, is_buy=True)
    print(f"\n✅ Program completed. Execution logs exported to '{log_file}'.\n")
