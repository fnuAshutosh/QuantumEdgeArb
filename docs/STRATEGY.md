# Trading Strategy Specification

This document describes the Bayesian cointegration pairs trading logic used
throughout the system.  All code must conform to these rules; the formulas are
implemented in `ml_model/cointegration.py` and `ml_model/nemo_classifier.py`.

## 1. Pair Selection

- Compute Engle–Granger two-step cointegration on historical prices.
- Run OLS: `price_A = α + β · price_B + ε`.
- Perform Augmented Dickey-Fuller (ADF) test on residuals `ε`.
- Accept the pair if the ADF p-value < `PVALUE_KILL_THRESHOLD` (0.05).
- Default pair used in POC is **NVDA / TSM**.

## 2. Signal Generation

Inputs: arrays `price_A`, `price_B` for the current bar.

1.  Calculate regression coefficients via `KalmanFilter.train`:
    ```python
    result = KalmanFilter().train(price_A, price_B)
    # result contains {'coef': [α, β], 'pvalue': p, ...}
    ```
2.  Compute spread and rolling z-score with window `ZSCORE_WINDOW` (20 bars):
    ```python
    spread = price_A - (β * price_B + α)
    mu = spread.rolling(ZSCORE_WINDOW).mean()
    sigma = spread.rolling(ZSCORE_WINDOW).std()
    z = (spread - mu) / sigma
    ```
3.  Pass the latest z-score to `NemoClassifier.classify` which uses the
    NVIDIA NIM (or stub) to return a regime and confidence.

## 3. Entry and Exit Rules

| Condition | Signal | Action |
|-----------|--------|--------|
| z < -ZSCORE_ENTRY_THRESHOLD and regime == "Mean Reversion Opportunity" | LONG spread | BUY A, SELL B |
| z > +ZSCORE_ENTRY_THRESHOLD and regime == "Mean Reversion Opportunity" | SHORT spread | SELL A, BUY B |
| regime == "Structural Break" | NO ENTRY | suppress orders |

**Exit:**
- |z| < ZSCORE_EXIT_THRESHOLD → close both legs.
- cointegration p-value > PVALUE_KILL_THRESHOLD → kill switch.
- regime changes to "Structural Break" mid-trade → immediate close.

## 4. Position Sizing

```
notional_per_leg = MAX_POSITION_USD / 2
qty_A = floor(notional_per_leg / price_A)
qty_B = floor(notional_per_leg / price_B)
```

No leverage is used in the proof‑of‑concept.

## 5. Risk Guardrail

Before routing any order the Python function `execution_engine/risk.py`
`check_risk(p_value)` is executed.  It must raise an exception if the p-value
exceeds the kill threshold.  Orders are only routed when this check passes.

---

Refer to [`PROMPT.md`](../PROMPT.md) for the full parameter list and thresholds.
