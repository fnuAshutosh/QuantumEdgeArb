import pytest
from ml_model.nemo_classifier import NemoClassifier

class DummyResponse:
    def json(self):
        return {"choices": [{"message": {"content": "{'regime': 'Mean Reversion Opportunity', 'confidence': 0.8}"}}]}
    def raise_for_status(self):
        pass


def test_classify_stub(monkeypatch):
    nm = NemoClassifier(base_url="http://example.com", api_key="key", model_id="m")
    def fake_post(url, json, headers, timeout):
        return DummyResponse()
    monkeypatch.setattr('requests.post', fake_post)
    res = nm.classify(1.23)
    assert res['regime'] == 'Mean Reversion Opportunity'
    assert 'confidence' in res
