import pytest

def test_order_flow_imbalance():
    """Verify Order Flow Imbalance (OFI) sign and volume delta pressure calculation."""
    bid_volume_change = 500.0
    ask_volume_change = -200.0
    
    # Standard OFI formulation from bid/ask queue deltas
    ofi = bid_volume_change - ask_volume_change
    
    assert ofi == 700.0
    assert ofi > 0  # Net buying pressure

def test_kyle_lambda_slippage():
    """Verify Kyle's Lambda market impact slippage estimation."""
    lambda_coefficient = 0.0005  # Price impact parameter
    order_size = 10000.0         # Executed shares/contracts
    
    expected_slippage = lambda_coefficient * order_size
    
    assert pytest.approx(expected_slippage, 0.001) == 5.0
