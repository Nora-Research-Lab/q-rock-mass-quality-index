import math

def compute_q(rqd: float, jn: float, jr: float, ja: float, jw: float, srf: float) -> float:
    """
    Compute the Q-value according to Barton et al. (1974).
    Q = (RQD / Jn) * (Jr / Ja) * (Jw / SRF)
    """
    if jn == 0 or ja == 0 or srf == 0:
        return 0.0
    return (rqd / jn) * (jr / ja) * (jw / srf)

def classify_q(q: float) -> str:
    """Return the rock mass class based on Q-value (Barton classification)."""
    if q < 0.001:
        return "Exceptionally poor"
    if q < 0.01:
        return "Extremely poor"
    if q < 0.1:
        return "Very poor"
    if q < 1:
        return "Poor"
    if q < 4:
        return "Fair"
    if q < 10:
        return "Good"
    if q < 40:
        return "Very good"
    if q < 100:
        return "Extremely good"
    # >= 100
    return "Exceptionally good"

def support_recommendation(q: float, span: float) -> str:
    """
    Simplified support recommendation based on Q-value and tunnel span.
    Returns one of: None, Spot bolting, Systematic bolting, Shotcrete and bolting,
    Steel sets and shotcrete.
    """
    if q >= 40:
        return "None"
    if q >= 10:
        return "Spot bolting"
    if q >= 4:
        return "Systematic bolting"
    if q >= 1:
        if span < 10:
            return "Shotcrete and bolting"
        else:
            return "Steel sets and shotcrete"
    if q >= 0.1:
        if span < 8:
            return "Shotcrete and bolting"
        else:
            return "Steel sets and shotcrete"
    # q < 0.1
    return "Steel sets and shotcrete"
