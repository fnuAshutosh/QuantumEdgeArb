import pytest
from execution_engine import router, risk

def test_route_order():
    assert router.route_order({"order_id":"o1"}, 0.01) is True

def test_check_risk_ok():
    assert risk.check_risk(0.01) is True

with pytest.raises(Exception):
    risk.check_risk(0.1)
