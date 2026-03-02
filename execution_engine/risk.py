def check_risk(p_value: float) -> bool:
    if p_value > 0.05:
        raise Exception("kill switch")
    return True
