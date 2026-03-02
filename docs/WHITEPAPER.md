# Whitepaper

This file collects the mathematical foundation and economic rationale for the
QuantumEdgeArb proof-of-concept.  It has been updated to include the complete
statistical formulas referenced elsewhere in the documentation.

## Engle–Granger Cointegration

**Step 1:** Estimate ordinary least squares (OLS) regression:

\[ price_{A,t} = \alpha + \beta \cdot price_{B,t} + \varepsilon_t \]

The residuals \(\varepsilon_t\) represent the spread away from the linear
relationship between the two price series.

**Step 2:** Perform the Augmented Dickey–Fuller (ADF) unit‑root test on
\(\varepsilon_t\).

- Null hypothesis \(H_0\): the residual has a unit root (non‑stationary)
- Alternative \(H_1\): the residual is stationary (cointegrated)
- Reject \(H_0\) if p-value < 0.05 (see `PVALUE_KILL_THRESHOLD`).

## Z‑Score Signal

Once cointegration is confirmed, compute the time‑series z-score of the spread
for entry/exit signals.

\[ spread_t = price_{A,t} - (\hat{\beta} \cdot price_{B,t} + \hat{\alpha}) \]
\[ \mu_{spread} = \frac{1}{W} \sum_{i=t-W+1}^{t} spread_i \]
\[ \sigma_{spread} = \sqrt{ \frac{1}{W-1} \sum_{i=t-W+1}^{t} (spread_i - \mu_{spread})^2 } \]
\[ z_t = \frac{spread_t - \mu_{spread}}{\sigma_{spread}} \]

Here, \(W\) is the rolling window size defined by `ZSCORE_WINDOW` (20 bars).
Entry occurs when \(|z_t| > ZSCORE_ENTRY_THRESHOLD = 2.0\) and exit when
\(|z_t| < ZSCORE_EXIT_THRESHOLD = 0.5\).

## Kalman Filtering (Future Work)

The current implementation uses rolling-window OLS for simplicity.  A true
Kalman filter treats \(\beta\) as a time-varying latent state:

\[ \beta_t = \beta_{t-1} + w_t, \quad w_t \sim \mathcal{N}(0,Q) \]
\[ y_t = x_t \beta_t + v_t, \quad v_t \sim \mathcal{N}(0,R) \]

Implementing this requires libraries such as `pykalman` or `filterpy` and is
slated for Phase 03+.

## Economic Rationale

The strategy exploits temporary deviations from a long‑term equilibrium between
paired assets.  By simultaneously going long the undervalued leg and short the
overvalued leg, the trade profits when mean reversion occurs.  The kill switch
on cointegration p-value and the regime classifier serve as risk controls,
preventing deployment of capital when the underlying statistical relationship
breaks down.
