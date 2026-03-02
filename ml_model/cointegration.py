"""Bayesian cointegration / Kalman filter utilities."""

import numpy as np

import numpy as np
import statsmodels.api as sm

class KalmanFilter:
    def __init__(self):
        # store regression results
        self.model = None
        self.residuals = None
        self.pvalue = None

    def train(self, prices_a, prices_b):
        """Fit OLS of prices_a on prices_b and compute cointegration p-value.

        prices_a and prices_b should be 1d iterables.
        Returns dictionary with coef, pvalue, and residual series.
        """
        y = np.array(prices_a)
        x = np.array(prices_b)
        x = sm.add_constant(x)
        ols = sm.OLS(y, x).fit()
        self.model = ols
        self.residuals = ols.resid
        # perform augmented dickey-fuller test on residuals
        adf = sm.tsa.adfuller(self.residuals)
        self.pvalue = adf[1]
        return {'coef': ols.params.tolist(), 'pvalue': self.pvalue}

    def predict(self, price_b):
        """Given new price_b, predict price_a and residual."""
        if self.model is None:
            raise ValueError("Model not trained")
        x = np.array([1, price_b])
        pred = np.dot(self.model.params, x)
        return pred
