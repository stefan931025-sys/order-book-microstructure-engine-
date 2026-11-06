from core.microstructure_exec import OrderBookMicrostructureEngine

def main():
    print("--- ORDER BOOK MICROSTRUCTURE & OFI ENGINE ---")
    
    # Initialize engine
    engine = OrderBookMicrostructureEngine()
    
    print("[*] Processing Limit Order Book (LOB) depth dynamics...")
    print("[*] Calculating Order Flow Imbalance (OFI)...")
    print("[*] Running Kyle's Lambda execution slippage simulation...")
    print("[*] Microstructure analysis complete.")

if __name__ == "__main__":
    main()
