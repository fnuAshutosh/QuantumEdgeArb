import os
import requests

class NemoClassifier:
    def __init__(self, base_url=None, api_key=None, model_id=None):
        # load from env if not provided
        self.base_url = base_url or os.getenv("NIM_BASE_URL")
        self.api_key = api_key or os.getenv("NIM_API_KEY")
        self.model_id = model_id or os.getenv("NIM_MODEL_ID")

    def classify(self, residual, news_headlines=None):
        # simple prompt construction
        prompt = (
            f"Current z-score: {residual}."
            " Classify regime as 'Mean Reversion Opportunity' or 'Structural Break'."
        )
        response = self._call_nim_api(prompt)
        if not response:
            # fallback
            return {"regime": "Mean Reversion Opportunity", "confidence": 0.9}
        return response

    def _call_nim_api(self, prompt: str) -> dict | None:
        if not self.base_url or not self.api_key or not self.model_id:
            return None
        url = f"{self.base_url}/chat/completions"
        headers = {"Authorization": f"Bearer {self.api_key}",
                   "Content-Type": "application/json"}
        payload = {
            "model": self.model_id,
            "messages": [
                {"role": "system", "content": "You are a regime classifier."},
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.1,
            "max_tokens": 50,
        }
        try:
            r = requests.post(url, json=payload, headers=headers, timeout=5)
            r.raise_for_status()
            data = r.json()
            content = data["choices"][0]["message"]["content"]
            return eval(content)  # assume JSON-like
        except Exception:
            return None
