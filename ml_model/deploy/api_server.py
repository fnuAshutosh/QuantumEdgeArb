import os
from fastapi import FastAPI
from pydantic import BaseModel

from ml_model.cointegration import KalmanFilter
from ml_model.nemo_classifier import NemoClassifier
from ml_model.src.preprocess import zscore

app = FastAPI()

class PredictRequest(BaseModel):
    prices_a: list[float]
    prices_b: list[float]
    current_price_b: float


def compute_signal(prices_a, prices_b):
    kf = KalmanFilter()
    result = kf.train(prices_a, prices_b)
    coef = result["coef"]
    pvalue = result.get("pvalue", 1.0)
    # compute spread and last zscore
    spread = [a - (coef[1] * b + coef[0]) for a, b in zip(prices_a, prices_b)]
    zs = zscore(spread, window=20)
    last_z = float(zs[-1]) if len(zs) > 0 else 0.0
    last_spread = float(spread[-1]) if spread else 0.0
    return coef, pvalue, last_z, last_spread


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/predict")
async def predict(body: PredictRequest):
    coef, pvalue, last_z, last_spread = compute_signal(body.prices_a, body.prices_b)
    classifier = NemoClassifier()
    regime_res = classifier.classify(last_z)
    action = "HOLD"
    if abs(last_z) > float(os.getenv("ZSCORE_ENTRY_THRESHOLD", 2.0)):
        action = "LONG_SPREAD" if last_z < 0 else "SHORT_SPREAD"
    return {
        "predicted_price_a": coef[0] + coef[1] * body.current_price_b,
        "residual": last_spread,
        "zscore": last_z,
        "pvalue": pvalue,
        "regime": regime_res.get("regime"),
        "regime_confidence": regime_res.get("confidence"),
        "action": action,
    }
