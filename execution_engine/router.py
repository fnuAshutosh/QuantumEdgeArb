import json

def route_order(order: dict, p_value: float) -> bool:
    # simple Python stub, log and return True
    print("[router] order=", json.dumps(order), "p_value=", p_value)
    return True


if __name__ == "__main__":
    route_order({"order_id": "test"}, 0.01)
