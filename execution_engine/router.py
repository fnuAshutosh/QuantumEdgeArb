"""Lightweight Python order router placeholder."""

from execution_engine.risk import check_risk


def route_order(order, p_value=None):
    """Route an order and apply risk checks if p_value provided."""
    if p_value is not None:
        try:
            check_risk(p_value)
        except Exception as e:
            print(f"Risk check failed: {e}")
            return False
    print(f"Routing order: {order}")
    # in production this would send to exchange
    return True


if __name__ == '__main__':
    # example usage
    print(route_order({'symbol':'NVDA','qty':10}, p_value=0.06))
    print(route_order({'symbol':'NVDA','qty':10}, p_value=0.01))
