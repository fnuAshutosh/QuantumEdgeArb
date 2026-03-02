"""Training script for Kalman cointegration model (stub)."""

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from cointegration import KalmanFilter


def main():
    # example data: simple linear relation with noise
    prices_a = [100, 101, 102, 103, 104, 105]
    prices_b = [50, 50.5, 51, 51.5, 52, 52.5]
    kf = KalmanFilter()
    result = kf.train(prices_a, prices_b)
    print("trained state", result)
    print("residuals", kf.residuals[:3])
    print("cointegration p-value", kf.pvalue)


if __name__ == '__main__':
    main()
