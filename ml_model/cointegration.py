import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller

class KalmanFilter:
    def __init__(self, window=None):
        # window not used in this simple implementation
        self.window = window

    def train(self, prices_a, prices_b):
        # convert to numpy arrays
        a = np.asarray(prices_a, dtype=float)
        b = np.asarray(prices_b, dtype=float)
        if len(a) != len(b):
            raise ValueError("price series must have equal length")
        # add constant for intercept
        X = sm.add_constant(b)
        model = sm.OLS(a, X).fit()
        coef = [model.params[0], model.params[1]]
        residuals = model.resid
        # adfuller on residuals
        try:
            adf = adfuller(residuals, maxlag=1, regression='c', autolag='AIC')
            pvalue = adf[1]
        except Exception:
            # adfuller may fail on very short input; treat as non-stationary
            pvalue = 1.0
        return {"coef": coef, "pvalue": pvalue, "residuals": residuals.tolist()}

    def predict(self, price_b, coef):
        alpha, beta = coef
        return alpha + beta * price_b

    def zscore(self, spread, window):
        spread = np.asarray(spread, dtype=float)
        if len(spread) < window:
            return np.zeros(len(spread))
        mu = np.convolve(spread, np.ones(window)/window, mode='valid')
        sigma = np.array([np.std(spread[i-window+1:i+1]) for i in range(window-1, len(spread))])
        z = (spread[window-1:] - mu) / sigma
        return z
