---
phase: 02-signal
plan: 01
type: execute
wave: 1
depends_on:
  - 01-bootstrap
files_modified:
  - ml_model/nemo_classifier.py
  - ml_model/deploy/api_server.py
  - ml_model/src/preprocess.py
  - ml_model/src/train.py
  - .env.example
requirements: [REQ-??]

must_haves:
  truths:
    - "NemoClassifier.classify calls NIM API and returns dict"
    - "/predict endpoint returns JSON conforming to schema"
  artifacts:
    - path: "ml_model/nemo_classifier.py"
      provides: "regime classification via HTTP"
  key_links: []
---

<objective>
Implement the signal pipeline components: real NIM call and prediction API.
</objective>

<tasks>

<task type="auto">
  <name>Create NemoClassifier stub</name>
  <done>completed</done>
  <files>ml_model/nemo_classifier.py</files>
  <action>
    Implement class `NemoClassifier` with method `classify(residual, news)`
    that returns a fixed dict `{"regime":"Mean Reversion Opportunity","confidence":0.9}`.
    Do not call external API yet; keep future hook commented.
  </action>
  <verify>
    <automated>python - <<'PY'
from ml_model.nemo_classifier import NemoClassifier
print(NemoClassifier().classify(1.0))
PY</automated>
  </verify>
  <done>`classify` method exists and returns expected dict.</done>
</task>

<task type="auto">
  <name>Implement basic API server</name>
  <done>completed</done>
  <files>ml_model/deploy/api_server.py</files>
  <action>
    Create FastAPI app with `/health` returning `{"status":"ok"}` and
    `/predict` accepting JSON according to schema and echoing back hardcoded
    values (e.g. zscore -1.0, regime "Mean Reversion Opportunity").
  </action>
  <verify>
    <automated>python - <<'PY'
from fastapi.testclient import TestClient
from ml_model.deploy.api_server import app
c = TestClient(app)
print(c.get('/health').json())
print(c.post('/predict', json={"prices_a":[],"prices_b":[],"current_price_b":0}).json())
PY</automated>
  </verify>
  <done>/health and /predict endpoints return JSON as expected.</done>
</task>

<task type="auto">
  <name>Add preprocessing utility</name>
  <done>completed</done>
  <files>ml_model/src/preprocess.py</files>
  <action>
    Write function `zscore(spread, window)` that computes rolling z-scores
    using simple Python loops or numpy.
  </action>
  <verify>
    <automated>python - <<'PY'
from ml_model.src.preprocess import zscore
import numpy as np
print(zscore(np.array([1,2,3,4,5]),3))
PY</automated>
  </verify>
  <done>Function returns array of same length with zeros or mocked values.</done>
</task>

<task type="auto">
  <name>Stub training script</name>
  <done>completed</done>
  <files>ml_model/src/train.py</files>
  <action>
    Implement `train()` that accepts two lists and returns dictionary with
    coef and pvalue, e.g. `{ 'coef':[0,1], 'pvalue':0.01 }`.
    Add `if __name__=='__main__'` to print result on sample data.
  </action>
  <verify>
    <automated>python ml_model/src/train.py</automated>
  </verify>
  <done>Script runs without error and prints dict.</done>
</task>

</tasks>
