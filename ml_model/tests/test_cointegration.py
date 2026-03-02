import numpy as np
import pytest
from ml_model.cointegration import KalmanFilter

def test_train_returns_keys():
    prices_a = [1, 2, 3, 4, 5]
    prices_b = [2, 4, 6, 8, 10]
    kf = KalmanFilter()
    res = kf.train(prices_a, prices_b)
    assert "coef" in res and isinstance(res["coef"], list)
    assert "pvalue" in res


def test_predict_and_zscore():
    kf = KalmanFilter()
    coef = [1.0, 2.0]
    assert kf.predict(3, coef) == 7.0
    spread = np.array([1,2,3,4,5])
    z = kf.zscore(spread, 3)
    assert isinstance(z, np.ndarray)
