from fastapi.testclient import TestClient
from ml_model.deploy.api_server import app

c = TestClient(app)

def test_health():
    assert c.get('/health').json() == {"status": "ok"}


def test_predict_empty():
    resp = c.post('/predict', json={"prices_a": [1,2,3], "prices_b": [1,2,3], "current_price_b": 3})
    data = resp.json()
    assert "zscore" in data
    assert "regime" in data
