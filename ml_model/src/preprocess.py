import numpy as np

def zscore(values, window):
    arr = np.asarray(values, dtype=float)
    result = np.zeros_like(arr)
    for i in range(len(arr)):
        if i + 1 >= window:
            windowed = arr[i+1-window:i+1]
            mu = np.mean(windowed)
            sigma = np.std(windowed, ddof=0)
            result[i] = (arr[i] - mu) / sigma if sigma != 0 else 0.0
        else:
            result[i] = 0.0
    return result
