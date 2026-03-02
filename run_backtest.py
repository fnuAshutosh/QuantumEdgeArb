import numpy as np, pandas as pd
from ml_model.cointegration import KalmanFilter
from ml_model.src.preprocess import zscore

np.random.seed(0)
N=200
price_b = np.cumsum(np.random.randn(N))+100
price_a = 5 + 1.2*price_b + np.random.randn(N)*0.5

df = pd.DataFrame({"A":price_a,"B":price_b})
train_n = int(0.7*N)
coef = KalmanFilter().train(df['A'][:train_n].tolist(), df['B'][:train_n].tolist())['coef']
spread = df['A'] - (coef[1]*df['B']+coef[0])
z = zscore(spread.values, window=20)
print('coef', coef)
print('last zscore', z[-1])
print('Sharpe approx', np.mean(spread)/np.std(spread))
