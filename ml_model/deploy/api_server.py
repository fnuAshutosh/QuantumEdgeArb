from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PredictRequest(BaseModel):
    prices_a: list[float]
    prices_b: list[float]
    current_price_b: float


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/predict")
async def predict(body: PredictRequest):
    # stubbed response; real logic would call KalmanFilter and NemoClassifier
    return {
        "predicted_price_a": body.current_price_b * 2,
        "residual": -0.31,
        "zscore": -2.10,
        "pvalue": 0.03,
        "regime": "Mean Reversion Opportunity",
        "regime_confidence": 0.89,
        "action": "LONG_SPREAD",
    }
