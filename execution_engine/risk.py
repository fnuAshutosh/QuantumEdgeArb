"""Simple risk engine stub."""

def check_risk(p_value):
    print(f"Checking risk, p_value={p_value}")
    if p_value > 0.05:
        raise Exception("Risk threshold exceeded: kill switch engaged")
    return False
