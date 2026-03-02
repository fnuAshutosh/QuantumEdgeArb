class NemoClassifier:
    def __init__(self, base_url=None, api_key=None, model_id=None):
        # credentials would come from env vars in real implementation
        self.base_url = base_url
        self.api_key = api_key
        self.model_id = model_id

    def classify(self, residual, news_headlines=None):
        # stub implementation: ignore inputs and return fixed regime
        return {"regime": "Mean Reversion Opportunity", "confidence": 0.9}

    # future: uncomment and implement actual HTTP call to NVIDIA NIM
    # def _call_nim_api(self, prompt):
    #     pass
